---
id: "REL-01"
type: "requirement"
group: "REL"
verification: "none"
---
# REL-01

BEACON shall record a scope\_decision of IN, OUT or UNKNOWN, with its reason and the Scope Criteria version, for each Discovered item it does not already hold and that is not an Erased item, and for each Revision.

**Rationale.** Admission is the one point at which an item leaves the analysis, so the decision behind it must be on record. An unchanged item that a Collection returns again gets no new decision (ACQ-04).

**Verification.** none yet
