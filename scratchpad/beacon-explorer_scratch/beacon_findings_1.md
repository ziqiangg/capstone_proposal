# Beacon findings 1 (beacon-explorer)

Sources: `Project-Beacon/beacon_notes/` (vault, current as of 2026-10-08, generated status at commit a3c475d) and `Project-Beacon/Beacon_Report.docx` (baseline of 25 Sep 2026, outdated; narrative only). The vault wins on every conflict. Paths below are relative to `Project-Beacon/beacon_notes/` unless they start with `Project-Beacon/`. Beacon_Report.docx has no line numbers; it is cited by section.

## TL;DR
Beacon is a daily AI-security briefing service. Each morning it collects articles, advisories and papers from a fixed list of English-language sources, keeps the ones about cybersecurity and AI security, merges reports of the same event, rates how significant each event is, and publishes a short evidence-backed Briefing on a web page. A condensed version goes to subscribed readers by Telegram. Every judgement it makes is recorded and traceable to its evidence. Maturity: 288 requirements are written but none is verified. Only the collection side (sources, page reading, article records, source monitoring) has an architecture. Six experiments tested extraction of titles, authors and dates; five are recorded and one is superseded, with the last result met and the four before it not met. The analysis stages after collection are specified but not yet designed, and several of their key decisions are open questions.

## Form B-ready facts

Problem and users
- Cybersecurity teams responsible for critical infrastructure must keep up with AI-related security news published continuously across many outlets; deciding relevance, spotting duplicate reports of one event, and relating each finding to the controls it affects is slow, repetitive and inconsistent. `Project-Beacon/Beacon_Report.docx` section 1 (Abstract) and section 2 (The Problem); `questions/Q-017.md:17` ("advice delivered to critical-infrastructure teams").
- Five problems it targets: coverage (too many sources to monitor), sense-making (duplicates, classification, trends, relevance), attention (reduce a large set to a manageable selection), defensibility (every judgement traceable to evidence), continuity (runs without someone remembering to start it). Beacon_Report.docx section 2.
- Beacon is not a general search or recommendation tool and not a compliance tool for any one system; it reads and writes English only; it never tells a reader about its own lateness or failures (those go to the operator); it publishes nothing on a day when nothing new is found. Beacon_Report.docx section 3; `requirements/OUT-09.md:9`.
- Four kinds of user: Reader (reads the Briefing, opts in to Telegram), Curator (owns the source list, criteria, corrections), Operator (runs and pauses cycles, can withdraw a published item at once), Administrator (manages user accounts). The development team is not a role. `requirements/A-terms.md:12-19`.

What a reader receives each day (defaults)
- A daily run starts after midnight Singapore time and is due to close by 08:00; the Briefing is published within a 30-minute grace period; the Telegram message goes out at 09:00. `requirements/parameters/CYCLE_DEADLINE.md:6`, `PUBLISH_GRACE_PERIOD.md:6`, `DELIVERY_SCHEDULE.md:6`.
- The web Briefing holds up to 10 developments in ranked order of significance, plus a description of each active trend (30-day window); intended reading time about 10 minutes; the latest Briefing is shown first. `requirements/parameters/MAX_RECOMMENDED_DEVELOPMENTS.md:6`, `TREND_WINDOW.md:6`, `TARGET_READING_MINUTES.md:6`, `requirements/UIX-02.md:9`.
- Each entry (an "Account") states what happened, why it matters, which controls and threat-framework items it bears on, where sources disagree, and its significance. `requirements/OUT-02.md:9`.
- The Telegram message carries the top 3 developments by default: headline, why it matters, significance and a link to the full record. `requirements/parameters/MAX_DELIVERY_DEVELOPMENTS.md:6`; `requirements/A-terms.md:118`.
- Readers can browse, search and filter everything held, and can see the items Beacon judged out of scope with the reason. `requirements/UIX-03.md:9`, `UIX-04.md:9`, `UIX-07.md:9`.
- Every statement is shown as a source's claim, Beacon's synthesis or Beacon's judgement, and is not published unless it traces to resolvable evidence. `requirements/OUT-05.md:9`, `requirements/EVD-05.md:9`.

