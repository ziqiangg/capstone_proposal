---
id: "ACQ-06"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-06

WHEN a Collection returns an item that BEACON already holds, that is not an Erased item and whose Article Record keeps a raw page, with extracted text that differs from the retained version, BEACON shall record the new version, with the raw page it was extracted from, as a Revision of that item and keep the prior version.

**Rationale.** Deduplication by URL and title cannot detect a revision. Any difference in the extracted text is the material change the Revision term requires; extracted text leaves out page furniture (A-terms), so a changed footer or banner is not a Revision. A Revision is forward-processed (FBK-06). Its raw page is kept as the first one is (ACQ-02), so that a Re-extraction can extract its text again (A-terms) and a reviewer can open every place a value was found. The return of an Erased item keeps nothing but, where BEACON holds the item, its Encounter (ACQ-22), so it is never a Revision; the first return of an item BEACON holds whose erasure was lifted cannot be compared, since its text and raw page were removed, and is kept as ACQ-27 says, and that of an item BEACON never held is kept as a new item (ACQ-02).

**Verification.** none yet
