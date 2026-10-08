---
id: ""
type: "question"
title: ""
status: "open"
component: ""
priority: "P2"
blocks: []
basis: ""
---
# <id> <title>

## What is unknown

<one paragraph. If two consumers would act on different parts of the answer,
this is two questions and they block each other in sequence -- split it. A wide
consumer set does not make a question compound; acting on different parts of the
answer does.>

## Why this priority

<why this band and not the one either side of it, in terms of the work that is
next (method/session-contract.md). A priority with no reason here means the
question is not ready to be worked; nothing checks that.>

## Answered when

<the observation that would settle it, checkable by someone who did not run it.
Name a threshold when a decision turns on it -- "at least 95 per cent of locators
resolve", never "locators resolve well" -- and a rate when no decision turns on
it, so a reader can apply their own threshold. Name the window any stability
claim held over. Do not change this after seeing a result: that voids the answer,
and the honest move is a second question.>

## If it stays unknown

<the behaviour the system runs meanwhile -- never "blocked". Write it so that
answering the question changes how often the fallback fires, not whether it
exists: "every model output is validated; invalid output becomes UNKNOWN with a
reason" survives its own answer.>

%%
States, and the field each one adds (see _schemas/question.json):
     open        -- as written
     answered    -- add `answer:`, one line saying what was settled. If a
                    decision settled it, name that decision here and let the
                    decision carry the reasoning
     superseded  -- add `superseded_by:`, the note that replaces this one; it
                    must exist and be live
     dropped     -- add `dropped_because:`, one line: why this stopped being
                    worth answering

     `basis` says what the claim rests on. The forms in use:
       "owner ruling, <date>"
       "measured <date> <over what>; not re-verified since"
       "vendor documentation read <date>"
       "none yet"

     Delete this comment once the note is filled in.
%%
