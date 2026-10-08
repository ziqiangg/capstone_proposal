# First Plan: complete `Form B_Guo_Zi_Qiang_Robin.docx`

## Context
Robin's SIT AAI4001 Capstone Form B is only partly filled in. Only Section A fields are done (title "Beacon", LTA, names, period). It is due **11 Oct 2026**. The capstone covers two LTA (CYAD) workstreams:
1. an **AI Guardrail evaluation test bench**, in `benchtest/`;
2. **Project Beacon**, an AI-security news intelligence Briefing for critical-infrastructure cyber teams, in `Project-Beacon/`.

The source material is large: about 490 vault notes, about 300 MB of framework JSON, an xlsx, notebooks and docx files. The main session must therefore delegate reading to subagents and keep its own context small.

After this plan is approved, execution runs **to completion with no further questions to Robin**. Every clarification is recorded below.

## Clarified decisions (binding; copy verbatim into CLAUDE.md)
| Topic | Decision |
|---|---|
| Scope | One capstone with **two workstreams**: Benchtest and Beacon. The drafter proposes a new combined title. |
| Period | Keep **8/10/2026 – 31/3/2027**. The 11 Apr presentation falls after the period. |
| Benchtest deadlines | Evaluation results by **1 Dec 2026**. Report in the first week of Dec. |
| Beacon deadlines | **Deployed by 1 Feb 2027**, with CI/CD and monitoring throughout **Feb**. **Mar = buffer and iteration.** (This replaces the README's 1 Apr / April dates.) |
| Phasing | Parallel, with the benchtest heavier first: Oct–early Dec mostly benchtest while Beacon design continues; Dec–Jan Beacon build; Feb deploy and monitor; Mar buffer. |
| SIT milestones | Form B by 11 Oct. Interim report [Form E1] by 6 Dec. Interim Presentation by 31 Jan. Final Report [Form E2] by 21 Mar. Final Presentation by 11 Apr. |
| Benchtest scope (tiered) | **Tier 1, proposed:** C3 harmful-content input classification and C5 jailbreak / prompt-attack detection, using NeMo Guardrails, Llama Guard 3/4, and LionGuard/Sentinel. **Tier 2, under investigation:** C1/C2/C4/C6 and C7–C24, each with a stated reason (e.g. too few comparable products, shared backend (Sentinel AWS checks ≈ Bedrock), needs RAG or agent architecture, or needs more compute). Purple Llama and GovTech Litmus are named as planned additions to the research. |
| Beacon scope | Kept **high-level** (outcomes only; no list of requirement families). |
| Red-team (Daniel Chua) | **Context only**, mentioned under Industry Relevancy. No committed integration. |
| Length | Benchmark is Daniel's per-section word count. Cap is **≤ 2.5×** that count. |
| Section C | Modules: AAI3008 Large Language Models, INF2006 Cloud Computing and Big Data, INF2005 Cyber Security Fundamentals, INF2003 Database Systems, INF2001 Introduction to Software Engineering. Additional skills are inferred from the work. **No certifications claimed.** |
| Resources | Development uses only an LTA laptop: i7-13700H, 32 GB RAM, RTX 4060 Laptop with 8 GB. Only **open-source, free, free-trial or free-credit** technology. No dedicated high-compute workstation or sandbox, except free cloud tiers or credits. **Sentinel access is available** (GovTech, SG IP). |
| Output | Edit the docx **in place**, using **tracked changes authored "Guo Zi Qiang Robin"**. Follow `template/Form B.docx` strictly. **Leave Supervisor Remarks and all Declarations untouched.** Leave the Academic Supervisor contact number and the Industry Supervisor designation as placeholders, and flag them. |
| Gantt | Create a detailed `Gantt_Guo_Zi_Qiang_Robin.xlsx` next to the docx, and an **abstracted** Gantt as an annex inside the docx (a native Word table at month granularity, inserted as a tracked change after "END OF FORM B"). |
| Autonomy | For any question the repo cannot answer, the main session picks the most conservative defensible option and logs it in `main_session/decisions_log.md`. Every such decision is listed in the final summary. |
| Git | Commit and push to `claude/affectionate-knuth-gfiu70` at each milestone. **No PR.** |
| doc-coauthoring | Installed, but **not used by default** because it is token-heavy. See Phase 4. |
| Reader | The **academic supervisor or assessor**: AI-literate, but new to both projects and to LTA. |
| Style | Plain language with sparing anchors (see the next section). British/SG spelling. APA 7th references, **max 10**. **All tables, figures and diagrams go in the annex**, and the body refers to them. |

## Writing style and translation (applies to drafter, reviewer, explorers)
Each workstream has its own ID system, vocabulary and depth:
- Benchtest: C1–C24, sheet names, `[Documented]` / `[Inferred]` tags.
- Beacon: requirement families like ACQ/SRC/DLV; C-/S-/K-/D-/Q-/X- IDs; capitalised defined terms like Cycle, Source Set, Significance, development, Curator; EARS phrasing; P0/P1/P2.

Form B must **translate** these into material that reads cold for an outsider.

1. **No internal IDs in the form body.** Examples:
   - "C3" becomes "harmful-content detection on user prompts".
   - "C5" becomes "jailbreak / prompt-attack detection".
   - "D-003" becomes "the framework versions Beacon maps against".

   The reviewer checks this mechanically with a regex sweep: `\b[A-Z]{3}-\d{2}\b`, `\b[CSKDQX]-\d{2,3}\b`, `\bC\d{1,2}\b`, `\bP[012]\b`, `\bCP-\d+`.
2. **Sparing anchors:** at most about 6 coined terms across the whole form, e.g. *guardrail*, *test bench*, *ablation*, *Briefing*. Each is defined in plain words at first use, and every acronym is expanded at first use (e.g. RAG, PII, SSP, ATT&CK, ATLAS, OSCAL, CI/CD). Everything else is rephrased.
3. **Depth ladder:** the body states *what, why and outcome*. Mechanism detail goes in at most one sentence or into an annex figure. Requirement-level detail stays out entirely (Beacon is kept high-level).
4. **Translation tables in findings:** every explorer's findings file adds a `## Translation table` with columns *internal term/ID → plain-language phrase → needed in Form B? (y/n)*. The drafter uses only these phrases, so the terminology stays consistent across sections.
5. **Two-workstream framing:** each section of B and D uses the same structure: a one-line umbrella statement, then **Workstream 1: Guardrail Evaluation Test Bench** and **Workstream 2: Beacon**. The section C answer is shared, not split.
6. **Format:**
   - Numbered lists for objectives and deliverables.
   - Short prose for overview and relevance.
   - Consistent tense: future tense for plans; present tense for what exists.
   - Voice matches Daniel's form; form-analyst reports it.
   - Fonts and styles come from the template's styles, never ad-hoc formatting.
7. **Citations:**
   - In-text APA 7th (Author, Year).
   - Reference list as an annex, with ≤10 entries.
   - Candidates: NVIDIA NeMo Guardrails, Meta Llama Guard 3/4 papers or model cards, GovTech LionGuard 2 / Sentinel, MITRE ATT&CK, MITRE ATLAS, NIST OSCAL, GovTech SSP, OWASP GenAI Top 10.
   - The explorers verify each entry via Context7 / WebFetch and supply the reference with a URL. No unverified reference is allowed.
8. **Annex order**, after "END OF FORM B", all inserted as tracked changes:
   - Annex A: Gantt, abstracted, as a native Word table.
   - Annex B: figures. These are (i) a guardrail checkpoint diagram rendered from `benchtest/helpful_explanation/*.html` and (ii) a high-level Beacon pipeline diagram (about 6 boxes in plain words).
   - Annex C: glossary of terms and acronyms.
   - Annex D: references.

   The body refers to them as e.g. "(see Annex B, Figure 1)".
9. **Cold-reader test:** the reviewer must, from the docx alone, restate in ≤5 sentences:
   - what each workstream builds;
   - why it matters to LTA;
   - what is delivered by when.

   Any term it cannot explain is a finding.

## Phase 0: Setup (main session, ~1 commit)
1. Create `main_session/plan/first_plan.md` (a copy of this approved plan), `main_session/decisions_log.md`, and `scratchpad/<agent>_scratch/` for each agent below, plus `scratchpad/main_session_scratch/`.
2. **`CLAUDE.md` at the root. It is necessary:** every subagent starts cold and loads CLAUDE.md automatically, so this is the single carrier of shared truth. Keep it to about 100 lines:
   - the clarified-decisions table above;
   - the source-of-truth precedence (below);
   - the path map: what lives where, and which files are outdated (`Beacon_Report.docx` is context only; the vault wins);
   - the scratchpad protocol (summary, with a pointer to `scratchpad/README.md`);
   - skill-usage rules (docx/xlsx via the skills; doc-coauthoring restricted; obsidian skills for the vault);
   - "never invent personal facts", the word caps, and "never read the bulk `*_output/` JSON; use `manifest.json`".
3. **Plugins and skills** in `.claude/settings.json`:
   - `extraKnownMarketplaces`: `kepano/obsidian-skills` and `anthropics/skills` (both GitHub sources).
   - `enabledPlugins`: `obsidian@obsidian-skills`, `document-skills@anthropic-agent-skills` (docx/xlsx/pdf/pptx).
   - So the skills work in *this* running session without a restart, also vendor `obsidian-markdown`, `obsidian-bases` and `doc-coauthoring` into `.claude/skills/`, keeping their LICENSE files. `anthropic-skills:docx`, `anthropic-skills:xlsx` and `anthropic-skills:pdf` are already available here through the account sync. Skip obsidian-cli, defuddle and knap, which need desktop or npm CLIs that are irrelevant headless.
4. **SessionStart hook** (via the `session-start-hook` skill): a script, `.claude/hooks/session-start.sh`, that ensures `pandoc`, `libreoffice`, `python-docx`, `openpyxl` and `matplotlib`, plus whatever the docx skill's scripts require (read its SKILL.md first). It must be idempotent and quiet.
5. **Other proposals (not installed; noted in the README):**
   - the Context7 and GitHub MCPs are already connected (no install);
   - `fewer-permission-prompts` can be run later if prompts become a nuisance.
6. Define the agents in `.claude/agents/*.md` (table below). Commit and push: "Set up agents, skills, CLAUDE.md".

## Agents (`.claude/agents/<name>.md`)
`tools` is omitted, so each agent inherits every tool: all MCP tools (Context7, GitHub), WebFetch/WebSearch, Skill, Bash, Read/Write/Edit. The scratchpad protocol limits each agent to writing only its own scratch folder, plus the deliverables it owns.

| Agent | Model / effort | Skills / MCP | Job | Writes |
|---|---|---|---|---|
| `benchtest-explorer` | sonnet / high | xlsx, docx, pdf; Context7 (NeMo Guardrails, PurpleLlama/Llama Guard, Garak); WebFetch (Sentinel, LionGuard, Litmus) | Distil the xlsx (sheets 3–4, C1–C24), notebooks and HTML explainers. Justify Tier 1 / Tier 2 with reasons. Minimum architecture. Fit on the 8 GB GPU: what runs locally (LG3-8B 8-bit yes; LG4-12B likely not) vs free cloud. Short notes on Purple Llama and Litmus. | `benchtest_findings_N.md` |
| `beacon-explorer` | sonnet / high | obsidian-markdown, obsidian-bases, docx | Read the vault (00-home, components, decisions, experiments, questions, requirement families via `.base` logic), plus Beacon_Report for narrative only. Output: purpose, users, pipeline, maturity, what is designed vs not, tech stack, risks, and high-level outcome statements for 1 Feb. | `beacon_findings_N.md` |
| `security-frameworks-explorer` | sonnet / medium | Context7 (OSCAL, STIX) | Read the README, notebooks (code cells only) and each `manifest.json`, never the bulk JSON. Output: what each corpus contributes to Beacon (SSP gen-ai profile, ATT&CK 19.2, ATLAS 2026.09, OSCAL), as Form B-ready sentences, plus Section C skills (STIX 2.1, OSCAL, scraping). | `security_frameworks_findings_N.md` |
| `form-analyst` | sonnet / medium | docx | Map the template's XML: paragraphs and styles per section, the italic guidance text, checkboxes, and where answers go (*compare with how Daniel's form placed answers*). Exact per-section word counts for Daniel's form, giving **2.5× caps**. Daniel's Section C as a style reference. Drift from the template in Robin's file. | `form_structure_findings_N.md` |
| `formb-drafter` | **opus / high** | docx (tracked-change workflow); doc-coauthoring only under the Phase 4 rule | Write the section text in markdown first, then apply it to the docx as tracked changes, plus the annex table. | `formb_draft_N.md`, then the docx |
| `annex-builder` | sonnet / medium | xlsx, dataviz, docx; Playwright + pre-installed Chromium (headless screenshots of the HTML explainers, since the Chrome extension is not available in this cloud session) | (1) Build the detailed Gantt xlsx: weekly columns 8 Oct – 11 Apr, workstream swimlanes, SIT milestones, dependencies. Export a month-level abstraction for Annex A. (2) Make the Annex B figures: crop or screenshot the guardrail explainer HTML, and draw the plain-language Beacon pipeline diagram as HTML/SVG rendered to PNG. (3) Build the glossary table from the merged translation tables. | the xlsx, `annex_N.md`, `figures/*.png` |
| `formb-reviewer` | **opus / high** | docx, pdf | A cold-reader critic, which replaces doc-coauthoring's reader-testing. Checks: template adherence, word caps, every claim traced to a findings citation, dates against the decisions table, the resource and open-source constraint, Tier 1/2 consistency, and Declarations/Remarks untouched. Renders docx → PDF → PNG (soffice + pdftoppm) and checks the layout visually. | `review_findings_N.md` |

