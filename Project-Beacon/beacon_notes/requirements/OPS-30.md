---
id: "OPS-30"
type: "requirement"
group: "OPS"
verification: "none"
---
# OPS-30

WHEN the Re-extractions that one release, one Curator's acceptance of a corrected Source Set entry or one Operator's command causes (ACQ-28, ACQ-29, ACQ-31) have each been made or failed, BEACON shall report in the next Operator digest, in one entry, how many fields the versions they recorded hold with no kept value for not meeting the rows (ACQ-12), per source, part failed and field, naming each, never a value, each count above zero.

**Rationale.** These Re-extractions are one run, one trigger however many versions they change (GOV-06), and part of no Stage (A-terms, Stage). Their breaches are BEACON's defects from that run, so they are kept under it, apart from a Cycle's (OPS-29), as its failures go to the Operator (ACQ-40): folded into a Cycle's count, they would hide whether the source's pages or BEACON's release broke the rows. The entry waits until each is made or failed, as the Curator's count does (ACQ-37). No value is shown (ACQ-18); a zero is left out (OPS-22).

**Verification.** none yet
