---
id: "OUT-09"
type: "requirement"
group: "OUT"
verification: "none"
---
# OUT-09

BEACON shall not state, in any output it Publishes or Delivers, whether a Cycle was complete, whether that output is late, or that any Stage, item or source failed.

**Rationale.** A Reader needs the intelligence, not BEACON's internal state; processing, lateness and failure are logged for the non-Reader roles (OPS-02, OPS-07). A correction or a withdrawal concerns content, not a failure, so correction marks and holding, correction and restore notices are unaffected.

**Verification.** none yet
