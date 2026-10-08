# Form B draft 2 (formb-drafter, Stage 1)

Revision of draft 1. Applies every fix in `scratchpad/formb-reviewer_scratch/review_findings_1.md` (including optional O-readability, IR-5, C-1, R-3, R-4) and decisions #27–#34.

How to read this file:
- Each fenced `text` block is the exact content of one answer box (one paragraph inside the existing plain-text content control).
- Each new line in a block becomes a `<w:br/>`. A blank line becomes two consecutive `<w:br/>`.
- Numbering is typed ("1. "). Workstream labels are plain text on their own line, not bold.
- Word counts use form-analyst's method: whitespace split, typed numerals and labels counted, line breaks counted as spaces. Caps are the working caps (floor of 2.5 times Daniel's counts).
- The italic "(Please use a separate sheet if necessary…)" guidance lines stay unchanged in the docx. They are not part of these blocks.

---

## A. Project Title (replaces "Beacon")

```text
AI Security for Critical Infrastructure: A Guardrail Evaluation Test Bench and the Beacon AI-Security Briefing Service
```
<!-- words: 16 / cap: none (Section A field). Keeps both workstreams. -->

---

## B. Capstone Project Details

### Project Overview

```text
Two workstreams strengthen how the Cyber Architecture & Development (CYAD) division of the Land Transport Authority (LTA) adopts artificial intelligence (AI) safely and monitors AI-related threats.

Workstream 1: Guardrail Evaluation Test Bench
Guardrails are safety checks around an AI chatbot that allow, block or flag each message, catching harmful requests or jailbreaks (attempts to trick the chatbot into ignoring its rules) (see Annex B, Figure 1). Products such as NVIDIA's NeMo Guardrails (Rebedea et al., 2023), Meta's Llama Guard (Inan et al., 2023) and the Government Technology Agency's (GovTech) Sentinel service (Government Technology Agency, n.d.-b), which serves the LionGuard 2 harmful-content classifier (Tan et al., 2025), differ in what they check and report, making fair comparison hard. The test bench will score each guardrail on the same labelled inputs. It supports ablation: changing one guardrail or setting at a time while holding everything else fixed, to measure its individual effect.

Workstream 2: Beacon
Beacon will be a daily service that turns high-volume AI-security news into an evidence-backed Briefing: a ranked digest of the day's most significant events, each stating what happened and why it matters (see Annex B, Figure 2). Each event is initially mapped to the Singapore Government's System Security Plan (SSP) control catalogue, published by GovTech (Government Technology Agency, 2025), and to attacker techniques in MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) and MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) (The MITRE Corporation, n.d.-a, n.d.-b), with every judgement traceable to its evidence.
```
<!-- words: 246 / cap: 247 -->

### Project Objectives

```text
Across both workstreams, the candidate is expected to:

Workstream 1: Guardrail Evaluation Test Bench
1. Complete the comparative research on guardrail products, adding Meta's Purple Llama safety tools (Meta AI, 2023) and GovTech's Litmus testing platform (Government Technology Agency, n.d.-a).
2. Build a minimal, reusable evaluation harness: a test program that loads labelled inputs, calls each guardrail and records its verdicts in one common format.
3. Evaluate Tier 1, the first proposed comparison: harmful-content classification of user prompts, and jailbreak / prompt-attack detection.
4. Report, with evidence, which guardrails suit which function, with results by 1 December 2026.

Workstream 2: Beacon
5. Build a daily pipeline that collects items from a fixed list of English-language public sources, filters them for relevance, merges duplicate reports of the same event and rates each event's significance.
6. Publish a web Briefing and send a condensed daily digest to subscribers through a messaging channel (Telegram bot, subject to LTA policy).
7. Provide an initial mapping of each event to SSP controls and ATT&CK and ATLAS techniques, with every judgement traceable to its evidence.
8. Deploy Beacon by 1 February 2027, with continuous integration and continuous deployment (CI/CD) and monitoring in place throughout February.
Stretch goal: detection of trends across recent events, once the earlier stages are stable.
```
<!-- words: 213 / cap: 270 -->

