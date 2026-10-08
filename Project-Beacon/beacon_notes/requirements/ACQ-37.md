---
id: "ACQ-37"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-37

WHEN the Re-extractions that one release, one Curator's acceptance of a corrected Source Set entry or one Operator's command causes (ACQ-28, ACQ-29, ACQ-31) have each been made or have failed, and have recorded any new version, BEACON shall add to the next Curator digest, once for them, the number of new versions they recorded.

**Rationale.** A release can change thousands of versions; one entry with their number, not one per version, keeps the digest readable. The count includes items older than the horizon of re-derivation, which gain the new version and have nothing re-derived; FBK-08 adds, for the same trigger, the number of records within that horizon it would re-derive. A returning item's Re-extraction (ACQ-30) is part of the record write of that return, a Stage after its Collection (A-terms, Stage), and is not counted here.

**Verification.** none yet
