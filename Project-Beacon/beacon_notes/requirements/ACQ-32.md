---
id: "ACQ-32"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-32

BEACON shall make each Re-extraction reading, where ACQ-30 caused it, the version of the Source Set entry under which the return was collected; otherwise, where a Curator has accepted a version of that entry as correcting the version under which the raw page it reads was collected, the latest version so accepted; and otherwise the version under which that raw page was collected.

**Rationale.** An item is read again under the entry it was collected under, so that a Re-extraction changes only what a release changed. A corrected version names the items it corrects, those collected under the version it corrects, and every later Re-extraction of them reads it, so that a later release's run does not undo the correction. A Re-extraction made for a comparison reads what the return was read under, so that the two sides differ only by what the source changed (ACQ-30).

**Verification.** none yet
