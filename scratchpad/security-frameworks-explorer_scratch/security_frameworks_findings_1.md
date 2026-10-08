# Security frameworks findings 1

## TL;DR
Beacon keeps four public security corpora as frozen, dated "Baselines": the Singapore Government System Security Plan (SSP) control set (248 controls, GovTech), MITRE ATT&CK v19.2 (Enterprise, ICS, Mobile), MITRE ATLAS 2026.09 (attacks on AI systems), and NIST OSCAL v1.2.3 schemas only (not content). Each cyber news development Beacon finds is mapped to the SSP control(s) and ATT&CK/ATLAS technique(s) it bears on, with evidence, reasoning and a confidence in words. This turns news into something a government critical-infrastructure team can act on in its own vocabulary; the SSP "gen-ai" system type (9 controls) is directly relevant. Skills for Section C: STIX 2.1, OSCAL, web scraping, version pinning. Caveat: outbound web was blocked (403/DNS), so the 4 references are NOT URL-verified this run; URLs come from the repo README (verified there 2026-09-23). Verify before use.

## Form B-ready facts
- SSP: Singapore Government control set at info.standards.tech.gov.sg; 248 controls in 26 domains, 2 catalogs (Cybersecurity 156, Digital Service Standards 92), 8 system types, 3 levels. Project-Beacon/security_frameworks/README.md:15-60 (counts at "Measured results, 2026-09-23")
- SSP levels: 0 "cardinal and mandatory", 1 "basic hygiene", 2 optional "best practices". README.md:19-21
- SSP "gen-ai" system type has 9 controls (4 Level 0, 5 Level 1). README.md (profile table); SSP_output/manifest.json countsPerSystemType
- SSP publishes no version number; snapshot keyed by retrieval date. README.md "Version tracking / pin"; beacon_notes/requirements/CTX-09.md:11
- MITRE ATT&CK v19.2, STIX 2.1, Enterprise (365 techniques, 493 sub-techniques), ICS (100/18), Mobile (143/47); git commit 6cda5ad. MITRE_ATTACK_output/manifest.json; README.md
- MITRE ATLAS (Adversarial Threat Landscape for AI Systems) 2026.09: 16 tactics, 208 techniques, 40 mitigations, 73 case studies; STIX 2.1 generated with the repo's own converter. MITRE_ATLAS_output/manifest.json; README.md
- ATLAS changes monthly and has no deprecation marker; ATT&CK marks revoked items. CTX-09.md:11; CTX-11.md:11
- OSCAL (Open Security Controls Assessment Language), NIST, v1.2.3 (published 2026-08-07), 9 JSON schemas downloaded. OSCAL_output/manifest.json; README.md
- Beacon uses OSCAL schemas only; any internal use of OSCAL/STIX is still an open question (Q-004, P2). Default if unresolved: each corpus read in its publisher's native format. beacon_notes/questions/Q-004.md:15-27
- Baselines are held unchanged with source, capture time and version. beacon_notes/decisions/D-003.md:14
- Each published mapping carries evidence, explanation, confidence in words, corpus name and item identifier (e.g. ATT&CK T1190, SSP AC-3). beacon_notes/requirements/CTX-06.md:9-11
- Acquisition is exploration code only (4 notebooks), not a pipeline; fully free/open data, runs on the LTA laptop. README.md:3-5
- Version pinning: ATT&CK PIN = release string, ATLAS PIN = release, OSCAL PIN = release tag; SSP has none. README.md per-notebook sections.

## Translation table
| Internal term | Plain phrase | Needed in Form B? |
|---|---|---|
| SSP (the GovTech control set; not a plan for one system) | Singapore Government System Security Plan control set | y (expand at first use) |
| system-type profile / "baseline" (SSP site) | the controls chosen for a type of system, at a level | n |
| Level 0/1/2 | mandatory / basic hygiene / optional best practice | n (maybe one clause) |
| gen-ai profile | the Government's controls for generative AI systems | y (one sentence) |
| Baseline (Beacon) | frozen, dated copy of a framework | y (coined term; define once) |
| CTX-01, CTX-02, CTX-09, CTX-11, D-003, Q-004 | -- | n (no IDs) |
| STIX 2.1 | Structured Threat Information eXpression, a standard data format for threat knowledge | y (Section C skill, expand) |
| OSCAL | Open Security Controls Assessment Language, NIST's machine-readable format for security controls | y |
| ATT&CK | MITRE ATT&CK, catalogue of real-world attacker techniques | y |
| ATLAS | MITRE ATLAS, the same for attacks on AI systems | y |
| mapping | linking a news item to the control or technique it bears on | y |
| PIN / pin | fixing a specific framework version | n (say "version pinning") |
| manifest | record of source, version and checksum for each download | n |

