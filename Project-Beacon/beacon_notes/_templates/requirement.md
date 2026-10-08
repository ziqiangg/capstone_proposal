---
id: ""
type: "requirement"
group: ""
verification: "none"
---
# <id>

<the requirement text>

**Rationale.** <why BEACON needs it>

**Verification.** <how the method in `verification` is applied to this row; "none yet" while it is `none`>

%%
`verification` is one of none, inspection, analysis, demonstration or test:
the method that shows the row is met, or `none` while no method is chosen.

States, and the field each one adds (see _schemas/requirement.json):
     current     -- as written; `status` may be omitted
     removed     -- add `status: "removed"` and `removed_because:`, one line:
                    why the row is gone. The file stays, so its id resolves

Delete this comment once the note is filled in.
%%
