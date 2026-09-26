"""Enumerate rendered JSX raster uses and fail the sixth source-pixel gate."""
import re,json,itertools,hashlib
from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parents[1]; AN=R/'analysis'
shots=json.loads((R/'src/shots-fifth.json').read_text(encoding='utf-8')); used={s['id']:s for s in shots}
def dims(name):return Image.open(R/'public/assets'/name).size
def numeric(p,key,default=0):
    expr=p.get(key,str(default)).strip('{}')
    assert re.fullmatch(r'[0-9. +*/()\-a-z]+',expr),(key,expr)
    return max(float(eval(expr,{'__builtins__':{}},dict(zip(['entry','slow','back','out'],v)))) for v in itertools.product([0,1],repeat=4))
def audit(version):
    source=(R/f'src/{version.title()}Edit.tsx').read_text(encoding='utf-8')
    rows=[]
    for m in re.finditer(r"if\(id==='([^']+)'\)(.*?)(?=\n\s*if\(id===|\n\s*return <Stage>\{null\})",source,re.S):
        shot,branch=m.groups()
        if shot not in used:continue
        for i,tag in enumerate(re.finditer(r'<(Picture|Crop|Phone|WebPage)\s+([^>]*?)/>',branch),1):
            kind,body=tag.groups(); props=dict(re.findall(r'(\w+)=("[^"]*"|\{[^}]*\})',body)); name=props['name'].strip('"'); iw,ih=dims(name)
            w=numeric(props,'w',440); h=numeric(props,'h',820); scale=numeric(props,'scale',1)
            sw,sh=iw,ih
            if kind=='Crop':
                sw=numeric(props,'sw');sh=numeric(props,'sh'); factor=w/sw; h=sh*factor;scale=1
                if version=='sixth':assert 0<=numeric(props,'sx') and 0<=numeric(props,'sy') and numeric(props,'sx')+sw<=iw and numeric(props,'sy')+sh<=ih,(shot,'crop exceeds image bounds')
            elif kind=='Phone':
                h=w*2622/1206; factor=max(w/iw,h/ih)*scale
            elif kind=='WebPage':
                if props.get('mode')=='"fullBleed"':w,h=1920,1080
                factor=w/iw; sh=min(ih,h/factor)
            else:
                contain=props.get('fit')=='"contain"'; factor=(min if contain else max)(w/iw,h/ih)*scale
                if contain:w,h=iw*factor,ih*factor;scale=1
                else:sw=w/(factor/scale);sh=h/(factor/scale)
            inherited=''
            if name=='notes-beijing.jpg':
                # Same photograph: the mobile derivative cropped away the sky and inflated 550px to 1087px.
                inherited='550 × 366 origin; mobile crop already enlarged'
                sw,sh=sw*550/iw,sh*550/iw;factor*=iw/550
            ui=not (name.startswith(('notes-','xdoctor-cover','xdoctor-episode-art','xdoctor-video','discovery-','commute-','train-','listening-fieldnotes')))
            grade='SAFE' if factor<=1.25 else ('BORDERLINE' if factor<=1.5 else 'UNACCEPTABLE')
            rows.append(dict(shot=shot,chapter=used[shot]['chapter'],kind=kind,name=name,original=[iw,ih],origin=inherited,crop=[round(sw,1),round(sh,1)],display=[round(w*scale,1),round(h*scale,1)],factor=round(factor,4),ui=ui,grade=grade))
    return rows
fifth=audit('fifth');sixth=audit('sixth')
def table(rows):
    out=['| Shot / use | Source | Original px | Actual crop px | Display px (max) | Enlargement | UI/text | Gate |','|---|---|---:|---:|---:|---:|---|---|']
    fmt=lambda a:' × '.join(str(x) for x in a)
    for r in rows:out.append(f"| {r['shot']} / {r['kind']} | {r['name']} | {fmt(r['original'])}{'; '+r['origin'] if r['origin'] else ''} | {fmt(r['crop'])} | {fmt(r['display'])} | {r['factor']:.3f}× | {'yes' if r['ui'] else 'no / artwork-photo'} | {r['grade']} |")
    return '\n'.join(out)
counts=lambda rows:{g:sum(r['grade']==g for r in rows) for g in ['SAFE','BORDERLINE','UNACCEPTABLE']}
(AN/'sixth-resolution-audit.md').write_text('# Fifth source-resolution audit\n\n'+f"Audited {len(fifth)} rendered raster instances in all {len(shots)} Fifth shots. {counts(fifth)}. UI/text above 2×: {sum(r['ui'] and r['factor']>2 for r in fifth)}.\n\n"+'Actual crop accounts for `objectFit: cover`, explicit Crop boxes, WebPage viewport height, and Phone aspect ratio. Maxima conservatively evaluate all motion endpoints; hidden offscreen pixels do not excuse overscaling. Display bounds include the image before stage clipping. Unused inherited branches are excluded because they do not render. SAFE ≤1.25×; BORDERLINE >1.25–1.5×; UNACCEPTABLE >1.5×. SAFE is a sampling-budget result, not proof of intrinsic source sharpness.\n\n'+table(fifth)+'\n',encoding='utf-8')
fail=[r for r in sixth if (r['ui'] and r['factor']>1.25) or (not r['ui'] and r['factor']>1.5)]
(AN/'sixth-pixel-quality-audit.md').write_text('# Sixth pixel-quality gate\n\n'+f"{len(sixth)} rendered raster uses / {len(shots)} shots. {counts(sixth)}. UI/text >2×: {sum(r['ui'] and r['factor']>2 for r in sixth)}. Gate failures: {len(fail)}.\n\n"+'Automated hard gate: every rendered Crop, Picture, WebPage and Phone must use known source dimensions; every explicit Crop must remain inside its source bounds. UI/text ≤1.25×; artwork/photo ≤1.5×. No sharpening, AI enlargement, screenshot contrast gain, grain, or blur used to conceal pixels. The previous sticker brightness filter is removed. Native encode inspection is recorded separately in the review.\n\n'+table(sixth)+'\n',encoding='utf-8')
(AN/'sixth-research/raster-uses.json').write_text(json.dumps({'fifth':fifth,'sixth':sixth},indent=2),encoding='utf-8')
saved=json.loads((AN/'sixth-research/fifth-preservation.json').read_text(encoding='utf-8'))
assert all(hashlib.sha256((R/p).read_bytes()).hexdigest()==v for p,v in saved.items()),'Preserved input changed'
assert not fail,fail
assert {r['shot'] for r in sixth}.issubset(used)
print('Fifth',counts(fifth),'Sixth',counts(sixth),'all',len(saved),'preservation hashes match')
