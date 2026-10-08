---
id: "ACQ-01"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-01

WHEN BEACON collects an enabled source, BEACON shall identify as a Discovered item every item that the Collection returns, whatever that item's Source publication time.

**Rationale.** A Collection that trusts a source's reported publication times misses items whose times are missing, backdated or wrong. Whether a Discovered item is new, unchanged or a Revision, and what is kept of the return of an Erased item, is decided by ACQ-04, ACQ-05, ACQ-06, ACQ-22 and ACQ-27. An item a source lists but whose content cannot be fetched (a paywall, a bot block) is not returned, so that Collection runs no Stage for it and makes no Failed item of it, whether or not BEACON holds the item from an earlier return; later Cycles try to fetch it again, within the bound ACQ-39 sets. An item a source offers and withdraws between two Collections is not covered; the daily Cycle (OPS-01) bounds that exposure.

**Verification.** none yet
