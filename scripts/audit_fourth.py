"""Shot-level source exposure, counting crops under their original image."""
import json,re
from pathlib import Path
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]
def audit(edit):
    text=(ROOT/f'src/{edit.title()}Edit.tsx').read_text(encoding='utf-8')
    shots=json.loads((ROOT/f'src/shots-{edit}.json').read_text())
    matches=list(re.finditer(r"if\(id==='([^']+)'\)",text));byid={}
    for i,m in enumerate(matches):
        chunk=text[m.start():matches[i+1].start() if i+1<len(matches) else len(text)]
        byid[m[1]]=set(re.findall(r'name="([^"]+)"',chunk))
    results=defaultdict(lambda:dict(shots=0,ms=0,chapters=set(),maxRunMs=0))
    for asset in set().union(*byid.values()):
        run=0
        for s in shots:
            if asset in byid.get(s['id'],set()):
                r=results[asset];r['shots']+=1;r['ms']+=s['durationMs'];r['chapters'].add(s['chapter'])
                run+=s['durationMs'];r['maxRunMs']=max(r['maxRunMs'],run)
            else:run=0
    return results,shots,byid
third,_,_=audit('third');fourth,shots,byid=audit('fourth')
out=['# Fourth edit source-usage audit','',
'Method: count each original image at most once per shot. Every crop is charged to that image. Approximate screen time includes the entire shot even when a transition fades a panel, so it is a conservative exposure estimate. Multi-image exposure totals can exceed runtime. Counts are of rendered shot definitions, not raw string references in the component. Captures of different states of the same episode are also grouped below; they are not independent feature evidence.','',
f'Third: {len(third)} used image sources, 58 shots, 178.95 s. Fourth: {len(fourth)} used image sources, {len(shots)} shots, 185.00 s.','',
'| Original source | Third shots / seconds | Fourth shots / seconds | Fourth chapters | Longest consecutive fourth exposure |','|---|---:|---:|---|---:|']
for a in sorted(set(third)|set(fourth),key=lambda a:-fourth.get(a,{}).get('ms',0)):
    t=third.get(a,dict(shots=0,ms=0));f=fourth.get(a,dict(shots=0,ms=0,chapters=set(),maxRunMs=0))
    out.append(f"| {a} | {t['shots']} / {t['ms']/1000:.2f} | {f['shots']} / {f['ms']/1000:.2f} | {', '.join(sorted(f['chapters'])) or '—'} | {f['maxRunMs']/1000:.2f} s |")
out += ['','## Dominance and family check','']
for a in ['ui-player.jpg','ui-comments-redacted.jpg','ui-notes-photos.jpg','ui-notes-text.jpg']:
    t=third[a];f=fourth[a];out.append(f"- {a}: {t['shots']} → {f['shots']} shots; {t['ms']/1000:.2f} → {f['ms']/1000:.2f} s.")
families={'X Doctor supplied player + public programme/episode/discussion':['ui-player.jpg','web-xdoctor-programme.png','web-xdoctor-2008.png','web-xdoctor-discussion.png'],
'2008 Show Notes UI and photographs':['ui-notes-text.jpg','ui-notes-photos.jpg','notes-beijing.jpg','notes-dvd.jpg','notes-stadium.png','notes-dorm.png'],
'Personal profile/history/sticker evidence':['ui-listening-hours.jpg','ui-stickers.jpg']}
for family,assets in families.items():
    duration=sum(s['durationMs'] for s in shots if set(assets)&byid[s['id']])
    out.append(f'- Family union, {family}: {duration/1000:.2f} s (simultaneous panels counted once).')
out += ['','## Editorial decisions','',
'- Player is still dominant in its own chapter, with web episode-title context and two different official player examples breaking the long run. It is removed from discovery and listening. Its opening / return uses are deliberate callbacks.',
'- Listening now has widget gallery / widget controls, lock-screen shortcuts, the supplied full notes page with its genuine bottom player, a mini-player detail, then widget rewind. The full notes page and its crop count as one source. Gallery crops still count as appstore-1.jpg; they are not new sources. The official feed was rejected here because it does not contain a mini-player.',
'- Comments move from official feature context to the real episode + personal 02:33, public thread, supplied input, public first listener, supplied second listener and player return. Both comments describe the same episode; public/mobile variation is visual diversity, not new testimony.',
'- Show Notes remains intentionally one episode and retains its object transitions. The long factual context is justified by separate outline, stadium, dormitory, Olympics and DVD imagery.',
'- No authentic current extra personal-history interface was available. History is 16.93 s, down from 19.56 s; it is still the least diverse chapter. Total and creator-specific time remain separate.',
'- Ending visual recap is 12.99 s, then identity 5.39 s. The final icon hold includes the last spoken sentence and the brief music resolve.',
'- The Daqing observation has no external episode artwork, because the exact episode is unverified.',
'- Public web sources, official promotional surfaces and personal screenshots are separate provenance tiers. A higher file count alone is not the acceptance criterion.']
(ROOT/'analysis/fourth-edit-asset-audit.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
print(out[4]);print('player',third['ui-player.jpg'],fourth['ui-player.jpg'])
