---
id: "ACQ-40"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-40

WHEN a Re-extraction that ACQ-28, ACQ-29 or ACQ-31 causes fails, BEACON shall report that failure, with the item, its source and the reason the Re-extraction failed, in the next Operator digest.

**Rationale.** A Re-extraction in a run is not part of a Stage (A-terms), so its failure makes no Failed item: it is not counted against the item's source (SRC-12), since the fault lies in BEACON's run, not in what the source offers, and it is reported to the Operator, whose runtime it is. A Re-extraction that fails gives no result, so nothing is recorded (ACQ-09, ACQ-33) and the item stays on its latest version. Where that version was not made by the procedures BEACON now runs and under the Source Set entry a return is collected under, the item is re-extracted when it returns (ACQ-30); the Operator's command (ACQ-31) reaches it in any case. ACQ-28 and ACQ-29 except such an item, so its source's Collection is not held back by it, and the run's count is added once every Re-extraction in it has been made or has failed (ACQ-37). A returning item's Re-extraction is part of its record write, and fails as a Stage does (A-terms).

**Verification.** none yet
