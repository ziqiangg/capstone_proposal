---
id: "SRC-12"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-12

BEACON shall keep, for each source, a count of that source's items that have become Failed items since the latest of these: the source was added to the Source Set, a Curator last enabled it, or a Curator last kept it (SRC-15).

**Rationale.** A source whose items keep failing costs processing and adds nothing; the count lets the Curator judge whether to keep it. Each item is counted once, however many Cycles it fails in. The count restarts when a Curator keeps the source or enables it again, so a source whose items start failing anew, for a new reason, is flagged again rather than failing unseen.

**Verification.** none yet
