---
id: "SRC-20"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-20

WHEN a Cycle closes, BEACON shall raise, for each source's Drift check for that Cycle, a Drift flag on the check's version for each thing that version holds about the source's pages that an item in that version's Drift window for that thing ([[DRIFT_WINDOW]]) contradicts and that the check covers by one page contradicting it.

**Rationale.** A contradiction, a page showing untrue something the entry holds about the source's pages, is not produced by chance, so one raises a flag without a rate. It is looked for in the Drift window SRC-16 judges most things over, so what is judged is fixed at the close. After a Curator keeps the version despite a flag for that thing, the next page that contradicts it is not news, so how often the pages contradict it is then judged as a rate (SRC-16; A-terms, Drift sign).

**Verification.** none yet
