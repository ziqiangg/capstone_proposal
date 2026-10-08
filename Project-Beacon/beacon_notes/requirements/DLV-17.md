---
id: "DLV-17"
type: "requirement"
group: "DLV"
verification: "none"
---
# DLV-17

IF Deliveries to a recipient fail [[RECIPIENT_FAILURE_LIMIT]] times in a row, THEN BEACON shall stop delivering to that recipient, record why, and show the Reader in the interface how to resume by re-linking their chat account.

**Rationale.** A chat account that keeps failing no longer reaches its Reader, and sending on to it hides that. Re-linking (DLV-18) shows that the Reader has a working chat account again.

**Verification.** none yet
