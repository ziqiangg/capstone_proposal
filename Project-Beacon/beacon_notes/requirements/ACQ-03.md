---
id: "ACQ-03"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-03

BEACON shall perform every Stage after Collection, in forward processing and in re-derivation alike, and every Re-extraction, from the item's retained Article Record and, in the field step and the record write, from what BEACON keeps of what the Collection returned for the item, without fetching the item from its source again or fetching anything that its raw page would load when rendered.

**Rationale.** Re-derivation and Re-extraction must stay possible when the original page is unavailable or has changed. What a kept page would load when rendered, its scripts or its data, is what is served now, not what was collected, so nothing is fetched for it; a kept page may be rendered again only where it can load nothing. Where a value cannot be derived from what is retained, nothing is fetched to fill it. The field step and the record write work on a return before the record holds it, so they read what BEACON keeps of the Collection's return, any text not yet recorded included (ACQ-17), beside what the record of a held item retains, and an attempt that fails is retried from them (OPS-14). A Collection, including one that returns an item BEACON already holds, is a fetch and is not bound by this row.

**Verification.** none yet