The main session is the orchestrator (the inherited model). It reads source files only to spot-check.

## Context preservation (main session)
- The main session **never reads raw sources** (vault, xlsx, notebooks, JSON). Each explorer writes a findings file with a fixed shape:
  1. `## TL;DR` (≤150 words);
  2. `## Form B-ready facts`, as bullets with `path:line` citations;
  3. `## Open questions → to_main_session`;
  4. `## Detail`.
- Explorers return a final message of **≤100 words** pointing to their file. The main session reads only TL;DR and Open questions. The **drafter and reviewer read the full findings files directly**, so detail flows agent-to-agent without passing through the main session's context.
- The main session holds one compact artefact, `main_session/content_brief.md`: a section-by-section outline with key points, the findings section that sources each, and the word cap. The drafter works from it.
- Use background agents run in parallel. If the main session needs a follow-up from an agent, it resumes that agent with SendMessage (its context is intact) instead of spawning a new one.

## Communication protocol (implements `scratchpad/README.md`)
- Folders: `scratchpad/<agent-name>_scratch/`, e.g. `benchtest-explorer_scratch/`. Findings: `<topic>_findings_<N>.md`. Messages: `to_<agent>[-<agent>]_<topic>_<N>.md`, placed in the **sender's** folder.
- Subagents cannot message each other live, so **the main session is the router**. After each agent returns, it globs `scratchpad/*_scratch/to_*`:
  - When a message is addressed to the main session, the main session answers it (rules below), writes `to_<agent>_<topic>_<N>.md` in `main_session_scratch/`, and resumes that agent via SendMessage with the file's path.
  - When a message is addressed to another agent, the main session passes the file path into that agent's next prompt, or resumes it.
