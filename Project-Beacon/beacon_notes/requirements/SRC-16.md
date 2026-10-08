---
id: "SRC-16"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-16

WHEN a Cycle closes, BEACON shall raise, for each source's Drift check for that Cycle, a Drift flag on the check's version for each thing the check covers, other than by one page contradicting it or one Collection meeting it (SRC-20, SRC-21), in which what BEACON read, recorded or met over that version's Drift window for that thing ([[DRIFT_WINDOW]]) departs from its Drift reference by more than chance alone would give with a probability of [[DRIFT_ALPHA]].

**Rationale.** A source's pages change without notice, as when a redesign moves the byline. Collections still complete, so no failure is recorded (SRC-12), yet what BEACON reads is wrong. Each version is judged against its own Drift reference, and as a rate, so an occasional page with no article on it raises no flag where a rise does. Flags are raised when a Cycle closes (OPS-16), as a flag reaches the Curator only through the daily digest (A-terms, Digest), and not for a source disabled by then, disabling being already an answer (SRC-01). How a departure is judged is fixed by design.

**Verification.** none yet
