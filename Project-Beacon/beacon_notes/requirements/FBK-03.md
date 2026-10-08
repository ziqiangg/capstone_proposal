---
id: "FBK-03"
type: "requirement"
group: "FBK"
verification: "none"
---
# FBK-03

WHEN a Curator corrects a Judgement, BEACON shall use the corrected Judgement in place of the original in everything it composes afterwards, without re-deriving any other Judgement, except as DEV-13 requires.

**Rationale.** A correction is a person's emergency fix of what BEACON got wrong, not a re-run of the analysis: the corrected value is recorded, with the original kept (FBK-02), so that the error does not reappear in later output, and nothing else changes because of it. This holds whether the Curator corrects the Judgement on its own (FBK-01) or as part of correcting a Published development (FBK-16), and a later re-derivation on a trigger does not overwrite it (FBK-21). A merge or a split is the one exception: the Judgements that rest on a development's membership are re-derived for each resulting development (DEV-13).

**Verification.** none yet
