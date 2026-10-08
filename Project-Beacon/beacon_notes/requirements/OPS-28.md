---
id: "OPS-28"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-28

WHEN BEACON drops an item, BEACON shall notify every Operator, once for that item, naming the item, its source and its failure reasons.

**Rationale.** An item that has failed in every Cycle allowed is an article that BEACON stops processing unless a later return of it is processed again (OPS-27), which the Operator hears of without having to consult BEACON. One alert per dropped item, never one per Cycle or per later drop of the same item, keeps the alert rare enough to be read; the dropped item is also logged in the Operator digest (OPS-23).

**Verification.** none yet
