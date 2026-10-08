# Form B draft 1 (formb-drafter, Stage 1)

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
Two complementary workstreams strengthen how the Land Transport Authority's (LTA) Cyber Architecture & Development (CYAD) division adopts artificial intelligence (AI) safely and monitors AI-related threats.

Workstream 1: Guardrail Evaluation Test Bench
Guardrails are safety checks around an AI chatbot that allow, block or flag each message, catching harmful requests or jailbreaks (attempts to trick the chatbot into ignoring its rules) (see Annex B, Figure 1). Products such as NeMo Guardrails (Rebedea et al., 2023), Llama Guard (Inan et al., 2023) and the Government Technology Agency's (GovTech) Sentinel service (Government Technology Agency, n.d.-b), which serves LionGuard 2 (Tan et al., 2025), differ in what they check and report, making fair comparison hard. The test bench will score every guardrail on the same labelled inputs, on equal terms. It supports ablation: changing one guardrail or setting at a time while holding everything else fixed, to measure its individual effect.

Workstream 2: Beacon
Beacon will be a daily service that turns the flood of AI-security news into a short, evidence-backed Briefing: a ranked digest of the day's most significant events, each stating what happened and why it matters (see Annex B, Figure 2). Each event is mapped to the Singapore Government's System Security Plan (SSP) control catalogue, published by GovTech (Government Technology Agency, 2025), and to attacker techniques in MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) and MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) (The MITRE Corporation, n.d.-a, n.d.-b), with every judgement traceable to its evidence.
```
<!-- words: 245 / cap: 247 -->

### Project Objectives

```text
Across both workstreams, the candidate is expected to:

Workstream 1: Guardrail Evaluation Test Bench
1. Complete the comparative research on guardrail products, adding Meta's Purple Llama safety tools (Meta AI, 2023) and GovTech's Litmus testing platform (Government Technology Agency, n.d.-a).
2. Build a minimal, reusable evaluation harness: a test program that loads labelled inputs, calls each guardrail and records its verdicts in one common format.
3. Evaluate Tier 1, the first proposed comparison: harmful-content classification of user prompts, and jailbreak / prompt-attack detection.
4. Report, with evidence, which guardrails suit which function, with results by 1 December 2026.

Workstream 2: Beacon
5. Build a daily pipeline that collects items from the source list, filters them for relevance, merges duplicate reports of the same event and rates each event's significance.
6. Publish a web Briefing and send a condensed daily digest to subscribers through a messaging channel (Telegram bot, subject to LTA policy).
7. Provide an initial mapping of each event to SSP controls and ATT&CK and ATLAS techniques, with every judgement traceable to its evidence.
8. Deploy Beacon by 1 February 2027, with continuous integration and continuous deployment (CI/CD) and monitoring in place throughout February.
Stretch goal: detection of trends across recent events, once the earlier stages are stable.
```
<!-- words: 209 / cap: 270 -->

### Industry Relevancy

```text
LTA operates critical infrastructure, so both the AI it adopts and the AI-related threats it faces have consequences beyond the organisation.

Workstream 1: Guardrail Evaluation Test Bench
The bench gives CYAD an evidence-based way to choose guardrails before any generative AI (GenAI) system is deployed, instead of relying on vendor claims. This supports the SSP, which defines a dedicated Generative AI system type with its own controls. A parallel LTA capstone (Daniel Chua) is building an AI red-teaming tool that simulates attacks on AI applications; the bench complements it on the defensive side, with no committed integration.

Workstream 2: Beacon
CYAD needs timely, defensible awareness of AI threats, expressed in the controls it must meet. By linking each news event to SSP controls and ATT&CK and ATLAS techniques, Beacon shortens the step from reading a report to knowing which controls it affects.
```
<!-- words: 142 / cap: 170 -->

### Project Scope

```text
Both workstreams use only open-source, free, free-trial or free-credit technology, developed on the provided development laptop (8 GB graphics processing unit, GPU).

Workstream 1: Guardrail Evaluation Test Bench
Tier 1 is in scope: harmful-content classification of user prompts (NeMo Guardrails, Llama Guard 3/4 and Sentinel's LionGuard 2), and jailbreak / prompt-attack detection (NeMo Guardrails and Sentinel, with Meta's Prompt Guard 2 as a planned third comparator). All other guardrail functions form Tier 2, under investigation, each for a stated reason: only one product offers it; products share the same underlying service; it needs a document-retrieval or tool-using agent set-up; or it needs more computing power. Limitations: larger guardrail models run on the laptop in 4-bit quantised (compressed) form where possible, or on free-tier cloud GPU credits; Llama Guard 4 results are subject to model access (Meta, 2025), with Llama Guard 3 as the committed baseline; only public or synthetic test prompts are sent to hosted services.

