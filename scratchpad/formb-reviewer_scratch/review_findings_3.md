# Review findings 3 (formb-reviewer): FINAL docx review

Reviewed: `Form B_Guo_Zi_Qiang_Robin.docx` (md5 `5f6f3847ccd394eb13732e0996fc2955`; not edited by this review; md5 identical before and after).
Compared against:
- `scratchpad/main_session_scratch/FormB_original_backup.docx` (original)
- `template/Form B.docx`
- `scratchpad/formb-drafter_scratch/formb_draft_2.md` (plus round-2 nits N-1 to N-4, per #37)
- `scratchpad/annex-builder_scratch/annex_5.md` and `figures/`

Grounded against: CLAUDE.md, `main_session/decisions_log.md` #1–#40, the four findings files, and `form_structure_findings_1.md` Part 3 (caps).

Method:
- Checks 1–6 ran on `pandoc --track-changes=accept` text, and on accepted text extracted per content control from `word/document.xml` (`w:t` with `w:br` as a line break, `w:del` dropped).
- Check 7 ran on the XML, plus `validate.py --original <backup> --author "Guo Zi Qiang Robin"`.
- Two LibreOffice renders, each 14 pages, all viewed page by page:
  - as submitted, with markup showing
  - with all changes accepted (`accept_changes.py`)
- Figures were checked again at 200 dpi.

Working files are in the session scratchpad (`rev3/`), outside the repository.

## Verdict
**PASS. The docx is ready to submit.** There are no blocking or required fixes. Three advisories follow (V-1 to V-3); none needs a docx edit.

## Summary table

| # | Check | Result | Notes |
|---|---|---|---|
| 0 | Docx text matches `formb_draft_2.md` + N-1..N-4 | PASS | All 10 answer fields (title + 9 controls) match character for character, line breaks included |
| 1 | Cold-reader test | PASS | 5-sentence restatement below. 2 residual terms, both non-blocking |
| 2a | ID regex sweep (body) | PASS | 0 hits for all 5 patterns, in the body and in the whole document |
| 2b | Acronyms expanded at first use | PASS | 12 of 12. "AI" in the title before its expansion is accepted (title) |
| 2c | Acronyms and coined terms in glossary (Annex C) | PASS | All present. Definitions match the body. A–Z order is correct |
| 2d | Coined terms ≤ about 6 | PASS | 6: guardrail, test bench, ablation, Briefing, evaluation harness, Tier 1/Tier 2 |
| 3 | Word counts vs caps | PASS | All under cap (table below) |
| 4 | Grounding / over-claims | PASS | No over-claims; figure content grounded |
| 5 | Dates and constraints | PASS | Body and Annex A agree with CLAUDE.md. Round-2 fix A-5 (buffer is March only) is applied |
| 6 | References | PASS | 10/10, APA 7, every citation and reference paired, real italics |
| 7a | Template structure preserved | PASS | Everything outside the 10 edited controls and the annex region is equivalent to the backup (see 7 detail) |
| 7b | All edits tracked, author "Guo Zi Qiang Robin" | PASS | 402 revision marks, every one by this author; validator PASSED |
| 7c | Supervisor Remarks, Declarations, 2 flagged placeholders and hyperlinks unchanged | PASS | Contact-number and designation placeholders are byte-identical. Remarks, Declarations and hyperlinks are content-identical; their only byte changes are rsid attributes and merged runs (V-1) |
| 7d | Annexes A–D present after END OF FORM B | PASS | 4 Heading1 annexes, each after a page break, in the same section |
| 7e | Render: layout, tables, figures, checkboxes | PASS | 14 pages viewed in each render; advisories V-2 and V-3 |

## Check 0: text against draft 2

The script compared each control's accepted text with the draft-2 fenced block after applying the four logged nits (#37). Every field matched, including the blank-line (double `w:br`) structure:
- **N-1:** the Figure 1 pointer is moved earlier.
- **N-2:** "Government Technology Agency (GovTech) Sentinel service".
- **N-3:** "analysis stages after collection".
- **N-4:** "existing comparative research".

Other content checks:
- **Annex A** matches `annex_5.md`. The milestone "M (results 1 Dec)" moved into the row label "Run Tier 1 evaluation (results 1 Dec)", as logged in `apply_log_1.md`.
- **Annex B** captions match. The embedded images are byte-identical (md5) to `annex-builder_scratch/figures/figure1_guardrail_checkpoints.png` and `figure2_beacon_pipeline.png`. Figure 2 now says "event(s)" (#40 applied).
- **Annex C** matches `annex_5.md`, with all rows merged into one A–Z list (N-5).
- **Annex D** matches draft 2.

## Check 1: cold-reader test

1. Workstream 1 builds a minimal evaluation harness, a "test bench", that scores NVIDIA's NeMo Guardrails, Meta's Llama Guard 3/4 and GovTech's Sentinel (LionGuard 2) on the same labelled prompts. Meta's Prompt Guard 2 is a planned third comparator for jailbreak detection. The comparison covers harmful-content classification and jailbreak detection (Tier 1), and the bench changes one setting at a time.
2. Workstream 2 builds Beacon, a cloud-hosted daily service. Beacon collects public AI-security news, filters it, merges duplicates and rates significance. It publishes a ranked web Briefing and a Telegram digest, with an initial evidence-traceable mapping of each event to SSP controls and MITRE ATT&CK/ATLAS techniques.
3. LTA runs critical infrastructure. Workstream 1 lets its CYAD division choose guardrails on evidence rather than vendor claims before deploying generative AI. Workstream 2 gives CYAD timely, defensible threat awareness expressed in control and attacker-technique terms.
4. Test bench results are due by 1 Dec 2026 and the report in 1–6 Dec. Beacon is deployed by 1 Feb 2027, with CI/CD and monitoring through February and March as buffer.
5. Form E1 is due 6 Dec, the Interim Presentation 31 Jan and Form E2 21 Mar, all on one 8 GB-GPU laptop with free tools. The Final Presentation is on 11 Apr, after the period.

Terms I could not fully explain from the document alone:
- "products share the same underlying service" (Scope, Tier 2 reasons). It is vague, but an informed reader can follow it. No fix.
- "Generative AI system type" (Industry Relevancy). It is context only, and accepted in rounds 1–2. No fix.

Round-2 items N-3 ("later pipeline stages") and N-4 ("the comparative research") are resolved in the docx.

## Check 2: jargon / ID sweep

| Regex | Body (before END OF FORM B) | Whole document |
|---|---|---|
| `\b[A-Z]{3}-\d{2}\b` | 0 | 0 |
| `\b[CSKDQX]-\d{2,3}\b` | 0 | 0 |
| `\bC\d{1,2}\b` | 0 | 0 |
| `\bP[012]\b` | 0 | 0 |
| `\bCP-\d+` | 0 | 0 |

Acronyms, where each is first expanded, and whether it is in Annex C:
- CYAD, LTA and AI: Overview, sentence 1. In Annex C.
- GovTech: Overview. In Annex C.
- SSP: Overview, per #17. In Annex C.
- ATT&CK and ATLAS: Overview. In Annex C.
- CI/CD: Objective 8. In Annex C.
- GPU: Scope. In Annex C.
- STIX, OSCAL and API: Additional Knowledge. In Annex C.

Other notes:
- MITRE, NVIDIA, NeMo and LionGuard are names. GB is a unit.
- Spelling: no US forms. "program" is used in the software sense. "Organization" is the template's own label and is untouched.
- Neither "Daniel" nor "Chua" appears in the body. "Chua, G." in Tan et al. (2025) is a different person, a co-author of that paper.

## Check 3: word counts

Counts use form-analyst's method: whitespace split, with typed numerals and labels counted. Caps are from `form_structure_findings_1.md` Part 3.

| Section | Docx count | Cap | Spare | Result |
|---|---|---|---|---|
| A Project Title | 16 | none | n/a | PASS |
| B Project Overview | 246 | 247 | 1 | PASS |
| B Project Objectives | 214 | 270 | 56 | PASS |
| B Industry Relevancy | 143 | 170 | 27 | PASS |
| B Project Scope | 220 | 222 | 2 | PASS |
| B Project Outputs and Deliverables | 83 | 110 | 27 | PASS |
| C Applicable Knowledge from the Degree Programme | 65 | 72 | 7 | PASS |
| C Additional Knowledge, Skillsets, or Certifications | 96 | 130 | 34 | PASS |
| C Training Required and Provided | 67 | 105 | 38 | PASS |
| D Project Timeline | 230 | 312 | 82 | PASS |
| Totals by lettered section | B 906 / 1020; C 228 / 307; D 230 / 312 | | | PASS |

These counts match the drafter's figures in `apply_log_1.md`.

## Check 4: grounding and over-claims

The body text is unchanged from draft 2, apart from the four nits; it passed grounding in round 2. Two items are new or newly visible in the docx.

| Claim | Source | Result |
|---|---|---|
| "existing comparative research" (N-4) | `benchtest_findings_1.md`, the research xlsx | OK |
| Figure 2 footer: "A reviewer can correct it, and an operator can withdraw a published item." | `beacon_findings_1.md:31` | OK. Annex only, at high level |
| Figure 2, step 4: mapping to SSP and ATT&CK/ATLAS shown as a core stage | #14, #26 | OK |
| Figure 1: five checkpoints; the caption says Tier 1 evaluates input checks | #25 | OK |

Over-claim sweep:
- Only Tier 1 is committed. Tier 2 is "under investigation". Prompt Guard 2 is "planned".
- Llama Guard 4 is "subject to model access", with Llama Guard 3 as the baseline. There is no 8-bit local claim.
- Beacon is described at outcome level, with no requirement families or IDs. Its mapping is "initial", trend detection is a stretch goal, Telegram is subject to LTA policy and no hosting provider is named.
- The red-team project is unnamed, context only, with "no committed integration".

## Check 5: dates and constraints

Body:
- Period 8 Oct 2026 – 31 Mar 2027.
- Form B 11 Oct.
- Test bench results 1 Dec; report in the first week of Dec / 1–6 Dec.
- E1 6 Dec.
- Beacon build Dec–Jan.
- Interim Presentation 31 Jan.
- Deploy 1 Feb 2027.
- CI/CD and monitoring throughout Feb.
- March buffer.
- E2 21 Mar.
- Final Presentation 11 Apr, after the period.

All of these match CLAUDE.md.

Annex A (rendered):
- Milestones are M in Oct, Dec, Jan, Mar, Mar and Apr.
- Tier 1 runs Nov, with results M in Dec.
- Report in Dec.
- Design Oct–Nov.
- Build Dec–Jan.
- Deploy M in Feb.
- CI/CD in Feb.
- **Buffer in Mar only.** A-5 is fixed.

The E1 row also shows X in Nov, which reads as preparation. This is consistent with the report feeding E1; no fix.

Constraints:
- Hardware: "a single provided development laptop with an 8 GB graphics processing unit (GPU)".
- Free and open-source: "only open-source, free, free-trial or free-credit technology", plus "free-tier cloud GPU credits".
- Tooling: "no further organisation-provided tooling or computing resources are assumed".

PASS.

## Check 6: references

- **Count:** 10 (limit 10).
- **In-text citations** found in the body:
  - Rebedea et al., 2023
  - Inan et al., 2023
  - Government Technology Agency, n.d.-b
  - Tan et al., 2025
  - Government Technology Agency, 2025
  - The MITRE Corporation, n.d.-a, n.d.-b
  - Meta AI, 2023
  - Government Technology Agency, n.d.-a
  - Meta, 2025

  Each resolves to exactly one entry, and every entry is cited.
- **Order:** APA 7. The two MITRE entries file under M (#33).
- **Formatting:**
  - Real italics on titles and proceedings names, checked in the XML runs.
  - 0.5-inch hanging indent, checked in the render.
  - Retrieval dates per #28.
  - Preprint DOI per #35.

PASS.

## Check 7: docx-only

**7a: Template structure.**
- The package contains the same parts as the backup, plus two new media files (`image3.png`, `image4.png`) and their relationships, rId17 and rId18. No other relationships changed.
- `styles.xml`, `numbering.xml`, `settings.xml`, the header, the footer, the theme and the glossary part are byte-identical to the backup.
- `document.xml` was compared after two steps:
  - The 10 edited controls (title + 9 answer boxes) were replaced by tokens, and the annex region was cut out.
  - Both files were normalised for rsid attributes, with the backup run-merged the way `merge_runs.py` merges runs.

  The rest of the body is identical to the backup.
- Heading order is A–F as in the template, then Annex A–D as un-numbered Heading1 (no stray letters in the render).
- The single section and the final sectPr are preserved.

**7b: Tracked changes.**
- 383 `w:ins`, 10 `w:del` and 9 `w:pPrChange`. All carry `w:author="Guo Zi Qiang Robin"` and date 2026-10-08T12:00:00Z. No other author appears.
- The edited controls contain no untracked text.
- In the annex:
  - All 209 paragraphs have an inserted paragraph mark.
  - All 44 table rows carry `trPr/ins`.
  - Both drawings sit inside `w:ins`.
  - No text is untracked.
- Placeholder text was removed as tracked deletions (#38).
- `validate.py --author` reports "All validations PASSED". Its "173 → 40" paragraph line is the known glossary-part quirk.

**7c: Protected content.**

| Item | sdt id | Status |
|---|---|---|
| Academic Supervisor contact number placeholder | -600105709 | Byte-identical |
| Industry Supervisor designation placeholder | 1956675477 | Byte-identical |
| Industry Supervisor Remarks | 1415043535 | Content-identical (rsid only) |
| Academic Supervisor Remarks | -38901724 | Content-identical (rsid only) |
| Declaration fields (15 controls) and 3 signature controls | -1464955567 … -2027085963 | Content-identical; 3 signature controls byte-identical, the others rsid/run-merge only |
| Email hyperlinks (rId8–10) | n/a | Unchanged (same relationship targets, same `w:hyperlink` elements) |
| Robin's General Information fields | various | Content-identical (rsid / run-merge only) |

**7d: Annexes.**
- A Summary Gantt Chart, B Figures, C Glossary and D References all come after END OF FORM B.
- Each starts on a new page.
- Both figures have alt text.

**7e: Render.** All 14 pages were viewed, in the markup render and in the accepted render.

| Page | What it shows | Result |
|---|---|---|
| 1–2 | General Information | Title wraps cleanly. Checkboxes are ☒ industry and ☒ single-disciplinary, as in the original. The two flagged placeholders are still red. Page 2 is mostly blank, the same as in the original render (template page break before B) |
| 3–5 | Section B | See V-2 |
| 6 | Section C | |
| 7 | Section D | |
| 8 | Supervisor Remarks | Placeholders intact |
| 9–10 | Declarations, END OF FORM B | |
| 11 | Annex A | The table fits the margins; shading and M/X marks are legible |
| 12 | Annex B | Both figures are sharp at 200 dpi; see V-3 |
| 13 | Annex C | Table fits on one page |
| 14 | Annex D | Hanging indents are correct |

The markup render shows struck-through placeholders and underlined insertions, all as expected.

## Advisories (non-blocking; no docx edit needed)

**V-1: rsid attributes stripped across the document.** The drafter's `merge_runs.py` step stripped rsid attributes and coalesced runs across the whole document. That includes the Supervisor Remarks and the Declarations, which are therefore not byte-identical to the backup.
- These are revision-session metadata and run splits only. Text, formatting, fields and controls are identical, and Word shows no tracked change for them.
- My assumption is that this satisfies "unchanged". Main session: note it in the final summary rather than rebuild.

**V-2: Heading split from its answer in the accepted render.** In the accepted LibreOffice render, the heading "Project Outputs and Deliverables" sits at the foot of page 4, and its guidance line and answer start on page 5. In the markup render they stay together.
- Pagination in Word may differ.
- If Robin exports a clean PDF from Word, he could check this page break. No change to the docx is needed for submission.

**V-3: Footer page count and Figure 2 text size.**
- The footer reads "Page N of 8" on all 14 pages in LibreOffice. This is the cached field accepted in #39.
- Recommend exporting any PDF from Word, not from LibreOffice, so the field refreshes to "of 14".
- The Figure 2 box text prints at roughly 6–7 pt. It is legible, but small; acceptable.

## Open questions → to_main_session
1. V-1: confirm that "content-identical, rsid/run-merge only" is acceptable for the protected regions. I assumed yes; the conservative alternative is a rebuild from the backup without `merge_runs.py`, which I do not recommend this close to the deadline.
2. For the final summary to Robin, these items remain:
   - The two flagged placeholders.
   - The footer's "of 8" (#39).
   - Exporting the PDF from Word (V-3).
   - The emails without mailto: (#6).
   - The stale declaration REF values, which Word refreshes (#8).
