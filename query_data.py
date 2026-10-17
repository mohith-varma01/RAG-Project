import argparse
import time
from tracemalloc import start
# from dataclasses import dataclass
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

# PROMPT_TEMPLATE = """
# You are a company-documentation assistant.

# Answer the question using only the supplied context.
# If the answer is not available in the context, clearly say
# that the provided documents do not contain enough information.
# Do not invent policies, dates, amounts, or procedures.

# Context:
# {context}

# Question:
# {question}

# Answer:
# """


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    start = time.perf_counter()

    # Prepare the DB.
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("Embedding initialization:", round(
    time.perf_counter() - start, 2
    ), "seconds")


    db = Chroma(
        persist_directory=CHROMA_PATH, 
        embedding_function=embedding_function,
        collection_name="HR_Handbook"
    )

    start = time.perf_counter()

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    
    print("Retrieval:", round(
    time.perf_counter() - start, 2
    ), "seconds")

    for doc, score in results:
        print("\nSCORE:", score)
        print(doc.page_content[:200])

    if len(results) == 0 or results[0][1] < 0.4:
        print(f"Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    #print(prompt)

    model = Ollama(model="llama3.2:3b")

    start = time.perf_counter()

    response_text = model.invoke(prompt)

    print("LLM generation:", round(
    time.perf_counter() - start, 2
    ), "seconds")

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)

    # sources = list(set(doc.metadata.get("source", "Unknown") for doc, score in results))
    # print(f"\nResponse: {response_text}")
    # print(f"Sources: {sources}")

if __name__ == "__main__":
    main()