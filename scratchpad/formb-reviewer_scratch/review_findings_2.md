# Review findings 2 (formb-reviewer): `formb_draft_2.md`

Reviewed: `scratchpad/formb-drafter_scratch/formb_draft_2.md`, Sections A–D and Annex D. This round reviews the draft only, so check 7 is skipped.
Cross-checked against: `scratchpad/annex-builder_scratch/annex_4.md`. It differs from `annex_3.md` only in three ways: the GenAI row is dropped, the Briefing definition is synced, and the test bench definition is synced. I also checked the root `Gantt_Guo_Zi_Qiang_Robin.xlsx`.
Grounded against: CLAUDE.md, `decisions_log.md` #1–#36, `benchtest_findings_1.md`, `beacon_findings_1.md`, `security_frameworks_findings_1.md` and `form_structure_findings_1.md` Part 3 (caps).
Method: I extracted the fenced `text` blocks (everything before "## Annex D") with a script. The regexes were run over those blocks and over the whole pre-annex file. Words were counted by whitespace split, using form-analyst's method.

## Verdict
**PASS. No blocking issue remains in the body draft.** All 26 round-1 findings are resolved, including every optional fix, and checks 1–6 pass afresh.

One required fix sits outside the drafter's text, in Annex A (A-5 below):
- The "Buffer and iteration" row is marked active in February.
- CLAUDE.md says "Mar is buffer and iteration".

It is a one-cell change for annex-builder. It must be applied before the docx is assembled, but it does not block this draft. The optional nits are listed separately at the end.

## Summary table

| # | Check | Result | Notes |
|---|---|---|---|
| 0 | Round-1 findings resolved | PASS | 26/26 resolved (table below) |
| 1 | Cold-reader test | PASS | Restated in 5 sentences. 4 residual terms, none blocking (N-3, N-4) |
| 2a | ID regex sweep, body | PASS | 0 hits for all 5 patterns, in the blocks and in the whole pre-annex file |
| 2b | Acronyms expanded at first use | PASS | 12 acronyms, all expanded at first use. GenAI is gone. "AI" in the title before its expansion is acceptable for a title |
| 2c | Acronyms and coined terms in glossary | PASS | All 12 acronyms and all 6 coined terms are in `annex_4.md`. The definitions match the body word for word |
| 2d | Coined terms ≤ about 6 | PASS | 6: guardrail, test bench, ablation, Briefing, evaluation harness, Tier 1/Tier 2 |
| 3 | Word counts vs caps | PASS | Every section is under its cap. Overview is at 246/247 and Scope at 220/222, so neither has room to grow |
| 4 | Grounding / over-claims | PASS | No over-claims. Red-team: no name, no integration. Beacon stays at outcome level |
| 5 | Dates and constraints | PASS (body); Annex A needs fix A-5 | Every body date matches CLAUDE.md. The hardware and free/open-source statements are correct |
| 6 | References | PASS | 10/10 references. Every entry is cited and every citation resolves. APA 7 ordering and format are correct |
| 7 | Docx-only checks | N/A | Draft-only round |

## Check 0: round-1 findings

