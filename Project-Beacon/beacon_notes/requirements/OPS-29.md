---
id: "OPS-29"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-29

BEACON shall show every Operator, in the Operator view for the latest Cycle closed (OPS-07) and in the Operator digest for each Cycle it reports (OPS-23), how many fields held with no kept value for not meeting the rows (ACQ-12) were in versions recorded by record writes completed by its close and after the previous Cycle's close, if any, per source, part failed and field, naming each, never a value, each count above zero.

**Rationale.** A field that breaks the rows is held with no kept value (ACQ-12); the breach is BEACON's defect, the Operator's to act on. A record write includes a returning item's Re-extraction (ACQ-30), so a release whose procedure breaks the rows shows here, which the Curator's Health entry leaves out (A-terms, Counted version). Bounded by two closes, each record write counts for one Cycle; a run's Re-extractions, part of no Stage, are reported by run (OPS-30). No value is shown (ACQ-18). A zero is left out, so a digest still goes only with an entry (OPS-22).

**Verification.** none yet
