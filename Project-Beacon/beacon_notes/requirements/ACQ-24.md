---
id: "ACQ-24"
type: "requirement"
group: "ACQ"
verification: "none"
---
# ACQ-24

WHEN a Curator lifts an erasure, BEACON shall restore nothing that the erasure removed.

**Rationale.** A lift lets a later Collection keep the item again, as a Revision made without comparison where BEACON holds it (ACQ-27) and as a new item where it does not (ACQ-02); it does not bring back what was erased, from a backup or from anywhere else, so that what an erasure removed never returns into BEACON.

**Verification.** none yet
