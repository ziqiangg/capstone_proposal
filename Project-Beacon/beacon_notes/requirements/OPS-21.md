---
id: "OPS-21"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-21

WHEN a source's count of Failed items reaches [[SOURCE_FAILURE_LIMIT]], BEACON shall notify every Operator, naming the source.

**Rationale.** Items that keep failing from one source may point at BEACON's own runtime, a broken extraction or a blocked address, which is the Operator's to check. One alert per source when its failures pile up, beside the single alert for each item BEACON drops, replaces an alert per Failed item or per day, which would train the Operator to ignore them; the Curator decides the source's future (SRC-14, SRC-15).

**Verification.** none yet