### Industry Relevancy

```text
LTA operates critical infrastructure, so both the AI it adopts and the AI-related threats it faces have consequences beyond the organisation.

Workstream 1: Guardrail Evaluation Test Bench
The bench gives CYAD an evidence-based way to choose guardrails before any generative AI system is deployed, instead of relying on vendor claims. This is timely because the SSP defines a dedicated Generative AI system type with its own controls. A parallel LTA AI red-teaming capstone project is building a tool that simulates attacks on AI applications; the bench complements it on the defensive side, with no committed integration.

Workstream 2: Beacon
CYAD needs timely, defensible awareness of AI threats, expressed in recognised security-control and attacker-technique terms. By linking each news event to SSP controls and ATT&CK and ATLAS techniques, Beacon aims to shorten the step from reading a report to knowing which controls it affects.
```
<!-- words: 143 / cap: 170 -->

### Project Scope

```text
Both workstreams use only open-source, free, free-trial or free-credit technology, developed on a single provided development laptop with an 8 GB graphics processing unit (GPU).

Workstream 1: Guardrail Evaluation Test Bench
Tier 1 is in scope: harmful-content classification of user prompts (NeMo Guardrails, Llama Guard 3/4 and Sentinel's LionGuard 2), and jailbreak / prompt-attack detection (NeMo Guardrails and Sentinel, with Meta's Prompt Guard 2 as a planned third comparator). All other guardrail functions form Tier 2, under investigation, each for a stated reason: too few comparable products; products share the same underlying service; it needs a response-generating, document-retrieval or tool-using agent set-up; or it needs more computing power. Checking chatbot responses is the natural next step. Limitations: larger guardrail models run on the laptop in 4-bit quantised (compressed) form where possible, or on free-tier cloud GPU credits; Llama Guard 4 results are subject to model access (Meta, 2025), with Llama Guard 3 as the committed baseline; only public or synthetic test prompts are sent to hosted services.

Workstream 2: Beacon
Beacon covers the outcomes in objectives 5 to 8, using English-language public sources only. It is an awareness service, not a compliance tool. It will be deployed on free-tier or free-credit cloud infrastructure in the Singapore region. Telegram delivery is subject to LTA policy; trend detection is a stretch goal.
```
<!-- words: 220 / cap: 222 -->

### Project Outputs and Deliverables

```text
Each workstream produces working software and evidence, followed by the shared academic submissions.

Workstream 1: Guardrail Evaluation Test Bench
1. Evaluation harness (source code)
2. Tier 1 results dataset
3. Test bench evaluation report (first week of December 2026)

Workstream 2: Beacon
4. Deployed Beacon service with CI/CD and monitoring (by 1 February 2027)
5. Beacon source code and documentation

Academic submissions
6. Interim Report (Form E1)
7. Interim Presentation
8. Final Report (Form E2)
9. Final Presentation
10. Detailed Gantt chart (Gantt_Guo_Zi_Qiang_Robin.xlsx)
```
<!-- words: 83 / cap: 110 -->

---

## C. Knowledge and Training Requirements (shared, not split by workstream)

### Applicable Knowledge from the Degree Programme

```text
The project draws on five modules:
AAI3008 Large Language Models: running, prompting and evaluating language models and guardrails.
INF2006 Cloud Computing and Big Data: cloud deployment, scheduled pipelines and cloud GPU use.
INF2005 Cyber Security Fundamentals: threat frameworks, security controls and attacks on AI.
INF2003 Database Systems: stored records, audit trails and results data.
INF2001 Introduction to Software Engineering: requirements, testing, version control and CI/CD.
```
<!-- words: 65 / cap: 72 -->

### Additional Knowledge, Skillsets, or Certifications Required

