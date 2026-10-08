---
id: "ACQ-34"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-34

BEACON shall record no extracted text in a version of an item's Article Record that a Re-extraction makes where ACQ-07 erased the text of the version holding the item's latest raw page.

**Rationale.** An erasure of text is not undone by extracting the text again from the raw page that ACQ-07 keeps: the item stays without its text until the source returns it changed, which is then a Revision (ACQ-06). Its fields come from the raw page, not from the erased text, so a Re-extraction decides them again as it does any item's, and a changed field is recorded in a new version (ACQ-09), which this row keeps without text. A Re-extraction made to compare a return with such an item (ACQ-30) records nothing.

**Verification.** none yet
