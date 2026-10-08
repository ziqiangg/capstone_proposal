---
id: "ACQ-41"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-41

WHEN a Curator erases an item that BEACON holds and for which BEACON keeps what a Collection returned but has not yet recorded in the item's Article Record, BEACON shall complete the record write of that return with its Encounter alone.

**Rationale.** The erasure removes the text and page that BEACON kept of the return (ACQ-17, ACQ-18), so a field step or record write tried again would have nothing to read and would fail until the item was dropped, counting a Curator's act against the source (SRC-12) and alerting the Operator to an item removed on purpose (OPS-28). The return ends as the return of an Erased item does (ACQ-22): its Encounter is recorded (ACQ-05), which says the source still listed the item, and nothing else; an Erased item has no field step (A-terms, Stage). With its record write complete, nothing of that return is left to retry (OPS-14, OPS-19), so the erasure makes no Failed item, adds nothing to its source's count and leads to no drop or alert. A failure recorded before the erasure stays as recorded (EVD-10, SRC-12). An item that BEACON does not hold has no record to take an Encounter (A-terms, Encounter), and its return ends under ACQ-42.

**Verification.** none yet
