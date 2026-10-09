"""Accept every tracked change in word/document.xml only; all other parts are copied byte-for-byte."""
import sys, zipfile
from lxml import etree

W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
q = lambda t: '{%s}%s' % (W, t)

zin = zipfile.ZipFile(sys.argv[1])
root = etree.fromstring(zin.read('word/document.xml'))
for tag in ('del', 'pPrChange', 'rPrChange', 'tblPrChange', 'trPrChange', 'tcPrChange'):
    for e in list(root.iter(q(tag))):
        e.getparent().remove(e)
for e in list(root.iter(q('ins'))):
    parent = e.getparent()
    if parent.tag in (q('rPr'), q('trPr')):
        parent.remove(e)
    else:
        i = parent.index(e)
        for c in reversed(list(e)):
            parent.insert(i, c)
        parent.remove(e)
doc = etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True)
names = [n for n in zin.namelist() if not n.endswith('/')]
names.sort(key=lambda n: n != '[Content_Types].xml')
with zipfile.ZipFile(sys.argv[2], 'w', zipfile.ZIP_DEFLATED) as zout:
    for n in names:
        zout.writestr(n, doc if n == 'word/document.xml' else zin.read(n))
