---
id: "SRC-17"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-17

BEACON shall add each open Drift flag to each Curator digest sent while that flag is open, naming the source, the version of its Source Set entry and the thing the flag names, with what BEACON saw, how many of the source's items that are not Erased items have their latest raw page collected under that version, which a version correcting it would reach (ACQ-29), and how many of the source's items whose Article Record keeps no raw page have their latest version recorded as made under that version (ACQ-36), which it would not, and, where a preparing for it found no Entry part or Standing to change (SRC-37), that it found none.

**Rationale.** A flag needs a Curator's decision, since the Curator owns the Source Set: disable the source (SRC-01), accept a version of its entry correcting the flagged one (ACQ-29), or keep the flagged version with a reason (SRC-18); the flag is open until one of them, or until nothing is left for it to act on (A-terms, Open (Drift flag)). A silence reports itself once (SRC-06), but an open flag means records are still being made under a version that may be reading the source wrongly, so it is repeated in each digest until it is decided. The two counts say what a correction would still reach; raw pages are kept until an erasure under ACQ-08 removes them (ACQ-02, ACQ-18), so the second count is normally zero. A Drift flag is not a Failed item, so it adds nothing to the source's count (SRC-12) and alerts no Operator.

**Verification.** none yet