Workstream 2: Beacon
Beacon is scoped as high-level outcomes: daily collection from English-language public sources, filtering, merging, significance rating, the Briefing, the Telegram digest and initial mapping. It is an awareness service, not a compliance tool. It will be deployed on free-tier or free-credit cloud infrastructure in the Singapore region. Telegram delivery is subject to LTA policy; trend detection is a stretch goal.
```
<!-- words: 219 / cap: 222 -->

### Project Outputs and Deliverables

```text
Each workstream produces working software and evidence, followed by the shared academic submissions.

Workstream 1: Guardrail Evaluation Test Bench
1. Evaluation harness (source code)
2. Tier 1 results dataset
3. Test bench evaluation report (first week of December 2026)

Workstream 2: Beacon
4. Deployed Beacon service with CI/CD and monitoring
5. Beacon source code and documentation

Shared
6. Interim Report (Form E1)
7. Interim Presentation
8. Final Report (Form E2)
9. Final Presentation
10. Detailed Gantt chart (Gantt_Guo_Zi_Qiang_Robin.xlsx)
```
<!-- words: 78 / cap: 110 -->

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
Practical knowledge of guardrail frameworks (NeMo Guardrails, Llama Guard, and LionGuard 2 through Sentinel); evaluation methods for safety classifiers (labelled test sets with near-miss examples, precision, recall and false-positive rates); running openly released models in compressed form within limited GPU memory; web collection and text extraction; the Structured Threat Information Expression (STIX) 2.1 and Open Security Controls Assessment Language (OSCAL) data formats; MITRE ATT&CK, MITRE ATLAS and the SSP; CI/CD and service monitoring; React for the web interface; and the Telegram bot application programming interface (API).

No formal certification is a prerequisite.
```
<!-- words: 92 / cap: 130 -->

### Training Required and Provided

```text
An initial orientation to LTA's AI and information-security policies will be required, including the approval needed before using any external service (for example, hosted guardrail services, cloud hosting and the Telegram channel). LTA provides the development laptop and the existing Sentinel access. All other learning is self-directed, through open documentation, published papers and free-tier cloud credits; no further organisation-provided tooling or computing resources are assumed.
```
<!-- words: 65 / cap: 105 -->

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

All ten entries in the brief's selection are cited in the body, so none is dropped. Order follows APA 7: alphabetical by author; for the same author, undated works first, then by year; "-a"/"-b" suffixes ordered by title. Italics shown with asterisks; apply real italics in the docx (the annex sits outside the plain-text controls). Retrieval dates are given for the undated web pages, whose content changes over time; the date is the verification date in the decisions log (#1, #2, #16).

Government Technology Agency. (n.d.-a). *Litmus*. Retrieved October 8, 2026, from https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus

Government Technology Agency. (n.d.-b). *Sentinel*. Retrieved October 8, 2026, from https://www.developer.tech.gov.sg/products/categories/cybersecurity/sentinel

Government Technology Agency. (2025). *System Security Plan (SSP)*. https://info.standards.tech.gov.sg/ssp/

Inan, H., Upasani, K., Chi, J., Rungta, R., Iyer, K., Mao, Y., Tontchev, M., Hu, Q., Fuller, B., Testuggine, D., & Khabsa, M. (2023). *Llama Guard: LLM-based input-output safeguard for human-AI conversations*. arXiv. https://arxiv.org/abs/2312.06674

Meta. (2025). *Llama Guard 4* [Model card and prompt format]. https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama-guard-4/

Meta AI. (2023, December 7). *Announcing Purple Llama: Towards open trust and safety in the new world of generative AI*. https://ai.meta.com/blog/purple-llama-open-trust-safety-generative-ai/

Rebedea, T., Dinu, R., Sreedhar, M., Parisien, C., & Cohen, J. (2023). NeMo Guardrails: A toolkit for controllable and safe LLM applications with programmable rails. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: System Demonstrations* (pp. 431–445). Association for Computational Linguistics. https://doi.org/10.18653/v1/2023.emnlp-demo.40

Tan, L., Chua, G., Ge, Z., & Lee, R. K.-W. (2025). LionGuard 2: Building lightweight, data-efficient and localised multilingual content moderators. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations* (pp. 264–285). Association for Computational Linguistics. https://arxiv.org/abs/2507.15339

The MITRE Corporation. (n.d.-a). *MITRE ATLAS: Adversarial Threat Landscape for Artificial-Intelligence Systems*. Retrieved October 8, 2026, from https://atlas.mitre.org/

The MITRE Corporation. (n.d.-b). *MITRE ATT&CK*. Retrieved October 8, 2026, from https://attack.mitre.org/

Note on placement of "The MITRE Corporation": APA 7 alphabetises a group author by its full name as written, so it is placed under "T". If the reviewer prefers alphabetising on the first significant word ("MITRE"), move both entries after "Meta AI"; the n.d.-a/-b letters do not change.

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

