---
id: ""
type: "contract"
title: ""
status: "proposed"
producer: ""
consumers: []
shape_status: "undesigned"
---
# <id> <title>

## Shape
<the fields, types and units; or `undesigned`, and what blocks designing it>

## Invariants
<what a consumer may rely on, and what it may not>

## Failure
<what this does when an input is missing, malformed or UNKNOWN; UNKNOWN is
never a default>

%%
States, and the field each one adds (see _schemas/contract.json):
     proposed    -- as written
     accepted    -- as written
     superseded  -- add `superseded_by:`, the note that replaces this one; it
                    must exist and be live
     removed     -- add `removed_because:`, one line: why it is gone, not what
                    replaced it

     Delete this comment once the note is filled in.
%%
