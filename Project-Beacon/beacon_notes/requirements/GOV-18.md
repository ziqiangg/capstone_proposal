---
id: "GOV-18"
type: "requirement"
group: "GOV"
verification: "none"
---
# GOV-18

BEACON shall provide no role with the means to change a Method or a procedure that supplies values under ACQ-10 or ACQ-13.

**Rationale.** A Method's model, prompt and settings decide every Judgement it produces, and a procedure that supplies values under ACQ-10 or ACQ-13 decides fields that every later Stage reads (ACQ-03). Each changes only with a new release of BEACON, which is tested and versioned as a whole; GOV-07 attributes a Method's change to that release, and a supplying procedure's change shows in the version that each value it supplies records (ACQ-13, ACQ-14). What a Curator changes for a source between releases is its Source Set entry, which is not part of such a procedure's settings (ACQ-14).

**Verification.** none yet
