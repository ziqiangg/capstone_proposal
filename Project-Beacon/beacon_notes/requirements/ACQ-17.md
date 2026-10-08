---
id: "ACQ-17"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-17

WHEN a Curator erases an item under ACQ-08, or BEACON erases an item's extracted text under ACQ-07, BEACON shall remove the extracted text of every version that the item's Article Record then holds, and any extracted text of the item that BEACON holds but has not yet recorded in a version.

**Rationale.** Split from ACQ-08. An item's text may be held in several versions (ACQ-06, ACQ-09), and as text not yet recorded while a step is retried; an erasure that left any of them would not have erased the text. A version recorded after the erasure is not reached by it, so an item whose text ACQ-07 erased, or whose erasure a Curator lifted (ACQ-23), can be kept again when it returns.

**Verification.** none yet
