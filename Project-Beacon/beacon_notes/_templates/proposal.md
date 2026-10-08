---
id: ""
type: "proposal"
title: ""
status: "proposed"
requirements: []
adds_to: ""
reason: ""
---
# <id> <title>

## The change
<Per row, annex or parameter changed: its text **as it stands**, quoted exactly,
and the text it is **replaced by**.
Per row or parameter removed: the two frontmatter lines apply adds,
`status: "removed"` and `removed_because: "<one line>"`; its body is unchanged.
Per one added: its full note block, each new row under its own placeholder in
its group -- `GOV-n1`, `GOV-n2` -- never `NEW-` before a numbered id, which R2
reads as that id.
A split keeps the row's id for its first part and adds the rest as new rows
whose Rationale names the row they came from.
`apply` copies this text verbatim, so anything not written here exactly is not
applied. See method/commit-grammar.md, "What an `apply` may carry".>

## Why
<what is wrong with the text as it stands>

## Assessment
<written by the proposal assessor; one paragraph per row or annex named>

> [!important] The owner rules
> Requirement text changes only when an accepted proposal is applied.

%%
`requirements` lists the rows this changes. If it ADDS a row, that row does
     not exist yet and cannot be named, so put the group in `adds_to` -- "OUT",
     "SRC" -- and it takes the next free number in that group unless the owner
     assigns one (when several proposals add rows, the owner assigns them all
     in one table first); a new parameter, "parameters". `adds_to` holds one group or a
     list of them -- ["OUT", "parameters"] -- so one proposal may add a row and
     its parameter, or rows in two groups. Fill whichever apply: a split
     changes one row and adds another, so it fills both. Delete an empty one.

     `reason` is one line: why the row as it stands is wrong. `## Why` expands it.

     States, and the field each one adds (see _schemas/proposal.json):
     proposed    -- as written
     assessed    -- add `assessment:`, the proposal assessor's verdict line;
                    its report goes under ## Assessment
     accepted    -- keep `assessment:`, add `approval:`, the owner's ruling:
                    who, when, and where it is recorded
     applied     -- keep `assessment:` and `approval:`; the rows now read as
                    proposed. Terminal
     rejected    -- keep `assessment:`, add `rejected_because:`, one line: the
                    owner's reason for declining it. Terminal
     withdrawn   -- drop any `assessment:`; add `withdrawn_because:`, one line:
                    why it is no longer proposed. Terminal

     Delete this comment once the note is filled in.
%%
