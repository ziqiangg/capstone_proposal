---
id: "DLV-27"
type: "requirement"
group: "DLV"
verification: "none"
---
# DLV-27

BEACON shall send a recipient, for any one development on any one day, at most one holding notice, at most one correction notice and at most one restore notice.

**Rationale.** Each notice is an interruption. A withdrawal followed by its correction or its restore needs both messages, so each kind is counted apart; a second notice of the same kind for the same development on the same day would only repeat what the recipient was already told.

**Verification.** none yet
