---
id: ""
type: "decision"
title: ""
status: "accepted"
requirements: []
architecture: []
basis: ""
---
# <id> <title>

## What is decided
<one paragraph, in the present tense>

## What it constrains
<what may no longer be done freely, and by whom>

## What would reverse it
<the observation that would make this wrong>

## Assumes
<what this proceeds under while a question it rests on is open, naming the
question, and the trigger that re-opens it. Delete the section when nothing is
assumed.>

%%
States, and the field each one adds (see _schemas/decision.json):
     accepted    -- as written
     superseded  -- add `superseded_by:`, the note that replaces this one; it
                    must exist and be live
     withdrawn   -- add `withdrawn_because:`, one line: why this is no longer
                    decided

     `basis` says what the claim rests on. The forms in use:
       "owner ruling, <date>"
       "measured <date> <over what>; not re-verified since"
       "vendor documentation read <date>"
       "none yet"

     Delete this comment once the note is filled in.
%%
