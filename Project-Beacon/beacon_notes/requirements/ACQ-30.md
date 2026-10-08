---
id: "ACQ-30"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-30

WHEN a Collection returns a held item that is not an Erased item and whose Article Record keeps a raw page, BEACON shall make a Re-extraction of the item before comparing the return with the item's retained version under ACQ-06, unless the versions recorded with the item's latest version (ACQ-36), or with its latest confirmation of that version (ACQ-33), are those of the procedures that BEACON now runs and of the Source Set entry under which the return was collected, and ACQ-07 did not erase the text of the version holding the item's latest raw page.

**Rationale.** A return is compared with what BEACON holds (ACQ-06). If the held text was made by an earlier procedure, or read under another version of the source's entry, the two sides would differ by BEACON's change as well as the source's, and the return would be recorded as a Revision when the source changed nothing. Extracting the held page again first, reading the entry version the return was read under (ACQ-32), leaves only what the source changed. An item whose text was erased under ACQ-07 holds no text to compare, so its page is always extracted again for the comparison, and no row records anything of that Re-extraction (ACQ-09, ACQ-33): the text it gives serves the comparison alone. An item whose record keeps no raw page returns under ACQ-27, and an Erased item under ACQ-22.

**Verification.** none yet
