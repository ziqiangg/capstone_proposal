# capstone_proposal: shared context for every session, agent and subagent

Goal: complete `Form B_Guo_Zi_Qiang_Robin.docx`, the SIT AAI4001 Capstone Form B for Guo Zi Qiang Robin at LTA (CYAD). It is due 11 Oct 2026.
Full plan: `main_session/plan/first_plan.md`. Logged autonomous decisions: `main_session/decisions_log.md`.
Do not ask Robin questions. Settle them with the precedence ladder below, then log the decision.

## Binding decisions
- **Scope:** one capstone with two workstreams: (1) Guardrail Evaluation Test Bench (`benchtest/`) and (2) Beacon (`Project-Beacon/`). The title is to be proposed (the current title "Beacon" will be replaced).
- **Period:** 8/10/2026 – 31/3/2027 (unchanged). The Final Presentation on 11 Apr falls after the period.
- **Benchtest:** evaluation results by 1 Dec 2026; report in the first week of Dec.
- **Beacon:** deployed by 1 Feb 2027, with CI/CD and monitoring throughout Feb. Mar is buffer and iteration.
- **Phasing:** parallel, with the benchtest heavier first. Oct to early Dec is mostly benchtest while Beacon design continues. Dec–Jan is the Beacon build.
- **SIT milestones:**
  - Form B by 11 Oct.
  - Interim report [Form E1] by 6 Dec.
  - Interim Presentation by 31 Jan.
  - Final Report [Form E2] by 21 Mar.
  - Final Presentation by 11 Apr.
- **Benchtest scope, in tiers:**
  - **Tier 1 (proposed):** harmful-content classification of user input, and jailbreak / prompt-attack detection. Products: NVIDIA NeMo Guardrails, Meta Llama Guard 3/4, GovTech LionGuard / Sentinel.
  - **Tier 2 (under investigation):** everything else. Each item needs a stated reason, e.g. too few comparable products, a shared backend, a need for a retrieval or agent architecture, or a need for more compute.
  - Meta Purple Llama and GovTech Litmus are planned additions to the research.
- **Beacon scope:** high-level outcomes only. Do not list requirement families.
- **Red-team project** (Daniel Chua's Form B): context only, under Industry Relevancy. No committed integration.
- **Length:** each section is at most 2.5× the word count of the same section in Daniel's Form B (`benchtest/red_team_proposal/`).
- **Section C modules:**
  - AAI3008 Large Language Models
  - INF2006 Cloud Computing and Big Data
  - INF2005 Cyber Security Fundamentals
  - INF2003 Database Systems
  - INF2001 Introduction to Software Engineering

  Additional skills are inferred from the work. No certifications are claimed.
- **Resources:** one LTA laptop only: i7-13700H, 32 GB RAM, RTX 4060 Laptop with 8 GB VRAM.
  - Technology must be open-source, free, free-trial or free-credit.
  - There is no high-compute workstation or sandbox, unless it comes from free cloud credits.
  - Sentinel access is available (GovTech, Singapore IP).
- **Output:**
  - Edit the docx in place, as tracked changes with author "Guo Zi Qiang Robin". Follow `template/Form B.docx` strictly.
  - Leave untouched: Supervisor Remarks, all Declarations, the Academic Supervisor contact number, and the Industry Supervisor designation. The last two are flagged as missing.
  - **Word-compatibility rules** (both caused a "Word found unreadable content" error; see decision #43):
    - Never put revision marks (`w:ins`, `w:del`, `w:pPrChange`, `w:rPrChange`) inside plain-text content controls (`w:sdt` with `w:text`). Write the answer text there as plain, uniformly formatted runs. Tracked changes are fine elsewhere, e.g. in the annexes.
    - Repack a .docx with Python `zipfile`: `[Content_Types].xml` first, no directory entries. Do not use `zip -r`.
    - `validate.py` and LibreOffice do not catch either problem.
  - Robin's latest edited version, saved from Word, is the base for any further edits.
- **Gantt:** a detailed `Gantt_Guo_Zi_Qiang_Robin.xlsx` at the repository root, plus an abstracted month-level Word table in Annex A.
- **Git:** commit and push to `claude/affectionate-knuth-gfiu70`. No PR.

## Writing style for Form B
- **Reader:** an academic supervisor or assessor who knows AI but is new to both projects and to LTA.
- **No internal IDs in the body.** That covers benchtest group codes (C1–C24) and Beacon IDs (ACQ-02, C-04, S-, K-, D-, Q-, X-, CP-, P0/P1/P2). Use the plain-language phrases from the findings translation tables.
- **Coined terms:** at most about 6 across the whole form, each defined at first use. Expand every acronym at first use.
- **Depth:** the body says what, why and the outcome. Mechanism goes in at most one sentence. Requirement-level detail is left out.
- **Workstream framing:** sections B and D open with a one-line umbrella statement, then "Workstream 1: Guardrail Evaluation Test Bench" and "Workstream 2: Beacon".
- **Lists:** numbered lists for objectives and deliverables; short prose elsewhere. Use the template's styles only.
- **Spelling and references:** British/Singapore spelling. In-text citations in APA 7th; at most 10 references, each one verified.
- **Annex:** every table, figure and diagram goes there, after "END OF FORM B":
  - A: Gantt
  - B: Figures
  - C: Glossary
  - D: References

## Precedence ladder (what wins when sources disagree)
1. This file and the plan.
2. The READMEs.
3. The Beacon vault `Project-Beacon/beacon_notes/` (current). Then `benchtest/` xlsx, notebooks and explainers.
4. `Project-Beacon/Beacon_Report.docx`, which is outdated and for context only.
5. Daniel's Form B, as a style precedent only.
6. External documentation (Context7 / WebFetch), for product facts only.
7. If none of these settles it: the most conservative option. Under-claim; never invent personal or organisational facts. Log it.

## Paths
| What | Where |
|---|---|
| Form template (read-only) | `template/Form B.docx` |
| Benchtest research | `benchtest/AI Guardrails Research and Comparison.xlsx`, `benchtest/demo/*.ipynb`, `benchtest/helpful_explanation/*.html` |
| Beacon vault | start at `beacon_notes/00-home.md`. Conventions are in `Project-Beacon/README.md`. `src/` is not in this repository |
| Security frameworks | read `README.md` and each `*_output/manifest.json` only. **Never read the bulk `*_output/` JSON** (about 300 MB) |

## Agents and the scratchpad protocol (details in `scratchpad/README.md`)
- Each agent writes only to `scratchpad/<agent-name>_scratch/` and to the deliverables it owns.
- **Findings files** are named `<topic>_findings_<N>.md`. Sections, in order:
  1. `## TL;DR` (≤150 words)
  2. `## Form B-ready facts` (bullets with `path:line`)
  3. `## Translation table` (internal term → plain phrase → needed in Form B? y/n)
  4. `## References (APA 7, verified)`
  5. `## Open questions → to_main_session`
  6. `## Detail`
- **Messages** are files named `to_<agent>[-<agent>]_<topic>_<N>.md`, saved in the sender's folder. The main session routes all messages.
- Final reply to the caller: ≤100 words, pointing to the file.

## Skills
- **docx / xlsx / pdf:** `anthropic-skills:docx`, `:xlsx`, `:pdf` (or the `document-skills` plugin). Always use them for .docx and .xlsx work.
- **Obsidian:** `obsidian-markdown` and `obsidian-bases` (`.claude/skills/`) for reading the vault.
- **doc-coauthoring:** token-heavy. Use it only when a Form B section has failed review twice on clarity, for that one section, and log the use.