| Ref | Required | Draft 2 | Status |
|---|---|---|---|
| O-1 | "NVIDIA's NeMo Guardrails", "Meta's Llama Guard" | line 31 | Resolved |
| O-2 | "the LionGuard 2 harmful-content classifier" | line 31 | Resolved |
| O-3 / G-6 | "score each guardrail on the same labelled inputs." | line 31 | Resolved |
| O-4 / G-5 | "initially mapped" | line 34 | Resolved |
| O-5 | "Two workstreams" | line 28 | Resolved |
| O (optional) | Reword the CYAD/LTA phrase, offset by "high-volume" and by dropping "short," | lines 28, 34 | Resolved |
| Ob-1 | "a fixed list of English-language public sources" | line 50 | Resolved |
| IR-1 / G-1 | No named student | line 64. "Daniel" and "Chua" give 0 hits | Resolved |
| IR-2 / G-3 | "This is timely because the SSP defines" | line 64 | Resolved |
| IR-3 / G-2 | "recognised security-control and attacker-technique terms" (#32) | line 67 | Resolved |
| IR-4 / G-8 | "Beacon aims to shorten" | line 67 | Resolved |
| IR-5 (optional) | GenAI removed | 0 hits. The glossary row is dropped in annex_4 | Resolved |
| S-1 | "a single provided development laptop with an 8 GB graphics processing unit (GPU)" | line 74 | Resolved |
| S-2 / G-4 | "too few comparable products", "response-generating", the next-step sentence (#20) | line 77 | Resolved |
| S-3 | "Beacon covers the outcomes in objectives 5 to 8…" | line 80 | Resolved |
| Out-1 | "Academic submissions" (#30) | line 98 | Resolved |
| Out-2 | "(by 1 February 2027)" | line 95 | Resolved |
| C-1 (optional) | "harmless prompts that resemble harmful ones" | line 126 | Resolved |
| T-1 / G-7 | "LTA provides the development laptop, and Sentinel access is already in place." | line 135 | Resolved |
| R-1 | MITRE entries filed under M (#33) | lines 187–189 | Resolved |
| R-2 | Tan et al. links to the ACL Anthology | line 193 | Resolved |
| R-3 (optional) | arXiv preprint form with DOI (#35) | line 181 | Resolved |
| R-4 (optional) | Retrieval date for the Llama Guard 4 page | line 183 | Resolved |
| A-1 | Figure 1 caption says "Tier 1 evaluates the input checks" and no repository path | annex_4:31 | Resolved |
| A-2 (optional) | Product-name glossary rows | annex_4:58–64 | Resolved |
| A-3 | Test bench definition matches the body | annex_4:56. The PROVISIONAL tag is gone | Resolved |
| A-4 | "Interim Report (Form E1)" / "Final Report (Form E2)" capitalised the same way | annex_4:11,13 | Resolved |

The working notes are out of Annex D. The drafter notes at lines 197–214 are clearly labelled "not for the docx".

## Check 1: cold-reader test

Restatement from the document alone:
1. Workstream 1 builds a minimal evaluation harness. The harness runs the same labelled prompts through NVIDIA's NeMo Guardrails, Meta's Llama Guard 3/4 and GovTech's Sentinel (LionGuard 2), with Meta's Prompt Guard 2 planned. Harmful-content classification and jailbreak detection can then be compared fairly, one setting at a time.
2. Workstream 2 builds Beacon, a daily cloud-hosted service. Beacon collects public AI-security news, filters it, merges duplicate reports and rates significance. It publishes a ranked web Briefing and a Telegram digest, with an initial evidence-traceable mapping of each event to Singapore Government SSP controls and MITRE ATT&CK/ATLAS techniques.
3. LTA runs critical infrastructure. Workstream 1 lets its CYAD division choose guardrails on evidence rather than vendor claims before deploying generative AI. Workstream 2 gives CYAD timely, defensible threat awareness in control and attacker-technique terms.
4. Test bench results are due by 1 Dec 2026, with the report in 1–6 Dec. Beacon is deployed by 1 Feb 2027, with CI/CD and monitoring through Feb and March as buffer.
5. Form E1 is due 6 Dec, the Interim Presentation 31 Jan and Form E2 21 Mar. The Final Presentation is on 11 Apr, after the period. Everything runs on one 8 GB-GPU laptop and free tools.

Terms I could not fully explain:

| Term | Where | Problem | Fix |
|---|---|---|---|
| "the later pipeline stages" | Timeline | The reader is not told which stages are "earlier", or that collection is already designed (`beacon_findings_1.md:36-37`) | N-3 (optional) |
| "the comparative research" | Objective 1 | The definite article points to research the body has not introduced. "Complete" implies that it exists, so this is a minor gap | N-4 (optional) |
| "products share the same underlying service" | Scope | Vague, but an informed reader can follow it | none |
| "Generative AI system type", Form E1/E2 | Industry Relevancy, Timeline | Accepted in round 1: the first is context, and an SIT assessor knows the second | none |

Resolved since round 1: LionGuard 2 (now described in the body), Prompt Guard 2 and the product names (glossary rows), "the source list" (Ob-1) and near-miss examples (C-1).

## Check 2: jargon / ID sweep

| Regex | Hits in the blocks | Hits in the whole pre-annex file |
|---|---|---|
| `\b[A-Z]{3}-\d{2}\b` | 0 | 0 |
| `\b[CSKDQX]-\d{2,3}\b` | 0 | 0 |
| `\bC\d{1,2}\b` | 0 | 0 |
| `\bP[012]\b` | 0 | 0 |
| `\bCP-\d+` | 0 | 0 |

Acronyms, where each is first expanded, and whether it is in Annex C (`annex_4.md`):
- AI: Overview. Yes.
- LTA: Overview. Yes.
- CYAD: Overview. Yes.
- GovTech: Overview. Yes.
- SSP: Overview, per #17. Yes.
- ATT&CK: Overview. Yes.
- ATLAS: Overview. Yes.
- CI/CD: Objective 8, per #31b. Yes.
- GPU: Scope. Yes.
- STIX: Additional Knowledge. Yes.
- OSCAL: Additional Knowledge. Yes.
- API: Additional Knowledge. Yes.

Other notes:
- MITRE, NVIDIA and NeMo are names, and GB is a unit. "LLM" appears only inside reference titles.
- Annex C has no rows the body does not use.
- British spelling: no US forms. The only "catalog" hit is "catalogue". "Program" is correct in the software sense.

## Check 3: word counts (caps from `form_structure_findings_1.md` Part 3)

| Section | Draft 2 | Cap | Result |
|---|---|---|---|
| A Project Title | 16 | none | PASS |
| B Overview | 246 | 247 | PASS (1 word spare) |
| B Objectives | 213 | 270 | PASS |
| B Industry Relevancy | 143 | 170 | PASS |
| B Scope | 220 | 222 | PASS (2 words spare) |
| B Outputs and Deliverables | 83 | 110 | PASS |
| C Applicable Knowledge | 65 | 72 | PASS |
| C Additional Knowledge | 96 | 130 | PASS |
| C Training | 67 | 105 | PASS |
| D Timeline | 229 | 312 | PASS |

My counts match the drafter's comments in every section.

## Check 4: grounding and over-claims

New or changed claims since round 1, and where each comes from:

| Claim | Source | Result |
|---|---|---|
| "LionGuard 2 harmful-content classifier", served by Sentinel | `benchtest_findings_1.md` translation table (LionGuard 2 row) | OK |
| "a fixed list of English-language public sources" | `beacon_findings_1.md:6,38` (ten English sources) | OK |
| "SSP defines a dedicated Generative AI system type with its own controls" | `security_frameworks_findings_1.md:9` (gen-ai type, 9 controls) | OK |
| "recognised security-control and attacker-technique terms" (no SSP obligation) | #32; `security_frameworks_findings_1.md:40` | OK |
| "parallel LTA AI red-teaming capstone project … no committed integration" | CLAUDE.md, #27 | OK. No name and no integration |
| Tier 2 reasons and "response checking is the natural next step" | #20; `benchtest_findings_1.md:7` | OK |
| "Sentinel access is already in place" (not attributed to LTA) | CLAUDE.md Resources; `benchtest_findings_1.md:21` | OK |
| Glossary product rows (Sentinel, LionGuard 2, Prompt Guard 2, NeMo, Llama Guard, Purple Llama, Litmus) | `benchtest_findings_1.md` TL;DR and translation table | OK |

Over-claim sweep:
- **Tier commitments.** Only Tier 1 is committed. Tier 2 is "under investigation". Prompt Guard 2 is "planned" (#19). Llama Guard 4 is "subject to model access", with Llama Guard 3 as the baseline (#24). There is no 8-bit local claim (#18).
- **Beacon.** Outcome-level only: no requirement families, counts, parameters or IDs. Mapping is "initial" (#14), trend detection is a stretch goal, Telegram is subject to LTA policy (#15) and hosting is unnamed (#11).
- **Red-team project.** Context only.

## Check 5: dates and constraints

| Item | Draft 2 | CLAUDE.md | Result |
|---|---|---|---|
| Period | 8 Oct 2026 – 31 Mar 2027 | same | PASS |
| Form B | 8–11 Oct, due 11 Oct | by 11 Oct | PASS |
| Test bench results | 1 Dec 2026 (Objective 4, Timeline) | by 1 Dec | PASS |
| Test bench report | first week of Dec (Outputs) / 1–6 Dec (Timeline) | first week of Dec | PASS |
| Form E1 | 6 Dec | by 6 Dec | PASS |
| Beacon build | Dec–Jan | Dec–Jan | PASS |
| Interim Presentation | 31 Jan | by 31 Jan | PASS |
| Beacon deploy | 1 Feb 2027 (Objective 8, Outputs 4, Timeline) | by 1 Feb | PASS |
| CI/CD and monitoring | throughout Feb | throughout Feb | PASS |
| March | buffer and iteration | Mar is buffer | PASS |
| Form E2 | 21 Mar | by 21 Mar | PASS |
| Final Presentation | 11 Apr, after the period | same | PASS |
| Phasing | test bench is the main focus until early Dec; Beacon design continues | same | PASS |
| Hardware | "a single provided development laptop with an 8 GB graphics processing unit (GPU)" | one laptop, RTX 4060 8 GB | PASS |
| Free/open-source | "only open-source, free, free-trial or free-credit technology"; "free-tier cloud GPU credits" (#23) | same | PASS |
| No other compute | "no further organisation-provided tooling or computing resources are assumed" | same | PASS |
| **Annex A buffer row** | `annex_4.md:25`: "Buffer and iteration (trend detection is a stretch goal)" is marked X in **Feb** and Mar | Mar is buffer. The body (line 157) says March | **Fix A-5** |

## Check 6: references

- **Count:** 10 (limit 10). PASS.
- **Citations against references:** I checked all 9 citation strings. Each resolves to exactly one entry, and each of the 10 entries is cited at least once (MITRE n.d.-a and n.d.-b share one citation). PASS.
- **Order (APA 7):**
  - Government Technology Agency n.d.-a, then n.d.-b, then 2025: undated works first, then by title.
  - Then Inan, then Meta, then Meta AI. The shorter name comes first.
  - Then The MITRE Corporation n.d.-a (ATLAS), then n.d.-b (ATT&CK), filed under M (#33).
  - Then Rebedea, then Tan.
  - PASS.
- **Format:**
  - The two proceedings entries use "In *Proceedings…* (pp.). Publisher. DOI/URL".
  - The preprint uses "(arXiv:ID). arXiv. DOI" (#35).
  - Changing pages use "Retrieved October 8, 2026, from" (#28).
  - Sentence-case titles.
  - All 11 Inan et al. authors are listed (fewer than 20).
  - PASS.
- **Verification:** every entry traces to #1, #2, #16 and #35 or to `benchtest_findings_1.md:83-93`. PASS.
- **Tan et al.:** the source title uses "&", and the entry spells it "and". This is acceptable (benchtest finding note). No change.

## Required fix (non-blocking for the draft; apply before docx assembly)

- **A-5 (annex-builder, Annex A):** in the row "Buffer and iteration (trend detection is a stretch goal)", clear the **Feb** cell, so the row is X in Mar only. This matches CLAUDE.md ("Mar is buffer and iteration") and body Timeline line 157.
  - The Feb X probably comes from the xlsx "Trend detection (stretch goal)" task (15 Feb – 15 Mar). If annex-builder wants to show that, split the row:
    - "Buffer and iteration": Mar X.
    - "Trend detection (stretch goal)": Feb X, Mar X.
  - The body line "February 2027: CI/CD, monitoring and fixes from live running" already covers February's work.

## Optional nits (none blocking; word deltas checked)

| ID | Section | Change | Words |
|---|---|---|---|
| N-1 | Overview | Avoid the back-to-back parentheses by moving the figure pointer earlier. "…allow, block or flag each message, catching harmful requests or jailbreaks (attempts to trick the chatbot into ignoring its rules) (see Annex B, Figure 1)." becomes "…allow, block or flag each message (see Annex B, Figure 1), catching harmful requests or jailbreaks (attempts to trick the chatbot into ignoring its rules)." | 0 (246) |
| N-2 | Overview | The possessive before a parenthesis remains: "the Government Technology Agency's (GovTech) Sentinel service". A word-neutral option is "the Government Technology Agency (GovTech) Sentinel service". Leave it if that reads worse | 0 |
| N-3 | Timeline | "design of the later pipeline stages continues at low intensity" becomes "design of the analysis stages after collection continues at low intensity" | +2 (231/312) |
| N-4 | Objective 1 | "Complete the comparative research on guardrail products" becomes "Complete the existing comparative research on guardrail products" | +1 (214/270) |
| N-5 | Annex C | The product-name rows (Sentinel … Litmus) are not in alphabetical order, unlike the two blocks above them. Either merge all rows into one A–Z list or alphabetise that block: Litmus, LionGuard 2, Llama Guard, NeMo Guardrails, Prompt Guard 2, Purple Llama, Sentinel | n/a |
| N-6 | xlsx / Timeline | The xlsx starts trend detection on 15 Feb, while body Timeline names it only under March. This is not a contradiction, because it is a stretch goal. Optionally start the xlsx task on 1 Mar | n/a |

## Open questions → to_main_session
1. A-5 needs routing to annex-builder. I assumed that the binding decision ("Mar is buffer and iteration") governs Annex A. The xlsx Buffer row already runs 1–31 Mar only (`Gantt_Guo_Zi_Qiang_Robin.xlsx`, Gantt sheet), so only the Word-table summary row is affected.
2. In round 1 I marked Annex A as PASS (`annex_2.md:25` had the same Feb X). I missed this then; it is corrected here.
