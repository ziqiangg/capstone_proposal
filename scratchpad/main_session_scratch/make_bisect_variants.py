"""Build Word-diagnosis variants of the Form B docx, each removing one suspect. Other parts are copied byte-for-byte."""
import sys, zipfile, copy
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
WP = 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'
q = lambda t: '{%s}%s' % (W, t)

cur, backup, outdir = sys.argv[1:4]

def load(p):
    return etree.fromstring(zipfile.ZipFile(p).read('word/document.xml'))

def save(root, name):
    zin = zipfile.ZipFile(cur)
    doc = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
    names = sorted((n for n in zin.namelist() if not n.endswith('/')), key=lambda n: n != '[Content_Types].xml')
    with zipfile.ZipFile(f'{outdir}/{name}', 'w', zipfile.ZIP_DEFLATED) as z:
        for n in names:
            z.writestr(n, doc if n == 'word/document.xml' else zin.read(n))
    print('wrote', name)

def sdt_by_id(root, kind):
    out = {}
    for sdt in root.iter(q('sdt')):
        pr = sdt.find(q('sdtPr'))
        if pr is not None and pr.find(q(kind)) is not None:
            out[pr.find(q('id')).get(q('val'))] = sdt
    return out

def restore_sdts(root, kind):
    orig = sdt_by_id(load(backup), kind)
    n = 0
    for sid, sdt in sdt_by_id(root, kind).items():
        if sid in orig:
            sdt.getparent().replace(sdt, copy.deepcopy(orig[sid])); n += 1
    return n

# T3: no annexes
root = load(cur); body = root.find(q('body'))
kids = list(body); end = next(i for i, e in enumerate(kids) if 'END OF FORM B' in ''.join(e.itertext()))
for e in kids[end + 1:]:
    if e.tag != q('sectPr'):
        body.remove(e)
save(root, 'T3_no_annexes.docx')

# T4: no Annex B figures
root = load(cur); n = 0
for dp in root.iter('{%s}docPr' % WP):
    if dp.get('id') in ('101', '102'):
        run = next(a for a in dp.iterancestors() if a.tag == q('r'))
        run.getparent().remove(run); n += 1
print(' figures removed:', n); save(root, 'T4_no_figures.docx')

# T5: answer fields and title restored to the original placeholders
root = load(cur); print(' text controls restored:', restore_sdts(root, 'text')); save(root, 'T5_answers_reverted.docx')

# T6: picture controls (signatures) restored to the original
root = load(cur); print(' picture controls restored:', restore_sdts(root, 'picture')); save(root, 'T6_signature_reverted.docx')
