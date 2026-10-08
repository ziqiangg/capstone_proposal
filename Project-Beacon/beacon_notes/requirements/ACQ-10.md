---
id: "ACQ-10"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-10

BEACON shall hold each of an Article Record's title, Item publisher, Authors and Source publication time in exactly one Field state, with where each value the source states was found.

**Rationale.** Split from ACQ-02. A source often omits its Authors and its publication time, so they are kept as the source's only where it states them; an item may credit several Authors, and each is kept. A later row relies on every item having a title (ACQ-07), so BEACON supplies one where the source states none that it can keep. Where each value was found, and every value where the source contradicts itself, let a reviewer judge how far to trust a field without fetching the page again, and after the raw page has gone.

**Verification.** none yet
