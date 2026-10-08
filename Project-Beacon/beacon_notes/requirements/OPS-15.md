---
id: "OPS-15"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-15

IF a source's Collection has not completed within [[COLLECTION_TIMEOUT]], THEN BEACON shall end that Collection and record the source as not collected in that Cycle.

**Rationale.** An unreachable source must not hold the day's Briefing: the day is Published without it (OPS-06), and the Operator sees it (OPS-07).

**Verification.** none yet
