---
id: ""
type: "step"
title: ""
status: "proposed"
component: ""
requirements: []
expects: []
produces: []
decisions: []
questions: []
---
# <id> <title>

## What it does
<one paragraph>

## Expects
<each contract in `expects`, and what this step assumes of it>

## Produces
<each contract in `produces`, and what this step guarantees about it>

## Done when
<the observable condition that says this step meets its requirements>

## Failure
<what this does when an input is missing, malformed or UNKNOWN; UNKNOWN is
never a default>

%%
States, and the field each one adds (see _schemas/step.json):
     proposed    -- as written
     accepted    -- as written
     superseded  -- add `superseded_by:`, the note that replaces this one; it
                    must exist and be live
     removed     -- add `removed_because:`, one line: why it is gone, not what
                    replaced it

     Delete this comment once the note is filled in.
%%
