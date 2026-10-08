---
id: "SRC-19"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-19

Each Curator digest shall report, for each Cycle closed since the previous digest, the Health entry of each source enabled when that Cycle started.

**Rationale.** A source decays in ways that record no failure: fewer new items, pages that cannot be fetched, titles that have to be supplied, fields that can no longer be read. Each count in the Health entry is one such sign, given per source and per Cycle, so that the Curator, who owns the Source Set, sees a source weaken before it falls silent (SRC-06), fails (SRC-14) or is flagged (SRC-16, SRC-20, SRC-21). A rise in fields held with no kept value is often the first sign that a source's pages have changed shape; one held so because what was found does not meet the rows (ACQ-12) is counted too, under its reason, so that the Curator's picture of the source is whole. The sources enabled when a Cycle starts are those it collects (SRC-10).

**Verification.** none yet
