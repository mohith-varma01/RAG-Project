
import os
import streamlit as st
import time
from pathlib import Path
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

def log_time(step_name, start_time):
    elapsed = time.perf_counter() - start_time
    print(f"[TIMING] {step_name}: {elapsed:.3f} seconds", flush=True)


# Configuration
CHROMA_PATH = "chroma"
COLLECTION_NAME = "HR_Handbook"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "llama3.2:3b"

PROMPT_TEMPLATE = """
You are a company documentation assistant.

Answer using only the provided context.
If the context does not contain the answer, say so clearly.
Do not invent company policies or facts.

Context:
{context}

Question:
{question}

Answer:
"""


# Load models and database once per app process

@st.cache_resource(show_spinner="Loading RAG models...")
def load_rag():
    print("\n[TIMING] Initializing RAG components...", flush=True)

    start = time.perf_counter()
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"local_files_only": True}
    )
    log_time("Embedding model initialization", start)

    start = time.perf_counter()
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME
    )
    log_time("ChromaDB initialization", start)

    start = time.perf_counter()
    model = Ollama(
        model=LLM_MODEL,
        keep_alive="10m",
        num_predict=256
    )
    log_time("Ollama wrapper initialization", start)

    print("[TIMING] RAG initialization complete\n", flush=True)

    return embeddings, db, model



def get_answer(question, db, model):
    timings = {}
    total_start = time.perf_counter()

    # 1. Convert question into an embedding
    start = time.perf_counter()
    query_vector = db._embedding_function.embed_query(question)
    timings["query_embedding"] = time.perf_counter() - start

    # 2. Search ChromaDB using the precomputed embedding
    start = time.perf_counter()
    raw_results = db.similarity_search_by_vector_with_relevance_scores(
        query_vector,
        k=3
    )
    timings["retrieval"] = time.perf_counter() - start

    if not raw_results or raw_results[0][1] < 0.4:
        timings["total"] = time.perf_counter() - total_start
        print("RAG timings:", timings)

        return (
            "I could not find sufficiently relevant information "
            "in the indexed documents."
        ), []

    # 3. Construct the prompt
    start = time.perf_counter()

    context = "\n\n---\n\n".join(
        doc.page_content for doc, score in raw_results
    )

    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    timings["prompt_construction"] = time.perf_counter() - start

    # 4. Generate answer
    start = time.perf_counter()
    #answer = model.invoke(prompt)
    answer_parts = []

    for chunk in model.stream(prompt):
        answer_parts.append(chunk)
    
    timings["generation"] = time.perf_counter() - start

    # 5. Collect sources
    start = time.perf_counter()

    sources = []

    for doc, score in raw_results:
        source = doc.metadata.get("source", "Unknown document")
        source_name = Path(source).name
        page = doc.metadata.get("page")

        if page is not None:
            source_name += f", page {int(page) + 1}"

        if source_name not in sources:
            sources.append(source_name)

    timings["source_formatting"] = time.perf_counter() - start
    timings["total"] = time.perf_counter() - total_start

    print("RAG timings:", {
        key: round(value, 3)
        for key, value in timings.items()
    })

    return answer, sources


# Web interface
st.set_page_config(
    page_title="Document Assistant",
    page_icon="💬",
    layout="centered"
)

st.title("Company Document Assistant")
st.caption(
    "Ask questions about your indexed Markdown and PDF documents."
)

if not os.path.exists(CHROMA_PATH):
    st.error(
        "ChromaDB was not found. Run python create_database.py first."
    )
    st.stop()

embeddings, db, model = load_rag()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("sources"):
            with st.expander("Sources"):
                for source in message["sources"]:
                    st.write(f"- {source}")

# Accept a new question
question = st.chat_input("Ask a question about your documents...")

# if question:
#     st.session_state.messages.append({
#         "role": "user",
#         "content": question
#     })

#     with st.chat_message("user"):
#         st.markdown(question)

#     # with st.chat_message("assistant"):
#     #     with st.spinner("Searching documents and generating answer..."):
#     #         try:
#     #             answer, sources = get_answer(
#     #                 question,
#     #                 db,
#     #                 model
#     #             )

#     #             st.markdown(answer)

#     #             if sources:
#     #                 with st.expander("Sources"):
#     #                     for source in sources:
#     #                         st.write(f"- {source}")

#     #             st.session_state.messages.append({
#     #                 "role": "assistant",
#     #                 "content": answer,
#     #                 "sources": sources
#     #             })

#     #         except Exception as e:
#     #             st.error(
#     #                 "Something went wrong. Check that Ollama is "
#     #                 "running and the configured model is installed."
#     #             )
#     #             st.exception(e)
#     with st.chat_message("assistant"):
#         with st.spinner("Searching documents..."):
#             results = db.similarity_search_with_relevance_scores(
#                 question,
#                 k=3
#             )

#         if not results or results[0][1] < 0.4:
#             answer = (
#                 "I could not find sufficiently relevant information "
#                 "in the indexed documents."
#             )
#             st.markdown(answer)
#         else:
#             context = "\n\n---\n\n".join(
#                 doc.page_content for doc, score in results
#             )

#             prompt = PROMPT_TEMPLATE.format(
#                 context=context,
#                 question=question
#             )

#             answer = st.write_stream(model.stream(prompt))


if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        total_start = time.perf_counter()

        # STEP 1: Embed the question
        start = time.perf_counter()
        query_vector = embeddings.embed_query(question)
        log_time("1. Query embedding", start)

        # STEP 2: Retrieve matching chunks
        start = time.perf_counter()
        results = db.similarity_search_by_vector_with_relevance_scores(
            query_vector,
            k=3
        )
        log_time("2. ChromaDB retrieval", start)

        if not results or results[0][1] < 0.4:
            answer = (
                "I could not find sufficiently relevant information "
                "in the indexed documents."
            )
            st.markdown(answer)
            sources = []

        else:
            # STEP 3: Build the prompt
            start = time.perf_counter()

            context = "\n\n---\n\n".join(
                doc.page_content for doc, score in results
            )

            prompt = PROMPT_TEMPLATE.format(
                context=context,
                question=question
            )

            log_time("3. Prompt construction", start)
            print(
                f"[TIMING] Context size: {len(context)} characters",
                flush=True
            )

            # STEP 4: Stream the answer and measure generation
            generation_start = time.perf_counter()
            first_token_time = [None]

            def timed_stream():
                for chunk in model.stream(prompt):
                    if first_token_time[0] is None:
                        first_token_time[0] = time.perf_counter()

                        print(
                            "[TIMING] Time to first chunk: "
                            f"{first_token_time[0] - generation_start:.3f} seconds",
                            flush=True
                        )

                    yield chunk

                print(
                    "[TIMING] Total generation time: "
                    f"{time.perf_counter() - generation_start:.3f} seconds",
                    flush=True
                )

            answer = st.write_stream(timed_stream())

            # STEP 5: Extract source filenames
            start = time.perf_counter()
            sources = []

            for doc, score in results:
                source = doc.metadata.get("source", "Unknown document")
                source_name = Path(source).name
                page = doc.metadata.get("page")

                if page is not None:
                    source_name += f", page {int(page) + 1}"

                if source_name not in sources:
                    sources.append(source_name)

            log_time("5. Source formatting", start)

            if sources:
                with st.expander("Sources"):
                    for source in sources:
                        st.write(f"- {source}")

        log_time("TOTAL question processing", total_start)
        print("\n")

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "sources": sources
        })