Pipeline (about 6 plain stages for the annex diagram; Beacon_Report.docx section 4 gives nine, merged here)
1. Collect: fetch what each enabled source offers; keep the original page and extract clean text and metadata.
2. Filter: decide whether each new item is in, out of, or unsure for Beacon's subject area (cybersecurity, including AI security); label its type and topic.
3. Merge: group items that report the same underlying event into one "development" and line up what they claim.
4. Assess: rate how significant each development is and whether it is new; identify trends across the last 30 days; relate each development to the SSP controls and the MITRE ATT&CK and ATLAS threat frameworks.
5. Publish: select the top developments, write one evidence-grounded account of each, and publish the Briefing on the web.
6. Deliver: send a condensed version to opted-in subscribers by Telegram bot, one to one.
Cross-cutting (annex footnote, not a stage): every judgement is logged with its evidence; a Curator can correct it and an Operator can withdraw a published item. Beacon_Report.docx section 4; `requirements/A-terms.md:64-66,112`.

Current maturity
- Scale of specification: 288 requirements in 16 families, 32 tunable settings, 43 contracts between steps, 38 steps, 9 components, 4 accepted decisions, 10 applied change proposals, 24 open questions, 1 answered, 1 superseded. `00-status.md:146-158`. (The 25 Sep report said 226 requirements and 27 parameters; the vault is newer.)
- Verification: all 288 requirements carry verification "none yet"; nothing is yet tested against its requirement. Counted from the `verification:` frontmatter of `requirements/*.md`.
- Designed: nine components are named. Six are decomposed into steps and contracts: onboarding a new source, page reading, collection, deciding an item's title/publisher/authors/date, the article record store, and source monitoring. Three (the daily run controller, the operator/curator views, the digests) are named but not decomposed. `architecture/components/C-01.md` to `C-09.md`; `00-status.md:79-84`.
- Not designed: no architecture exists yet for the stages after collection (scope decision, classification, consolidation, assessment, trends, mapping, selection, composition, delivery). Each has written requirements only, and their central inputs are open: the scope criteria (`questions/Q-006.md`), the significance scale (`Q-008.md`), the labelled evaluation set (`Q-010.md`), how a confidence is expressed (`Q-011.md`), which mappings are allowed (`Q-009.md`), and whether mapping and trend evidence holds (`Q-001.md`, `Q-002.md`). `00-status.md:47-76`.
- Initial source list is settled: ten English sources (METR, Calif, The Hacker News, The Straits Times Tech, CNA Business, OpenAI news, CISA advisories, CSA/SingCERT, arXiv cs.CR, HiddenLayer). A site that bars crawlers (The Register) was excluded on policy grounds. `questions/Q-005.md:10,37-45`; `experiments/X-001.md:19`.
- Initial reference frameworks are fixed and captured: the Singapore Government SSP control set (248 controls, 26 domains, 8 system types, captured 2026-09-23), MITRE ATT&CK 19.2 (Enterprise, ICS, Mobile) and MITRE ATLAS 2026.09 (16 tactics, 208 techniques, 40 mitigations, 73 case studies). `decisions/D-003.md`; `Project-Beacon/security_frameworks/README.md` (measured results, 2026-09-23).
- Starting genre labels for items: threats, capability, research, regulatory, incident. `decisions/D-001.md`.

