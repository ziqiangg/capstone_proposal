Each agent or subagent manages its own folder in `scratchpad/`.
Folders are named `<agent name>_scratch`, for example:
- `main_session_scratch/`
- `benchtest-explorer_scratch/`
- `beacon-explorer_scratch/`
- `security-frameworks-explorer_scratch/`
- `form-analyst_scratch/`
- `formb-drafter_scratch/`
- `annex-builder_scratch/`
- `formb-reviewer_scratch/`

An agent or subagent can draft:
1. `<topic>_findings_<version_number>.md`, containing findings from its delegated scope ONLY.
2. `to_<agent name>_<topic>_<version_number>.md`, containing messages to other agents or subagents.

If a message is addressed to several agents, separate the names with `-` hyphens, for example `to_X-Y_animalfact_1.md`.

## Findings file shape
Use these sections, in order:
1. `## TL;DR` (≤150 words)
2. `## Form B-ready facts` (bullets with `path:line` citations)
3. `## Translation table` (internal term → plain phrase → needed in Form B?)
4. `## References (APA 7, verified)`
5. `## Open questions → to_main_session`
6. `## Detail`

## Routing
Subagents cannot message each other live. The main session routes every message:
- After each agent returns, the main session reads `scratchpad/*_scratch/to_*` files.
- It answers questions addressed to `main_session`, writing `main_session_scratch/to_<agent>_<topic>_<N>.md` and logging the decision in `main_session/decisions_log.md`.
- It passes other messages on to their addressee.

A revision gets a new file with the version number incremented. Old versions are kept as an audit trail.
