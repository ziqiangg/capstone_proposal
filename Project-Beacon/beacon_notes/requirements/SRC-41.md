---
id: "SRC-41"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-41

IF preparing a version under SRC-37 has been ended by BEACON's own failure and so has every repeat of it that SRC-40 allows, THEN BEACON shall report that failure in the next Operator digest, with the source, the flagged version and the reason, for each flag it answers that no earlier such report names.

**Rationale.** BEACON's failures go to the Operator, who can see a crash or a lost connection and fix it, as a failed Onboarding is reported (SRC-35); a Curator cannot. A failure that a repeat cures is reported nowhere, as a Stage's failure that a retry fixes is not (OPS-14). A flag tried again at each later close (SRC-37) is reported once, when its preparing first fails every repeat, as a dropped item is told once (OPS-28), lest a lasting fault alert the Operator daily. A finished preparing ends the trying (SRC-37). The flags stay open, in each Curator digest (SRC-17).

**Verification.** none yet
