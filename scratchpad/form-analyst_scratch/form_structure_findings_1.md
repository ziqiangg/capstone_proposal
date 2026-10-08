# Form structure findings 1 (form-analyst)

Inputs read-only. Unzipped copies: `scratchpad/form-analyst_scratch/{tpl,robin,daniel}/`. Paragraph dumps: `tpl.dump`, `robin.dump`, `daniel.dump` (index = order of every `w:p` in `word/document.xml`, including paragraphs inside content controls and table cells). Pandoc output: `tpl.md`, `robin.md`, `daniel.md`.

## TL;DR
- Every answer field is a Word content control (`w:sdt`). The 11 free-text answers are block-level plain-text controls with `w:text w:multiLine="1"`. Each holds exactly one paragraph, so line breaks are `<w:br/>` and lists are typed ("1. ..."), as Daniel did.
- Daniel kept the italic "(Please use a separate sheet...)" line, deleted only the red placeholder, and used no new styles, tables or real lists.
- Robin's file differs from the template only in the General Information fields (11 text/date fields, 2 checkboxes). Sections B to E are untouched placeholders. There are no tracked changes yet and `trackRevisions` is absent.
- Section letters are A to E, then F for "Declaration of Conformity". Daniel's free-text total is 656 words and the per-section caps are in Part 3.
- Open issues: plain-text controls forbid real numbered lists. Mailto hyperlinks are broken. The declaration cached values are stale.

## Form B-ready facts
- Sections are numbered by Heading1 + `numId 34` (upperLetter): A General Capstone Project Information, B Capstone Project Details, C Knowledge and Training Requirements, D Project Timeline, E Supervisor Remarks, F Declaration of Conformity (`ListParagraph`, `template/Form B.docx` word/document.xml; verified by rendering the template with LibreOffice). So the CLAUDE.md "Section C modules" = Knowledge and Training; "sections B and D" = Capstone Project Details and Project Timeline.
- Daniel's word counts and caps: see Part 3 (`scratchpad/form-analyst_scratch/daniel.dump` lines 68-114).
- Tracked-change mechanics: `robin/word/settings.xml` has no `w:trackRevisions` and no `w:ins`/`w:del` anywhere. `documentProtection edit="forms" enforcement="0"` (not enforced). See Part 6.
- Page: A4 (11906x16838), margins 1440 left/right, 1560 top/bottom, single section. `sectPr` is the last child of `w:body`, after "END OF FORM B" (idx 172).
- Footer text is "AAI4001 Capstone Project - Form B; R2021-01 Page {PAGE} of {SECTIONPAGES}" (`word/footer1.xml`). Keep the annex in the same section or the "of N" count changes.
- Declarations pull header values through `REF <Bookmark> \h` fields. Bookmarks (id 0-10): `Candidate_Name`, `Candidate_Matriculation_Number`, `Academic_Supervisor_{Name,Email_Address,Contact_Number,Designation}`, `Industry_Supervisor_{Name,Email_Address,Contact_Number,Designation,Department_Division}`. `Candidate_Matriculation_Number`, `*_Designation` are bookmarked but not referenced in the declarations. Do not delete these bookmarks or the sdt wrappers inside them.

## Translation table
Not applicable to this task (form structure only). Style terms used below:

| Internal term | Plain phrase | Needed in Form B? |
|---|---|---|
| sdt / content control | answer box | n |
| placeholder run | grey/red italic guidance | n |

## References (APA 7, verified)
None needed.

