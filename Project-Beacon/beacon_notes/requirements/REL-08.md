---
id: "REL-08"
type: "requirement"
group: "REL"
verification: "none"
---
# REL-08

IF a Discovered item that is not an Erased item is not in English, THEN BEACON shall record its scope\_decision as OUT, with the reason that it is not in English.

**Rationale.** BEACON reads and writes English only. An item in another language is recorded rather than silently skipped, so it stays visible (UIX-07), and a source that publishes in another language shows up for what it is.

**Verification.** none yet
