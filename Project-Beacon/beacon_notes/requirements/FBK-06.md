---
id: "FBK-06"
type: "requirement"
group: "FBK"
verification: "none"
---
# FBK-06

BEACON shall begin forward processing of each item it discovers that it does not already hold and that is not an Erased item, each Revision and each item that joins a development, in the Cycle in which that item is discovered or joins.

**Rationale.** New input is always processed, so BEACON keeps up with the field. Processing begins with the scope decision (REL-01). A Stage that fails is retried (OPS-05, OPS-10), so the row requires processing to begin in that Cycle, not to finish in it.

**Verification.** none yet