- Version bump: each revision writes `_N+1`. Old versions stay, giving an audit trail.

## How the main session answers questions without Robin
Precedence ladder; take the first rung that answers:
1. The clarified-decisions table and CLAUDE.md.
2. The READMEs.
3. The vault, which is the up-to-date Beacon truth. Then the xlsx, notebooks and explainers.
4. `Beacon_Report.docx` for context only. It is outdated; the vault wins.
5. Daniel's Form B as a style and format precedent.
6. External docs via Context7 or WebFetch, for product facts only (versions, capabilities).
7. Otherwise, take the **most conservative defensible option**: under-claim, phrase as "planned" or "under investigation", never invent personal or organisational facts. Log it in `decisions_log.md` with the question, the decision, the rationale and the source.

## Context7 / GitHub MCP / subagents
- **Context7:** explorers use it to verify the product claims that land in Form B (NeMo Guardrails rails and Colang, Llama Guard taxonomy and versions, Garak, OSCAL/STIX). It is not used for writing.
- **GitHub MCP:** its scope is this repo only. It is used only to confirm that the branch, commit and push state matches after each push. Upstream repos (obsidian-skills, anthropics/skills) are fetched by `git clone` into the scratchpad, since the MCP is out of scope for them.
- **Built-in Explore agent:** used by the main session for small ad-hoc spot-checks, instead of reading files itself.

