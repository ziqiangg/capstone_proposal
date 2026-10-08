---
id: "ACQ-35"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-35

BEACON shall make no Re-extraction of an Erased item.

**Rationale.** An erasure under ACQ-08 answers a request that the item not be kept; extracting it again would bring back what the erasure removed. An Erased item keeps no raw page once the erasure is made (ACQ-18); this row holds as well while that removal is under way, and when the Operator names the item (ACQ-31). After a lift the item is not an Erased item, but a held item's record keeps no raw page until it returns (ACQ-27), and an item BEACON does not hold has no record until it returns (ACQ-02).

**Verification.** none yet
