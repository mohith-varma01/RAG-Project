
## 1. Purpose and principles
This playbook standardizes how support receives, investigates, and resolves customer questions. Acknowledge the issue, confirm the desired outcome, collect only necessary information, and explain the next step in plain language. Do not promise a resolution time unless an approved service target applies. Never blame the customer or another team.

## 2. Ticket severity
- **P1 — Critical:** Confirmed widespread outage or a security incident with significant immediate impact. Notify the on-call lead immediately and follow the incident process.
- **P2 — High:** A major feature is unavailable for multiple customers or a key business workflow is severely impaired with no reasonable workaround.
- **P3 — Normal:** A limited issue affects one customer or a non-critical feature; a workaround may exist.
- **P4 — Low / Request:** General questions, cosmetic defects, documentation requests, and feature suggestions.

Severity is based on customer impact and urgency, not how strongly a customer phrases a message. Reassess when new facts emerge.

## 3. Initial response workflow
1. Verify customer identity using the approved method.
2. Acknowledge and summarize the issue.
3. Ask focused questions only when necessary.
4. Check the knowledge base, known-issues list, and status page.
5. Record steps attempted and the exact error, avoiding unnecessary sensitive data.
6. Assign severity and route the ticket.
7. Explain next steps and the next update time if a target is known.

## 4. Identity and privacy
Never ask for a password, one-time passcode, full payment-card number, or authentication secret. Verify the requester before discussing account-specific details or changing access. If verification fails, explain the limitation and use the approved recovery process.

Do not disclose one customer’s information to another customer, even if the requester claims to be a colleague or family member. Requests for data export, deletion, or access to personal data must go through the designated privacy workflow.

## 5. Troubleshooting
Start with least-disruptive checks. Confirm service status, product version, relevant settings, and reproducibility. Do not ask customers to disable security controls, share credentials, or run unapproved scripts.

Engineering escalations should include:
- concise problem statement;
- affected product and environment;
- steps to reproduce;
- expected versus actual behavior;
- timestamp and time zone;
- relevant request or correlation ID, if available;
- troubleshooting already completed;
- customer impact and severity.

Do not include secrets or unnecessary personal information in ticket notes.

## 6. Escalation rules
Escalate P1 issues immediately to the on-call lead. Escalate suspected security or privacy incidents to Information Security or the Privacy team without waiting for routine troubleshooting. Route billing disputes to Billing Operations, account-access issues to Identity Support, and product defects to Engineering.

If the owner is unclear, ask the support lead rather than leaving the ticket unassigned. Keep ownership explicit until the receiving team accepts the case.

## 7. Customer communication
Separate confirmed facts from hypotheses. A good update says what is known, what is being investigated, and when the next update will arrive. Avoid internal jargon, speculative root causes, and unapproved guarantees.

Example: “Thanks for sharing the details. We’ve reproduced the error and assigned it to our technical team. We are checking the cause and will update you by 3 p.m. IST. You do not need to repeat the troubleshooting steps already listed in the ticket.”

If an update time changes, tell the customer before the promised time passes where practical.

## 8. Refunds and account adjustments
Follow the current Refund and Billing Standard. Do not promise a refund, credit, or account adjustment outside your authority. Verify the transaction and route exceptions to Billing Operations.

## 9. Closing a ticket
Before closing, confirm the issue is resolved or the customer has received the answer or next-step instructions. Record the resolution and any useful knowledge-base update. If the customer does not respond, follow the team’s current closure schedule; do not invent a deadline.

## 10. Knowledge-base quality
When an issue reveals a missing article, propose an update with symptoms, confirmed cause, resolution, and product version. Do not publish unreviewed instructions that could expose data or weaken security. Product and Security owners approve articles in their domains.

## 11. Scenarios
**Login failure for one user:** Verify identity, check service status and account state, collect the exact error, and route to Identity Support if standard recovery fails.

**Many customers cannot complete checkout:** Assess scope and impact. If a critical workflow is widely unavailable, notify the on-call lead and consider P1.

**Customer emails a password:** Do not repeat it in ticket notes. Follow the secret-handling procedure and advise the customer to change it if Security directs.

**Customer asks for a refund:** Verify the transaction and consult the Refund and Billing Standard. Do not promise an outcome before the authorized team decides.

## 12. Metrics and document control
The team may monitor first response time, resolution time, reopen rate, customer satisfaction, escalation quality, and knowledge-base usefulness. Fast closure is not success if the issue remains unresolved or the answer is inaccurate. Owner: Customer Experience. Review quarterly and after significant product or workflow changes.
