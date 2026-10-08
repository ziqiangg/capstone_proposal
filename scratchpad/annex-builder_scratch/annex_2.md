# Annex content (annex-builder, round 2)

## Annex A: month-level Gantt (for Word table)

Legend: X = active; M = milestone in that month. 8 Oct 2026 to 31 Mar 2027 is the capstone period; the Final Presentation (11 Apr) falls after it. Detailed weekly chart: `Gantt_Guo_Zi_Qiang_Robin.xlsx`.

| Row | Oct 2026 | Nov | Dec | Jan 2027 | Feb | Mar | Apr |
|---|---|---|---|---|---|---|---|
| **Academic milestones** | | | | | | | |
| Form B (11 Oct) | M | | | | | | |
| Interim report, Form E1 (6 Dec) | | X | M | | | | |
| Interim Presentation (by 31 Jan) | | | | M | | | |
| Final report, Form E2 (21 Mar) | | | | | | M | |
| Capstone period ends (31 Mar) | | | | | | M | |
| Final Presentation (11 Apr) | | | | | | | M |
| **Workstream 1: Guardrail Evaluation Test Bench** | | | | | | | |
| Complete research; build evaluation harness | X | X | | | | | |
| Run Tier 1 evaluation | | X | M (results 1 Dec) | | | | |
| Test bench evaluation report; tidy code and dataset | | | X | | | | |
| **Workstream 2: Beacon** | | | | | | | |
| Design (low intensity) | X | X | | | | | |
| Build: collect, filter, merge, rate, publish, map | | | X | X | | | |
| Deploy (1 Feb) | | | | | M | | |
| CI/CD, monitoring and fixes | | | | | X | | |
| Buffer and iteration (trend detection is a stretch goal) | | | | | X | X | |

Note: deploy (1 Feb 2027) is marked in Feb only, matching the body.

## Annex B: figure captions

- **Figure 1.** Where a guardrail can sit around an AI chatbot. Input checks inspect what the user types; conversation rules and action checks (dashed boxes) are written by the developer; retrieval checks clean passages from the organisation's documents; output checks inspect the answer before the user sees it. Adapted from the project's NeMo Guardrails explainer (benchtest/helpful_explanation/nemo-rails-explained.html).
- **Figure 2.** The Beacon daily pipeline in six steps: collect, filter, merge, rate and map, publish, deliver. Every judgement is recorded with its evidence.

Files: `scratchpad/annex-builder_scratch/figures/figure1_guardrail_checkpoints.png` (3680 px wide, 2x) and `figure2_beacon_pipeline.png` (2280 px wide, 2x). Insert at about 16 cm width.

## Annex C: glossary (from the drafter's "Terms used" list)

| Term | Plain definition |
|---|---|
| AI | Artificial intelligence. |
| API | Application programming interface. |
| ATLAS | MITRE Adversarial Threat Landscape for Artificial-Intelligence Systems: a public knowledge base of attacker tactics and techniques against AI systems. |
| ATT&CK | MITRE Adversarial Tactics, Techniques, and Common Knowledge: a public knowledge base of real-world attacker tactics and techniques. |
| CI/CD | Continuous integration and continuous deployment: automated testing and release of software changes. |
| CYAD | Cyber Architecture & Development division, Land Transport Authority. |
| GenAI | Generative AI: AI systems that produce text, images or other content. |
| GovTech | Government Technology Agency (Singapore). |
| GPU | Graphics processing unit. |
| LTA | Land Transport Authority. |
| OSCAL | Open Security Controls Assessment Language: a machine-readable format for security controls. |
| SSP | The Singapore Government's System Security Plan control catalogue, published by GovTech. |
| STIX | Structured Threat Information Expression: a standard data format for threat knowledge. |
| Ablation | Changing one guardrail or setting at a time while holding everything else fixed, to measure its individual effect. |
| Briefing | Beacon's short, evidence-backed daily digest: a ranked list of the day's most significant AI-security events, each stating what happened and why it matters. |
| Evaluation harness | The test program that loads labelled inputs, calls each guardrail and records its verdicts in one common format. |
| Guardrail | A safety check around an AI chatbot that allows, blocks or flags each message. |
| Test bench (Guardrail Evaluation Test Bench) | The set-up that scores every guardrail on the same labelled inputs, on equal terms. |
| Tier 1 / Tier 2 | Tier 1: the first proposed comparison (harmful-content classification of user prompts; jailbreak / prompt-attack detection). Tier 2: all other guardrail functions, under investigation, each for a stated reason. |

## Open questions → to_main_session
- Glossary limited to the acronym and coined-term tables; the "other technical terms" list was left out as instructed.
