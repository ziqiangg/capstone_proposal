---
id: "FBK-08"
type: "requirement"
group: "FBK"
verification: "none"
---
# FBK-08

WHEN a trigger in the Trigger Register occurs, BEACON shall, before re-deriving, add to the next Curator digest the number of records within [[REDERIVE_HORIZON]] that it would re-derive.

**Rationale.** Re-deriving can be costly, so the Curator, who owns the horizon, sees the size first and confirms or narrows it (FBK-10).

**Verification.** none yet
