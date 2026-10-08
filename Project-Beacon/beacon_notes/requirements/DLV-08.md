---
id: "DLV-08"
type: "requirement"
group: "DLV"
verification: "none"
---
# DLV-08

WHEN BEACON Publishes a scheduled Cycle's Briefing, BEACON shall send that day's Delivery at [[DELIVERY_SCHEDULE]] or, if the Briefing is Published after that time, as soon as it is Published, unless delivery is suspended or no development qualifies for that Delivery.

**Rationale.** A Delivery always follows that day's publication, so a late Briefing delays the day's Delivery and never causes an older one to be sent. A fixed time of day lets recipients expect it. A day on which nothing is Published has no Delivery. While delivery is suspended, the day's Delivery is recorded as skipped (DLV-21); when no development qualifies, nothing is sent (DLV-20).

**Verification.** none yet
