# capstone_proposal

SIT AAI4001 Capstone Form B for Guo Zi Qiang Robin at LTA (Cyber Architecture & Development).
The capstone has two workstreams:
1. **Guardrail Evaluation Test Bench** (`benchtest/`)
2. **Beacon**, a daily AI-security briefing service (`Project-Beacon/`)

Shared rules for every Claude session and agent are in [`CLAUDE.md`](CLAUDE.md). The approved plan is [`main_session/plan/first_plan.md`](main_session/plan/first_plan.md).

## Deadlines
| When | What |
|---|---|
| 11 Oct 2026 | Form B submitted |
| 1 Dec 2026 | Benchtest evaluation results |
| First week of Dec 2026 | Benchtest report |
| 6 Dec 2026 | Interim report [Form E1] |
| 31 Jan 2027 | Interim Presentation |
| 1 Feb 2027 | Beacon deployed |
| Feb 2027 | Beacon CI/CD and monitoring |
| Mar 2027 | Buffer and iteration |
| 21 Mar 2027 | Final Report [Form E2] |
| 31 Mar 2027 | Project period ends (period runs 8/10/2026 – 31/3/2027) |
| 11 Apr 2027 | Capstone Project Presentation (after the period) |

## Form B rules
- Follow `template/Form B.docx` strictly when editing `Form B_Guo_Zi_Qiang_Robin.docx`. Make all edits as tracked changes authored "Guo Zi Qiang Robin".
- Use `benchtest/red_team_proposal/Form B (Daniel Chua).docx` as a style reference, especially for section C (Knowledge and Training Requirements). Each section may run to at most 2.5× Daniel's per-section length.
- Put tables, figures, the glossary and references (APA 7th, max 10) in annexes after "END OF FORM B". The detailed Gantt chart is in `Gantt_Guo_Zi_Qiang_Robin.xlsx`.
- Constraints:
  - Development runs on one LTA laptop (i7-13700H, 32 GB RAM, RTX 4060 8 GB).
  - Only open-source, free, free-trial or free-credit technology.
  - Sentinel (GovTech) access is available.

## Layout
| Path | What |
|---|---|
| `template/Form B.docx` | Blank Form B template (read-only) |
| `Form B_Guo_Zi_Qiang_Robin.docx` | The form being completed |
| `benchtest/` | Guardrail research, demos, explainers, and the red-team Form B ([README](benchtest/README.md)) |
| `Project-Beacon/` | Beacon vault, outdated report, and security-framework acquisition ([README](Project-Beacon/README.md)) |
| `main_session/` | Plan, decisions log, content brief |
| `scratchpad/` | Per-agent working folders ([README](scratchpad/README.md)) |
| `.claude/` | Project agents, vendored skills, settings, SessionStart hook |

## Claude Code setup
- **Plugins** (`.claude/settings.json`): `obsidian@obsidian-skills` ([kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)) and `document-skills@anthropic-agent-skills` ([anthropics/skills](https://github.com/anthropics/skills)).
- **Vendored skills** in `.claude/skills/`: `obsidian-markdown`, `obsidian-bases`, `doc-coauthoring`. Use `doc-coauthoring` only under the rule in CLAUDE.md, because it is token-heavy.
- **Agents** in `.claude/agents/`: benchtest-explorer, beacon-explorer, security-frameworks-explorer, form-analyst, formb-drafter, annex-builder, formb-reviewer.
- **SessionStart hook**: `.claude/hooks/session-start.sh` ensures python-docx, openpyxl and matplotlib are installed.
- **Already connected**: the Context7 and GitHub MCPs.
- **Optional later**: the `fewer-permission-prompts` skill.
