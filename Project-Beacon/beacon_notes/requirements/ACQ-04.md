---
id: "ACQ-04"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-04

IF a Collection returns an item that BEACON already holds and its extracted text is unchanged, THEN BEACON shall not process it as a new item.

**Rationale.** Repeat processing wastes effort and distorts every downstream count. The criterion for "the same item", across sources included, is an open question.

**Verification.** none yet
