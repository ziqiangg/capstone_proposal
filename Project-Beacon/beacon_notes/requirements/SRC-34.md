---
id: "SRC-34"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-34

IF an Onboarding is ended by BEACON's own failure, at whatever point, THEN BEACON shall start that Onboarding again from the same link, a bounded number of times.

**Rationale.** A refusal rests on an Onboarding that finished looking (A-terms, Onboarding outcome). One that BEACON's own failure ended did not: a way that seemed to reach no page, or a listing not yet found, may be BEACON's own crash or lost connection. So it gives no outcome, nothing reaches a Curator as refused or proposed (SRC-27), and grounds it observed are not made a refusal; a finished repeat observes them again. Most failures are transient, so it is started again, its repeats bounded as a Stage's retries are (OPS-14); the bound is fixed by design, no parameter covering an Onboarding.

**Verification.** none yet
