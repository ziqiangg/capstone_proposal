# Annex content (annex-builder, round 1)

## Annex A: month-level Gantt (for Word table)

Legend: X = active; M = milestone in that month. 8 Oct 2026 to 31 Mar 2027 is the capstone period; the Final Presentation (11 Apr) falls after it. Detailed weekly chart: `Gantt_Guo_Zi_Qiang_Robin.xlsx`.

| Row | Oct 2026 | Nov | Dec | Jan 2027 | Feb | Mar | Apr |
|---|---|---|---|---|---|---|---|
| **SIT milestones** | | | | | | | |
| Form B (11 Oct) | M | | | | | | |
| Interim report, Form E1 (6 Dec) | | X | M | | | | |
| Interim Presentation (by 31 Jan) | | | | M | | | |
| Final report, Form E2 (21 Mar) | | | | | | M | |
| Capstone period ends (31 Mar) | | | | | | M | |
| Final Presentation (11 Apr) | | | | | | | M |
| **Workstream 1: Guardrail Evaluation Test Bench** | | | | | | | |
| Complete research; build evaluation harness | X | X | | | | | |
| Run Tier 1 evaluation | | X | M (results 1 Dec) | | | | |
| Benchtest report; tidy code and dataset | | | X | | | | |
| **Workstream 2: Beacon** | | | | | | | |
| Design (low intensity) | X | X | | | | | |
| Build: collect, filter, merge, rate, publish, map | | | X | X | | | |
| Deploy (1 Feb) | | | | M | M | | |
| CI/CD, monitoring and fixes | | | | | X | | |
| Buffer and iteration (trend detection is a stretch goal) | | | | | X | X | |

Note: deploy date 1 Feb sits at the Jan/Feb boundary, so it is marked in both columns; the drafter may keep only Feb.

## Annex B: figure captions

- **Figure 1.** Where a guardrail can sit around an AI chatbot. Input checks inspect what the user types; conversation rules and action checks (dashed boxes) are written by the developer; retrieval checks clean passages from the organisation's documents; output checks inspect the answer before the user sees it. Adapted from the project's NeMo Guardrails explainer (benchtest/helpful_explanation/nemo-rails-explained.html).
- **Figure 2.** The Beacon daily pipeline in six steps: collect, filter, merge, rate and map, publish, deliver. Every judgement is recorded with its evidence.

Files: `scratchpad/annex-builder_scratch/figures/figure1_guardrail_checkpoints.png` (3680 px wide, 2x) and `figure2_beacon_pipeline.png` (2280 px wide, 2x). Insert at about 16 cm width.

## Annex C: glossary (PROVISIONAL)

The drafter's "## Terms used" list did not exist when this was written. Drafted from the brief and translation tables. Prune to terms actually in the draft once `formb_draft_1.md` exists.

| Term | Plain definition |
|---|---|
| Ablation | A controlled experiment that switches off, swaps or varies one part at a time so the effect of that part can be measured. |
| Briefing | Beacon's short daily web page of the most significant AI-security developments, each backed by evidence. |
| CI/CD (continuous integration and continuous delivery) | Automated steps that test and release each change to software. |
| Critical infrastructure | Systems whose failure would seriously affect essential services such as transport. |
| CYAD | Cyber Defence Division (Cyber Assurance and Defence team) at LTA. Expand per the form's own wording. |
| Development | One real-world event, together with all the reports about it, merged into one item. |
| Guardrail | A safety check placed around an AI chatbot that inspects text and allows, blocks or changes it. |
| Harness (evaluation harness) | The smallest software needed to feed test inputs to a guardrail and record its answers. |
| Jailbreak / prompt attack | Input crafted to trick an AI model into ignoring its rules. |
| Labelled inputs | Test prompts with a known correct answer, such as harmful or harmless, used to score a guardrail. |
| LionGuard / Sentinel | GovTech Singapore's safety classifier and guardrail service. |
| LLM (large language model) | An AI model trained on large amounts of text to generate language. |
| LTA | Land Transport Authority, Singapore. |
| Llama Guard | Meta's open-weight safety model for classifying prompts and responses. |
| MITRE ATT&CK / ATLAS | Public catalogues of attacker techniques; ATLAS covers attacks on AI systems. |
| NeMo Guardrails | NVIDIA's open-source toolkit for adding guardrails to chatbots. |
| OSCAL | Open Security Controls Assessment Language, a machine-readable format for security controls. |
| Purple Llama | Meta's open project of safety tools and evaluations for generative AI. |
| Litmus | GovTech's tool for testing AI applications for safety weaknesses. |
| Quantised (4-bit) model | A model stored with lower-precision numbers so it fits in less GPU memory. |
| SSP (System Security Plan) | The Singapore Government's set of security controls, including a Generative AI system type. |
| STIX 2.1 | A standard data format for sharing cyber-threat information. |
| Test bench | Short for Guardrail Evaluation Test Bench: the harness, test inputs and results that compare guardrails fairly. |
| Tier 1 / Tier 2 | Tier 1: harmful-content detection on prompts, and jailbreak detection (proposed). Tier 2: further comparisons under investigation, each with a stated reason. |
| Telegram digest | The condensed Briefing sent to subscribed readers by Telegram bot. |

## Open questions → to_main_session
- Glossary is provisional (see above); re-run against the drafter's "Terms used" list.
- Figure 1 is NeMo-specific (adapted from the explainer, with its "diagram N" cross-references removed). Acceptable as a generic checkpoint diagram; say "adapted from" in the caption.
- Gantt: all rows owner "Robin"; weekly columns run Thu to Wed from 8 Oct; sub-task dates are planning estimates, but the Gantt includes the placeholder phrase "Rate and map" as one box in Figure 2 although mapping is a stretch/reduced-scope outcome in the Beacon findings; brief lists mapping as a core objective, so kept.