What the experiments showed (collection and extraction only)
- Fetching works: over 7 runs on one day across the ten sources, the original page was kept for 1,235 of 1,235 listed items (100%), no source failed entirely in any run, and a run took 15.7 minutes. Two sources needed browser-impersonation to avoid being refused. `experiments/X-001.md:9,37-60`.
- Getting titles, authors and dates right was the hard part. Three held-out tests missed their target (44/60, 50/60 correct against a target of 54; a structure check agreed with the owner's hand check on 7-9 of 10 against a target of 9), mainly because a generic extractor or a language model guessed metadata the page did not state (e.g. crediting a site's own organisation as an author, or a vendor named in the body). `experiments/X-001.md:9`, `X-002.md:9`, `X-003.md:9`, `X-004.md:9`.
- A rule-based design that takes each field from the first page source that states it, with no model call, then met the target on the 60 labelled items: 57/60 all three fields right (54 needed), 30/30 on the most recent six months. Caveat recorded in the vault: it was tuned on those items, so it is a reproduction not a fresh accuracy measurement. `experiments/X-006.md:9,95-115`.
- Conclusion to carry into Form B: collection is feasible on a laptop; metadata accuracy on unseen sources remains to be shown; the downstream judgements have not been tested at all.

Technology stack (as used so far; open-source, free, laptop-sized)
- Local language models run through Ollama on the 8 GB GPU, one model loaded at a time: qwen3:8b for reading page headers (about 1.4 s a call once loaded) and qwen2.5vl:7b for reading scanned PDF pages (about 2 minutes a page). No hosted model service has been used in experiments. `experiments/X-002.md:26-27`; `experiments/X-004.md:61`; `questions/Q-016.md:46`.
- Collection tools: plain HTTP, feed reading, TLS-impersonation client, real Chrome for sites that refuse a plain client, trafilatura and defuddle for text extraction, htmldate for date heuristics, a PDF-to-text converter ("anydoc"). Each site's robots.txt and crawl delay is honoured. `experiments/X-001.md:23,56-60`; `experiments/X-002.md:17`.
- Delivery channel: Telegram bot. Operator and curator interfaces are intended in React. `requirements/A-terms.md:112`; `architecture/components/C-02.md:12`.
- Frameworks are acquired from public sources with scripts (BeautifulSoup scraping for SSP, git clones for ATT&CK and ATLAS). `Project-Beacon/security_frameworks/README.md`.
- Working assumptions already in the vault: open-source components preferred, data in open formats, the model provider behind one interface; secrets in a managed store, encryption in transit and at rest, a second factor for every role except Reader; an external heartbeat that alerts the operator if no run has started by 00:30. `questions/Q-016.md:23-28`.
- Not stated anywhere in the vault: the database, the web back end, the hosting location for a daily run, CI/CD tooling. The `src/` code folder is not in this repository (CLAUDE.md), so the stack cannot be verified beyond the experiments. See open questions.

Outcomes achievable by each date (conservative proposal; this is my inference, not a vault statement)
- By 1 Feb 2027 (deployed): a scheduled daily run that collects from the ten-source list, keeps original pages and extracted text, filters for relevance, groups duplicate reports into developments, rates significance with local open-weight models, and publishes a web Briefing with traceable evidence; a Telegram bot delivering the condensed top developments to opted-in readers; simple Curator and Operator views for sources, corrections and withdrawal. Trend identification and mapping to SSP, ATT&CK and ATLAS are stretch outcomes: include them at a reduced scope only if the earlier stages are stable. Rationale: only collection has been designed; the vault itself lists the scope criteria, the significance scale and the evaluation set as unsettled.
- February 2027: CI/CD (automated tests and releases) and monitoring (daily run health, source health and drift alerts, an external heartbeat, cost and quota dashboards), as the vault's quality-attribute assumptions already describe. `questions/Q-016.md:23-28`.
- March 2027: buffer and iteration: evaluation of the scope and significance judgements against labelled examples, fixes found in live running, and the final report.

