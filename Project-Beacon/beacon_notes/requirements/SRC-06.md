---
id: "SRC-06"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-06

WHEN [[SOURCE_SILENCE_PERIOD]] has passed since an enabled source last yielded an item, or since it was enabled if it has yielded none, BEACON shall add that source, once for that silence, to the next Curator digest.

**Rationale.** Silence is not an error, so no failure record fires. It has to be pushed rather than waited for, once so that it does not repeat every Cycle, and in the daily digest so that it does not interrupt.

**Verification.** none yet
