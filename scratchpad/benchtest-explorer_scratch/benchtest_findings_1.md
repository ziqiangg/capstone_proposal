# Benchtest findings 1 (benchtest-explorer)

Date: 2026-10-08. Scope: `benchtest/` only (xlsx, two notebooks, three HTML explainers, Daniel's Form B for context). Evidence labels: **[Doc]** = stated in the repo files; **[Ext]** = verified outside the repo (WebSearch / Context7); **[Inf]** = my inference; **[TBV]** = to be verified.
Cell references use the workbook `benchtest/AI Guardrails Research and Comparison.xlsx`, written as sheet!cell. The notebooks and HTML files carry no stable line numbers, so I cite them by cell index or title.

## TL;DR
The test bench compares AI guardrails (safety checks wrapped around a chatbot) by running the same labelled inputs through each product and scoring the verdicts. The README says the goal is ablation studies on guardrails, not "an elaborate application", with a minimum architecture just big enough for each guardrail to be invoked at all. Tier 1 (proposed) is harmful-content classification of user prompts plus jailbreak / prompt-attack detection: NeMo Guardrails, Llama Guard 3/4 and Sentinel (LionGuard 2, prompt-attack) are compared on single-turn labelled prompts through a harness only (no RAG, no agent, no output side). Tier 2 holds the other 22 comparison groups, each with a reason (single product, shared backend, needs RAG or agent, or compute). On the 8 GB RTX 4060 the repo's own notebook shows Llama Guard 3-8B in 8-bit uses 8.5 GB, so it does not fit; 4-bit would, and Llama Guard 4 (12B) is cloud-only. Sentinel is reachable for Robin. Purple Llama (Prompt Guard 2) fills the gap in jailbreak detection; Litmus is GovTech's pre-deployment testing platform.

## Form B-ready facts
- Purpose: build a test bench that can meaningfully evaluate AI guardrails; decide which functions can be compared together, which group goes first, and what minimum architecture version 1 needs. `benchtest/README.md` section 1.
- "Minimum architecture" is deliberately small: the goal is ablation studies, "not to build an elaborate application"; the architecture only needs to be good enough that each guardrail can be invoked (example: a Retrieval Rail needs a RAG component). `benchtest/README.md` section 1.
- Research base: 29 guardrail functions across 4 sources (Amazon Bedrock 1, NeMo Guardrails 16, Llama Guard 5, Sentinel 7), each described by nine questions (function, threat, where it operates, method, output, input needed, minimum test set-up, open uncertainties, sources). `3. Guardrail Research Table`!A3:AG21 (columns E to AG).
- The functions were grouped into 24 candidate comparison groups: 6 groups with two or more products and 18 single-product groups. `4. Candidate Comparison Groups`!A4, A11.
- Tier 1 = harmful-content classification of user prompts (sheet 4 group C3) and jailbreak / prompt-attack detection (C5). `4. Candidate Comparison Groups`!A7, A9; CLAUDE.md Binding decisions.
- Tier 1 common test inputs are single-turn prompts: harmful, benign, and benign near-misses; for attacks, jailbreak, injection and benign prompts. `4. Candidate Comparison Groups`!C7, C9.
- Tier 1 ground truth is a binary harmful/benign (or attack/benign) label per prompt plus a category mapped to a common taxonomy; the products' taxonomies differ (Llama Guard 14 categories, LionGuard 6, AWS 5). `4. Candidate Comparison Groups`!D7, D9.
- Tier 1 metrics: true-positive, false-positive and false-negative rates at each product's own decision point; latency; AUPRC (area under the precision-recall curve) and threshold sweeps only where a score exists (Sentinel LionGuard and prompt-attack). `4. Candidate Comparison Groups`!F7, F9.
- Tier 1 minimum architecture: a harness (loader, product adapters, common result format, recorder, evaluator); no output side, RAG, tool execution or multi-agent parts. `4. Candidate Comparison Groups`!G7, G9; `3. Guardrail Research Table`!F16, G16, V16.
- Llama Guard does not detect jailbreaks or prompt injection (Meta points to Prompt Guard 2), so Llama Guard sits in the harmful-content group but not the attack group. `3. Guardrail Research Table`!V6; notebook `Demonstrating Llama Guard 3 and 4.ipynb` cell 0.
- The Llama Guard notebook demonstrates that a "DAN" jailbreak wrapped around a harmless request is classified safe (expected behaviour, not a defect). Notebook cells 4, 11 (output).
- Sentinel is a hosted service from GovTech returning a 0 to 1 score per check; it never blocks. It is in closed beta for Singapore public officers, over a Singapore IP, with an API key issued after an interest form. `3e. GovTech Sentinel Inventory`!C60, B68; `benchtest/helpful_explanation/sentinel-explained.html`.
- Sentinel's AWS-powered checks wrap Amazon Bedrock Guardrails, so they share a backend and are not an independent comparator. `4. Candidate Comparison Groups`!H7, H9.
- Hardware fact from the repo's own run: Llama Guard 3-8B loaded in 8-bit used 8.46 GB of GPU memory on a 14.6 GB Tesla T4. Notebook `Demonstrating Llama Guard 3 and 4.ipynb`, cell 7 output.
- The author's note in the notebook: Llama Guard 4 "is too large to be run in Colab or locally on a laptop"; the Llama Guard 4 run failed with a 403 (gated model access not yet granted), so no Llama Guard 4 result exists in the repo. Notebook cell 20, cell 22 output.
- Planned additions: Meta's Purple Llama and GovTech's Litmus, "to further bolster sheets 3 and 4". `benchtest/README.md` section 2 note.
- Red-team project: context only (see Detail section 7). `benchtest/README.md` section 3; CLAUDE.md Binding decisions.

## Translation table
Internal term / code -> plain phrase -> needed in Form B? (y/n). Use only the plain phrases in the form body.

| Internal term / code | Plain-language phrase | Needed in Form B? |
|---|---|---|
| Benchtest / the benchtest | Guardrail Evaluation Test Bench (the "test bench") | y (defined at first use) |
| Guardrail / rail | a safety check placed around an AI chatbot that inspects text and allows, blocks or changes it | y (defined at first use) |
| Ablation / ablation study | a controlled experiment that switches off, swaps or varies one part at a time so the effect of that part can be measured | y (defined at first use) |
| Minimum architecture | the smallest amount of surrounding software needed to feed test inputs to a guardrail and record its answers | y (use "minimum set-up" if words are short) |
| Tier 1 (proposed) | the first comparison, proposed: harmful-content detection on user prompts, and jailbreak / prompt-attack detection | y |
| Tier 2 (under investigation) | further comparisons still under investigation, each with a stated reason | y |
| C1 | personal-data detection and masking on user input | n |
| C2 | personal-data detection and masking on model output | n |
| C3 | harmful-content detection on user prompts | y |
| C4 | harmful-content detection on model responses | n |
| C5 | jailbreak / prompt-attack detection | y |
| C6 | off-topic detection against the chatbot's stated purpose | n |
| C7 | conversation-flow control | n |
| C8 | filtering of retrieved document passages | n |
| C9 | forbidden-pattern blocking on input | n |
| C10 | forbidden-pattern blocking on output | n |
| C11 | detection of oversized or padded input | n |
| C12 | detection of injected code in model output | n |
| C13 | checking of tool calls before they run | n |
| C14 | checking of tool results | n |
| C15 | custom checks wrapped around actions | n |
| C16 | checking an answer against supporting evidence (fact-checking) | n |
| C17 | self-consistency check for made-up answers | n |
| C18 | harmful-content detection on image-plus-text prompts | n |
| C19 | harmful-content detection on image-plus-text responses | n |
| C20 | detection of code-interpreter abuse | n |
| C21 | user-defined safety policy applied to prompts | n |
| C22 | user-defined safety policy applied to responses | n |
| C23 | detection of leaked hidden instructions (system prompt) | n |
| C24 | detection of whether the model refused | n |
| Sheet "3. Guardrail Research Table" | the product research table (nine questions per function) | n |
| Sheet "3b. NeMo Rail Inventory" | catalogue of NeMo's built-in checks | n |
| Sheet "3c. NeMo Evaluation Tooling" | NeMo's own testing tools and datasets | n |
| Sheet "3d. Llama Guard Inventory" | catalogue of Llama Guard versions | n |
| Sheet "3e. GovTech Sentinel Inventory" | catalogue of Sentinel's checks and access routes | n |
| Sheet "4. Candidate Comparison Groups" | the shortlist of comparable checks | n |
| Columns E to AG (letters used as function IDs, e.g. F, V, AB) | one guardrail function per product | n |
| R1 to R9 (cell refs such as "AF R4") | research question 1 to 9 | n |
| [Documented] / [Inferred] / [Not disclosed] / [To be verified] | stated in the source / our inference / the vendor does not say / still to check | n |
| LLMRails / IORails | NeMo's two internal run modes (older and newer engine) | n |
| LG1 to LG4 | Llama Guard versions 1 to 4 | n (write "Llama Guard 3/4") |
| S1 to S14 | Llama Guard hazard categories (violent crimes ... code-interpreter abuse) | n |
| Sentinel | GovTech's hosted guardrail service (closed beta) | y |
| LionGuard 2 | GovTech's Singapore-tuned harmful-content classifier, served through Sentinel | y |
| NemoGuard / Nemotron safety model | NVIDIA's safety-classifier models that NeMo can call | n |
| Prompt Guard 2 | Meta's small classifier for jailbreak and prompt-injection attacks | y (as a planned addition) |
| AUPRC | area under the precision-recall curve (a threshold-free accuracy measure) | n (or explain in the glossary) |
| Harness | the test program that loads inputs, calls each product and records results | n |
| Decision point | the product's own pass / block cut-off | n |

## References (APA 7, verified)
Verification method: WebSearch returned the official or primary page with matching title and URL (decisions_log #1). WebFetch was not used (DNS blocked). Context7 confirmed the library facts used (NeMo rail names, jailbreak heuristics, garak generator).

1. Rebedea, T., Dinu, R., Sreedhar, M., Parisien, C., & Cohen, J. (2023). NeMo Guardrails: A toolkit for controllable and safe LLM applications with programmable rails. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing: System Demonstrations* (pp. 431-445). Association for Computational Linguistics. https://doi.org/10.18653/v1/2023.emnlp-demo.40 (arXiv: https://arxiv.org/abs/2310.10501). [Ext: WebSearch returned arxiv.org/pdf/2310.10501, research.nvidia.com and aclanthology pages; Context7 /nvidia-nemo/guardrails confirmed the "llama guard check input", "jailbreak detection heuristics" and "jailbreak detection model" input flows.]
2. Inan, H., Upasani, K., Chi, J., Rungta, R., Iyer, K., Mao, Y., Tontchev, M., Hu, Q., Fuller, B., Testuggine, D., & Khabsa, M. (2023). *Llama Guard: LLM-based input-output safeguard for human-AI conversations*. arXiv. https://arxiv.org/abs/2312.06674 [Ext: WebSearch returned arxiv.org/pdf/2312.06674 and the Meta research page.] Covers Llama Guard 1 only. For Llama Guard 4 (and 3) cite the model documentation in item 2b if the form needs the current versions.
 2b. Meta. (2025). *Llama Guard 4* [Model card and prompt format]. https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/llama-guard-4/ [Ext: WebSearch returned this Meta developer page, which defers to the GitHub model card. The Llama Guard 3 official card was not returned (only mirrors), so it is not cited.] APA note: no named author, so Meta is the author; no retrieval date is needed for a versioned page.
3. Tan, L., Chua, G., Ge, Z., & Lee, R. K.-W. (2025). LionGuard 2: Building lightweight, data-efficient and localised multilingual content moderators. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing: System Demonstrations* (pp. 264-285). Association for Computational Linguistics. https://arxiv.org/abs/2507.15339 [Ext: WebSearch returned arxiv.org/pdf/2507.15339 and the ACL Anthology entry 2025.emnlp-demos.20.] The title in the source uses "&"; APA 7 spells it out in running text.
4. Derczynski, L., Galinkin, E., Martin, J., Majumdar, S., & Inie, N. (2024). *garak: A framework for security probing large language models*. arXiv. https://arxiv.org/abs/2406.11036 [Ext: WebSearch; Context7 /nvidia/garak confirmed the `guardrails` generator and probe families.] Needed only if garak is named as a source of attack prompts.
5. Meta AI. (2023, December 7). *Announcing Purple Llama: Towards open trust and safety in the new world of generative AI*. https://ai.meta.com/blog/purple-llama-open-trust-safety-generative-ai/ [Ext: WebSearch returned this official Meta post.] Needed only if Purple Llama is named.

Not for the reference list (supporting, WebSearch-verified): GovTech Litmus developer portal page https://www.developer.tech.gov.sg/products/categories/cybersecurity/litmus ; GovTech Sentinel developer portal page https://www.developer.tech.gov.sg/products/categories/cybersecurity/sentinel ; Meta Prompt Guard docs https://developer.meta.com/ai/docs/model-cards-and-prompt-formats/prompt-guard/ . Recommendation for the form (limit 10): items 1, 2 (or 2b), 3 and, if short of space, 5.

## Open questions -> to_main_session
1. **Plan correction (important).** The plan's agent table says "LG3-8B 8-bit yes" on the 8 GB GPU. The repo's own notebook output shows 8-bit Llama Guard 3-8B using 8.46 GB allocated (8.5 GB weights) on a 14.6 GB T4 (cell 7), which exceeds 8 GB VRAM once overhead is added. Conservative assumption used here: 8-bit does not fit; only a 4-bit load (about 4 to 5 GB, unofficial, third-party estimate) fits and must be validated against a cloud reference run. The Form B must not claim 8-bit local. No message file written; please log as a decision.
2. Jailbreak group has no Llama Guard member (Llama Guard is not built for it). Assumption: describe Tier 1 jailbreak detection as NeMo vs Sentinel, with Meta's Prompt Guard 2 as a planned third comparator (part of the "Purple Llama" addition). Prompt Guard 2 is not in the workbook, so this is [Inf] from the README note; model sizes (22M, 86M) come from WebSearch of Meta's page.
3. Assumption on Tier 2 reason for harmful-content on responses (C4): its true reason is "needs a response-generating component and labelled responses" and is a natural extension of Tier 1; it is not in the list of valid reasons. Placed in Tier 2 under "needs a response-generating component".
4. The README defines "minimum architecture" but not "ablation"; my plain definition is [Inf] from the README's sentence. Confirm if a stricter definition is intended.
5. Sentinel limits are undisclosed (rate limits, SLA, data region, retention; text may reach OpenAI, Google or AWS). Assumption: use only public or synthetic prompts with Sentinel; no LTA-internal text. `3e. GovTech Sentinel Inventory`!H60.
6. Free-cloud quotas (Colab, Kaggle) come from third-party sites only; no official page was returned. Treated as approximate.
7. Llama Guard 4 access: the gated-model request had not been granted when the notebook ran (403). Assumption: Robin requests access at the start; Llama Guard 4 results are not promised if access is delayed.

## Detail

### 1. Purpose, "minimum architecture" and "ablation"
- Purpose (README): build a test bench that can meaningfully evaluate AI guardrails; answer three scoping questions: which guardrail functions can be evaluated together, which group goes first, and what minimum architecture version 1 needs.
- Minimum architecture, in plain words: the least amount of surrounding software that still lets a guardrail be switched on and its answer captured. For Tier 1 that is a test program that reads labelled prompts, sends them to each product, and writes down the verdict, score and time. It is not a chatbot application. A deeper guardrail needs more (a retrieval guardrail needs a document store; a tool-call guardrail needs a tool-using agent), which is why those groups are Tier 2.
- Ablation, in plain words: change one thing at a time and measure the difference. For this bench, examples (all [Inf], drawn from the notebook and workbook): guardrail on versus off; one guardrail at a time; same guardrail with different cut-offs; different backend model behind the same rail (e.g. NeMo calling Llama Guard); full-precision versus 4-bit model; different policy prompt wording (Llama Guard custom categories on/off). garak itself has a probe family named `dan.Ablation_Dan_11_0` [Ext, Context7], so the word is also used in attack testing.

### 2. Tier 1 in detail
Source: sheet 4 rows C3 and C5; sheet 3 columns F, G, V, AA, AB, AF, AG.

**C3 Harmful-content classification of user prompts** (sheet 4 row 7)
- Products and functions: NeMo Guardrails input content-safety rail (sheet 3 col G; a classifier LLM judges the message; options include Nemotron safety models, Llama Guard, ShieldGemma or the main LLM); Llama Guard input classification (col V; versions 3-1B, 3-8B, 3-8B-INT8, 4-12B); Sentinel LionGuard 2 (col AA; six categories with levels; score 0 to 1); Sentinel generic moderation via AWS Bedrock (col AG; shares backend with Amazon Bedrock, not independent; scores observed only 0.0 or 1.0; no self-harm category).
- Common inputs: single-turn user prompts, harmful and benign, plus benign near-misses; seeds from Anthropic HH-RLHF red-team-attempts (harmful) and helpful-base (benign) usable for binary labels only; OpenAI Moderation set and ToxicChat are not in the repo (`3c`!A26, A27; ToxicChat is CC BY-NC 4.0, non-commercial). LionGuard needs English, Singlish, Chinese, Malay and Tamil copies (`3. ...`!AA16).
- Ground truth: binary label per prompt; plus a category label mapped to a common taxonomy; compare per category only where a mapping exists. Llama Guard S1-S14 (13 MLCommons + S14), LionGuard 6 categories (with Level 1/2), AWS 5 categories, NeMo Nemotron S1-S23 or S1-S22. The `3d` category crosswalk maps Llama Guard versions to each other.
- Outputs captured: decision, category codes or per-category scores, Llama Guard first-token probability only if extracted, latency, error.
- Metrics: TPR, FPR, FNR on the binary label at each product's own decision point; precision and F1; AUPRC and cut-off sweeps only for LionGuard (and Llama Guard if probabilities are extracted); AWS and NeMo give verdicts, not scores.
- Minimum architecture: loader, adapters, common result format, recorder, evaluator; NeMo input rail with a safety-model endpoint and prompt; GPU-served Llama Guard with its template and a verdict parser; Sentinel key (Singapore IP) or self-hosted LionGuard.
- Caveats from the sheet: NeMo can call Llama Guard, so those two may share a model; NVIDIA's published Llama Guard vs self-check numbers use an old main LLM and are not comparable; `nemoguardrails eval run` can drive only the NeMo member; Llama Guard 3 and 4 scores are not comparable because no threshold is documented.

**C5 Jailbreak and prompt-attack detection on user input** (sheet 4 row 9)
- Products: NeMo input jailbreak detection (col F; two options: perplexity heuristics, English only, based on `gpt2-large`, LLMRails only; or the NemoGuard JailbreakDetect embedding classifier via an endpoint; allow/block only, no score; fails open if the detector is down); Sentinel prompt-attack (col AB; GovTech, model undisclosed; score + confidence; input/output scope disputed); Sentinel AWS prompt_attack (col AG, shared Bedrock backend). Context7 confirms the NeMo flows `jailbreak detection heuristics` and `jailbreak detection model` and the heuristic thresholds (89.79 and 1845.65).
- Common inputs: single-turn jailbreak, injection and benign prompts; benign prompts must mention instructions or code and include non-English text (heuristics misfire on code and non-English). garak probe families (dan, encoding, goodside, promptinject, gcg) can seed attacks; benign controls must be added (`4`!C9). Context7 confirms `garak --probes promptinject` and the `guardrails` generator.
- Ground truth: binary attack/benign under one agreed definition, optionally an attack style. Definitions differ (NeMo none documented; Sentinel three intents; AWS jailbreak, injection, possibly leakage). garak labels come from its own detectors (some model-based), so they are a seed, not truth.
- Metrics: TPR/FPR/FNR at each decision point; latency; AUPRC and sweeps only for Sentinel prompt-attack. garak reports protection rates per probe, not false positives.
- Minimum architecture: same harness; NeMo input rail with a detector (heuristics need torch and transformers, or a server endpoint); Sentinel key. No self-hosted Sentinel prompt-attack exists.
- Caveat: only two independent products exist for this group (three counting AWS, but it shares a backend with Sentinel). Meta's Prompt Guard 2 [Ext] is a 22M or 86M classifier labelling prompts benign or malicious, English-only (22M) or multilingual (86M); it would add a third independent comparator and is small enough for the laptop. This is my [Inf] addition, tied to the planned Purple Llama work.

**Why these two are Tier 1** (sheet 4): they are the only groups with three or more products whose input is a single prompt, whose ground truth can be written without extra components, and whose minimum architecture is only the harness. [Inf, consistent with CLAUDE.md]

### 3. Tier 2: every other group and a one-line reason
Groups with 2+ products (sheet 4 rows 5, 6, 8, 10) and single-product groups (rows 12 to 29). "Single product" means no comparator among NeMo / Llama Guard / Sentinel yet.

| Group (plain) | Why under investigation |
|---|---|
| C1 personal-data masking, input | Shared backend: Sentinel's check is Amazon Bedrock Guardrails, and NeMo's depends on a separate scanner (e.g. Presidio), so there are too few independent products; Llama Guard has no masking. |
| C2 personal-data masking, output | Same shared-backend reason; also may release data during streaming. |
| C4 harmful content on model responses | Needs a response-generating component (stub or real model) and labelled responses; natural extension of Tier 1. |
| C6 off-topic detection | Too few comparable products (NeMo topic control vs Sentinel off-topic); policy must be rendered into each format; Sentinel is English only. |
| C7 conversation-flow control | Single product (NeMo); needs an authored dialogue configuration and a main model. |
| C8 retrieved-passage filtering | Single product; needs a retrieval (RAG) component. |
| C9 forbidden-pattern blocking, input | Single product; deterministic rule matching that tests configuration, not learned detection. |
| C10 forbidden-pattern blocking, output | Same as C9. |
| C11 oversized-input detection | Single product; statistical rule with thresholds we set. |
| C12 injected-code detection, output | Single product (fixed rule set); output side. |
| C13 tool-call checking | Single product; needs a tool-using (agent) set-up. |
| C14 tool-result checking | Single product; needs an agent set-up. |
| C15 custom action checks | Single product; tests our own authored logic; needs an agent set-up. |
| C16 fact-checking against evidence | Single product; needs retrieved evidence (RAG) and a judge model. |
| C17 self-consistency check | Single product; needs a live model and at least two extra model calls per test (compute). |
| C18 image-plus-text prompts | Llama Guard only (Llama Guard 4 and 3-11B-Vision); compute beyond 8 GB and image data. |
| C19 image-plus-text responses | Same as C18. |
| C20 code-interpreter abuse | Llama Guard only; needs agent turns with code; compute for the 8B and 12B models. |
| C21 user-defined policy, prompts | Llama Guard only; compare within one family; compute for the larger versions. |
| C22 user-defined policy, responses | Same as C21. |
| C23 leaked-instruction detection | Sentinel only; closed beta; undisclosed model; output side. |
| C24 refusal detection | Sentinel only; analytics rather than a block control; undisclosed model. |

Observation: the workbook's own coverage block shows NeMo appears in 17 groups (C1 to C17), Llama Guard in 7 (C3, C4, C18 to C22), Sentinel in 8 (C1 to C6, C23, C24) [Inf from rows 5 to 29]. The calculated coverage cells hold no cached values (the xlsx was not recalculated), so I counted by hand.

### 4. Feasibility
Hardware: i7-13700H, 32 GB RAM, RTX 4060 Laptop 8 GB VRAM (CLAUDE.md).

| Model / service | Size and quantisation | Fits 8 GB local? | Notes |
|---|---|---|---|
| Llama Guard 3-1B | 1.12B params; checkpoint about 2.9 GB (`3d`!D6, N7 note) | Yes | Text only, 8 languages. Not tuned for S14. Easy ablation baseline. |
| Llama Guard 3-1B-INT4 | about 437 MiB .pte for ExecuTorch (mobile runtime) (`3d`!M7) | Yes, but different runtime | Not a Hugging Face transformers model; keep out of Tier 1 unless a use appears. |
| Llama Guard 3-8B | bf16 about 16 GB | No | `3d`: weights 16.1 GB on disk (notebook cleanup output). |
| Llama Guard 3-8B-INT8 (8-bit, bitsandbytes) | 8.46 GB allocated measured on T4 (notebook cell 7) | **No** (exceeds 8 GB with overhead) | Contradicts the plan's "8-bit yes". |
| Llama Guard 3-8B, 4-bit NF4 (bitsandbytes) | about 4 to 5 GB (third-party estimates, [Ext, approximate]) | Probably yes | Unofficial; verdicts can differ from Meta's. The repo notebook uses the same NF4 recipe for Llama Guard 4 and labels it unofficial (cell 22). Needs a cloud 8-bit/bf16 reference run to quantify the loss, which doubles as an ablation. |
| Llama Guard 3-11B-Vision | 11B; multimodal | No | Tier 2 only (C18/C19). Repo is gated with an EU flag (`3d`!L10). |
| Llama Guard 4 (12B) | about 24 GB bf16 (notebook cell 1); 4-bit would still be about 6 GB+ with vision tower unquantised | Unlikely | Notebook logic requires at least 14 GB for 4-bit (cell 22). The author wrote it is too large for a laptop (cell 20). Cloud only. [Inf for the 6 GB figure] |
| NeMo Guardrails library | pip package, CPU is enough | Yes | Notebook ran it with a 135M local model on CPU and a 1.7B 4-bit model on GPU (cells 5, 11). The repo output shows the 1.7B self-check rail refused both a jailbreak and the word "hello", so a tiny model is a poor judge (cell 14 output). Use embeddings-only or a real safety model. |
| NeMo jailbreak heuristics | `gpt2-large` perplexity model (Context7) | Yes | English only; high false positives on code and non-English. |
| NeMo jailbreak model / content-safety models | served as NVIDIA NIM endpoints; 8B-class safety models (`3. ...`!G14, F16) | Endpoint access, [TBV] free credits | Local serving of an 8B model hits the same 8 GB limit as above. Do not assume free credits without checking. |
| Sentinel (LionGuard 2, prompt-attack, AWS checks) | hosted API | Not a GPU issue | Reachable: Robin has access (Singapore IP; CLAUDE.md). Closed beta; rate limits, SLA, data region and retention are not disclosed (`3e`!H60). |
| Self-hosted LionGuard 2 / 2.1 / Lite | 0.85M-parameter head plus an embedder | Lite: yes (EmbeddingGemma 300M, fully local). 2 needs an OpenAI key, 2.1 a Gemini key (`3e`!E5 to E7, F5 to F7) | A fallback if Sentinel is rate-limited. No self-hosted option for prompt-attack. |
| Prompt Guard 2 (planned) | 22M or 86M [Ext] | Yes | Meta page via WebSearch. |

Free cloud tiers (third-party sources only, [TBV]): Google Colab free gives a best-effort T4 (the repo run saw a 14.6 GB T4); Kaggle gives about 30 GPU-hours per week on one P100 (16 GB) or two T4s (32 GB combined). A T4 fits Llama Guard 3-8B in 8-bit and Llama Guard 4 in 4-bit; Llama Guard 4 in bf16 needs about 24 GB, which only a two-T4 split could hold [Inf]. T4 has no native bf16 (notebook cell 4 comment).
Plan that fits the constraints [Inf]: run the harness, NeMo, Llama Guard 3-1B and 3-8B (4-bit) locally; run the reference (8-bit) and Llama Guard 4 on free cloud GPUs; call Sentinel from the laptop. Risks to the 1 Dec results date: Hugging Face gated-access approval delays (the repo run was refused with a 403), Sentinel rate limits, and the labelling effort for datasets.

### 5. Purple Llama and GovTech Litmus: what they are and why they are planned
- **Purple Llama** [Ext]: Meta's umbrella project for open trust-and-safety tools and evaluations, announced 7 Dec 2023 with CyberSec Eval (security benchmarks) and Llama Guard (input/output safeguard). It has since grown to include Prompt Guard (prompt-attack classifier), Code Shield and LlamaFirewall (the last two from third-party summaries only, not verified). The GitHub repository is `meta-llama/PurpleLlama`; the workbook already pins model cards to a PurpleLlama commit (`3d`!P4). Why planned: Llama Guard is one member of Purple Llama, and the other members fill gaps in the comparison: Prompt Guard 2 for jailbreak detection (Llama Guard cannot do this) and CyberSec Eval for prompt-injection and code-interpreter testing, which would strengthen sheets 3 and 4 as the README says.
- **GovTech Litmus** [Ext]: GovTech's pre-deployment testing platform for generative AI applications, part of the AI Guardian pair with Sentinel (Sentinel guards live systems; Litmus tests before launch). It checks reliability, bias and unsafe responses, tests both base models and the applications on top, and fits CI/CD pipelines; the developer portal labels it Testing-as-a-Service, proof of concept. The Sentinel getting-started page points to a joint "Litmus and Sentinel" interest form (`3e`!B68). Why planned: it is a government testing product in the same space as the bench, so its test design and coverage are a reference for the test inputs and metrics, and the same onboarding route may give access. Availability to Robin is [TBV]; no access is claimed.

### 6. Section C skills (benchtest side)
Only what the work requires; no certifications claimed; no claim about what Robin already knows.
- Evaluating safety classifiers: precision, recall, F1, false-positive rate, area under the precision-recall curve, threshold sweeps, and labelled-test-set design including near-miss controls. (AAI3008 Large Language Models; also general statistics.)
- Working with open-weight language models: Hugging Face loading, prompt templates, parsing model verdicts, 4-bit and 8-bit quantisation, GPU memory budgeting. (AAI3008)
- Guardrail frameworks: NeMo Guardrails configuration and its rule language (Colang); calling hosted REST APIs such as Sentinel's. (AAI3008, INF2001)
- Threat knowledge: jailbreak and prompt-injection attack styles, handling harmful test data safely and within dataset licences (e.g. ToxicChat is non-commercial). (INF2005 Cyber Security Fundamentals)
- Reproducible experiments: a test harness with a common result format, versioned configurations, and a results store queried for analysis. (INF2001 Introduction to Software Engineering; INF2003 Database Systems)
- Using free cloud notebooks and quotas under limits, and keeping runs repeatable across laptop and cloud. (INF2006 Cloud Computing and Big Data)
- Sentinel-specific onboarding and API use are new and inferred from the work, not claimed as existing skills.

### 7. Red-team project (context only)
Daniel Chua's Form B (`benchtest/red_team_proposal/Form B (Daniel Chua).docx`): an open-source AI red-teaming tool for the OWASP GenAI LLM Top 10 (2026), for LTA's Cyber Architecture and Development division, period 31/8/2026 to 9/4/2027. It orchestrates existing tools (Garak, PyRIT, Giskard, Inspect AI; Promptfoo is evaluated) plus custom attack modules and produces pentest-style reports; it is tested against a deliberately vulnerable sandbox application. Relationship: attack-side counterpart to the defence-side test bench. README section 3 says the idea is that the red-team tool will be pitted against the bench; CLAUDE.md says context only, no committed integration, mentioned under Industry Relevancy. Safe wording: "A parallel LTA capstone is building an AI red-teaming tool; the two efforts are complementary, with no committed dependency." Overlap to note without committing: garak can both seed attack prompts for the jailbreak group and drive NeMo directly; both projects use open-source tools only.

### 8. Notes on sources and gaps
- Workbook sheet 4 has a "coverage" block (A31 onward) whose formulas had no cached values, so group-per-product counts were done by hand from the group rows.
- The Llama Guard notebook ran Part 1 on a Colab T4; Part 2 (Llama Guard 4) produced an OSError because model access was not granted; Llama Guard 4 behaviour in the repo is therefore documentation-only.
- The NeMo notebook shows only a toy demonstration (greeting flow, finance refusal with embeddings-only matching, self-check input rail); it is not an evaluation. Its recorded output over-blocks ("hello" refused by a 1.7B judge).
- The HTML explainers (`llama-guard-explained.html`, `nemo-rails-explained.html`, `sentinel-explained.html`) are plain-language diagrams of the five checkpoints (input, dialog, retrieval, action, output) and are the planned source for the Annex B guardrail-checkpoint figure. Their statement that NeMo's built-in Llama Guard rails were written for Llama Guard 1 and need prompt rewriting for versions 3/4 is explicitly untested ("our reading of the code").
