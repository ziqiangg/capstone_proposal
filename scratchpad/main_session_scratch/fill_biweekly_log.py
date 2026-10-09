"""Fill the SIT Capstone Biweekly Log template for Trimester 1 Week 6 (28 Sep - 9 Oct 2026)."""
import sys, copy, zipfile
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
q = lambda t: '{%s}%s' % (W, t)
XML_SPACE = '{http://www.w3.org/XML/1998/namespace}space'

TITLE = '– Guardrail Test Bench and Beacon'
CELLS = {(0, 1): 'Guo Zi Qiang Robin', (0, 3): '31/08/26 - 09/04/27',
         (1, 1): '2400989', (1, 3): 'Trimester 1/ Week 6',
         (2, 1): 'Land Transport Authority (LTA)'}
BOXES = {
    'Describe the background': [
        "Weeks 5–6 at LTA's Cyber Architecture & Development division: I scoped my capstone into two workstreams, an AI guardrail "
        "evaluation test bench and Beacon, a daily AI-security news briefing service, while advancing Beacon's data-collection design "
        "and the guardrail comparison research.",
    ],
    'List the task(s) assigned': [
        '1. Beacon: ran six experiments on extracting article details (title, authors, publication date) from news sources, '
        'reviewed and accepted ten requirement changes, and designed the data-collection architecture.',
        '2. Test bench: extended the comparison of NVIDIA NeMo Guardrails, Meta Llama Guard and GovTech Sentinel/LionGuard, '
        'agreed the scope and timeline with my supervisors, and drafted Form B (due 11 Oct).',
    ],
    'Include the outcome of you': [
        '• A rule-based extraction method met its accuracy targets (57/60 on held-out articles, 30/30 on recent ones) after earlier '
        'model-assisted designs fell short; the collection design and the Form B draft are complete.',
        '• Learned that simple deterministic methods can beat language models for structured details, and that tiering the guardrail '
        'comparison keeps the test bench feasible on an 8 GB laptop GPU.',
    ],
}

def set_text(run, text):
    for t in run.findall(q('t')):
        run.remove(t)
    t = etree.SubElement(run, q('t'))
    t.text = text
    t.set(XML_SPACE, 'preserve')

src, dst = sys.argv[1], sys.argv[2]
zin = zipfile.ZipFile(src)
root = etree.fromstring(zin.read('word/document.xml'))
body = root.find(q('body'))

# Title: replace the italic placeholder run with the bold style of "Capstone"
title_p = body[0]
runs = [r for r in title_p.findall(q('r')) if r.find(q('t')) is not None]
placeholder = next(r for r in runs if 'edit title' in ''.join(r.itertext()))
bold = next(r for r in runs if 'Capstone' in ''.join(r.itertext()))
placeholder.replace(placeholder.find(q('rPr')), copy.deepcopy(bold.find(q('rPr'))))
set_text(placeholder, TITLE)
for r in runs:
    if r is not placeholder and ''.join(r.itertext()).strip() in ('[', ']', 'edit title accordingly', 'accordingly]'):
        title_p.remove(r)

# Details table
rows = body.find(q('tbl')).findall(q('tr'))
for (ri, ci), text in CELLS.items():
    tc = rows[ri].findall(q('tc'))[ci]
    label_run = rows[ri].findall(q('tc'))[ci - 1].find('.//' + q('r'))
    p = tc.find(q('p'))
    for r in p.findall(q('r')):
        p.remove(r)
    r = etree.SubElement(p, q('r'))
    r.append(copy.deepcopy(label_run.find(q('rPr'))))
    set_text(r, text)

# Answer boxes: both the DrawingML and VML fallback copies of each text box
for key, lines in BOXES.items():
    hits = 0
    for txbx in root.iter(q('txbxContent')):
        first = txbx.find(q('p'))
        if key not in ''.join(first.itertext()):
            continue
        run = first.find(q('r'))
        color = run.find(q('rPr')).find(q('color'))
        if color is not None:
            color.set(q('val'), '000000')
        for extra in first.findall(q('r'))[1:]:
            first.remove(extra)
        ppr = first.find(q('pPr'))
        if ppr is None:
            ppr = etree.Element(q('pPr'))
            first.insert(0, ppr)
        for tag in ('ind', 'spacing'):
            if ppr.find(q(tag)) is not None:
                ppr.remove(ppr.find(q(tag)))
        spacing = etree.Element(q('spacing'))
        spacing.set(q('after'), '0')
        anchor_el = ppr.find(q('numPr')) if ppr.find(q('numPr')) is not None else ppr.find(q('pStyle'))
        if anchor_el is not None:
            anchor_el.addnext(spacing)
        else:
            ppr.insert(0, spacing)
        set_text(run, lines[0])
        anchor = first
        for line in lines[1:]:
            p = copy.deepcopy(first)
            set_text(p.find(q('r')), line)
            anchor.addnext(p)
            anchor = p
        hits += 1
    assert hits == 2, (key, hits)

# Date: remove the dd/mm/yy placeholder, keep "Date:" and the tab
date_p = next(p for p in body.findall(q('p')) if ''.join(p.itertext()).startswith('Date'))
for r in date_p.findall(q('r')):
    if ''.join(r.itertext()).strip() in ('dd/mm/', 'yy'):
        date_p.remove(r)

doc = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
names = sorted((n for n in zin.namelist() if not n.endswith('/')), key=lambda n: n != '[Content_Types].xml')
with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zout:
    for n in names:
        zout.writestr(n, doc if n == 'word/document.xml' else zin.read(n))
print('wrote', dst)
