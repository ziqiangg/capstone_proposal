---
id: "FBK-07"
type: "requirement"
group: "FBK"
verification: "none"
---
# FBK-07

BEACON shall re-derive a Judgement it has already recorded only on a trigger in the Trigger Register, an Operator's retry (OPS-10) or a Curator's merge or split (DEV-13).

**Rationale.** Output already recorded changes only for a registered reason, so it stays predictable and testable. A Curator's correction is not a cause: it records the corrected value and re-runs nothing (FBK-03), except that a merge or split leaves the Judgements resting on membership stale, so those are re-derived (DEV-13).

**Verification.** none yet
