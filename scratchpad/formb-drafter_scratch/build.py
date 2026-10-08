"""Build tracked-change Form B document.xml from formb_draft_2.md and annex_5.md.

Usage: python3 -I build.py <work_dir>
Reads <work_dir>/document.merged.xml and rels.merged.xml (merged-run copies of
the original), writes <work_dir>/un/word/document.xml and its rels.
"""
import re
import sys
from pathlib import Path
from xml.sax.saxutils import escape

WORK = Path(sys.argv[1])
ROOT = Path("/home/user/capstone_proposal")
DRAFT = ROOT / "scratchpad/formb-drafter_scratch/formb_draft_2.md"
ANNEX = ROOT / "scratchpad/annex-builder_scratch/annex_5.md"
AUTHOR = "Guo Zi Qiang Robin"
DATE = "2026-10-08T12:00:00Z"

_id = [1000]


def nid():
    _id[0] += 1
    return _id[0]


def attrs():
    return f'w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}"'


def typo(s):
    return s.replace("'", "’")


def t(s):
    return f'<w:t xml:space="preserve">{escape(typo(s))}</w:t>'


# ---------------------------------------------------------------- text
draft = DRAFT.read_text()
heads = re.findall(r"^#{2,3} (.+)$", draft, re.M)
parts = re.split(r"^#{2,3} .+$", draft, flags=re.M)
blocks = {}
for h, p in zip(heads, parts[1:]):
    m = re.search(r"```text\n(.*?)```", p, re.S)
    if m:
        blocks[h] = m.group(1).rstrip("\n")

NITS = [  # review_findings_2.md N-1 to N-4 (decision #37)
    ("Project Overview",
     "allow, block or flag each message, catching harmful requests or jailbreaks (attempts to trick the chatbot into ignoring its rules) (see Annex B, Figure 1).",
     "allow, block or flag each message (see Annex B, Figure 1), catching harmful requests or jailbreaks (attempts to trick the chatbot into ignoring its rules)."),
    ("Project Overview",
     "the Government Technology Agency's (GovTech) Sentinel service",
     "the Government Technology Agency (GovTech) Sentinel service"),
    ("D. Project Timeline",
     "design of the later pipeline stages continues at low intensity",
     "design of the analysis stages after collection continues at low intensity"),
    ("Project Objectives",
     "Complete the comparative research on guardrail products",
     "Complete the existing comparative research on guardrail products"),
]
for h, a, b in NITS:
    assert blocks[h].count(a) == 1, (h, a)
    blocks[h] = blocks[h].replace(a, b)

CAPS = {
    "Project Overview": (-1188283889, 247),
    "Project Objectives": (-1461255160, 270),
    "Industry Relevancy": (-344099556, 170),
    "Project Scope": (464701024, 222),
    "Project Outputs and Deliverables": (-967980080, 110),
    "Applicable Knowledge from the Degree Programme": (773065924, 72),
    "Additional Knowledge, Skillsets, or Certifications Required": (274985427, 130),
    "Training Required and Provided": (-122541047, 105),
    "D. Project Timeline": (697813163, 312),
}
counts = {}
for h, (_, cap) in CAPS.items():
    counts[h] = len(blocks[h].split())
    assert counts[h] <= cap, (h, counts[h], cap)

doc = (WORK / "document.merged.xml").read_text()

# ---------------------------------------------------------------- title
title = blocks['A. Project Title (replaces "Beacon")']
old = '<w:sdtContent><w:r><w:t>Beacon</w:t></w:r></w:sdtContent>'
assert doc.count(old) == 1
doc = doc.replace(old,
    f'<w:sdtContent><w:del {attrs()}><w:r><w:delText>Beacon</w:delText></w:r></w:del>'
    f'<w:ins {attrs()}><w:r>{t(title)}</w:r></w:ins></w:sdtContent>')


# ---------------------------------------------------------------- block controls
def fill(doc, sid, text):
    key = f'<w:id w:val="{sid}"/>'
    i = doc.index(key)
    s = doc.rindex("<w:sdt>", 0, i)
    e = doc.index("</w:sdt>", i) + len("</w:sdt>")
    blk = doc[s:e]
    assert blk.count("<w:p ") == 1 and "<w:showingPlcHdr/>" in blk
    blk = blk.replace("<w:showingPlcHdr/>", "")
    blk = blk.replace("</w:sdtPr>", "</w:sdtPr><w:sdtEndPr/>", 1)
    m = re.search(r'(<w:p [^>]*>)<w:pPr><w:pStyle w:val="BodyText"/></w:pPr>(.*?)</w:p>', blk, re.S)
    assert m
    runs = m.group(2)
    deleted = runs.replace("<w:t>", "<w:delText>").replace(
        '<w:t xml:space="preserve">', '<w:delText xml:space="preserve">').replace("</w:t>", "</w:delText>")
    ins = []
    for k, line in enumerate(text.split("\n")):
        if k:
            ins.append("<w:r><w:br/></w:r>")
        if line:
            ins.append(f"<w:r>{t(line)}</w:r>")
    newp = (m.group(1)
            + '<w:pPr><w:pStyle w:val="BodyText"/><w:jc w:val="left"/>'
            + f'<w:pPrChange {attrs()}><w:pPr><w:pStyle w:val="BodyText"/></w:pPr></w:pPrChange></w:pPr>'
            + f"<w:del {attrs()}>{deleted}</w:del>"
            + f"<w:ins {attrs()}>{''.join(ins)}</w:ins></w:p>")
    blk = blk[:m.start()] + newp + blk[m.end():]
    return doc[:s] + blk + doc[e:]


