---
id: "ACQ-02"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-02

BEACON shall retain an Article Record for each Discovered item it does not already hold and that is not an Erased item, containing its extracted text; its source, URL and collection time; its title, Item publisher, Authors and Source publication time, each in a Field state (ACQ-10); where the item credits as its author its Item publisher, or its source where the source is recorded in place of its Item publisher, that it does, that credit never being recorded among its Authors; and its raw page.

**Rationale.** Every later Stage reads these fields (ACQ-03). Keeping them for items that are not admitted lets a scope decision be re-derived after the Scope Criteria change. The Item publisher is kept apart from the Authors, so that a site's own name is never read as a credit; where an item credits its Item publisher, or the source recorded in place of it, the record says so and the credit is read as the publisher's own, never as an Author. ACQ-06 keeps each Revision's prior version. The raw page is kept with the record, however old the item, so that a Re-extraction can extract the text again from it (A-terms), for instance to follow the item's headings, lists and tables more closely, and so that every place a value was found can still be opened; it is kept until an erasure removes it (ACQ-18).

**Verification.** none yet