Key risks and limitations
- Design is ahead of build on the front end only; the largest stages are specified but undesigned, with a 1 Feb target. `00-status.md:47-84`.
- Free-only and 8 GB VRAM: judgement quality of an 8-billion-parameter local model is untested for relevance, merging, significance and mapping; the experiments showed a model hallucinating authors when unconstrained, and constrained output was needed. `questions/Q-017.md:35`; `experiments/X-006.md:111`.
- Prompt injection: Beacon turns text anyone can publish into advice for infrastructure teams; the defence (adversarial test set of at least 100 items per judgement) is not yet built. `questions/Q-017.md`.
- Source fragility: sites change layout or block crawlers; mitigated by drift detection and failure counts in design, untested in running. A site that blocks only after days of daily visits was not testable. `experiments/X-001.md:41`.
- Labels and ground truth: no labelled evaluation set exists for relevance; a provisional 300-item set is the fallback. `questions/Q-010.md`.
- Hosting and cost: a daily unattended run needs a host; the cost ceilings are an unsettled item. `questions/Q-016.md:23`.
- Privacy and consent: personal data handling for subscribers' chat accounts is an open question. `questions/Q-018.md`.
- Vault and report disagree on counts (226 vs 288 requirements); use the vault.
- Subject is English-only, ten sources initially, not a compliance tool.

Skills Section C needs (infer; modules per CLAUDE.md)
- AAI3008 Large Language Models: prompting and constraining local models, evaluation of model judgements, prompt-injection awareness.
- INF2006 Cloud Computing and Big Data: scheduled pipelines, containerised deployment, monitoring, cost control, handling a growing document store.
- INF2005 Cyber Security Fundamentals: security frameworks (SSP, ATT&CK, ATLAS), secure handling of secrets, role-based access, threat awareness.
- INF2003 Database Systems: versioned records, audit trail, search over stored text, backup and restore.
- INF2001 Introduction to Software Engineering: requirements specification, testing, CI/CD, version control, design documentation.
- Inferred from the work (no certifications claimed): web scraping and text extraction, Python, building a Telegram bot, a React interface, requirements engineering and experiment design, which the vault already shows in the experiment write-ups.

## Translation table

Internal term -> plain phrase -> needed in Form B? (y/n). Pick at most about 6 coined terms across the whole form; suggested keepers are marked "keep as defined term".

### ID families (never appear in the body)
| Internal | Plain phrase | Needed? |
|---|---|---|
| ACQ- (Acquisition rows) | collecting and storing articles | n (use phrase) |
| SRC- (Sources) | the list of sources and their upkeep | n |
| REL- (Relevance) | deciding whether an item is on-topic | n |
| CLS- (Classification) | labelling items by type and topic | n |
| DEV- (Developments) | grouping reports of the same event | n |
| ASM- (Assessment) | rating significance | n |
| TRD- (Trends) | spotting patterns over time | n |
| CTX- (Security context) | linking to security standards and threat frameworks | n |
| EVD- (Evidence and traceability) | keeping the evidence behind every judgement | n |
| FBK- (Feedback and correction) | human corrections and re-checking | n |
| GOV- (Governance) | who may change what | n |
| OPS- (Operations) | running, monitoring and recovery | n |
| SEL- (Selection) | choosing the day's top developments | n |
| OUT- (Output) | what is published | n |
| DLV- (Delivery) | sending to subscribers | n |
| UIX- (User interface) | the web interface | n |
| C-01..C-09 | components (named blocks of the system) | n |
| S-001..S-038 | steps | n |
| K-001..K-043 | hand-over formats between steps | n |
| D-001..D-004 | recorded decisions | n |
| Q-001..Q-026 | open questions | n |
| X-001..X-006 | experiments | n (say "feasibility tests") |
| CP-001..CP-010 | requirement change proposals | n |
| P0 / P1 / P2 | urgency bands for open questions | n |
| A-terms, Annex A1-A3 | glossary of defined terms | n |
| UPPER_CASE names (CYCLE_DEADLINE, TREND_WINDOW, MIN_SIGNIFICANCE etc.) | adjustable settings | n |
| [[wikilinks]], .base views | vault navigation | n |