for h, (sid, _) in CAPS.items():
    doc = fill(doc, sid, blocks[h])


# ---------------------------------------------------------------- annex helpers
def para(runs_xml="", style="BodyText", ppr=""):
    return (f'<w:p><w:pPr><w:pStyle w:val="{style}"/>{ppr}<w:rPr><w:ins {attrs()}/></w:rPr></w:pPr>'
            + (f"<w:ins {attrs()}>{runs_xml}</w:ins>" if runs_xml else "") + "</w:p>")


def run(text, rpr=""):
    return f"<w:r>{('<w:rPr>' + rpr + '</w:rPr>') if rpr else ''}{t(text)}</w:r>"


def page_break():
    return para('<w:r><w:br w:type="page"/></w:r>')


def heading(text):
    return para(run(text), style="Heading1")


LEFT0 = '<w:ind w:left="0"/><w:jc w:val="left"/>'
CELLP = '<w:spacing w:before="20" w:after="20" w:line="240" w:lineRule="auto"/>' + LEFT0


def cell(text, width, bold=False, fill=None, center=False, span=1, sz=18):
    rpr = ("<w:b/>" if bold else "") + f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
    tcpr = f'<w:tcW w:w="{width}" w:type="dxa"/>'
    if span > 1:
        tcpr += f'<w:gridSpan w:val="{span}"/>'
    if fill:
        tcpr += f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>'
    tcpr += '<w:vAlign w:val="center"/>'
    ppr = CELLP.replace('<w:jc w:val="left"/>', '<w:jc w:val="center"/>') if center else CELLP
    body = run(text, rpr) if text else ""
    return f"<w:tc><w:tcPr>{tcpr}</w:tcPr>{para(body, ppr=ppr)}</w:tc>"


def row(cells, header=False):
    trpr = f"<w:trPr>{'<w:tblHeader/>' if header else ''}<w:ins {attrs()}/></w:trPr>"
    return f"<w:tr>{trpr}{''.join(cells)}</w:tr>"


def table(widths, rows):
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in widths)
    return ('<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/>'
            f'<w:tblW w:w="{sum(widths)}" w:type="dxa"/><w:tblInd w:w="0" w:type="dxa"/>'
            '<w:tblLayout w:type="fixed"/><w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" '
            'w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/></w:tblPr>'
            f"<w:tblGrid>{grid}</w:tblGrid>{''.join(rows)}</w:tbl>")


def md_runs(text, base_rpr=""):
    """*italic* segments -> italic runs."""
    out = []
    for k, seg in enumerate(re.split(r"\*(.+?)\*", text)):
        if seg:
            out.append(run(seg, base_rpr + ("<w:i/><w:iCs/>" if k % 2 else "")))
    return "".join(out)


annex = ANNEX.read_text()


def md_table(section_title):
    s = annex.index(section_title)
    lines = []
    for line in annex[s:].split("\n")[1:]:
        if line.startswith("## "):
            break
        if line.startswith("|"):
            lines.append([c.strip() for c in line.strip().strip("|").split("|")])
    return lines[0], [r for r in lines[2:]]


# ---------------------------------------------------------------- Annex A
A = []
A.append(page_break())
A.append(heading("Annex A: Summary Gantt Chart"))
A.append(para())
A.append(para(run("Month-level summary of the project plan. X = active in that month; M = milestone in that month. "
                  "The project period is 8 October 2026 to 31 March 2027; the Final Presentation (11 April 2027) falls after it. "
                  "The detailed weekly chart is provided in Gantt_Guo_Zi_Qiang_Robin.xlsx."), ppr=LEFT0))
A.append(para())
hdr, rows = md_table("## Annex A")
assert len(hdr) == 8, hdr
W = [3426] + [800] * 7
trs = [row([cell("Activity", W[0], bold=True, fill="D9D9D9")]
           + [cell(m, W[i + 1], bold=True, fill="D9D9D9", center=True) for i, m in enumerate(hdr[1:])], header=True)]
