---
id: "SRC-04"
type: "requirement"
group: "SRC"
verification: "none"
---
# SRC-04

BEACON shall record, for each source, the time of the last Collection of that source that completed without error, whether or not it returned any item.

**Rationale.** In the output, a dead source looks the same as a quiet week. Only the product can tell the two apart. A Collection that fetched something new, or had nothing new to fetch, read a working source; one that timed out, did not read its listing to its end or fetched none of the new items it listed did not (A-terms, Completed without error). A bot block's page counts as no fetch where the entry holds something as appearing on every page and the page shows none of it, and leaves the listing unread where no page answered for it, retries included, shows what the entry holds for locating it. An item ACQ-39 stops is left out, lest it freeze a working source's time. An empty listing records the time; SRC-21 flags one new for its source, and a listing whose first page is answered only with pages that show nothing the entry holds for locating it, as a bot wall's are, not one unreached or partly read.

**Verification.** none yet
