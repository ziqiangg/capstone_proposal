---
id: "OPS-19"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-19

BEACON shall process each Unfinished item of a closed Cycle, and each of its Failed items that BEACON has not dropped since that Cycle began, as part of the next scheduled Cycle, resuming at the Stage it had reached.

**Rationale.** An item left out of one day's Briefing is not lost; it contributes to the next day's once it finishes. A Failed item is retried in later Cycles only up to a bound, after which it is dropped (OPS-27), so one broken item is not carried from Cycle to Cycle without end; if a later return of it is processed again, it is dropped again after as many failing Cycles, each time it comes back (OPS-27).

**Verification.** none yet