## Open questions → to_main_session
1. **Numbered lists vs plain-text control.** CLAUDE.md asks for numbered lists, but a plain-text control (`w:text`) cannot hold several paragraphs or real list numbering. Assumption (conservative, follows Daniel): type "1. ", "2. " at the start of each line, separated by `<w:br/>`. Alternative if real lists are wanted: remove `<w:text .../>` (making it a rich-text control) and use `ListParagraph` + a new `w:num`; this departs from the template and Daniel.
2. **Bold sub-labels inside answers** ("Workstream 1: ..."): per-run bold is not allowed inside plain-text controls in Word's UI. Assumption: write the label as plain text on its own line, no bold. Same alternative as above.
3. **Hyperlinks in Robin's two email fields** have `Target="pulakesh.upadhyaya@singaporetech.edu.sg"` and `Target="tan_zi_qi@lta.gov.sg"` (rels rId9, rId10) without `mailto:`. Clicking them fails. Not fixed (outside scope); needs a tracked fix or a leave-as-is decision.
4. **Academic supervisor name/designation** in Robin's file: "Professor Upadhyaya, Pulakesh", "Assistant Professor AI & Data Science (Infocomm Technology)". Daniel's form has "Pulakesh Upadhyaya" and "Assistant Professor". CLAUDE.md says leave the Academic Supervisor contact number and Industry Supervisor designation. The name and designation formatting is not covered. Assumption: leave unchanged.
5. **Declaration cached values** (REF field results) in Robin's file still show placeholders, e.g. "The industry supervisor's name". Do not edit (Declarations are protected by decision). Fields refresh when Word updates fields on open or print. Optional main-session decision: whether to set `w:updateFields` in settings.xml (not recommended; it triggers a prompt).
6. **Daniel's timeline guidance** edited the italic line to "a Gantt chart may be included as annex". The template and Robin say "should be included in the annex". Follow the template (keep as is).

## Detail

### 1. Template structure (ordered)
Paragraph styles: nearly everything is `BodyText` (Arial; `ind left 408`; `jc both`; tab 426; line 247 auto). Headings: `Heading1` (Arial bold 13pt, numbered), `Heading3` (Arial bold 12pt, numbered level 1), `ListParagraph` (only "Declaration of Conformity"). Empty `BodyText` paragraphs act as spacers. Six `BodyText` paragraphs hold `<w:r><w:br w:type="page"/></w:r>` and sit before B, C, D, E, F and before the Academic declaration. Idx numbers are from `tpl.dump`.

| Idx | Section / field | Control (sdt) and anchor | Guidance text (italic) |
|---|---|---|---|
| 0-4 | Title block: "Singapore Institute of Technology", "Information and Communications Technology Cluster", "AAI4001 Capstone Project", "Capstone Project Details (Form B)" (underlined) | none | none |
| 6 | A. General Capstone Project Information (Heading1) | none | none |
| 8 | "Project Information:" bold | none | none |
| 10 | (Project Title) | run-level text sdt id 664052563 | *The capstone project title* |
| 12 | (Organization) | text sdt id -1463258527 | *The organization name* |
| 14-17 | (Initiation) two checkboxes | `w14:checkbox` sdt, one per option (sdt idx 2,3); industry = first | none |
| 19-22 | (Multi-disciplinary) two checkboxes | `w14:checkbox` (sdt idx 4,5); single-disciplinary = second | none |
| 24 | "Candidate Particulars:" | none | none |
| 26 | (Name of Candidate) | text sdt -417796748, bookmark `Candidate_Name` | *The candidate's full name* |
| 28 | (Matriculation Number) | text sdt -1092778840 | *The candidate's matriculation number* |
| 30-32 | (Programme) | NOT a control: hyperlink rId8 "Applied Artificial Intelligence" | none |
| 34 | (Project Period) | two date sdts (418453129; -2102243038), format `d/M/yyyy`, `en-SG` | *Project start date* / *Project end date* |
| 37-45 | Main Academic Supervisor: Name, Email, Contact Number, Designation | text sdts 2141225020, -320198354, -600105709, -1355726687 | *The academic supervisor's ...* |
| 48-58 | Industry Supervisor: Name, Email, Contact, Designation, Department / Division | text sdts 861784053, 2058896490, -82374714, 1956675477, 244779553 | *The industry supervisor's ...* |
| 62 | B. Capstone Project Details (Heading1) | none | none |
| 64-67 | Project Overview: | block sdt id -1188283889 | line "(Please use a separate sheet if necessary)" (idx 65, italic sz 20) plus placeholder "Please provide a description of the candidate's capstone project, including its purpose, etc." |
| 69-72 | Project Objectives: | block sdt -1461255160 | "...detailed description of the project objectives, i.e., what is the candidate expected to accomplish" |
| 74-77 | Industry Relevancy: | block sdt -344099556 | "...relevance of the project to the hosting organization, and / or to the industry at large" |
| 79-82 | Project Scope: | block sdt 464701024 | "...detailed description of the project scope, including any limitations of the project" |
| 84-87 | Project Outputs and Deliverables (no colon) | block sdt -967980080 | "...detailed description of the expected outputs and deliverables by the candidate" |
| 91 | C. Knowledge and Training Requirements (Heading1) | none | none |
| 93-96 | Applicable Knowledge from the Degree Programme | block sdt 773065924 | "...pre-requisite knowledge and / or skillsets from the degree programme..." |
| 98-101 | Additional Knowledge, Skillsets, or Certifications Required | block sdt 274985427 | "...beyond the degree programme..." |
| 103-106 | Training Required and Provided | block sdt -122541047 | "...additional relevant training that is required by, and that will be provided to the candidate..." |
| 110-113 | D. Project Timeline (Heading1) | block sdt 697813163 | idx 111 "(Please use a separate sheet if necessary; Gantt chart should be included in the annex)" then placeholder "...detailed timeline of the project, including expected output and deliverables" |
| 117-126 | E. Supervisor Remarks (Heading1, idx 118 note); Industry Supervisor Remarks (Heading3, idx 120), Academic Supervisor Remarks (Heading3, idx 124) | block sdts 1415043535 and -38901724 | "Please provide any other details... references or research papers..." (leave untouched) |
| 130 | F. Declaration of Conformity (ListParagraph) | none | none |
| 132-144, 146-156, 159-169 | Declaration by Industry Supervisor / Candidate / Academic Supervisor (Heading3), text with underlined phrases, a 2-column table each: Signature (picture sdt) and field list | picture sdts, text sdts, date sdt; REF fields | leave untouched |
| 172 | "END OF FORM B" (BodyText, centred, bold) | none | none |

