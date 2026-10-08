# AI Guardrails Research for Scoping the Test Bench

## 1. Objective
The ultimate objective of this project is to develop a test bench that can meaningfully evaluate AI guardrails. This research is intended to determine:
1. Which guardrail functions can be meaningfully evaluated together.
2. Which comparison group should be evaluated first.
3. What minimum architecture is required for the first version of the test bench.

why did i use the term 'minimum architecture'. The goal is to test via ablation studies how these guardrails perform and not to build an elaborate application. However, to test guardrails comprehensively an architecture needs to be well designed enough that these guardrails can be invoked in the first place. An example, to test a Retrieval Rail, there needs to be a RAG component.

---

## 2. Research Progress

refer to benchtest\AI Guardrails Research and Comparison.xlsx

Note: I intend to add Meta's Purple Llama, the wider safety toolkit that Llama Guard belongs to, and GovTech's Litmus, its AI testing and evaluation product to further bolster sheets 3 and 4

---

## 3. 
For context, working simultaneously alongside the Guardrail Research and Bench Test team is an AI Red Teaming Group, refer to
benchtest\red_team_proposal\Form B (Daniel Chua).docx
for extra information about their project and timeline. The idea is that the their AI Red Teaming tool will be pitted against our guardrail bench test.