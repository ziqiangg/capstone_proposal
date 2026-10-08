# BEACON vault

## Views

| View | What it shows |
|---|---|
| [[requirements.base]] | the owner's requirements by group and by verification method, and the annexes that define the terms they name |
| [[parameters.base]] | each parameter a row names, and the rows that link it |
| [[architecture.base]] | components, their steps, and the contracts between them |
| [[decisions.base]] | what is decided, by status |
| [[questions.base]] | what is open, grouped by the component that owns it and by priority |
| [[experiments.base]] | designed, recorded, retired |
| [[proposals.base]] | requirement changes, and what each waits for |

## Where things go

| Kind | Lives in |
|---|---|
| The owner's requirements, and the annexes they name | `requirements/` |
| Components, and the steps and contracts inside them | `architecture/` |
| What is settled, and what would reverse it | `decisions/` |
| What is not settled, and what the system does meanwhile | `questions/` |
| What reading could not settle | `experiments/` |
| Requirement and annex changes, assessed, then ruled by the owner | `proposals/` |

A folder appears when its first note is written, so one that is missing means
nothing of that kind exists yet.
