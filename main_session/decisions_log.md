# Decisions log (autonomous decisions by the main session)

| # | Date | Question (from) | Decision | Rationale / source |
|---|---|---|---|---|
| 1 | 2026-10-08 | How to verify references when direct fetch is blocked (security-frameworks-explorer) | Treat a reference as verified when WebSearch returns the official page (title and URL). Most sites fail DNS or return 403 for WebFetch and curl | Network policy; WebSearch reachable |
| 2 | 2026-10-08 | Who publishes SSP, and should IM8 be named? (security-frameworks-explorer) | Publisher is the Government Technology Agency (GovTech), Singapore, on info.standards.tech.gov.sg, under the ICT&SS Policy Reform (also called the IM8 Reform). Cite as "Government Technology Agency. (2025). *System Security Plan (SSP)*. https://info.standards.tech.gov.sg/ssp/". The SSP pages were last updated 16 Sep 2025. The SSP lists a Generative AI system type | WebSearch: the info.standards.tech.gov.sg pages, and the GovTechSG/tech-standards README on GitHub |
| 3 | 2026-10-08 | Is OSCAL used inside Beacon? (security-frameworks-explorer) | Phrase as "may adopt" or a possible export format. Not a commitment | The vault leaves this as an open question |
| 4 | 2026-10-08 | Real numbered lists vs plain-text content controls (form-analyst Q1) | Follow Daniel and the template: type "1. ", "2. " and separate lines with `<w:br/>` inside the existing plain-text controls. Do not convert the controls | Template adherence (README), Daniel's precedent |
| 5 | 2026-10-08 | Bold workstream sub-labels (form-analyst Q2) | Put the plain-text label on its own line ("Workstream 1: Guardrail Evaluation Test Bench"), not bold | Same as above |
| 6 | 2026-10-08 | Email hyperlinks lack mailto: (form-analyst Q3) | Leave as is (Robin's own fields; a relationship-target change cannot be tracked). Flag in the final summary | Minimal change; under-claim |
| 7 | 2026-10-08 | Academic supervisor name/designation formatting (form-analyst Q4) | Leave unchanged | Robin's entries; never edit personal facts |
| 8 | 2026-10-08 | Stale cached values in declaration REF fields (form-analyst Q5) | Do not edit and do not set updateFields. Flag that Word refreshes them when fields are updated (F9) or printed | Declarations are protected |
| 9 | 2026-10-08 | Timeline guidance wording (form-analyst Q6) | Keep the template wording ("should be included in the annex") | Template adherence |
| 10 | 2026-10-08 | Where tables and figures go, given single-paragraph controls | Annexes A–D go after "END OF FORM B", outside any content control, as tracked insertions. Real Word tables and images are allowed there | Plan, writing style §8 |