```text
Practical knowledge of guardrail frameworks (NeMo Guardrails, Llama Guard, and LionGuard 2 through Sentinel); evaluation methods for safety classifiers (labelled test sets, including harmless prompts that resemble harmful ones, precision, recall and false-positive rates); running openly released models in compressed form within limited GPU memory; web collection and text extraction; the Structured Threat Information Expression (STIX) 2.1 and Open Security Controls Assessment Language (OSCAL) data formats; MITRE ATT&CK, MITRE ATLAS and the SSP; CI/CD and service monitoring; React for the web interface; and the Telegram bot application programming interface (API).

No formal certification is a prerequisite.
```
<!-- words: 96 / cap: 130 -->

### Training Required and Provided

```text
An initial orientation to LTA's AI and information-security policies will be required, including the approval needed before using any external service (for example, hosted guardrail services, cloud hosting and the Telegram channel). LTA provides the development laptop, and Sentinel access is already in place. All other learning is self-directed, through open documentation, published papers and free-tier cloud credits; no further organisation-provided tooling or computing resources are assumed.
```
<!-- words: 67 / cap: 105 -->

---

## D. Project Timeline

```text
The project runs from 8 October 2026 to 31 March 2027 with the two workstreams in parallel: the test bench is the main focus until early December while Beacon's design continues, and Beacon is built in December and January.

Workstream 1: Guardrail Evaluation Test Bench
October 2026: complete the comparative research (adding Purple Llama and Litmus), build the evaluation harness and request Llama Guard 4 access.
November 2026: run the Tier 1 evaluations on the laptop and on free cloud GPU credits.
1 December 2026: evaluation results complete.
1–6 December 2026: test bench evaluation report, which also feeds the Interim Report (Form E1).

Workstream 2: Beacon
October – November 2026: design of the later pipeline stages continues at low intensity.
December 2026 – January 2027: build the pipeline in order: collection, filtering, merging, significance rating, the Briefing and Telegram digest, then initial mapping.
1 February 2027: Beacon deployed.
February 2027: CI/CD, monitoring and fixes from live running.
March 2027: buffer and iteration; trend detection as a stretch goal.

Academic milestones
8–11 October 2026: Form B, due 11 October.
6 December 2026: Interim Report (Form E1).
31 January 2027: Interim Presentation.
21 March 2027: Final Report (Form E2).
31 March 2027: end of the project period.
11 April 2027: Final Presentation (after the project period).

A summary Gantt chart is in Annex A; the detailed chart is provided in Gantt_Guo_Zi_Qiang_Robin.xlsx.
```
<!-- words: 229 / cap: 312 -->

---

## Annex D: References (APA 7)

Government Technology Agency. (n.d.-a). *Litmus*. Retrieved October 8, 2026, from https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus

Government Technology Agency. (n.d.-b). *Sentinel*. Retrieved October 8, 2026, from https://www.developer.tech.gov.sg/products/categories/cybersecurity/sentinel

Government Technology Agency. (2025). *System Security Plan (SSP)*. https://info.standards.tech.gov.sg/ssp/

Inan, H., Upasani, K., Chi, J., Rungta, R., Iyer, K., Mao, Y., Tontchev, M., Hu, Q., Fuller, B., Testuggine, D., & Khabsa, M. (2023). *Llama Guard: LLM-based input-output safeguard for human-AI conversations* (arXiv:2312.06674). arXiv. https://doi.org/10.48550/arXiv.2312.06674

Meta. (2025). *Llama Guard 4* [Model card and prompt format]. Retrieved October 8, 2026, from https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama-guard-4/

Meta AI. (2023, December 7). *Announcing Purple Llama: Towards open trust and safety in the new world of generative AI*. https://ai.meta.com/blog/purple-llama-open-trust-safety-generative-ai/

