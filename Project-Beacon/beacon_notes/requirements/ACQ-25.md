---
id: "ACQ-25"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-25

BEACON shall record with an Encounter that the return was not compared with the item's retained version (ACQ-06) where, and only where, the Encounter is of an Erased item.

**Rationale.** An Erased item's retained text and raw page were removed (ACQ-17, ACQ-18), so its return cannot be compared, and since nothing of the return is kept (ACQ-22), whether the item changed at its source is not known; the Encounter says so rather than be read as an unchanged return. The first return of an item BEACON holds whose erasure was lifted is kept as a Revision marked as made without comparison (ACQ-27), and that of an item it does not hold as a new item (ACQ-02); neither is marked here. Every other held item's Article Record keeps a raw page (ACQ-02, ACQ-06, ACQ-27), so its return can be compared; a return whose comparison fails is not marked, so that a defect is never recorded as an ordinary state.

**Verification.** none yet
