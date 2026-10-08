---
id: "SRC-31"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-31

BEACON shall propose a version of a source's Source Set entry in an Onboarding only from a sample of [[ONBOARDING_SAMPLE_SIZE]] of the source's items, spread across the periods from which the source lists items, or of every item the source lists where it lists fewer.

**Rationale.** An Entry part that holds on a few recent pages may fail on older ones made under an earlier layout, so the sample spreads across the source's periods. Its size weighs the pages each part is checked on against the pages fetched from a source no Curator has yet accepted. A source that lists fewer items is sampled whole rather than refused, and its outcome says how many items were sampled (A-terms, Onboarding outcome). A refused Onboarding is not bound: it may end before items can be fetched, or because the source disallows fetching them.

**Verification.** none yet