Suggested umbrella sentence: "Beacon links each cyber news development to the Singapore Government security controls it affects and to known attacker techniques (MITRE ATT&CK, and MITRE ATLAS for AI systems), using frozen, dated copies of each framework so every link stays traceable."

Why it matters to a government critical-infrastructure cyber team (plain, under-claimed): analysts read news in attacker-technique terms and must act in the government's control terms; a traceable news-to-control/technique link shortens triage. The gen-ai system type means AI-specific controls and ATLAS techniques are directly relevant as the agency adopts generative AI. Do not claim LTA adoption or SSP obligation beyond the repo.

Section C skills (inferred, no certifications): STIX 2.1 (reading ATT&CK/ATLAS bundles; INF2005); OSCAL (catalog/profile models; schema-based validation; INF2005/INF2003); web scraping and parsing (BeautifulSoup over heading structure, discovery rather than assumption; INF2001); version pinning and snapshot integrity (git commit, release tag, sha256; INF2006/INF2001); structured data handling (INF2003); LLM-based mapping with evidence (AAI3008).

## References (APA 7, verified)
NOT URL-verified this run: attack.mitre.org, atlas.mitre.org, pages.nist.gov and info.standards.tech.gov.sg all returned DNS failure or proxy 403; Context7 not applicable to these sites. URLs below are those recorded in the repo README as checked on 2026-09-23. Treat as "repo-verified", re-check before submission. Retrieval date shown is the repo's, not mine.
1. MITRE Corporation. (n.d.). *MITRE ATT&CK* [Knowledge base]. https://attack.mitre.org/ (STIX data: https://github.com/mitre-attack/attack-stix-data)
2. MITRE Corporation. (n.d.). *MITRE ATLAS: Adversarial Threat Landscape for Artificial-Intelligence Systems* [Knowledge base]. https://atlas.mitre.org/ (data: https://github.com/mitre-atlas/atlas-data)
3. National Institute of Standards and Technology. (n.d.). *Open Security Controls Assessment Language (OSCAL)*. https://pages.nist.gov/OSCAL/ (repo: https://github.com/usnistgov/OSCAL)
4. Government Technology Agency of Singapore. (n.d.). *System Security Plan (SSP)* [Control catalog]. Singapore Government ICT&SS Policy Reform. https://info.standards.tech.gov.sg/ssp/ . Note: README names "Singapore Government ICT&SS Policy Reform site" as publisher; GovTech attribution is from the brief and must be confirmed. IM8 not referenced (not in repo); omit unless confirmed.

## Open questions → to_main_session
- Reference verification: network blocked; can the main session verify the 4 URLs and the SSP publisher name (GovTech vs. Ministry/Smart Nation group) and adopt IM8 only if confirmed?
- Assumed: OSCAL described as "schemas only" per the brief; Q-004 leaves internal use open, so Form B should say Beacon "may adopt" it, not that it does.
- Assumed: gen-ai profile figures (9 controls) taken from the 2026-09-23 snapshot; live site may differ.

## Detail
- Notebooks: SSP_exploration (scrape, catalog + profiles, raises on zero controls/unknown ids), MITRE_ATTACK_git_exploration (git clone of STIX data; optional PIN), MITRE_ATLAS_git_exploration (dist YAML to STIX via atlas_to_stix.py, with and without ATT&CK Enterprise), OSCAL_git_exploration (GitHub API release assets). README.md:7-155.
- SSP profile sizes: dss-high 92, dss-others 92, gen-ai 9, high-risk-cloud 137, low-risk-cloud 117, low-risk-on-premises 103, medium-risk-cloud 117, sandbox 117; 6 controls in no profile; 784 profile memberships validated. README.md.
- Counts to reuse in Form B (at most one): "248 controls, 700+ attacker techniques across ATT&CK and 208 AI-attack techniques in ATLAS" (ATT&CK Enterprise 365+493 =858; all domains techniques+sub 1,166 including ICS/Mobile; use cautiously).
- Gaps: no bulk JSON opened; no LTA-specific facts invented.
