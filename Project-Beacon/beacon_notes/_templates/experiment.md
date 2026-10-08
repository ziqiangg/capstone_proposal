---
id: ""
type: "experiment"
title: ""
status: "designed"
question: ""
criterion: ""
budget_minutes: 0
---
# <id> <title>

## Hypothesis
<frozen before the run>

## Setup
<inputs, versions, machine>

## Criterion
<frozen before the run; a threshold, not a direction>

## Budget and staging
<smoke, then screen, then full; the stop condition implemented in the script>

## Result
Not run.

%%
States, and the field each one adds (see _schemas/experiment.json):
     designed    -- as written
     recorded    -- add `result:`, what was measured, against the frozen
                    criterion, including a failure
     superseded  -- add `superseded_by:`, the note that replaces this one; it
                    must exist and be live
     abandoned   -- add `abandoned_because:`, one line: why it was not run, or
                    not finished

     Delete this comment once the note is filled in.
%%
