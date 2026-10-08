import sys,re
from lxml import etree
W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
ns={'w':W}
def q(t):return '{%s}%s'%(W,t)
def dump(path):
    root=etree.parse(path).getroot()
    body=root.find(q('body'))
    i=0
    for el in body.iter(q('p')):
        st=el.find('w:pPr/w:pStyle',ns)
        st=st.get(q('val')) if st is not None else '-'
        num=el.find('w:pPr/w:numPr',ns)
        n='num' if num is not None else ''
        intbl='T' if any(a.tag==q('tc') for a in el.iterancestors()) else ''
        insdt=[]
        for a in el.iterancestors():
            if a.tag==q('sdt'):
                pr=a.find('w:sdtPr',ns)
                kinds=[c.tag.split('}')[1] for c in pr if c.tag.split('}')[1] in('text','date','dropDownList','comboBox','checkbox','richText','docPartObj')]
                al=pr.find('w:alias',ns); ph=pr.find('w:showingPlcHdr',ns)
                insdt.append(','.join(kinds)+('/ph' if ph is not None else '')+('/'+al.get(q('val')) if al is not None else ''))
        txt=''
        ital=0;tot=0
        for r in el.iter(q('r')):
            t=''.join(x.text or '' for x in r.iter(q('t')))
            if '<w:br' : t+= '\\n' * len(r.findall('w:br',ns))
            txt+=t
            if t.strip():
                tot+=1
                if r.find('w:rPr/w:i',ns) is not None: ital+=1
        print(f'{i:3d} [{st}]{n}{intbl} {"sdt:"+"|".join(insdt) if insdt else ""} i={ital}/{tot} :: {txt[:90]!r}')
        i+=1
dump(sys.argv[1])
