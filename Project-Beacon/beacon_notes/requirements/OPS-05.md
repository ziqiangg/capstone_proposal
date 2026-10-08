---
id: "OPS-05"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-05

WHEN BEACON resumes an interrupted Cycle, or an Operator retries failed work (OPS-10), BEACON shall run only the Stages that failed or did not run, for the items and sources they affect.

**Rationale.** A resumption that redoes everything is a restart, and nobody will use it. Automatic resumption, after a host restart for example, serves continuity (E).

**Verification.** none yet
