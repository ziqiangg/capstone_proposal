---
id: "OPS-12"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-12

WHEN [[CYCLE_DEADLINE]] passes while scheduled Cycles are not paused and before that day's scheduled Cycle has closed, BEACON shall notify every Operator that the day's Briefing is late, and of what is holding it back, without the Operator having to consult BEACON.

**Rationale.** A failure that waits to be looked for is found when the Briefing is already missing. The deadline is the latest point at which lateness is announced, so the Operator can act during the grace period, before Readers miss anything. A Cycle that never started is late too. While an Operator has paused scheduled Cycles, no Briefing is due, so none is late.

**Verification.** none yet
