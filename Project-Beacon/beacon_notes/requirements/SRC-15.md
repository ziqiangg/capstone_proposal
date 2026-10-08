---
id: "SRC-15"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-15

BEACON shall provide a Curator with the means to keep a source that has reached [[SOURCE_FAILURE_LIMIT]], recording the Curator, the time and the reason.

**Rationale.** Keeping a failing source is a decision, as disabling or removing it is, so it should be made explicitly and leave its reason on record; otherwise a flagged source stays in limbo. Keeping it restarts its count (SRC-12), so the source is flagged again if its failures pile up anew.

**Verification.** none yet
