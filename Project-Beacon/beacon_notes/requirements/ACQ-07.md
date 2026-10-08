---
id: "ACQ-07"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-07

WHEN [[EXCLUDED_TEXT_RETENTION]] has passed since a Discovered item received a scope\_decision of OUT that no later scope\_decision replaced, or since BEACON last dropped an item of which BEACON has since processed no return other than one recorded as an Encounter with unchanged extracted text (ACQ-04), BEACON shall erase that item's extracted text, keeping the rest of its Article Record and its scope decision.

**Rationale.** The text of an item no statement rests on is kept so that a trigger can re-derive its scope decision. This row erases it only where a Curator sets [[EXCLUDED_TEXT_RETENTION]] to a duration, where storing it costs more than it serves. Title, URL, reason and scope decision stay, so UIX-07 still shows the item to Readers.

**Verification.** none yet
