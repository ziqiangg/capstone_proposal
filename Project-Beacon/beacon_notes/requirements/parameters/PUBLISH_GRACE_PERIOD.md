---
id: "PUBLISH_GRACE_PERIOD"
type: "parameter"
bounds: "how long after CYCLE_DEADLINE a scheduled Cycle may stay open for Unfinished items; 0 or more; no longer than from CYCLE_DEADLINE to DELIVERY_SCHEDULE, and ending before 24:00"
unit: "duration"
default: "30 minutes"
owner: "Curator"
---
# PUBLISH_GRACE_PERIOD

Its bounds name [[CYCLE_DEADLINE]] and [[DELIVERY_SCHEDULE]].
