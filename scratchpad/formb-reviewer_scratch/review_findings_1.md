# Review findings 1 (formb-reviewer): `formb_draft_1.md`

Reviewed: `scratchpad/formb-drafter_scratch/formb_draft_1.md` (Sections A–D and Annex D references). I read it as an academic assessor who is new to both projects.
Grounded against: `benchtest_findings_1.md`, `beacon_findings_1.md`, `security_frameworks_findings_1.md`, `form_structure_findings_1.md`, CLAUDE.md, `decisions_log.md` #1–#31 and `content_brief.md`. I also cross-checked `annex-builder_scratch/annex_2.md`, the glossary source.
Method: I extracted the fenced `text` blocks (the body, everything before "## Annex D") with a script. Words were counted by whitespace split, using form-analyst's method. My counts match the drafter's in every section.

## Verdict
**FAIL. Revise to draft 2. The fixes are small.** The draft is clear, well framed and inside every cap. Five things block a PASS:
- (a) Daniel Chua is still named (#27).
- (b) Two over-claims in Industry Relevancy, plus three wording over-claims elsewhere.
- (c) Scope leaves out the Tier 2 point from decision #20.
- (d) The Outputs group label is "Shared", but #30 says "Academic submissions".
- (e) Two APA 7 defects in the reference list.

All fixes below have been word-counted. Every section stays within its cap after them.

## Summary table

| # | Check | Result | Notes |
|---|---|---|---|
| 1 | Cold-reader test | PASS | Restated in 5 sentences. 7 terms are unclear (list below), none of them blocking |
| 2a | ID regex sweep, body | PASS | 0 hits for all 5 patterns, also over the whole pre-annex file including comments |
| 2b | Acronyms expanded at first use | PASS | All 13 acronyms are expanded at first use. In the Section A title "AI" comes before the expansion, which is acceptable for a title |
| 2c | Acronyms in glossary | PASS | All 13 are in `annex_2.md` Annex C. Product names are not; see A-2 (optional) |
| 2d | Coined terms ≤ about 6 | PASS | Exactly 6: guardrail, test bench, ablation, Briefing, evaluation harness, Tier 1/Tier 2. Each is defined at first use |
| 3 | Word counts vs caps | PASS | Every section is under its cap (table below). Overview (245/247) and Scope (219/222) are tight |
| 4 | Grounding / over-claims | **FAIL** | G-1 to G-7 below. Red-team: no integration is claimed, but the named person must go. Beacon detail stays high-level |
| 5 | Dates and constraints | PASS | Every date matches CLAUDE.md. The hardware and open-source/free statements match CLAUDE.md and #12. One optional clarity fix (S-1) |
| 6 | References | **FAIL** (minor) | 10 references, each cited, each citation resolves. Ordering of the MITRE entries and the Tan et al. URL are wrong (R-1, R-2) |
| 7 | Docx-only checks | N/A | This round reviews the draft only |

## Check 1: cold-reader test

Restatement from the document alone:
1. Workstream 1 builds a minimal evaluation harness. The harness runs the same labelled prompts through several AI guardrail products (NeMo Guardrails, Llama Guard 3/4, GovTech's Sentinel/LionGuard 2, and later Prompt Guard 2), so that harmful-content classification and jailbreak detection can be compared fairly, one setting at a time.
2. Workstream 2 builds Beacon, a daily automated service. Beacon collects public AI-security news, filters it, merges duplicate reports and rates significance. It publishes a ranked web Briefing and a Telegram digest, and gives an initial, evidence-traceable mapping of each event to Singapore Government SSP controls and MITRE ATT&CK/ATLAS techniques.
3. LTA operates critical infrastructure. Workstream 1 gives its cyber division (CYAD) evidence for choosing guardrails before it deploys generative AI. Workstream 2 gives CYAD timely, defensible threat awareness in control and attacker-technique terms.
4. Test bench results are due by 1 Dec 2026, with the report in the first week of Dec. Beacon is deployed by 1 Feb 2027, with CI/CD and monitoring through Feb, and March is buffer.
5. The SIT submissions are Form E1 (6 Dec), the Interim Presentation (31 Jan), Form E2 (21 Mar) and the Final Presentation (11 Apr, after the period). All work uses one 8 GB-GPU laptop and free tools.

Terms I could not fully explain from the document:

| Term | Where | Problem | Fix ref |
|---|---|---|---|
| LionGuard 2 | Overview | It is named as "served" by Sentinel, but what it does is never said | O-2 |
| NeMo Guardrails, Llama Guard | Overview | The vendors (NVIDIA, Meta) are not given, so the reader cannot tell what kind of product each one is | O-1 |
| Prompt Guard 2 | Scope | It is introduced only as a "third comparator", with no description | A-2 (glossary) |
| "the source list" | Objective 5 | The definite article points to a list the reader has never seen | Ob-1 |
| near-miss examples | Additional Knowledge | Not defined | C-1 (optional) |
| "Generative AI system type" | Industry Relevancy | It is not said what an SSP "system type" is. This is acceptable, because the clause is context | none |
| Form E1 / E2 | Outputs, Timeline | SIT-internal names. An SIT assessor knows them | none |

## Check 2: jargon / ID sweep

| Regex | Hits (body) |
|---|---|
| `\b[A-Z]{3}-\d{2}\b` | 0 |
| `\b[CSKDQX]-\d{2,3}\b` | 0 |
| `\bC\d{1,2}\b` | 0 |
| `\bP[012]\b` | 0 |
| `\bCP-\d+` | 0 |

Acronyms, where each is first expanded, and whether it is in the glossary (`annex_2.md`): all PASS.
- AI: Overview. In glossary.
- LTA: Overview. In glossary.
- CYAD: Overview. In glossary.
- GovTech: Overview. In glossary.
- SSP: Overview, per #17. In glossary.
- ATT&CK: Overview. In glossary.
- ATLAS: Overview. In glossary.
- CI/CD: Objective 8, per #31b. In glossary.
- GenAI: Industry Relevancy. In glossary.
- GPU: Scope. In glossary.
- STIX: Additional Knowledge. In glossary.
- OSCAL: Additional Knowledge. In glossary.
- API: Additional Knowledge. In glossary.

Other notes:
- MITRE, NeMo and the module codes are names, not acronyms. "GB" is a unit.
- GenAI, API, STIX and OSCAL are each used only once after expansion. This is acceptable. GenAI could optionally be dropped (see IR-5).
- British spelling: no US spellings found (I searched for -ize, color, center, catalog, defense, labeled and similar).

## Check 3: word counts (caps from `form_structure_findings_1.md` Part 3)

| Section | Draft 1 | Cap | Result | After all fixes below |
|---|---|---|---|---|
| A Project Title | 16 | none | PASS | 16 |
| B Overview | 245 | 247 | PASS | 247 (at cap) |
| B Objectives | 209 | 270 | PASS | 213 |
| B Industry Relevancy | 142 | 170 | PASS | 144 |
| B Scope | 219 | 222 | PASS | 220 |
| B Outputs and Deliverables | 78 | 110 | PASS | 83 |
| C Applicable Knowledge | 65 | 72 | PASS | 65 |
| C Additional Knowledge | 92 | 130 | PASS | 92 (up to 97 with C-1) |
| C Training | 65 | 105 | PASS | 67 |
| D Timeline | 229 | 312 | PASS | 229 |

## Check 4: grounding and over-claims

Claims that trace correctly (sample of the load-bearing ones):

| Claim in the draft | Source |
|---|---|
| Tier 1 functions and products | CLAUDE.md; `benchtest_findings_1.md:14-18` |
| Jailbreak comparators (NeMo and Sentinel, with Prompt Guard 2 planned) | #19 |
| Ablation definition | #21 |
| 4-bit or free cloud GPU credits | #18, #23 |
| Llama Guard 4 subject to access | #24 |
| Public or synthetic prompts only | #22 |
| Sentinel serves LionGuard 2 | `benchtest_findings_1.md:76` |
| Purple Llama and Litmus as planned additions | `benchtest_findings_1.md:25` |
| Beacon pipeline stages, Briefing and Telegram | `beacon_findings_1.md:6,24-31` |
| Initial mapping committed, trend detection stretch | #14 |
| Hosting | #11 |
| Telegram subject to LTA policy | #15 |
| SSP Generative AI system type | `security_frameworks_findings_1.md:9` |
| React and the Telegram bot API | `beacon_findings_1.md:51` |
| Section C modules | CLAUDE.md |

Beacon detail stays at outcome level: no requirement families, IDs, parameters or counts appear.

Problems:

| ID | Section | Text | Problem | Severity |
|---|---|---|---|---|
| G-1 | Industry Relevancy | "A parallel LTA capstone (Daniel Chua)" | Decision #27: do not name another student | **Blocking** |
| G-2 | Industry Relevancy | "expressed in the controls it must meet" | Implies LTA has an SSP obligation. `security_frameworks_findings_1.md:40`: "Do not claim LTA adoption or SSP obligation beyond the repo." The wording came from the brief, so this is logged as an open question; the conservative assumption is to under-claim | **Blocking** |
| G-3 | Industry Relevancy | "This supports the SSP, which defines…" | Claims the bench supports the SSP. No source shows that the SSP's generative AI controls cover guardrails | Moderate |
| G-4 | Scope | Tier 2 reasons | #20 requires the "needs a response-generating component" reason and that response checks be described as the natural next extension after Tier 1. Both are missing. Also, "only one product offers it" is narrower than the source reason "too few comparable products": off-topic detection has two products (`benchtest_findings_1.md:141`) | Moderate |
| G-5 | Overview | "Each event is mapped to…" | Unqualified. #14 commits only an **initial** mapping. Objective 7 and Scope already say "initial" | Minor |
| G-6 | Overview | "score every guardrail" | Only the Tier 1 products are scored | Minor |
| G-7 | Training | "LTA provides … the existing Sentinel access" | Sentinel access comes from GovTech, as a closed beta for public officers (`benchtest_findings_1.md:21`). CLAUDE.md says only that access "is available". Do not attribute its provision to LTA | Minor |
| G-8 | Industry Relevancy | "Beacon shortens the step…" | Present tense for a system that has not been built | Minor |

Red-team project: "the bench complements it on the defensive side, with no committed integration" is correct (CLAUDE.md). Only the name must go (G-1).

## Check 5: dates and constraints

| Item | Draft | CLAUDE.md | Result |
|---|---|---|---|
| Period | 8 Oct 2026 – 31 Mar 2027 | same | PASS |
| Form B | 8–11 Oct, due 11 Oct | by 11 Oct | PASS |
| Test bench results | 1 Dec 2026 (Objective 4, Timeline) | by 1 Dec 2026 | PASS |
| Test bench report | first week of Dec / 1–6 Dec | first week of Dec | PASS |
| Form E1 | 6 Dec | by 6 Dec | PASS |
| Beacon build | Dec–Jan | Dec–Jan | PASS |
| Interim Presentation | 31 Jan | by 31 Jan | PASS |
| Beacon deploy | 1 Feb 2027 | by 1 Feb 2027 | PASS |
| CI/CD and monitoring | through Feb | throughout Feb | PASS |
| March | buffer and iteration | buffer and iteration | PASS |
| Form E2 | 21 Mar | by 21 Mar | PASS |
| Final Presentation | 11 Apr, after the period | 11 Apr, after the period | PASS |
| Phasing | test bench heavier until early Dec; Beacon design continues | same | PASS |
| Annex A (`annex_2.md`) | deploy in Feb only | matches the body | PASS |
| Hardware | "the provided development laptop (8 GB GPU)" | one laptop, RTX 4060 8 GB, per #12 | PASS. Optional S-1 makes "one laptop" explicit |
| Open-source/free | "only open-source, free, free-trial or free-credit technology" | same | PASS |
| No LTA compute/sandbox | Training: "no further organisation-provided tooling or computing resources are assumed" | same | PASS |

## Check 6: references

- Count: 10 (limit 10). PASS.
- Citation to reference: every in-text citation (the drafter's table at lines 197–208) resolves to exactly one entry, and every entry is cited at least once. PASS.
- Verification: all ten trace to findings or the decisions log (#1, #2, #16; `benchtest_findings_1.md:83-93`). PASS.
- Suffix logic: GovTech n.d.-a Litmus / n.d.-b Sentinel / 2025 SSP, and MITRE n.d.-a ATLAS / n.d.-b ATT&CK. Both are ordered by title and come before dated works. PASS.
- Defects:
  - **R-1 (FAIL):** APA 7 alphabetises group authors by the first significant word of the name, so "The" is ignored. Move both "The MITRE Corporation" entries to sit between "Meta AI. (2023…)" and "Rebedea…". Keep the author string "The MITRE Corporation" as given in #16. The -a/-b letters do not change. Delete the drafter's placement note (line 195) from the annex.
  - **R-2 (FAIL):** Tan et al. (2025) is cited as an EMNLP 2025 proceedings paper with page numbers, but it links to the arXiv preprint. APA 7 requires the URL of the version cited. Replace `https://arxiv.org/abs/2507.15339` with `https://aclanthology.org/2025.emnlp-demos.20/`; WebSearch returned that ACL Anthology entry ID (`benchtest_findings_1.md:89`). Use a DOI only if it is verified.
  - R-3 (optional): Inan et al. (2023). APA 7's preprint form is "*Title* (arXiv:2312.06674). arXiv. https://doi.org/10.48550/arXiv.2312.06674". The current form is acceptable.
  - R-4 (optional): add "Retrieved October 8, 2026, from" to Meta (2025), because model-card pages change (as in #28).

## Per-section fix instructions (for formb-drafter, draft 2)

Word deltas were checked by script against the draft 1 text.

### A. Project Title
No change.

### B. Overview (245, becomes 247 at cap; do not add anything else)
- **O-1:** "Products such as NeMo Guardrails (Rebedea et al., 2023), Llama Guard (Inan et al., 2023)" becomes "Products such as NVIDIA's NeMo Guardrails (Rebedea et al., 2023), Meta's Llama Guard (Inan et al., 2023)". +2 words.
- **O-2:** "which serves LionGuard 2 (Tan et al., 2025)" becomes "which serves the LionGuard 2 harmful-content classifier (Tan et al., 2025)". +2 words.
- **O-3 (G-6):** "The test bench will score every guardrail on the same labelled inputs, on equal terms." becomes "The test bench will score each guardrail on the same labelled inputs." −3 words.
- **O-4 (G-5):** "Each event is mapped to" becomes "Each event is initially mapped to". +1 word.
- **O-5 (offset):** "Two complementary workstreams" becomes "Two workstreams". −1 word.
- Optional readability fix, word-neutral: replace "the Land Transport Authority's (LTA) Cyber Architecture & Development (CYAD) division adopts" with "the Cyber Architecture & Development (CYAD) division of the Land Transport Authority (LTA) adopts". This removes the possessive before a parenthesis. It adds 2 words, which would take the Overview over its cap. Use it only together with a 2-word cut, for example "turns the flood of AI-security news into" becoming "turns high-volume AI-security news into" (−1), plus dropping "short," before "evidence-backed Briefing" (−1).

### B. Objectives (209, becomes 213)
- **Ob-1:** In Objective 5, "collects items from the source list" becomes "collects items from a fixed list of English-language public sources". +4 words.

### B. Industry Relevancy (142, becomes 144)
- **IR-1 (G-1, #27):** "A parallel LTA capstone (Daniel Chua) is building an AI red-teaming tool that simulates attacks" becomes "A parallel LTA AI red-teaming capstone project is building a tool that simulates attacks". Keep the rest of the sentence ("…on the defensive side, with no committed integration.").
- **IR-2 (G-3):** "This supports the SSP, which defines" becomes "This is timely because the SSP defines".
- **IR-3 (G-2):** "expressed in the controls it must meet." becomes "expressed in recognised security-control and attacker-technique terms."
- **IR-4 (G-8):** "Beacon shortens the step" becomes "Beacon aims to shorten the step".
- IR-5 (optional): "generative AI (GenAI) system" becomes "generative AI system". GenAI is used only once. If you take this, ask annex-builder to drop the GenAI glossary row.

### B. Scope (219, becomes 220)
- **S-1 (constraint clarity):** "developed on the provided development laptop (8 GB graphics processing unit, GPU)." becomes "developed on a single provided development laptop with an 8 GB graphics processing unit (GPU)." This also fixes the awkward "(…, GPU)" expansion.
- **S-2 (G-4, #20):**
  - "only one product offers it;" becomes "too few comparable products;".
  - "it needs a document-retrieval or tool-using agent set-up; or it needs more computing power." becomes "it needs a response-generating, document-retrieval or tool-using agent set-up; or it needs more computing power. Checking chatbot responses is the natural next step."
- **S-3 (offset; it repeats Objectives 5–7):** "Beacon is scoped as high-level outcomes: daily collection from English-language public sources, filtering, merging, significance rating, the Briefing, the Telegram digest and initial mapping." becomes "Beacon covers the outcomes in objectives 5 to 8, using English-language public sources only."
- Keep the remaining Beacon sentences as they are: not a compliance tool; Singapore-region hosting; Telegram subject to LTA policy; trend detection as a stretch goal.

### B. Outputs and Deliverables (78, becomes 83)
- **Out-1 (#30):** the group label "Shared" becomes "Academic submissions".
- **Out-2:** "4. Deployed Beacon service with CI/CD and monitoring" becomes "4. Deployed Beacon service with CI/CD and monitoring (by 1 February 2027)". This matches item 3, which carries its date.

### C. Applicable Knowledge
No change.

### C. Additional Knowledge
- C-1 (optional): "labelled test sets with near-miss examples" becomes "labelled test sets, including harmless prompts that resemble harmful ones". +5 words, so 97/130.

### C. Training (65, becomes 67)
- **T-1 (G-7):** "LTA provides the development laptop and the existing Sentinel access." becomes "LTA provides the development laptop, and Sentinel access is already in place."

### D. Timeline
No change. Keep "Academic milestones", which matches Annex A (#31d).

### Annex D: References
Apply R-1 and R-2. R-3 and R-4 are optional. Remove the drafter's working notes (lines 173, 195 and 197–208) before the text goes into the docx.

## Cross-check notes for annex-builder (route via main session)
- **A-1 (decision #25):** the Figure 1 caption in `annex_2.md:31` does not say that "Tier 1 evaluates the input checks", which #25 requires. It also contains a repository path (`benchtest/helpful_explanation/nemo-rails-explained.html`) that an assessor cannot open. Replace it with "Adapted from the project's NeMo Guardrails explainer."
- A-2 (optional): add short glossary rows for the product names, which the body uses but does not explain: Sentinel, LionGuard 2, Prompt Guard 2, NeMo Guardrails, Llama Guard, Purple Llama, Litmus. The plain meanings are in the drafter's "Other technical terms" table. These rows do not count as coined terms.
- A-3: if O-3 is applied, change the glossary's "Test bench" definition from "every guardrail…, on equal terms" to "each guardrail in the comparison on the same labelled inputs", to match.
- A-4 (minor): Annex A says "Interim report, Form E1" and "Final report, Form E2", while the body says "Interim Report (Form E1)" and "Final Report (Form E2)". Use one capitalisation.

## Open questions → to_main_session
1. G-2: the content brief's wording, "mapped to the controls it must meet", conflicts with `security_frameworks_findings_1.md:40` ("do not claim … SSP obligation"). I assumed the conservative under-claim (IR-3). Please confirm, or log a decision if LTA's SSP obligation is to be stated.
2. R-1: I assumed APA 7's rule that group authors are alphabetised by the first significant word, which ignores "The". If the main session prefers literal ordering, the drafter's current order stands. The author string "The MITRE Corporation" (#16) is unchanged either way.
3. A-1 and A-2 need routing to annex-builder.
