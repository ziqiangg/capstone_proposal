---
id: "OPS-14"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-14

IF a Stage fails for a Discovered item, THEN BEACON shall retry that Stage for that item automatically, up to [[STAGE_RETRY_LIMIT]] times within the Cycle.

**Rationale.** Most failures are transient. Without an automatic retry, one flaky call either holds the Briefing until someone intervenes or drops the item; OPS-10 remains for what the retries do not fix.

**Verification.** none yet
