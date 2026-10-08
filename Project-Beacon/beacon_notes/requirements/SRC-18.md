---
id: "SRC-18"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-18

BEACON shall provide a Curator with the means to keep a version of a source's Source Set entry despite what an open Drift flag on it names, recording the Curator, the time and the reason.

**Rationale.** A Curator may judge that what a flag shows is the source's own change and not a fault of its entry, such as a source that has stopped naming its authors. Keeping the version is a decision, as disabling the source or correcting its entry is, so it is made explicitly and leaves its reason on record, as a keep of a failing source does (SRC-15); without it a flag the Curator does not act on stays open. A keep closes the flag (A-terms, Open (Drift flag)), and from then on that version is judged for what the flag named only on what came since the keep (SRC-16; A-terms, Drift window, Drift reference).

**Verification.** none yet
