---
id: "OPS-16"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-16

BEACON shall close a Cycle once every Collection in it has completed or timed out and it has no Unfinished item or, for a scheduled Cycle, once [[PUBLISH_GRACE_PERIOD]] has passed after [[CYCLE_DEADLINE]], whichever comes first.

**Rationale.** Waiting for every reachable item keeps the day's intelligence whole; the grace period stops one slow item from holding it indefinitely. Selection, trends and Publication all start from this point.

**Verification.** none yet
