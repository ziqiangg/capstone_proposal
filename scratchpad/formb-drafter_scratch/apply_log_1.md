# Apply log 1 (formb-drafter, Stage 2)

Target: `Form B_Guo_Zi_Qiang_Robin.docx`, edited in place. Backup: `scratchpad/main_session_scratch/FormB_original_backup.docx`, which was byte-identical to the target before the edit.
Builder: `scratchpad/formb-drafter_scratch/build.py`. Working files: `scratchpad/formb-drafter_scratch/work/`. That folder holds the unpacked package, `out.docx`, `accepted.docx` and the renders in `render/` (markup) and `render_acc/` (changes accepted).

## Sources
- Body text comes from `formb_draft_2.md`, plus the round-2 nits N-1 to N-4 (#37). N-1 moves the Figure 1 pointer. N-2 changes "Government Technology Agency (GovTech) Sentinel service". N-3 changes "analysis stages after collection". N-4 adds "existing".
- Final word counts against caps:
  - Overview 246/247
  - Objectives 214/270
  - Industry Relevancy 143/170
  - Scope 220/222
  - Outputs 83/110
  - Applicable Knowledge 65/72
  - Additional Knowledge 96/130
  - Training 67/105
  - Timeline 230/312
- Annex A table, figure captions and Annex C come from `annex-builder_scratch/annex_5.md`. The figures come from `annex-builder_scratch/figures/`.
- Annex D comes from draft 2 (10 entries).

## What was changed (all tracked, author "Guo Zi Qiang Robin", ids 1001–1402)
- **Project Title.** The run "Beacon" is marked w:del. The new title is marked w:ins inside the existing run-level control.
- **The 9 free-text controls of B, C and D**, located by sdt id. In each one:
  - `showingPlcHdr` is removed and `<w:sdtEndPr/>` is added.
  - The red placeholder run is marked w:del.
  - The answer is one w:ins containing text runs and `<w:br/>` line breaks.
  - The paragraph gets `jc left`, recorded as a tracked w:pPrChange.
  - The italic "(Please use a separate sheet…)" lines are unchanged.
- **Annexes A–D**, inserted after "END OF FORM B" and before the final sectPr, in the same section:
  - Each annex starts with a template page-break paragraph and an un-numbered `Heading1`.
  - A: a TableGrid table, 9026 dxa wide, with a header row and shaded group rows. Shaded X marks an active month and bold M a milestone. The cell "M (results 1 Dec)" is moved into the row label to fit the column.
  - B: two inline PNGs at 15.5 cm wide (rId17 → media/image3.png, rId18 → media/image4.png), with alt text and `Caption`-style captions.
  - C: a two-column TableGrid table, sorted A–Z as one list (reviewer N-5).
  - D: BodyText paragraphs with a 720/720 hanging indent and real italics.
- **Every inserted paragraph mark, table row (trPr) and run** is tracked.

## Not touched
- Supervisor Remarks (both still show the placeholder).
- All Declarations, including the REF fields.
- The Academic Supervisor contact number and the Industry Supervisor designation.
- The email hyperlinks.
- settings.xml: `trackRevisions` was not switched on.
- Headers and footers.

## Deviation from form-analyst's recipe
- Placeholder text is removed as a tracked w:del, not silently.
  - Reason: the validator's `--author` check flags any untracked text change, so silent removal would fail.
  - Effect: in Word's markup view the old red placeholder shows struck through. Accepting all changes removes it.

## Validation and visual check
- `validate.py "Form B_Guo_Zi_Qiang_Robin.docx" --original <backup> --author "Guo Zi Qiang Robin"` → All validations PASSED.
  - The "Paragraphs: 173 → 40" line is a quirk of the validator: it counts the last document.xml it finds, which is the glossary part. The real body count is 173 → 382.
- I rendered the file to PDF with LibreOffice, both with markup and with changes accepted, and viewed all 14 pages.
  - The layout is intact and the section order is unchanged.
  - The tables fit within the margins, and the figures are legible.

## Notes for main session
1. The footer reads "Page N of 8" on all 14 pages in the LibreOffice render. This is the stale cached SECTIONPAGES value (8 in the original too). LibreOffice does not recompute it; Word updates page fields on layout and print. I left it unchanged, because the footer is not in scope and an edit there would be an untracked change.
2. The Figure 2 image (annex-builder) still uses the word "development" in boxes 3 and 5, while the body says "event". This is minor. Annex-builder could relabel it if wanted.
3. `trackRevisions` is not switched on in settings.xml (form-analyst marked it optional). Turn it on if later edits by reviewers should be tracked automatically.