Industry-supervisor header sdt ids in order: Name 861784053, Email 2058896490, Contact -82374714, Designation 1956675477, Department 244779553 (verified by `robin` sdt index 14-18). Academic: Name 2141225020, Email -320198354, Contact -600105709, Designation -1355726687.

Anchoring guidance for the drafter: locate block controls by `w:sdtPr/w:id` (stable, unique in each file except checkboxes) or by the preceding unique bold label ("Project Overview:", etc.). The sdt is the next sibling of the empty spacer paragraph after the italic "(Please use a separate sheet...)" line. Do not use paragraph index alone, since it shifts after edits.

Placeholder XML (template): `<w:sdtPr>` has `<w:showingPlcHdr/>`, `<w15:color w:val="FF0000"/>`, `<w:text w:multiLine="1"/>`; the content paragraph is `BodyText` with runs `rStyle=PlaceholderText`, `<w:i/>`, `color FF0000`, split across 1 to 5 runs.

### 2. How Daniel placed answers; recommended convention
- Guidance: kept the italic "(Please use a separate sheet if necessary)" lines (idx 65 etc.) unchanged. Deleted only the placeholder runs inside the control. Removed `<w:showingPlcHdr/>`, added empty `<w:sdtEndPr/>`.
- Answer formatting: plain runs with no `rStyle`, no italic, no colour (black body text); paragraph `BodyText` plus `<w:jc w:val="left"/>` (overrides the justified style) in sections B and C and the timeline; the two Supervisor Remarks stay as placeholders.
- Structure: each answer is one paragraph in the control. Line breaks are `<w:br/>` runs. A blank line between sub-paragraphs is two consecutive `<w:br/>`. Lists are typed text ("1. Research...", "2. ...") with a `<w:br/>` between items. No new styles, no real lists, no tables, no bold or sub-headings. Timeline is "Phase n (Weeks a-b): Name --- outputs" lines separated by blank lines.
- Header fields filled in controls; full programme title typed in an sdt (Robin's file keeps the template hyperlink). Daniel did not use the declaration fields beyond cached values.
- Recommended convention for Robin: (a) keep the italic "(Please use...)" lines; (b) remove placeholder runs and `showingPlcHdr`, add `<w:sdtEndPr/>`; (c) one paragraph per control, `BodyText` + `jc left` (same as Daniel), runs without rStyle/italic/colour; (d) numbered lists typed as "1. text" separated by `<w:br/>`, with a blank line (two `<w:br/>`) between prose paragraphs; (e) workstream labels as plain text lines "Workstream 1: Guardrail Evaluation Test Bench"; (f) all tables and figures go in the annexes (Daniel had none); (g) every edit tracked (Part 6).

### 3. Daniel's word counts and caps
Method: for each of Daniel's block controls, concatenated all `w:t` text in the control with each `<w:br/>` treated as whitespace, split on whitespace, counted tokens. Typed list numerals ("1.") count as words in the main figure; the figure without them is also given. Excludes the italic guidance line and headings. 2.5x cap is exact; the working cap is the floor (an under-claim).

| Section (Daniel) | Words (with numerals) | Words (numerals excluded) | 2.5x cap (exact) | Working cap (floor) |
|---|---|---|---|---|
| B Project Overview | 99 | 99 | 247.5 | 247 |
| B Project Objectives | 108 | 101 | 270.0 | 270 |
| B Industry Relevancy | 68 | 68 | 170.0 | 170 |
| B Project Scope | 89 | 89 | 222.5 | 222 |
| B Project Outputs and Deliverables | 44 | 34 | 110.0 | 110 |
| C Applicable Knowledge from the Degree Programme | 29 | 29 | 72.5 | 72 |
| C Additional Knowledge, Skillsets, or Certifications | 52 | 52 | 130.0 | 130 |
| C Training Required and Provided | 42 | 42 | 105.0 | 105 |
| D Project Timeline | 125 | 125 | 312.5 | 312 |
| E Industry/Academic Supervisor Remarks | 0 (placeholder) | 0 | no cap | no cap (Robin leaves untouched) |
| Totals | B 408; C 123; D 125; free text 656 | | B 1020; C 307.5; D 312.5; all 1640 | |

Caveats: Section A fields are not free text. Daniel's Section B total is 408 words, so the overall budget for Robin's Section B is about 1020 words. Sections can be reallocated only if the per-section cap rule is relaxed; CLAUDE.md says each section, so treat caps per sub-section above. A "section" could also be read as a whole lettered section (B 1020, C 307, D 312); the sub-section reading is the stricter and is the one tabulated. Count Robin's text with the same method (script: `python3 -I` over `w:t` plus `w:br` as space).

### 4. Daniel's voice and tense
- Third person, formal, no "I/we". Future tense for what the tool does and what will be provided: "The tool will orchestrate existing open-source security testing frameworks"; "will be provided by the Cyber Architecture & Development (CYAD) division as needed".
- Present tense for scope, relevance and purpose: "The project covers research, architecture design, and development of..."; "The project addresses a capability gap within the CYAD division".
- Objectives open with a lead-in and imperative infinitives: "The candidate is expected to:" then "1. Research and document all ten...", "2. Evaluate existing open-source...", "6. Generate professional, OWASP-mapped, reproducible pentest-style reports."
- Deliverables are bare noun phrases: "1. AI Red Team Tool v1.0 (source code)", "8. Benchmark & Accuracy Report".
- Timeline is present tense with a plan summary then phases: "The project follows an approximately 32-week plan across eight phases:" then "Phase 1 (Weeks 1-4): Foundation & Research --- AI Security Fundamentals Report; ...". Uses week numbers, not dates.
- Conventions: British spelling ("organisations", "minimises"), "e.g." in brackets, "&" in names, long sentences (30+ words), semicolon-separated lists, acronyms expanded at first use (LLM, CYAD), tool names in parentheses.
- Section C quoted as style reference (Daniel, verbatim):
  - Applicable Knowledge: "Foundational knowledge from the Applied Artificial Intelligence programme, including machine learning and neural network fundamentals, Python programming, software engineering practices, and coursework covering cybersecurity, data structures, and system design."
  - Additional Knowledge: "Practical knowledge of LLM/GenAI system architecture (prompts, RAG, embeddings, agentic tool-calling), AI-specific security concepts (OWASP GenAI LLM Top 10 2026, MITRE ATLAS), and familiarity with open-source AI red-teaming frameworks (e.g. Garak, PyRIT, Promptfoo, Giskard, Inspect AI). [blank line] No formal certification is a prerequisite, though prior exposure to application security testing would be beneficial."
  - Training: "An initial orientation to the organisation's AI application landscape and internal security testing policies and authorisation procedures will be required. Any organisation-specific tooling, source-code access, and lab/sandbox environment setup will be provided by the Cyber Architecture & Development (CYAD) division as needed."
- Note: Daniel's Section C names no modules, so Robin's explicit module list (AAI3008, INF2006, INF2005, INF2003, INF2001) is richer than the precedent; it must still stay within the cap of 72 words for the first sub-section.

### 5. Robin's file vs the template
Diffs found by comparing paragraph dumps (`diff tpl.dump robin.dump`) and sdt states:
- Filled: Project Title "Beacon" (sdt 0; to be replaced); Organization "Land Transport Authority (LTA)"; Initiation checkbox "industry" set (`w14:checked 1`, glyph U+2612, font MS Gothic); Multi-disciplinary: "single-disciplinary" set; Name "Guo Zi Qiang Robin"; Matric "2400989"; Project Period `8/10/2026` to `31/3/2027` (date controls with `fullDate="2026-10-08T00:00:00Z"`); Academic name "Professor Upadhyaya, Pulakesh"; email; designation "Assistant Professor AI & Data Science (Infocomm Technology)"; Industry name "Tan Zi Qi"; email "tan_zi_qi@lta.gov.sg"; contact "+65 9823 2058"; department "IT, CYBERSECURITY & DIGITAL SERVICES/Cyber Architecture & Development".
- Still placeholders: Academic Supervisor Contact Number (sdt 12; leave); Industry Supervisor Designation (sdt 17; leave, flagged missing); all 11 Section B/C/D/E block controls (sdt 19-29); all declaration fields and signatures (sdt 30-46).
- Structural drift: none. The paragraph count, styles, section order, bookmarks (0-10), REF fields, the unchanged sectPr and the page breaks are identical. Section headings are unchanged. New rsid `00E90AAC` (17 paragraphs/runs) and `00E453E0`, `00EC4D6C` appear in settings.xml but not in the body.
- Checkbox mechanics: two `w14:checkbox` sdts per question. Toggle by setting `w14:checked w14:val` (0/1) and replacing the glyph (`&#9744;` Segoe UI Symbol unchecked; `&#9746;` MS Gothic with `w:eastAsia` + `w:hint="eastAsia"` checked). Already done correctly.
- Content controls: 47 sdts in each of the template and Robin's file (Daniel 48). Properties common to all: `w15:color FF0000`; text controls have `<w:text/>`; block controls `<w:text w:multiLine="1"/>`; date controls `d/M/yyyy` `en-SG`. The "Programme" hyperlink is not a control.
- Hyperlink problems: see Open question 3. The email controls use `rStyle Hyperlink` inside `w:hyperlink`.
- Document protection: `documentProtection edit="forms" enforcement="0"` (not enforced). docProps/core.xml: creator "Goh Weihan", lastModifiedBy "Cybersecurity Department", revision 335.

### 6. Tracked-change mechanics for this file
- Existing: zero `w:ins`, `w:del`, `w:moveFrom/To`, comments, or `w:author` attributes in `document.xml`, `styles.xml`, `settings.xml`, headers or footers. No `comments.xml` part.
- settings.xml: no `w:trackRevisions`, no `w:revisionView`. Setting `<w:trackRevisions/>` is a settings-level choice (not an edit that needs marking); per CLAUDE.md the edits are tracked as author "Guo Zi Qiang Robin". Insert `<w:trackRevisions/>` before `<w:defaultTabStop>` (schema order: zoom, ..., trackRevisions, ..., defaultTabStop) if the flag should be on for later reviewers. rsids: 895 `w:rsid` entries in settings.xml, `rsidRoot 00914BEA`; new revisions may add an rsid (optional) or omit rsid attributes entirely.
- IDs: bookmarks use `w:id` 0-10. Use revision `w:id` values from 1001 upward (unique across ins/del/rPr marks and not colliding with bookmark ids).
- Date format: ISO 8601 UTC, e.g. `w:date="2026-10-08T12:00:00Z"`. Author: `w:author="Guo Zi Qiang Robin"`.
- Filling a placeholder control (recommended recipe): remove `<w:showingPlcHdr/>`; delete the placeholder runs without `w:del` (Word treats placeholder text as not real content); add `<w:sdtEndPr/>` after `sdtPr`; add the paragraph pPr `<w:jc w:val="left"/>`; insert the answer as `<w:ins w:id=".." w:author="Guo Zi Qiang Robin" w:date=".."><w:r><w:t xml:space="preserve">text</w:t></w:r></w:ins>`, with line breaks as `<w:ins ...><w:r><w:br/></w:r></w:ins>`. Preserve the `xml:space="preserve"` attribute where spaces lead or trail.
- Replacing existing text (e.g. the title "Beacon" in sdt 0, run `rsidR=00E90AAC`): wrap the old run in `<w:del ...>` converting `<w:t>` to `<w:delText>`, then add a `<w:ins>` run after it, both inside `w:sdtContent`.
- Paragraph insertion for annexes: new paragraphs need `<w:pPr><w:rPr><w:ins .../></w:rPr></w:pPr>` (marks the paragraph mark as inserted) plus `<w:ins>` around runs. New table rows need `<w:trPr><w:ins .../></w:trPr>` and each cell's content wrapped. Validate with `scripts/office/validate.py out.docx --original <file> --author "Guo Zi Qiang Robin"`.
- Do not touch: Supervisor Remarks controls, Declarations (incl. REF fields and picture sdts), Academic Supervisor contact (sdt 12), Industry Supervisor designation (sdt 17).

### 7. Annexes after "END OF FORM B"
- Anchor: the paragraph with text "END OF FORM B" (idx 172; `BodyText`, `jc center`, `rPr b`), followed immediately by the body's final `w:sectPr`. Insert new paragraphs between them (the sectPr must stay the last child of `w:body`).
- Page break: copy the template pattern, a `BodyText` paragraph containing `<w:r><w:br w:type="page"/></w:r>` (used six times already), as a tracked insertion. Put one before Annex A and between annexes.
- Heading style: `Heading1` is bold Arial 13pt and gets its letter only from direct `numPr` (numId 34), so a `Heading1` paragraph without `numPr` gives an unnumbered heading, avoiding a "G." letter that would collide with the A to F scheme. `Heading2` (centred, bold, 16.5pt, no numbering) is also available. `Heading3` is bold 12pt. Recommendation: `Heading2` or un-numbered `Heading1` titled "Annex A: Gantt Chart", "Annex B: Figures", "Annex C: Glossary", "Annex D: References". These must be typed in plain text ("Annex A ..."), not auto-lettered.
- Body text for annexes: `BodyText` (indented 408, justified); use `jc left` for tables and captions.
- Table styles available in styles.xml: `TableGrid` (single borders, Times New Roman 10pt by default; override cell paragraph with `BodyText`/`TableParagraph` and Arial), `PlainTable1`, `ListTable1Light-Accent3`, `TableTheme`. Paragraph styles for cells: `TableParagraph`, `TableText-TextLeft`, `TableText-TextRight`. Template tables (declaration signature tables) use `TableGrid`-like borders; fonts come from `BodyText` with `ind left=0`. Caption style `Caption` exists (italic, 9pt, colour text2) for table/figure captions.
- Page: A4 portrait text width = 11906 - 2880 = 9026 DXA. A month-level Gantt as a Word table with about 7 month columns plus a label column fits within this. A landscape section would need a new `sectPr` inside a paragraph; the footer uses `SECTIONPAGES`, so a new section makes "of N" count that section only, and `pgNumType start=1` would restart numbering. Avoid landscape.
- Images: figures go in via a normal drawing; the package already has `media/image1.png` (signature placeholder). New media must be added to `[Content_Types].xml` (png Default exists) and `word/_rels/document.xml.rels` (existing rIds up to rId16, check before choosing new ones).
