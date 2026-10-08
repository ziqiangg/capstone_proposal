---
id: "ACQ-14"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-14

BEACON shall record a Supplied value's procedure in the item's Article Record by naming that procedure's version, keeping that version's description, with the model's identity, the wording of its prompt and its settings where a model supplies values, once for as long as any Article Record names that version, that description leaving out the Source Set entry under which the value was supplied, which is not part of a procedure's settings and whose version ACQ-36 records.

**Rationale.** Split from ACQ-02. A procedure's description is kept once for each version rather than with every value, and a source's Source Set entry is not part of it, so that a change to one source's entry does not change the procedure's version for every source; the procedure's version, and the entry's version recorded with the version of the record that holds the value (ACQ-36), together trace what produced a value. A value supplied in a Collection was supplied under the entry the item was collected under; one supplied in a Re-extraction, under the entry that ACQ-32 sets.

**Verification.** none yet
