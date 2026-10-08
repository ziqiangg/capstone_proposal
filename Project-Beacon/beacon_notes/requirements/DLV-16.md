---
id: "DLV-16"
type: "requirement"
group: "DLV"
verification: "none"
---
# DLV-16

IF a Delivery attempt to a recipient fails, THEN BEACON shall retry it up to [[DELIVERY_RETRY_LIMIT]] times.

**Rationale.** A transient channel failure should not cost a recipient that day's Delivery.

**Verification.** none yet