Acronyms, each expanded at first use in the body (section of first use in brackets):
| Term | Expansion / plain meaning | First use |
|---|---|---|
| AI | artificial intelligence | Overview |
| API | application programming interface | Additional Knowledge |
| ATLAS | MITRE Adversarial Threat Landscape for Artificial-Intelligence Systems: a public knowledge base of attacker tactics and techniques against AI systems | Overview |
| ATT&CK | MITRE Adversarial Tactics, Techniques, and Common Knowledge: a public knowledge base of real-world attacker tactics and techniques | Overview |
| CI/CD | continuous integration and continuous deployment: automated testing and release of software changes | Objectives |
| CYAD | Cyber Architecture & Development division (LTA) | Overview |
| GenAI | generative AI: AI systems that produce text, images or other content | Industry Relevancy |
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
| test bench (Guardrail Evaluation Test Bench) | the set-up that scores every guardrail on the same labelled inputs, on equal terms | Overview |
| ablation | changing one guardrail or setting at a time while holding everything else fixed, to measure its individual effect | Overview |
| Briefing | Beacon's short, evidence-backed daily digest: a ranked list of the day's most significant AI-security events, each stating what happened and why it matters | Overview |
| evaluation harness | the test program that loads labelled inputs, calls each guardrail and records its verdicts in one common format | Objectives |
| Tier 1 / Tier 2 | Tier 1: the first proposed comparison (harmful-content classification of user prompts; jailbreak / prompt-attack detection). Tier 2: all other guardrail functions, under investigation, each for a stated reason | Objectives / Scope |

Other technical terms used in plain sense (glossary candidates if space allows):
| Term | Plain meaning |
|---|---|
| jailbreak / prompt attack | an attempt to trick a chatbot into ignoring its rules |
| harmful-content classification | deciding whether a prompt asks for harmful material |
| labelled inputs / labelled test set | test prompts each marked in advance as harmful or benign (or attack or benign) |
| near-miss example | a benign prompt that resembles a harmful one, used to measure false alarms |
| precision, recall, false-positive rate | standard measures of how often a check is right when it flags, how much it catches, and how often it flags benign input |
| 4-bit quantised (compressed) form | a model stored at reduced numerical precision so it fits in less GPU memory |
| mapping | linking a news event to the security control or attacker technique it bears on |
| significance | how serious, large or new an event is |
| red-teaming | simulated attacks on a system to find weaknesses |
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

- Internal-ID regex sweep over all blocks (`\b[A-Z]{3}-\d{2}\b`, `\b[CSKDQX]-\d{2,3}\b`, `\bC\d{1,2}\b`, `\bP[012]\b`, `\bCP-\d+`): 0 hits.
- Every section of B and D opens with an umbrella line, then "Workstream 1: Guardrail Evaluation Test Bench", then "Workstream 2: Beacon". Outputs and Timeline add a third, shared group ("Shared" / "Academic milestones") after the two workstreams for the SIT submissions.
- Phrasing follows decisions #11 (hosting), #12 (laptop), #14 (mapping committed, trends stretch), #15 (Telegram), #17 (SSP expansion), #18 (4-bit or free cloud credits, never 8-bit local), #19 (jailbreak comparators), #21 (ablation), #22 (public or synthetic prompts only), #23 (no quota numbers), #24 (Llama Guard 4 subject to access).
- Section C claims no certification and no LTA-provided sandbox or compute.
- Timeline cross-checked against annex-builder's Annex A abstract (`scratchpad/annex-builder_scratch/annex_1.md`): phases and dates agree. Annex A marks the deploy in both Jan and Feb; the body says 1 February 2027, so Feb only is suggested.

## Open questions → to_main_session

1. Daniel Chua is named in Industry Relevancy, following the brief ("a parallel LTA red-teaming project (Daniel Chua)"). Assumption: naming him is acceptable, since it is a fellow candidate's public capstone. Drop the parenthesis if not wanted (saves 2 words).
2. Retrieval dates for the four undated web references use the verification date, 8 October 2026 (decisions #1, #16). Assumption: acceptable under APA 7 for pages that change over time.
3. The internal name "benchtest report" is rendered as "Test bench evaluation report" in Outputs and Timeline. Assumption: the plain name is preferred.
4. The Outputs and Timeline sections add a third group for shared academic submissions after the two workstream groups. Assumption: this keeps the two-workstream frame while putting the SIT milestones in one place.
5. For annex-builder (please route): the provisional Annex C glossary differs from this draft. (a) CYAD is expanded there as "Cyber Defence Division"; the form and Robin's department field say Cyber Architecture & Development. (b) CI/CD is "continuous delivery" there and "continuous deployment" here; use one (this draft's wording, or change both). (c) "Development", "LLM" and "Critical infrastructure" entries: the body uses "event", never "LLM" (only inside a reference title), and "critical infrastructure" in plain sense, so drop the first two. (d) Annex A row "Benchtest report" should read "Test bench evaluation report", and "SIT milestones" should read "Academic milestones" or expand SIT (Singapore Institute of Technology), since the body avoids the acronym. Use the "## Terms used" list above as the source.
