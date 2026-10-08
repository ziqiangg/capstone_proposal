---
id: "OPS-27"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-27

IF an item has been a Failed item in [[ITEM_RETRY_CYCLES]] Cycles, not counting any Cycle before the one in which a Collection first returned it after BEACON last dropped it, THEN BEACON shall stop processing it and record it as dropped, with its source and its failure reasons.

**Rationale.** An item that fails day after day costs processing and would keep its source's failures in view for ever; after a bounded number of attempts it is dropped, and the record keeps it visible to the non-Reader roles (OPS-23). A dropped item that a later Collection returns is processed as that return is, and the Cycles counted towards a drop start again at the first such return, so that a defect fixed since lets the return through, while an item that still fails is dropped again after as many Cycles as before, each time it comes back. It stays the same item, so the Operator is told only once that it was dropped (OPS-28), and its source counts it once (SRC-12).

**Verification.** none yet
