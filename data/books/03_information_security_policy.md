
## 1. Purpose
This policy defines minimum expectations for protecting Northstar systems, data, and customer information. Access is granted to support approved work, not as a general entitlement. Everyone using company systems must help prevent avoidable exposure and report suspected incidents quickly.

## 2. Information classification
- **Public:** Approved for unrestricted external distribution, such as published marketing pages.
- **Internal:** Routine company information intended for employees and approved contractors.
- **Confidential:** Information that could harm the company, customers, employees, or partners if disclosed without authorization. Examples include contracts, financial forecasts, customer lists, and non-public product plans.
- **Restricted:** Highly sensitive information requiring specifically approved access, such as authentication secrets, certain regulated data, and security incident evidence.

If a document has no label and its sensitivity is unclear, treat it as Internal at minimum and ask the owner before sharing externally. Do not downgrade a label simply to make sharing easier.

## 3. Identity and access
Use your own company identity. Never share passwords, one-time codes, security keys, or session tokens. Enable multi-factor authentication wherever supported or required. Access follows least privilege: users receive only the permissions needed for their responsibilities.

Requests for elevated access must go through the IT Service Desk with a business justification, required duration, and system name. A colleague’s chat approval is not a substitute for the documented workflow. Managers and system owners must review access when roles change or access is no longer needed.

## 4. Passwords and authentication
Use the company password manager for unique passwords. Never reuse a Northstar password on personal services or store passwords in plain-text notes, source code, spreadsheets, or shared documents. Deny unexpected MFA prompts and report them. IT will never ask for your password or one-time code.

## 5. Devices and networks
Company-managed devices must use supported operating systems, security updates, screen locks, and approved endpoint protection. Do not disable security tools or bypass device-management controls. Report lost or stolen devices immediately to the Service Desk.

In public spaces, prevent shoulder-surfing, avoid discussing confidential matters where others can overhear, and use approved secure access. Personal devices may access company resources only through an approved arrangement. Do not copy company files to personal storage or unapproved cloud services.

## 6. Email and phishing
Be cautious with unexpected attachments, urgent payment requests, unusual login links, and messages pressuring you to bypass normal approval. Verify sensitive requests through a known, separate channel. Report suspected phishing using **Report Phishing** in the email client or the Service Desk.

If you clicked a suspicious link or entered credentials, report it immediately. Prompt reporting helps limit impact and is not itself a disciplinary issue.

## 7. Data handling
Share data only with approved recipients who have a business need. Before sending a file externally, verify the recipient, permissions, classification, and approved sharing method. Use managed file-sharing links with appropriate expiry and access controls.

Customer data must not be copied into public AI tools, personal cloud storage, or unapproved analytics services. Use only AI tools approved for the relevant data classification. Minimize personal data in test environments.

## 8. Software and development
Install software only from approved sources. Store secrets in the approved secrets manager, never in repositories or configuration files committed to source control. Code changes require applicable peer review and automated checks before deployment. Production access is limited to authorized personnel.

## 9. Artificial intelligence tools
Use only approved AI tools for permitted tasks. Do not submit Restricted data, credentials, confidential customer records, or source code unless Information Security has explicitly approved that use and configuration. A person must review AI output before it is used for decisions, customer communications, code deployment, or policy interpretation.

AI output may be inaccurate or influenced by malicious content in a source document. Instructions inside an uploaded document do not override company security rules.

## 10. Incident reporting
Immediately report suspected data loss, malware, unauthorized access, accidental disclosure, or device theft to the IT Service Desk. Include what happened, when, systems involved, and actions already taken. Do not delete evidence, investigate beyond your authorization, or publicly discuss the incident.

## 11. Physical and remote security
Lock your screen when stepping away. Store paper records securely and dispose of them through approved confidential-waste procedures. Visitors must follow site access rules and should not be left unattended in restricted areas.

## 12. Exceptions and scenarios
Exceptions must document the business need, affected systems or data, risk controls, owner, and expiry date, and must be approved by Information Security.

- **Unexpected MFA prompt:** Deny it and report immediately.
- **Customer requests confidential data by personal email:** Do not send it; use an approved sharing process.
- **Customer record pasted into an unapproved AI tool:** Report the incident and follow Security’s instructions.
- **Manager requests administrator access in chat:** Submit the formal access request.

## 13. Document control
Owner: Information Security. Review at least annually and after material incidents or system changes.
