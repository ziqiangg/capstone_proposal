---
id: "SRC-35"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-35

IF an Onboarding has been ended by BEACON's own failure and so has every repeat of it that SRC-34 allows, THEN BEACON shall report that failure once, with the link and the reason, in the next Operator digest.

**Rationale.** BEACON's failures go to the Operator, who can see a crash or a lost connection and fix it, as a failed Re-extraction is reported to the Operator (ACQ-40); a Curator cannot. A failure that a repeat cures is reported nowhere, as a Stage's failure that a retry fixes is not (OPS-14), so the report waits until the bounded repeats have all failed, and it is made once, as a dropped item is told once (OPS-28). Without it the failure would be silent, and a defect that keeps recurring would stay hidden.

**Verification.** none yet
