---
id: "EVD-02"
type: "requirement"
group: "EVD"
verification: "none"
---
# EVD-02

Each decision record shall carry the Judgement's kind, its outcome, its reason, the Method version, its Evidence locators, its confidence for each value it assigns, the version of each Governed Artefact and each Baseline it used, the value of each parameter it used, and the time.

**Rationale.** A later reviewer needs every one of these fields, and a record missing any of them cannot be re-derived or defended. Confidence is given per value, so a set of tags keeps its per-tag confidence.

**Verification.** none yet