### Defined terms
| Internal term | Plain phrase | Needed? |
|---|---|---|
| BEACON | the system (title of this workstream to be proposed; expand any acronym only if the owner confirms one) | y |
| Cycle (scheduled / exceptional) | a daily run (or a manually started extra run) | y, plain phrase "daily run" |
| Complete cycle / incomplete | a run in which every source and item was processed / not | n |
| Stage | one processing step an item passes through | n |
| Item | one article, advisory or paper | y (plain) |
| Source / Source Set | a publisher Beacon reads / the approved list of sources | y; "source list" |
| Entry / Entry part | the stored recipe for reading one source | n |
| Onboarding / Onboarding outcome | adding a new source from its web address | n |
| Collection | one fetch of a source | n |
| Discovered item / Held item / Admitted item | an item found / already stored / accepted as on-topic | n |
| Encounter, Yield, Revision | seeing a stored item again / a new item / a changed version | n |
| Raw page | the original page, kept as fetched | y (plain) |
| Extracted text | clean article text | y (plain) |
| Article Record | the stored copy of an item with its details and versions | y (plain "stored record") |
| Re-extraction | re-reading a stored page with improved rules | n |
| Chunk | a section-sized piece of text | n |
| Field decision, Supplied value, Field state | choosing an item's title, publisher, authors and date from what the page states | n (say "metadata") |
| Item publisher / Author | who published / who wrote the item | n |
| Source publication time | the date the source states | n |
| Drift flag / Drift sign / Drift check | an alert that a source's layout has changed | y (one phrase, "layout-change alert") |
| Health entry | a daily health summary for a source | n |
| Standing | how well-checked a stored recipe part is | n |
| Failed item / Dropped item / Failure reason | an item that could not be processed / given up on / why | n |
| Digest / Notification | a daily summary or message to staff about system state | n |
| Judgement | any decision Beacon makes rather than copies from a source | y; keep as defined term |
| Method / Method in force | the versioned procedure behind a judgement (model, prompt, settings) | n |
| Decision Record | the logged record of one judgement | y (plain "decision log") |
| Claim / Aligned claims | an assertion in an item / assertions about the same fact | n |
| Evidence locator | a pointer to the supporting passage | y (plain "traceable to the passage") |
| Confidence | how certain a judgement is | n |
| Statement class | claim, synthesis or judgement label | n |
| Speculative | marked as unconfirmed | n |
| Scope Criteria / scope decision (IN/OUT/UNKNOWN) | the rules that decide if an item is on-topic | y (plain "relevance filter") |
| Relevance | on-topic for cybersecurity and AI security | y |
| item_type / Genre vocabulary | item type (threat, capability, research, regulatory, incident) | n |
| subject_tags / Subject vocabulary | topic labels | n |
| Vocabulary gap | no existing label fits | n |
| Development | one real-world event reported by several items | y; keep as defined term |
| Contributing item | an item that reports a development | n |
| Development record | the web page for one development | n |
| Published development | a development that has appeared in a Briefing | n |
| Merge / Split | human correction joining or dividing developments | n |
| Entity | a named party, product or system | n |
| Materially new information | genuinely new facts about a known development | n |
| Novel | newly created in this run | n |
| Significance | how serious, large or new a development is | y; keep as defined term |
| Assessment / Current assessment / Criteria version | the dated significance rating | n |
| Trend / Trend characterisation (emerging, recurring, intensifying, stable, declining) / Active trend | a pattern across developments over 30 days | y (plain) |
| Recommendation Set | the day's ranked shortlist | n ("shortlist") |
| Account | the written summary of one development | n ("summary") |
| Briefing | the daily published digest | y; keep as defined term |
| Publish / Deliver | put on the web / send by Telegram | y (plain) |
| Delivery / Delivered entry | the daily Telegram message / one development in it | y (plain) |
| Delivery channel / Bot / Chat account | Telegram / Beacon's Telegram account / a subscriber's account | y (say "Telegram") |
| Recipient / Opt-in / Opt-out | subscriber / consent / withdrawal | y (plain) |
| Correction notice, Holding notice, Restore notice | messages telling subscribers a development was corrected, withdrawn pending review, or restored | n |
| Revised result | an updated judgement after re-checking | n |
| Reader / Curator / Operator / Administrator | reader / editorial owner / runtime owner / account manager | y; Curator and Operator suggested, Reader and Administrator plain |
| Development Team | the people who build Beacon | n |
| Governed Artefact | a controlled, versioned configuration (source list, criteria, vocabularies) | n |
| Trigger / Trigger Register | an event that forces re-checking of earlier judgements | n |
| Re-derivation / Forward processing | re-running a judgement / processing new items | n |
| Labelled example / Labelled evaluation set / Provenance class | human-labelled test data | y (plain "labelled test set") |
| Baseline / Active Baseline | a dated copy of a standard or threat framework Beacon maps against | n (say "reference copy") |
| Framework item / Mapping | a control or technique / linking a development to it | y (plain "mapping") |
| SSP | Singapore Government Security and Digital Service Standards control set (the vault's name for it) | y, expand at first use |
| system-type profile / Level (SSP) | control selection per system type / required level | n |
| MITRE ATT&CK, MITRE ATLAS | threat knowledge bases for general attacks / attacks on AI | y, expand at first use |
| STIX, OSCAL | machine-readable formats for threat and control data | n |
| Emergency brake | operator can withdraw a published item at once | n |
| Prompt injection | text that tries to steer the language model | y if space allows |

## References (APA 7, verified)
Verification status is limited: the sandbox could not reach attack.mitre.org, atlas.mitre.org or info.standards.tech.gov.sg (DNS or proxy refusal). Entries were checked against the publishers' GitHub repositories (fetched) and the repository's own README (`Project-Beacon/security_frameworks/README.md`), so the descriptions are verified and the page URLs are not live-checked. Treat as "partly verified"; re-check the three URLs from a machine with web access before submission.

- MITRE Corporation. (n.d.-a). *MITRE ATT&CK*. https://attack.mitre.org/ (description confirmed from the publisher's attack-stix-data README: a globally accessible knowledge base of adversary tactics and techniques based on real-world observations; vault uses version 19.2.)
- MITRE Corporation. (n.d.-b). *MITRE ATLAS: Adversarial Threat Landscape for Artificial-Intelligence Systems*. https://atlas.mitre.org/ (the publisher's atlas-data README expands ATLAS as "Adversarial Threat Landscape for AI Systems", a public knowledge base of adversary tactics and techniques targeting AI systems; vault uses content version 2026.09. Use "Adversarial Threat Landscape for AI Systems" if the form prefers the repository's wording.)
- Government Technology Agency of Singapore. (n.d.). *Singapore Government Security and Digital Service Standards: System security plan (SSP) control catalog and system-type profiles* [Web page]. https://info.standards.tech.gov.sg/ssp/ (NOT live-verified; the vault README names the site as "Singapore Government ICT&SS Policy Reform site" and the publisher, so confirm the exact page title and publisher name before using. If unconfirmed, drop this entry and cite the SSP in text only.)

Optional context only, not recommended for the 10-reference cap unless space allows: Beacon_Report.docx also cites ISO/IEC/IEEE 29148:2018 and Mavin et al. (2009) for requirements wording; neither is central to the Form B.

## Open questions → to_main_session
1. Hosting for the 1 Feb deployment: the vault never states where a daily unattended run will live, and one LTA laptop cannot be assumed to run 24/7. Conservative assumption used here: free-cloud-credit or the laptop in a scheduled mode, left unspecified in Form B ("hosted on free-tier or free-credit infrastructure, to be confirmed"). Please settle the line.
2. Whether the experiment machine (8 GB GPU, "one laptop") is the same LTA laptop (RTX 4060 8 GB). Assumed yes; the vault does not name the hardware.
3. Title of the workstream: the vault name is BEACON (given as a name, not an acronym in the notes). Confirm whether to keep a name for the workstream within the proposed new title, and whether to expand it.
4. Whether trend identification and framework mapping are committed or stretch by 1 Feb. I propose stretch (reduced scope). Per CLAUDE.md, Beacon scope is high-level outcomes only.
5. Is the Telegram bot channel acceptable under LTA policy (external messaging service)? The vault assumes it; no LTA context is in the repo. I recommend the form not claim LTA approval.
6. Reference verification: three URLs could not be live-checked from this sandbox (see References). Please have the reference check repeated with web access.
7. The "SSP" is called the "System Security Plan (SSP)" in the security_frameworks README but is defined in the vault glossary as the control set GovTech publishes, not a plan for any system. I used the glossary wording. Confirm preferred expansion.

## Detail

### Family and architecture inventory
- 16 requirement families with counts in the vault (rows): ACQ 42, ASM 9, CLS 6, CTX 13, DEV 14, DLV 33, EVD 11, FBK 23, GOV 19, OPS 30, OUT 12, REL 8, SEL 10, SRC 42, TRD 5, UIX 11 (total 288), plus the glossary A-terms. Counted from `requirements/` file names. Not to be listed in Form B.
- Components: C-01 daily run controller; C-02 operator/curator read views; C-03 digests; C-04 source onboarding and source list; C-05 page reading; C-06 collection; C-07 field decision; C-08 article record; C-09 source watch. `architecture/components/`.
- The vault's status page lists 43 hand-over formats still "proposed" and none implemented. `00-status.md:86-141`.

### Experiments (collection and extraction)
| Test | Aim | Outcome |
|---|---|---|
| X-001 | Can the stack fetch and keep pages from 10 sources, and keep structure and metadata | Fetch part met (1,235/1,235, no source failed); structure check not counted (agreed with hand check 8/10, 9 needed) |
| X-002 | Which tool order gives title, authors, date over six months | Not met (9/10 sources covered all months; 25/30 labelled right, 27 needed) |
| X-003 | Pre-registered design on held-out labels | Not met (44/60; 54 needed; 9/20 structure confirmations, 18 needed) |
| X-004 | Second design over twelve months | Not met (50/60 and 26/30 recent; structure check passed 18/20) |
| X-005 | Applied credit rules to X-004 labels | Superseded by X-006 |
| X-006 | Deterministic metadata, no model call | Met (57/60, 30/30 recent, authors 57/60); reproduction on seen items, not fresh accuracy |
All at `experiments/X-00n.md:9` (result line).

### Daily-run timeline default
Start after 00:00 SGT; due 08:00; grace to 08:30; Telegram at 09:00 and not before the grace period ends; the vault's working assumption is a typical day closes by 06:00 and pages load within 2 seconds. `requirements/parameters/*.md`, `questions/Q-016.md:24`.

### Scale assumptions in the vault (not commitments)
200 sources, 2,000 items a day, five years of retention, 250 recipients. `questions/Q-016.md:25`. Far beyond the initial ten sources; do not state in Form B.

### Source boundaries
Beacon honours robots.txt, waits at least 2 seconds between requests and the site's stated crawl delay (15 s on arXiv). The Register was excluded because its robots.txt denies crawlers. `experiments/X-001.md:19,23`.

### Conflicts between report and vault
- Report: 9 stages, 226 requirements, 27 parameters, Q-005 open. Vault: 288, 32, Q-005 answered with ten sources, extraction design settled by experiments. Vault used.
- Report ids and Beacon_Report.docx wording ("AI-security horizon scanning for critical-infrastructure teams") is narrative only.
