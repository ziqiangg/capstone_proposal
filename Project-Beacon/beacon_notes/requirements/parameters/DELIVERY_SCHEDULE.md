---
id: "DELIVERY_SCHEDULE"
type: "parameter"
bounds: "the time of day at which each day's Delivery is sent, read in the timezone of CYCLE_DEADLINE; where that day's Briefing is Published later, the Delivery follows its publication; no earlier than CYCLE_DEADLINE plus PUBLISH_GRACE_PERIOD"
unit: "time of day"
default: "09:00"
owner: "Curator"
---
# DELIVERY_SCHEDULE

Its bounds name [[CYCLE_DEADLINE]] and [[PUBLISH_GRACE_PERIOD]].
