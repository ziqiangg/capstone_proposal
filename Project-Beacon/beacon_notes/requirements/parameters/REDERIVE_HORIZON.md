---
id: "REDERIVE_HORIZON"
type: "parameter"
bounds: "how far back from a trigger re-derivation reaches, and how far back from a release the Re-extraction that the release makes reaches; `all`, or a duration no shorter than SELECTION_PERIOD; a Curator may narrow it for one trigger's re-derivation, never below SELECTION_PERIOD"
unit: "duration or `all`"
default: "equal to TREND_WINDOW, tracking it"
owner: "Curator"
---
# REDERIVE_HORIZON

Its bounds and default name [[SELECTION_PERIOD]] and [[TREND_WINDOW]].
