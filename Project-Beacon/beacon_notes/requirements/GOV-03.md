---
id: "GOV-03"
type: "requirement"
group: "GOV"
verification: "none"
---
# GOV-03

BEACON shall hold every parameter in the parameter register with its bounds, its unit, its default, its owner and its current value.

**Rationale.** A value with no recorded owner is changed by whoever notices it last. The parameter register is a Governed Artefact, so GOV-05 versions it and GOV-07 records each change. The delivery channel's configuration is not a parameter; a delivery-family row covers it.

**Verification.** none yet
