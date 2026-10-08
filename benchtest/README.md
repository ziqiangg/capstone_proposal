# AI Guardrails Research for Scoping the Test Bench

## 1. Objective
The ultimate objective of this project is to develop a test bench that can meaningfully evaluate AI guardrails. This research is intended to determine:
1. Which guardrail functions can be meaningfully evaluated together.
2. Which comparison group should be evaluated first.
3. What minimum architecture is required for the first version of the test bench.

why did i use the term 'minimum architecture'. The goal is to test via ablation studies how these guardrails perform and not to build an elaborate application. However, to test guardrails comprehensively an architecture needs to be well designed enough that these guardrails can be invoked in the first place. An example, to test a Retrieval Rail, there needs to be a RAG component.

---

## 2. Research Progress

refer to benchtest/AI Guardrails Research and Comparison.xlsx

Note: I intend to add Meta's Purple Llama, the wider safety toolkit that Llama Guard belongs to, and GovTech's Litmus, its AI testing and evaluation product to further bolster sheets 3 and 4

---

## 3. Context: the AI Red Teaming project
For context, working simultaneously alongside the Guardrail Research and Bench Test team is an AI Red Teaming Group, refer to
benchtest/red_team_proposal/Form B (Daniel Chua).docx
for extra information about their project and timeline. The idea is that the their AI Red Teaming tool will be pitted against our guardrail bench test.

---

## 4. Agreed scope for Form B (Oct 2026)
- **Tier 1 (proposed):**
  - Harmful-content classification of user prompts: NVIDIA NeMo Guardrails, Meta Llama Guard 3 (Llama Guard 4 subject to gated access), and GovTech LionGuard 2 via Sentinel.
  - Jailbreak / prompt-attack detection: NeMo Guardrails and Sentinel's prompt-attack check, with Meta Prompt Guard 2 (Purple Llama) planned as a third comparator.
  - Minimum architecture: a harness of dataset loader → per-product adapter → common result format → evaluator. No retrieval (RAG) or agent component.
- **Tier 2 (under investigation):** every other comparison group in sheet 4. Each one is held back for one of these reasons:
  - only one product offers the function;
  - comparators share a backend (Sentinel's AWS checks and Bedrock);
  - it needs a retrieval, agent or response-generating component;
  - it needs more compute.
- **Compute:** one LTA laptop with an RTX 4060 (8 GB). Llama Guard 3-8B does not fit in 8-bit (8.46 GB measured in the demo notebook), so it runs in 4-bit locally or on free-tier cloud GPU credits. Llama Guard 4 (12B) is cloud-only.
- **Sentinel:** access is available (GovTech, Singapore IP). Only public or synthetic test prompts are sent to hosted services.
- **Deadlines:** evaluation results by 1 Dec 2026; report in the first week of Dec 2026. The red-team project is context only; no integration is committed.
- Detailed findings: `scratchpad/benchtest-explorer_scratch/benchtest_findings_1.md`.
