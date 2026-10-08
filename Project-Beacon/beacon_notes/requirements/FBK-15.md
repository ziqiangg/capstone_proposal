---
id: "FBK-15"
type: "requirement"
group: "FBK"
verification: "none"
---
# FBK-15

WHEN a trigger in the Trigger Register occurs, BEACON shall add to the next Operator digest the trigger and the number of records within [[REDERIVE_HORIZON]] that it would re-derive.

**Rationale.** Re-derivation loads the system the Operator runs, so the Operator is informed; the decision stays with the Curator (FBK-08, FBK-10). OPS-07 shows its progress.

**Verification.** none yet
