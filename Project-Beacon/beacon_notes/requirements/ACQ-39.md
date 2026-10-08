---
id: "ACQ-39"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-39

IF BEACON has tried to fetch the content of an item that an enabled source lists in one Cycle and in [[LISTED_ITEM_RETRY_CYCLES]] later Cycles, and has not fetched it from the first of those Cycles on, THEN BEACON shall not try to fetch that content again.

**Rationale.** A Collection that cannot fetch an item's content does not return it (ACQ-01), so no Stage runs for it and it becomes no Failed item, and the bound on Failed items (OPS-27) does not reach it; without a bound of its own, a paywalled or blocked page would be tried in every Cycle for ever, each try costing crawl time inside the Collection's limit (OPS-15). The Cycles counted are an unbroken run of tries that fetched nothing, so the row reaches alike an item BEACON has never fetched and a held item its source still lists whose page BEACON can no longer fetch; a fetch that succeeds ends the run, and a held item that BEACON stops fetching keeps what its record holds. Only a Cycle in which BEACON tried counts, so a Cycle in which the source was not collected does not use up the bound. How many times BEACON tries within one Collection, and how long it waits between tries, is fixed by design. How such an item is reported is not stated here.

**Verification.** none yet
