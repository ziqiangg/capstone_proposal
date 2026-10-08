---
id: "ACQ-21"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-21

WHEN BEACON restores data from a backup, BEACON shall make again, in the restored data and in the order they were made, every erasure under ACQ-07 or ACQ-08 and every lift of an erasure under ACQ-23 made after that backup was made.

**Rationale.** A restore brings back what the backup held, including text erased since it was made. Making each later erasure again removes that text, and making each later lift again leaves the item as it stood before the restore, so that a restore neither undoes an erasure nor revives one that was lifted. Erasures and lifts are made again in their order, because an item may be erased, lifted and erased again, and only that order arrives at its state before the restore.

**Verification.** none yet