## Execution phases
- **P1, explore (parallel):**
  - Run benchtest-explorer, beacon-explorer, security-frameworks-explorer and form-analyst together.
  - The main session routes to_* messages and logs decisions.
- **P2, synthesise:**
  - The main session writes `content_brief.md`, including the proposed title and a phase-level timeline.
  - The main session then **improves the four READMEs**:
    - root: fix backslash paths; set the new Beacon dates (Feb); add a decisions summary and a pointer to CLAUDE.md, the plan and the Gantt;
    - benchtest: fill the empty "## 3." and record the Tier 1/2 scope and Sentinel access;
    - Project-Beacon: fix paths, point to 00-home/00-status, and note that `src/` is not in this repo;
    - scratchpad: add the agent folder names and the routing protocol.
  - Commit and push.
- **P3, draft (parallel):** formb-drafter writes `formb_draft_1.md` from the brief. annex-builder builds the Gantt xlsx, the Annex B figures and the glossary, using the brief and the merged translation tables.
  - Timeline backbone:
    - Oct–Nov: benchtest research and harness, then C3/C5 ablations. Beacon design continues.
    - Results by 1 Dec. Benchtest report and Form E1 by 6 Dec.
    - Dec–Jan: Beacon build. Interim Presentation by 31 Jan.
    - Deploy by 1 Feb. Feb: CI/CD and monitoring.
    - Mar: buffer and iteration. Form E2 by 21 Mar. Period ends 31 Mar.
    - Presentation by 11 Apr.
  - The drafter checks the timeline section against the Gantt abstract. Each findings file also includes its translation table and verified APA references (≤10 in total, selected by the main session into the brief).
