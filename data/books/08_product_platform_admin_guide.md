
## 1. Product overview
Northstar Workspace is a fictional collaboration platform used to manage projects, share approved files, assign tasks, and review activity. This guide is test content, not a real vendor manual.

## 2. Workspace roles
- **Workspace Owner:** Manages workspace settings, billing contacts, and ownership transfer.
- **Administrator:** Manages members, groups, approved integrations, and selected configuration.
- **Member:** Creates and edits content according to project permissions.
- **Guest:** Accesses only projects or files explicitly shared with them.

Assign the least privileged role needed. A user who needs access to one project should not automatically receive workspace-wide administrator permissions.

## 3. Inviting a member
1. Open **Workspace Settings**.
2. Select **Members**.
3. Choose **Invite Member**.
4. Enter the work email and intended role.
5. Review the invitation and send it.
6. Confirm the user appears as Pending until acceptance.

If the invitation does not arrive, verify the email, check spam or quarantine, and confirm the domain is allowed by organization settings. If the issue remains, raise a support ticket with workspace ID and approximate invitation time. Never ask for the user’s password.

## 4. Changing a member’s role
Open Workspace Settings, select Members, locate the user, choose Edit Role, select the minimum required role, and save. Role changes may affect access immediately. Confirm the business reason and follow internal approval before granting administrator privileges.

If a change does not appear, ask the user to refresh and sign in again if appropriate. Escalate persistent problems with user ID, workspace ID, current role, intended role, and timestamp.

## 5. Projects and permissions
Projects may be private to invited members or visible to a wider workspace audience. File permissions may be more restrictive than project visibility. Before sharing a link externally, inspect its audience, expiry, and download settings. Copying a link does not necessarily grant access.

For “Access denied,” check:
- whether the user is signed into the correct account;
- whether they belong to the workspace;
- whether they have project membership;
- whether the file has additional restrictions;
- whether the link expired or was revoked.

Do not bypass a permission error by making confidential content public. Ask the content owner to grant correct access.

## 6. Integrations
Only administrators may enable workspace-wide integrations. Confirm the integration is on the approved list and review requested permissions. Grant only the scopes needed for the workflow.

If syncing stops, check connection status, authorization expiry, service status, and recent configuration changes. Reauthorize only through the approved flow. Never paste an integration token into a ticket or public channel.

## 7. Notifications
Users can configure email and in-app notifications for assignments, mentions, comments, and project activity. For missing notifications, check preferences, project membership, email delivery status, and organization restrictions. A delay does not necessarily mean the underlying task or comment was lost; verify the record in the application.

## 8. Audit logs
Authorized administrators may review available audit events for membership changes, permission updates, integration activity, and selected administrative actions. Logs may not contain the full content of messages or files. Access logs only for a legitimate business purpose.

For an audit-log issue, include approximate time range, actor if known, action type, and workspace ID. Absence of a visible event does not prove an action did not occur; retention and event coverage may vary.

## 9. Data export and deletion
Requests to export or delete organization data must follow the approved privacy and administrative process. Verify the requester’s authority and scope before an irreversible action. Route requests involving personal data to the designated privacy contact. This guide does not authorize overriding legal holds or retention requirements.

## 10. Troubleshooting
**Cannot sign in:** Confirm the account and identity provider, check service status, and use approved account recovery.

**Can open project but not file:** Check file-level permissions, link expiry, and owner restrictions.

**Integration stopped syncing:** Check connection, authorization, service status, and recent changes; reauthorize through the approved workflow if appropriate.

**Too many alerts:** Review notification preferences and project subscriptions before changing organization-wide settings.

**Member has left the company:** Follow the identity and offboarding process. Remove or transfer access through approved controls, never by sharing credentials.

## 11. Known limitations
Some changes may take several minutes to propagate. The status page is the source for known incidents. Available features depend on plan and configuration. If a setting is not visible, verify plan and product version before assuming the interface is broken.

## 12. Escalation and document control
Contact Product Operations for configuration questions, IT Service Desk for identity or device problems, and Information Security for suspected unauthorized access or exposure. Include relevant identifiers and timestamps, but never passwords, authentication codes, or secrets. Owner: Product Operations. Review quarterly or after significant product changes.
