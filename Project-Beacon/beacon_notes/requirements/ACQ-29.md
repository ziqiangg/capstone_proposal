---
id: "ACQ-29"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-29

WHEN a Curator accepts a version of a source's Source Set entry as correcting an earlier version of that entry, BEACON shall make, before that source's next Collection, a Re-extraction of every item of that source that is not an Erased item and whose latest raw page was collected under the earlier version, however long ago it was collected, other than an item whose Re-extraction under this row fails (ACQ-40).

**Rationale.** The text and fields of an item collected under a faulty entry were shaped by the fault. Raw pages are kept (ACQ-02), so every such item can be read again under the corrected version (ACQ-32), however late the fault is found. Doing so before the source's next Collection means that Collection compares its returns with texts made under the corrected entry.

**Verification.** none yet