The MITRE Corporation. (n.d.-a). *MITRE ATLAS: Adversarial Threat Landscape for Artificial-Intelligence Systems*. Retrieved October 8, 2026, from https://atlas.mitre.org/

The MITRE Corporation. (n.d.-b). *MITRE ATT&CK*. Retrieved October 8, 2026, from https://attack.mitre.org/

Rebedea, T., Dinu, R., Sreedhar, M., Parisien, C., & Cohen, J. (2023). NeMo Guardrails: A toolkit for controllable and safe LLM applications with programmable rails. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: System Demonstrations* (pp. 431–445). Association for Computational Linguistics. https://doi.org/10.18653/v1/2023.emnlp-demo.40

Tan, L., Chua, G., Ge, Z., & Lee, R. K.-W. (2025). LionGuard 2: Building lightweight, data-efficient and localised multilingual content moderators. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations* (pp. 264–285). Association for Computational Linguistics. https://aclanthology.org/2025.emnlp-demos.20/

---

## Drafter notes on Annex D (not for the docx)

- Order follows APA 7: alphabetical by the first significant word of the author (so "The MITRE Corporation" files under M, #33); for the same author, undated works first, then by year; "-a"/"-b" ordered by title. Italics are shown with asterisks; apply real italics in the docx.
- Retrieval dates per #28 (undated or changing pages, including the Llama Guard 4 model card).
- Tan et al. (2025) now links to the ACL Anthology version (the version cited, with page numbers). The Inan et al. (2023) entry uses APA 7 preprint form with the arXiv DOI.

In-text citations used in the body (check list for the reviewer):
| Citation | Section(s) |
|---|---|
| (Rebedea et al., 2023) | Overview |
| (Inan et al., 2023) | Overview |
| (Government Technology Agency, n.d.-b) — Sentinel | Overview |
| (Tan et al., 2025) | Overview |
| (Government Technology Agency, 2025) — SSP | Overview |
| (The MITRE Corporation, n.d.-a, n.d.-b) — ATLAS, ATT&CK | Overview |
| (Meta AI, 2023) — Purple Llama | Objectives |
| (Government Technology Agency, n.d.-a) — Litmus | Objectives |
| (Meta, 2025) — Llama Guard 4 | Scope |

---

## Terms used (for annex-builder's Annex C glossary)

Acronyms, each expanded at first use in the body (section of first use in brackets). Change from draft 1: GenAI removed (reviewer IR-5), so annex-builder should drop the GenAI glossary row.
| Term | Expansion / plain meaning | First use |
|---|---|---|
| AI | artificial intelligence | Overview |
| API | application programming interface | Additional Knowledge |
| ATLAS | MITRE Adversarial Threat Landscape for Artificial-Intelligence Systems: a public knowledge base of attacker tactics and techniques against AI systems | Overview |
| ATT&CK | MITRE Adversarial Tactics, Techniques, and Common Knowledge: a public knowledge base of real-world attacker tactics and techniques | Overview |
| CI/CD | continuous integration and continuous deployment: automated testing and release of software changes | Objectives |
| CYAD | Cyber Architecture & Development division (LTA) | Overview |
| GovTech | Government Technology Agency (Singapore) | Overview |
| GPU | graphics processing unit | Scope |
| LTA | Land Transport Authority | Overview |
| OSCAL | Open Security Controls Assessment Language: a machine-readable format for security controls | Additional Knowledge |
| SSP | the Singapore Government's System Security Plan control catalogue, published by GovTech | Overview |
| STIX | Structured Threat Information Expression: a standard data format for threat knowledge | Additional Knowledge |

Coined or defined terms (6, each defined at first use):
| Term | Plain meaning | First use |
|---|---|---|
| guardrail | a safety check around an AI chatbot that allows, blocks or flags each message | Overview |
| test bench (Guardrail Evaluation Test Bench) | the set-up that scores each guardrail in the comparison on the same labelled inputs | Overview |
| ablation | changing one guardrail or setting at a time while holding everything else fixed, to measure its individual effect | Overview |
| Briefing | Beacon's evidence-backed daily digest: a ranked list of the day's most significant AI-security events, each stating what happened and why it matters | Overview |
| evaluation harness | the test program that loads labelled inputs, calls each guardrail and records its verdicts in one common format | Objectives |
| Tier 1 / Tier 2 | Tier 1: the first proposed comparison (harmful-content classification of user prompts; jailbreak / prompt-attack detection). Tier 2: all other guardrail functions, under investigation, each for a stated reason | Objectives / Scope |

Other technical terms used in plain sense (glossary candidates if space allows):
| Term | Plain meaning |
|---|---|
| jailbreak / prompt attack | an attempt to trick a chatbot into ignoring its rules |
| harmful-content classification | deciding whether a prompt asks for harmful material |
| labelled inputs / labelled test set | test prompts each marked in advance as harmful or benign (or attack or benign) |
| harmless prompts that resemble harmful ones | benign test prompts used to measure false alarms (near-miss examples) |
| precision, recall, false-positive rate | standard measures of how often a check is right when it flags, how much it catches, and how often it flags benign input |
| 4-bit quantised (compressed) form | a model stored at reduced numerical precision so it fits in less GPU memory |
| mapping | linking a news event to the security control or attacker technique it bears on |
| significance | how serious, large or new an event is |
| red-teaming | simulated attacks on a system to find weaknesses |
| response-generating set-up | a component that produces chatbot answers, needed before response checks can be tested |
| Generative AI system type (SSP) | the SSP's set of controls for generative AI systems |
| Sentinel | GovTech's hosted guardrail service |
| LionGuard 2 | GovTech's Singapore-tuned harmful-content classifier, served through Sentinel |
| NeMo Guardrails | NVIDIA's open-source toolkit for adding guardrails to chatbot applications |
| Llama Guard | Meta's openly released safety classifier for chatbot inputs and outputs |
| Prompt Guard 2 | Meta's small classifier for jailbreak and prompt-attack detection (part of Purple Llama) |
| Purple Llama | Meta's umbrella project of open safety tools and evaluations |
| Litmus | GovTech's pre-deployment testing platform for generative AI applications |
| Telegram bot | an automated Telegram account that sends Beacon's daily digest to subscribers |

---

## Self-checks done

- Internal-ID regex sweep over all blocks (the five plan patterns): 0 hits. Also 0 hits for "Daniel", "Chua", "GenAI", "must meet" and "Shared".
- Every word count re-measured by script after the edits; every section is within its cap (Overview 246/247, Scope 220/222).
- Reviewer fixes applied: O-1 to O-5 plus the optional Overview readability swap (offset by "high-volume" and dropping "short,"); Ob-1; IR-1 to IR-4 plus optional IR-5; S-1 to S-3; Out-1, Out-2; optional C-1; T-1; R-1, R-2 plus optional R-3, R-4. Working notes moved out of Annex D.
- Decisions applied: #27 (no named student), #28 (retrieval dates), #29 (test bench evaluation report), #30 ("Academic submissions" in Outputs), #31b (CI/CD = continuous integration and continuous deployment), #32 (IR-3 under-claim), #33 (APA group-author ordering). Timeline keeps "Academic milestones" (#31d, matching Annex A).
- Terms list updated: GenAI removed; test bench, Briefing and near-miss rows reworded to match the body; "response-generating set-up" added.

## Open questions → to_main_session

1. Inan et al. (2023) now uses the arXiv DOI (https://doi.org/10.48550/arXiv.2312.06674), following reviewer R-3. arXiv assigns this DOI to every paper by its ID. Assumption: it counts as verified with the arXiv ID already verified (#1).
2. For annex-builder (please route): drop the GenAI glossary row (IR-5). Use the reworded test bench and Briefing definitions in the Terms list above (A-3).
