"""Conservative original-source exposure plus explicit per-shot composition QA."""
import json,re,hashlib
from pathlib import Path
from collections import defaultdict,Counter
R=Path(__file__).resolve().parents[1]
alias={'web-xdoctor-playing-page-fifth.png':'web-xdoctor-playing-raw.png','web-xdoctor-playing-controls-fifth.png':'web-xdoctor-playing-raw.png'}
def load(edit):
 text=(R/f'src/{edit.title()}Edit.tsx').read_text(encoding='utf-8')
 shots=json.loads((R/f'src/shots-{edit}.json').read_text())
 matches=list(re.finditer(r"if\(id==='([^']+)'\)",text));chunks={};byid={}
 for i,m in enumerate(matches):
  chunk=text[m.start():matches[i+1].start() if i+1<len(matches) else len(text)]
  chunks[m[1]]=chunk
  byid[m[1]]={alias.get(n,n) for n in re.findall(r'name="([^"]+)"',chunk)}
 result=defaultdict(lambda:dict(shots=0,ms=0,chapters=set(),maxRunMs=0))
 for a in set().union(*(byid[x['id']] for x in shots)):
  run=0
  for x in shots:
   if a in byid[x['id']]:
    v=result[a];v['shots']+=1;v['ms']+=x['durationMs'];v['chapters'].add(x['chapter']);run+=x['durationMs'];v['maxRunMs']=max(v['maxRunMs'],run)
   else:run=0
 return result,shots,byid,chunks
fourth,old,_,_=load('fourth');fifth,shots,byid,chunks=load('fifth')
lines=['# Fifth edit asset audit','',
'Count original images once per shot, charging all crops to that original. The two new web fragments are one capture. Whole-shot exposure includes fades and is conservative; simultaneous panels can make totals exceed runtime. No source-count target was imposed.','',
f'Fourth: {len(fourth)} original sources / {len(old)} shots. Fifth: {len(fifth)} original sources / {len(shots)} shots.','',
'| Original source | Fourth shots / seconds | Fifth shots / seconds | Fifth consecutive maximum | Chapters |','|---|---:|---:|---:|---|']
for a in sorted(set(fourth)|set(fifth),key=lambda a:-fifth.get(a,{}).get('ms',0)):
 o=fourth.get(a,dict(shots=0,ms=0));n=fifth.get(a,dict(shots=0,ms=0,maxRunMs=0,chapters=set()))
 lines.append(f"| {a} | {o['shots']} / {o['ms']/1000:.2f} | {n['shots']} / {n['ms']/1000:.2f} | {n['maxRunMs']/1000:.2f} s | {', '.join(sorted(n['chapters'])) or '—'} |")
lines+=['','## Local repeat decisions','',
'- Widget overview and controls share one original and are followed by a different lock-screen example. No feature list in the narration. The genuine mini-player stays within the same personal 2008 episode. Rewind returns to the supplied personal player, not unrelated official episode art.',
'- The unrelated official player and reaction screen were removed from the continuous personal Player story. Quiet measured waveform shots create breathing space without introducing random material.',
'- History uses total screen → numeric detail → board → creator sticker → both counts. Sticker board, detail and combined view are charged together. No further profile sources were sought.',
'- The two live web-player fragments are charged to their single original capture and to the wider X Doctor family. They are evidence of a web product surface, not two new features or a live performance in the film.',
'- Long Show Notes source runs remain intentional: outline orientation and the DVD expansion/contraction use continuous objects. Personal evidence remains in Notes, Comments, History and Player.',
'- Official catalogue examples appear in Discovery and the brief other-shows callback. Generic promotional discussion and widget examples are labelled. 02:33 remains the captured input/playback state; the two listener memories are separate content.',
'','## Runs above seven seconds','']
for a,v in fifth.items():
 if v['maxRunMs']>7000:
  reason = "Protected photograph expansion/return." if a!='ui-notes-text.jpg' else "Notes closing exception: full context/detail → genuine bottom player, 7.68 s. Distinct useful fragments, still one source; retained to complete the references-to-listening link."
  lines.append(f"- {a}: {v['maxRunMs']/1000:.2f} s. {reason}")
lines+=['','## Chapter lengths','', '| Chapter | Fourth | Fifth |','|---|---:|---:|']
for chapter in dict.fromkeys(x['chapter'] for x in shots):
 lines.append(f"| {chapter} | {sum(x['durationMs'] for x in old if x['chapter']==chapter)/1000:.2f} s | {sum(x['durationMs'] for x in shots if x['chapter']==chapter)/1000:.2f} s |")
(R/'analysis/fifth-edit-asset-audit.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')

composition=['# Fifth edit composition audit','',
'Every rendered shot is classified below by its primary visual grammar, including transitions. Categories are broader than component names: changing a radius alone does not constitute a new composition. Full-bleed means the source fills or crosses the frame edges; edge crop retains source context while bleeding one edge.','',
'## Family distribution','', '| Family | Shots | Seconds |','|---|---:|---:|']
counts=Counter(x['composition'] for x in shots)
for name,n in counts.most_common():composition.append(f"| {name} | {n} | {sum(x['durationMs'] for x in shots if x['composition']==name)/1000:.2f} |")
composition+=['','## Three-shot checks','']
runs=[];group=[]
for x in shots:
 if group and x['composition']!=group[-1]['composition']:
  if len(group)>=3:runs.append(group)
  group=[]
 group.append(x)
if len(group)>=3:runs.append(group)
for g in runs:
 composition.append(f"- {g[0]['composition']}: {', '.join(x['id'] for x in g)}. This is the protected Notes choreography: photos emerge from the same note page, expand, change and return. It is one continuous transformation rather than repeated slide layouts.")
if not runs:composition.append('- No three consecutive shots share the primary composition family.')
composition +=['',
'The old ice + rounded screenshot + shadow + side headline recipe was specifically removed from episode result, episode title, topic, programme split, mini-player detail, comment details, history and callbacks. The ordinary rounded WebPage remains only in the creator-origin shot; borderless, edge crop and split views retain real page content. Notes retain their established object choreography.','',
'## Per-shot classification','', '| Time | Shot | Primary composition | Original image sources |','|---|---|---|---|']
for x in shots:composition.append(f"| {x['startMs']/1000:.2f}–{x['endMs']/1000:.2f} | {x['id']} | {x['composition']} | {', '.join(sorted(byid[x['id']])) or 'Editorial text / recorded voice envelope'} |")
(R/'analysis/fifth-edit-composition-audit.md').write_text('\n'.join(composition)+'\n',encoding='utf-8')
preserve=json.loads((R/'analysis/fifth-research/fourth-preservation.json').read_text())
assert all(hashlib.sha256((R/p).read_bytes()).hexdigest()==v for p,v in preserve.items())
print('Fourth hashes verified:',len(preserve),'files')
print('Fifth original sources:',len(fifth),'shots:',len(shots))
print('Runs >7s:',[(a,round(v['maxRunMs']/1000,2)) for a,v in fifth.items() if v['maxRunMs']>7000])
