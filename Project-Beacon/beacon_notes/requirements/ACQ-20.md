---
id: "ACQ-20"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-20

BEACON shall delete each backup that holds a Copy no later than an expiry stated for that backup when it is made.

**Rationale.** A backup is not edited each time an item is erased, so an erasure reaches it by its expiry: once every backup made before an erasure has expired, nothing the erasure removed remains in BEACON. An expiry stated when the backup is made makes that time known in advance.

**Verification.** none yet
