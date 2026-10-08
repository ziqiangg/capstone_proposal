---
id: "SRC-14"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-14

WHEN a source's count of Failed items reaches [[SOURCE_FAILURE_LIMIT]], BEACON shall add that source, with its Failed items and their failure reasons, to the next Curator digest.

**Rationale.** The Curator owns the Source Set, so the Curator decides whether to keep the source (SRC-15), disable it (SRC-01) or remove it from the Source Set. The daily digest carries the flag without an interruption; the Operator is alerted separately to check whether BEACON's own runtime is at fault (OPS-21).

**Verification.** none yet
