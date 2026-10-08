---
id: "OPS-13"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-13

WHEN a Delivery has any recipient whose outcome is failed after its retries, BEACON shall add to the next Operator digest, once for that Delivery, the number of recipients affected and the reasons.

**Rationale.** One entry per Delivery, not one per failed recipient; it is neither a late Briefing nor a Failed item, so it waits for the daily digest.

**Verification.** none yet
