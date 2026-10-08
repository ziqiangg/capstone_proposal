---
id: "OPS-01"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-01

WHILE scheduled Cycles are not paused, BEACON shall, without a person starting it, start one scheduled Cycle on each calendar day, no earlier than 00:00 of that day, reckoned in [[CYCLE_DEADLINE]]'s timezone.

**Rationale.** A product that has to be started by someone stops being started. The daily cadence is fixed, not a parameter. A Cycle may run past the time its Briefing is due rather than publish unfinished work (OPS-16). While an Operator has paused scheduled Cycles (OPS-09), none starts, and no Briefing is due (OPS-12).

**Verification.** none yet
