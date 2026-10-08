---
id: "ACQ-38"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-38

WHEN a Collection returns an item for which BEACON keeps what an earlier Collection returned but has not yet recorded in the item's Article Record, BEACON shall replace what it keeps of the earlier return with that return.

**Rationale.** What an earlier return left unrecorded is kept only because its field step or record write failed or has not completed (A-terms, Stage). A later return is what the source offers now, so the field step and the record write work on it from then on (ACQ-03), and a page that kept failing is not tried again in place of a newer one. The item stays the same item: if it is a Failed item that BEACON has not dropped, its Cycles go on being counted towards a drop, and if BEACON dropped it, the count starts again with the first return since (OPS-27); its source counts it once (SRC-12). An erasure removes what is kept before it is recorded (ACQ-17, ACQ-18) and completes that return's record write (ACQ-41, ACQ-42), and a later return of an Erased item keeps nothing that is not recorded (ACQ-22), so this row has nothing to replace for an item erased since.

**Verification.** none yet
