"""Remove revision marks from plain-text content controls and repack a docx Word-style."""
import sys, zipfile
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
q = lambda t: '{%s}%s' % (W, t)
REV = ('ins', 'del', 'pPrChange', 'rPrChange')

def plain_text_sdts(root):
    for sdt in root.iter(q('sdt')):
        pr = sdt.find(q('sdtPr'))
        if pr is not None and pr.find(q('text')) is not None:
            yield sdt

src, dst = sys.argv[1], sys.argv[2]
zin = zipfile.ZipFile(src)
root = etree.fromstring(zin.read('word/document.xml'))
removed = 0
for sdt in plain_text_sdts(root):
    for e in list(sdt.iter(q('pPrChange'))):
        e.getparent().remove(e); removed += 1
problems = []
for i, sdt in enumerate(plain_text_sdts(root)):
    left = [t for t in REV for _ in sdt.iter(q(t))]
    rprs = {etree.tostring(r.find(q('rPr'))) if r.find(q('rPr')) is not None else b'' for r in sdt.iter(q('r'))}
    if left or len(rprs) > 1:
        problems.append((i, left, len(rprs)))
print('pPrChange removed:', removed, '| problems:', problems)
if problems:
    sys.exit(1)
doc = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
names = [n for n in zin.namelist() if not n.endswith('/')]
names.sort(key=lambda n: n != '[Content_Types].xml')
with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zout:
    for n in names:
        zout.writestr(n, doc if n == 'word/document.xml' else zin.read(n))
