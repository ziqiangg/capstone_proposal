# Content brief: Form B (for formb-drafter and annex-builder)

Read alongside these files:
- `CLAUDE.md` (decisions, style)
- `main_session/decisions_log.md` (#1–#24)
- findings: `scratchpad/benchtest-explorer_scratch/benchtest_findings_1.md`, `scratchpad/beacon-explorer_scratch/beacon_findings_1.md`, `scratchpad/security-frameworks-explorer_scratch/security_frameworks_findings_1.md`, `scratchpad/form-analyst_scratch/form_structure_findings_1.md`

Use translation-table phrases only. No internal IDs.

## Placement mechanics (form-analyst, decisions #4–#10)
- Each answer goes inside its existing plain-text content control as one paragraph. Lines are separated by `<w:br/>`, and numbering is typed ("1. ").
- Workstream labels are plain text on their own line.
- Keep the italic "(Please use a separate sheet…)" guidance. Replace the placeholder only.
- Every edit is tracked with `w:author="Guo Zi Qiang Robin"`.
- Annexes A–D go after "END OF FORM B", outside the controls.

## Section A: General information
- **Project Title** (replaces "Beacon"): *AI Security for Critical Infrastructure: A Guardrail Evaluation Test Bench and the Beacon AI-Security Briefing Service*. The drafter may shorten it, but must keep both workstreams.
- **Do not change anything else**: period 8/10/2026 – 31/3/2027, checkboxes, names. The two flagged placeholders also stay as they are.

## Section B: Capstone Project Details
Every subsection uses the same frame: a one-line umbrella statement, then "Workstream 1: Guardrail Evaluation Test Bench", then "Workstream 2: Beacon". Word caps are 2.5× Daniel's counts.

| Subsection | Cap | Must cover |
|---|---|---|
| Overview | 247 | Umbrella: both workstreams strengthen how LTA's cyber team adopts and watches AI safely. W1: guardrails are safety filters around a chatbot that block harmful or manipulative inputs. Today they are hard to compare, and the bench measures them fairly on the same labelled inputs (ablation, defined in plain words). W2: Beacon is a daily service that turns the flood of AI-security news into a short, evidence-backed Briefing. It maps each item to the Singapore Government SSP controls and to MITRE ATT&CK/ATLAS techniques. Refer to Annex B, Figures 1 and 2. |
| Objectives | 270 | Numbered list, about 4 objectives per workstream. W1: (1) finish the comparative research, adding Purple Llama and Litmus; (2) build a minimal, reusable evaluation harness; (3) evaluate Tier 1, i.e. harmful-content classification of prompts and jailbreak/prompt-attack detection; (4) report which guardrails suit which function, with evidence by 1 Dec. W2: (5) a daily pipeline covering collection, filtering, merging duplicate reports and significance rating; (6) a web Briefing and a Telegram digest; (7) an initial framework mapping, with every judgement traceable to its evidence; (8) deploy by 1 Feb with CI/CD and monitoring through Feb. Trend detection is a stretch goal (decision #14). |
| Industry Relevancy | 170 | LTA operates critical infrastructure. W1: evidence-based choice of guardrails before any GenAI deployment; links to the SSP Generative AI system type. W2: CYAD needs timely, defensible awareness of AI threats, mapped to the Singapore Government control catalogue and to MITRE techniques (no claim that LTA is obliged to meet the SSP; #32). Context only: a parallel LTA red-teaming project (Daniel Chua) builds attack tooling, so the bench complements it. No committed integration (CLAUDE.md). |
| Scope | 222 | W1: Tier 1 is in scope. Tier 2 is "under investigation", with the reasons collapsed into 3–4 plain categories (single product only; shared backend; needs a retrieval or agent architecture; compute). Limitations: one 8 GB laptop, so larger models run 4-bit or on free cloud credits (#18); open-source/free only; only public or synthetic prompts go to hosted services (#22); Llama Guard 4 is subject to access (#24). W2: high-level outcomes only. English-language public sources. Not a compliance tool. Hosting is free-tier/free-credit in the Singapore region (#11). Telegram is subject to LTA policy (#15). Trend detection is a stretch goal. |
| Outputs and Deliverables | 110 | Numbered list. W1: evaluation harness (code); results dataset; benchtest report (first week of Dec). W2: deployed Beacon service with CI/CD and monitoring; source code and documentation. Common: Form E1 interim report, Interim Presentation, Form E2 final report, final presentation; `Gantt_Guo_Zi_Qiang_Robin.xlsx`. |

## Section C: Knowledge and Training Requirements (shared, not split)
| Subsection | Cap | Content |
|---|---|---|
| Applicable Knowledge | 72 | Name the five modules: AAI3008 Large Language Models, INF2006 Cloud Computing and Big Data, INF2005 Cyber Security Fundamentals, INF2003 Database Systems, INF2001 Introduction to Software Engineering. Give one clause each on how it is used. |
| Additional Knowledge | 130 | Guardrail frameworks (NeMo Guardrails, Llama Guard, LionGuard/Sentinel); evaluation methodology (labelled datasets, precision/recall-style metrics); running quantised models on limited GPU; web collection and text extraction; STIX 2.1 and OSCAL formats; MITRE ATT&CK/ATLAS and the SSP; CI/CD and monitoring; React; Telegram bot API. "No formal certification is a prerequisite." |
| Training | 105 | Orientation to LTA's AI and security policies, and to the approval needed for any external service. LTA provides the development laptop and the existing Sentinel access. Everything else is self-directed through open documentation and free-tier credits. Never claim LTA will provide a sandbox or compute. |

## Section D: Project Timeline (cap 312)
Frame it as phases with dates, in typed lines. Then: "A summary Gantt chart is in Annex A; the detailed chart is provided in Gantt_Guo_Zi_Qiang_Robin.xlsx."

| When | Phase |
|---|---|
| 8 Oct – 11 Oct | Form B |
| Oct | W1: research completion and harness build. W2: design continues at low intensity |
| Nov | W1: Tier 1 evaluation runs |
| 1 Dec | W1 results |
| 1–6 Dec | Benchtest report and Form E1 (6 Dec) |
| Dec – Jan | W2 build: collection→filtering→merging→rating→Briefing/Telegram→mapping. Interim Presentation by 31 Jan |
| 1 Feb | Deploy |
| Feb | CI/CD, monitoring, fixes |
| Mar | Buffer and iteration. Form E2 by 21 Mar. Period ends 31 Mar |
| 11 Apr | Final presentation (after the period) |

## Sections E and F
Supervisor Remarks and Declarations: **untouched**.

## Annexes (annex-builder supplies them; the drafter inserts them)
- **A:** month-level Gantt table, Oct 2026 – Apr 2027, rows by workstream plus SIT milestones.
- **B:** Figure 1 is the guardrail checkpoint diagram (from `benchtest/helpful_explanation/`). Figure 2 is the Beacon pipeline in about 6 plain boxes, taken from the stage list in beacon_findings.
- **C:** glossary. Only terms and acronyms used in the form.
- **D:** references, APA 7, at most 10. Use this selection; cite only those actually cited in the body, and drop unused ones:
  1. Rebedea et al. (2023), NeMo Guardrails
  2. Inan et al. (2023), Llama Guard
  3. Meta (2025), Llama Guard 4 model card
  4. Tan et al. (2025), LionGuard 2
  5. Meta AI (2023), Purple Llama
  6. Government Technology Agency (n.d.), Sentinel, developer portal: https://www.developer.tech.gov.sg/products/categories/cybersecurity/sentinel
  7. Government Technology Agency (n.d.), Litmus: https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus
  8. Government Technology Agency (2025), System Security Plan (SSP), https://info.standards.tech.gov.sg/ssp/
  9. MITRE Corporation (n.d.), MITRE ATT&CK
  10. MITRE Corporation (n.d.), MITRE ATLAS

  Exact strings are in the findings files.