for r in rows:
    label = r[0]
    if label.startswith("**"):
        trs.append(row([cell(label.strip("*"), sum(W), bold=True, fill="F2F2F2", span=8)]))
        continue
    vals = r[1:]
    if label == "Run Tier 1 evaluation":
        label = "Run Tier 1 evaluation (results 1 Dec)"
        vals = ["M" if v.startswith("M") else v for v in vals]
    cs = [cell(label, W[0])]
    for i, v in enumerate(vals):
        if v == "X":
            cs.append(cell("X", W[i + 1], fill="BFBFBF", center=True))
        elif v == "M":
            cs.append(cell("M", W[i + 1], bold=True, center=True))
        else:
            assert v == "", v
            cs.append(cell("", W[i + 1], center=True))
    trs.append(row(cs))
A.append(table(W, trs))
A.append(para())

# ---------------------------------------------------------------- Annex B
caps = dict(re.findall(r"- \*\*(Figure \d)\.\*\* (.+)", annex))
EMU_W = 5580000  # 15.5 cm


def image(rid, docpr, name, px_w, px_h, descr):
    cy = round(EMU_W * px_h / px_w)
    a = "http://schemas.openxmlformats.org/drawingml/2006/main"
    pic = "http://schemas.openxmlformats.org/drawingml/2006/picture"
    return ('<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
            f'<wp:extent cx="{EMU_W}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
            f'<wp:docPr id="{docpr}" name="{name}" descr="{escape(descr, {chr(34): "&quot;"})}"/>'
            f'<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="{a}" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
            f'<a:graphic xmlns:a="{a}"><a:graphicData uri="{pic}"><pic:pic xmlns:pic="{pic}">'
            f'<pic:nvPicPr><pic:cNvPr id="0" name="{name}.png"/><pic:cNvPicPr/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{EMU_W}" cy="{cy}"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic>'
            '</wp:inline></w:drawing></w:r>')


IMGP = '<w:ind w:left="0"/><w:jc w:val="center"/>'
CAPP = '<w:ind w:left="0"/><w:jc w:val="left"/>'
B = [page_break(), heading("Annex B: Figures"), para()]
for n, rid, docpr, (pw, ph), descr in [
        (1, "rId17", 101, (1840, 762), "Diagram of the five places a guardrail check can sit around an AI chatbot: input, conversation rules, retrieval, action and output."),
        (2, "rId18", 102, (2280, 650), "Diagram of the Beacon daily pipeline in six steps: collect, filter, merge, rate and map, publish, deliver.")]:
    B.append(para(image(rid, docpr, f"Figure {n}", pw, ph, descr), ppr=IMGP))
    B.append(para(run(f"Figure {n}. ", "<w:b/><w:i w:val=\"0\"/>") + run(caps[f"Figure {n}"]), style="Caption", ppr=CAPP))
    B.append(para())

# ---------------------------------------------------------------- Annex C
hdrC, rowsC = md_table("## Annex C")
rowsC = sorted(rowsC, key=lambda r: r[0].lower())  # one A-Z list (reviewer N-5)
WC = [2600, 6426]
trs = [row([cell("Term", WC[0], bold=True, fill="D9D9D9", sz=20), cell("Plain definition", WC[1], bold=True, fill="D9D9D9", sz=20)], header=True)]
for term, defi in rowsC:
    trs.append(row([cell(term, WC[0], bold=True, sz=20), cell(defi, WC[1], sz=20)]))
C = [page_break(), heading("Annex C: Glossary"), para(),
     para(run("Acronyms and terms used in this form, in alphabetical order."), ppr=LEFT0), para(),
     table(WC, trs), para()]

# ---------------------------------------------------------------- Annex D
s = draft.index("## Annex D: References (APA 7)")
e = draft.index("\n---", s)
refs = [l.strip() for l in draft[s:e].split("\n")[1:] if l.strip()]
assert len(refs) == 10, len(refs)
REFP = '<w:spacing w:after="160"/><w:ind w:left="720" w:hanging="720"/><w:jc w:val="left"/>'
D = [page_break(), heading("Annex D: References"), para()]
for r in refs:
    D.append(para(md_runs(r), ppr=REFP))

annex_xml = "".join(A + B + C + D)
end = doc.index("END OF FORM B")
pend = doc.index("</w:p>", end) + len("</w:p>")
assert doc[pend:].startswith("<w:sectPr")
doc = doc[:pend] + annex_xml + doc[pend:]

(WORK / "un/word/document.xml").write_text(doc)

rels = (WORK / "rels.merged.xml").read_text()
img = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"
assert "rId17" not in rels and "rId18" not in rels
rels = rels.replace("</Relationships>",
                    f'<Relationship Id="rId17" Type="{img}" Target="media/image3.png"/>'
                    f'<Relationship Id="rId18" Type="{img}" Target="media/image4.png"/></Relationships>')
(WORK / "un/word/_rels/document.xml.rels").write_text(rels)

print("counts", counts)
print("last revision id", _id[0])
for h in ["Project Overview", "Project Objectives", "D. Project Timeline"]:
    print(h, len(blocks[h].split()))
