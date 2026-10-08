---
id: "ACQ-42"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-42

WHEN a Curator erases an item that BEACON does not hold and for which BEACON keeps what a Collection returned, BEACON shall complete the record write of that return, recording nothing of it.

**Rationale.** An item that BEACON does not hold has a return kept and not yet recorded only because its field step or record write failed or has not completed (A-terms, Stage); a takedown must hold whether or not BEACON had finished recording the item. The erasure removes what was kept (ACQ-17, ACQ-18), and the item has no Article Record, so no Encounter can be recorded (A-terms, Encounter) and nothing of the return is. With its record write complete, nothing of that return is left to retry (OPS-14, OPS-19), so the erasure makes no Failed item, adds nothing to its source's count (SRC-12) and leads to no drop or alert (OPS-27, OPS-28). The erasure persists: the item is an Erased item until a Curator lifts the erasure (A-terms; ACQ-23), so a later return of it is given no Article Record (ACQ-02) and nothing of it is retained (ACQ-22). The erasure's own record (ACQ-08), who erased it, when and why, is the trace. A failure recorded before the erasure stays as recorded (EVD-10, SRC-12).

**Verification.** none yet
