---
id: "CYCLE_DEADLINE"
type: "parameter"
bounds: "time of day by which each scheduled Cycle's Briefing is due; a Cycle not closed by then makes its Briefing late; later than 00:00, and earlier than 24:00 by more than PUBLISH_GRACE_PERIOD"
unit: "time of day + IANA timezone"
default: "08:00 Asia/Singapore"
owner: "Curator"
---
# CYCLE_DEADLINE

Its bounds name [[PUBLISH_GRACE_PERIOD]].
