---
id: ""
type: "parameter"
bounds: ""
unit: ""
default: ""
owner: ""
---
# <id>

%%
A parameter is a named value that a requirement row states BEACON's
behaviour against, and that an actor in A-terms A1 sets without any
requirement text changing. A value fixed by design, or one no current row
names, is not a parameter. The filename is the name, in UPPER_SNAKE.

bounds   -- what it bounds: its meaning and its limits
unit     -- count, duration, set, enum, ...
default  -- a value, or `unset`
owner    -- the A1 actor who sets it: Reader, Curator, Operator or
            Administrator

Rows link it as [[NAME]]; the backlinks are its "referenced by", so no
field stores that. It changes like a row: an applied proposal; a new one
may also arrive by the owner's `require`.

States, and the field each one adds (see _schemas/parameter.json):
     current     -- as written; `status` may be omitted
     removed     -- add `status: "removed"` and `removed_because:`, one line:
                    why it is gone. The file stays, so its name resolves

Delete this comment once the note is filled in.
%%
