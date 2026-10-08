---
id: "LISTED_ITEM_RETRY_CYCLES"
type: "parameter"
bounds: "the number of later Cycles in which BEACON tries again to fetch the content of an item that an enabled source lists, after a Cycle in which a Collection could not fetch it and with no fetch of it since, after which BEACON tries no more; such a try makes no Failed item, so this bound is apart from ITEM_RETRY_CYCLES, which bounds a Failed item; 1 or more"
unit: "count of Cycles"
default: "3"
owner: "Operator"
---
# LISTED_ITEM_RETRY_CYCLES

Its bounds name [[ITEM_RETRY_CYCLES]].
