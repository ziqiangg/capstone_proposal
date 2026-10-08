---
id: "SRC-30"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-30

WHEN BEACON collects a source, BEACON shall fetch its pages only in the ways of fetching that its Source Set entry in force names, trying them in the order it names them.

**Rationale.** Some sites refuse an ordinary request, and some ways of fetching get round that. Whether BEACON does so for a source is a decision about that source, so it is made in the entry a Curator accepted (SRC-28) and never by BEACON on its own. An Onboarding establishes the ways and their order, and one that cannot is a refusal (A-terms, Onboarding outcome). A rise in refusals under a source's first way raises a Drift flag (SRC-16), so that the order is established and accepted again.

**Verification.** none yet
