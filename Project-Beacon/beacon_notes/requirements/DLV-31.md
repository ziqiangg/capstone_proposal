---
id: "DLV-31"
type: "requirement"
group: "DLV"
verification: "none"
---
# DLV-31

WHEN [[PERSONAL_DATA_RETENTION]] has passed since a Reader stopped being a recipient, BEACON shall erase that Reader's linked chat account and the Delivery outcomes recorded for it, keeping, for each Delivery, the number of recipients per outcome.

**Rationale.** A former recipient's chat account serves no purpose once no Delivery can go to it. Counts per outcome keep delivery health visible to the Operator without keeping who received what. A Reader who opts in again links a chat account again (DLV-26).

**Verification.** none yet
