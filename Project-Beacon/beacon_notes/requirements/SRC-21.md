---
id: "SRC-21"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-21

WHEN a Cycle closes, BEACON shall raise, for each source's Drift check for that Cycle, a Drift flag on the check's version for each whole-Collection event (A-terms, Drift sign) that the source's Collection in that Cycle met under that version and the check covers by that Collection meeting it, a listing with no entries only where no listing read under that version before it was put into effect had none.

**Rationale.** Three things a source's Collection can meet as a whole leave no item to judge and no baseline for a rate: an empty listing; a listing answered only with pages that show nothing of where it is, as a bot wall's are; and every listed item BEACON tried to fetch refused in every way. None makes a Failed item (ACQ-01, SRC-12), so each raises a flag on its first occurrence, as a contradiction does (SRC-20). An empty listing is not news for a source whose listing was empty before its version was put into effect; a bot wall always is.

**Verification.** none yet