- **P4, review loop (≤2 rounds):**
  - formb-reviewer writes `review_findings_N.md`, and the drafter revises.
  - If a section fails twice on clarity, the drafter may invoke doc-coauthoring for that **one section only**, and the use is logged.
- **P5, apply to docx:**
  - The drafter applies the final text as tracked changes (author "Guo Zi Qiang Robin"):
    - Section A fields: title, period unchanged;
    - Sections B, C and D;
    - Annexes A–D (Gantt table, figures, glossary, references).
  - Answer placement follows form-analyst's map: keep the italic guidance lines, and put the answer under each one, as Daniel's form does.
  - formb-reviewer does a final pass on the rendered PDF.
  - Commit and push, including the docx and the xlsx.
- **P6, close:** Summarise to Robin:
  - deliverables;
  - word count per section against its cap;
  - every logged decision;
  - placeholders left: Academic Supervisor contact and Industry Supervisor designation.

## Critical files
- Modified: `Form B_Guo_Zi_Qiang_Robin.docx`, `README.md`, `benchtest/README.md`, `Project-Beacon/README.md`, `scratchpad/README.md`.
- Created:
  - `CLAUDE.md`, `.claude/settings.json`, `.claude/agents/*.md` (7: benchtest-explorer, beacon-explorer, security-frameworks-explorer, form-analyst, formb-drafter, annex-builder, formb-reviewer), `.claude/skills/{obsidian-markdown,obsidian-bases,doc-coauthoring}/`, `.claude/hooks/session-start.sh`;
  - `main_session/plan/first_plan.md`, `main_session/decisions_log.md`, `main_session/content_brief.md`;
  - `Gantt_Guo_Zi_Qiang_Robin.xlsx`, `scratchpad/*_scratch/` (figures are kept under `scratchpad/annex-builder_scratch/figures/`).
- Read-only references: `template/Form B.docx`, `benchtest/red_team_proposal/Form B (Daniel Chua).docx`.

## Verification
- `soffice --headless --convert-to pdf` opens the docx without errors, and `pdftoppm` pages are inspected visually for layout, the annex table and checkboxes.
- python-docx confirms:
  - heading and paragraph sequence identical to the template, apart from the inserted answer runs and the annex;
  - all edits are `w:ins`/`w:del` with author "Guo Zi Qiang Robin";
  - Declarations and Supervisor Remarks are byte-identical.
- Jargon sweep: the regexes from the style section return 0 hits in the body (Sections A–E). Every acronym is expanded at first use and appears in Annex C. There are ≤10 references, every in-text citation has an entry, and every entry is cited.
- Cold-reader restatement, run by the reviewer, passes.
- A word-count script checks each section against its cap from form-analyst.
- A date grep checks the docx and the xlsx against the decisions table: 1 Dec, 6 Dec, 31 Jan, 1 Feb, Feb, 21 Mar, 31 Mar, 11 Apr.
- The xlsx opens in openpyxl and LibreOffice, with no formula errors (xlsx skill recalc check).
- `git status` is clean, and the push to `claude/affectionate-knuth-gfiu70` is confirmed via GitHub MCP `list_commits`.
