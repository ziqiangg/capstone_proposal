STAGE 2: apply the final text to the docx.
Inputs:
- text: scratchpad/formb-drafter_scratch/formb_draft_2.md, plus the round-2 optional nits in scratchpad/formb-reviewer_scratch/review_findings_2.md that do not change meaning or exceed a cap (decision #37)
- Annex A month table, figure captions and Annex C glossary: scratchpad/annex-builder_scratch/annex_5.md
- figures: scratchpad/annex-builder_scratch/figures/figure1_guardrail_checkpoints.png and figure2_beacon_pipeline.png
- Annex D: your draft 2
- mechanics: scratchpad/form-analyst_scratch/form_structure_findings_1.md (anchors, tracked-change recipe, annex placement); decisions #4–#10
- backup of the original: scratchpad/main_session_scratch/FormB_original_backup.docx

Rules:
- Edit "Form B_Guo_Zi_Qiang_Robin.docx" in place, using the docx skill workflow (unpack in your scratch folder, merge_runs, edit, pack).
- Every change is w:ins / w:del with w:author="Guo Zi Qiang Robin".
- Change only the Project Title and the free-text controls of B, C and D.
- Insert Annexes A–D after "END OF FORM B": a page break; an annex heading in an existing template style; Annex A as a real Word table; Annex B with the 2 images and captions, sized to fit A4 margins; Annex C as a table; Annex D as a reference list with hanging indent if a style allows.
- Do not touch Supervisor Remarks, Declarations, the two flagged placeholders, or the hyperlinks.
- Validate with: python /mnt/skills/public/docx/scripts/office/validate.py <out> --original <backup> --author "Guo Zi Qiang Robin"
- Render to PDF and PNG and view every page yourself before you reply.

Write a short apply log in your scratch folder, apply_log_1.md.
