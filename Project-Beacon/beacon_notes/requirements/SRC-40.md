---
id: "SRC-40"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-40

IF preparing a version under SRC-37 is ended by BEACON's own failure, at whatever point, THEN BEACON shall start that preparing again, a bounded number of times, the same at each close that starts one.

**Rationale.** A prepared version rests on a re-reading that finished (SRC-38). One that BEACON's own failure ended may show a part as not found because of BEACON's own crash or lost connection, so it gives no version and nothing reaches a Curator (SRC-39). Most failures are transient, so it is started again, its repeats bounded as an Onboarding's are (SRC-34); the bound is fixed by design. Where every repeat fails, the next close starts it again with the same bound (SRC-37), so a fixed fault yields a version unasked. The flags stay open meanwhile, in each Curator digest (SRC-17).

**Verification.** none yet
