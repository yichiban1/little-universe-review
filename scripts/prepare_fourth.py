"""Prepare browser evidence, separate fourth-edit narration, and preserve hashes."""
import json, hashlib, shutil
from pathlib import Path
from PIL import Image, ImageDraw
import fitz

ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'public/assets'
R=ROOT/'analysis/fourth-research'
R.mkdir(exist_ok=True)
if (R/'third-preservation.json').exists():
    raise SystemExit('Acquisition is already archived. Use build_fourth.py to rebuild; do not overwrite original captures or preservation hashes.')
preserve=['src/ThirdEdit.tsx','src/ThirdFilm.tsx','src/shots-third.json','src/timing-third.json','public/audio/narration-third.mp3','out/little-universe-review-third-edit.mp4']
(R/'third-preservation.json').write_text(json.dumps({p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in preserve},indent=2))
for p in A.glob('web-*.png'):
    shutil.copy2(p,R/p.name)
    im=Image.open(p)
    if p.name=='web-home-fourth.png' or p.name=='web-xdoctor-outline.png': continue
    if p.name=='web-xdoctor-discussion-raw.png':
        draw=ImageDraw.Draw(im)
        masks=json.loads((ROOT/'analysis/fourth-discussion-masks.json').read_text())
        for m in masks:
            r=m['r']
            if m.get('href') and '/user/' in m['href'] or (m['tag']=='IMG' and r['w']<60):
                draw.rectangle((r['x']-2,r['y']-2,r['x']+r['w']+2,r['y']+r['h']+2),fill='#d6dadd')
        # Also omit inline reply names, preserving main listener texts.
        for box in [(258,150,755,249),(258,494,756,526)]: draw.rectangle(box,fill='#f1f2f3')
        im.crop((202,66,774,844)).save(A/'web-xdoctor-discussion.png')
    elif 'programme' in p.name:
        im.crop((202,105,774,875)).save(p)
    elif 'topic' in p.name:
        im.crop((202,105,774,880)).save(p)
    else:
        # Retain app masthead, artwork, episode title and notes introduction;
        # omit public commenter identities below the collapsed notes.
        end={'web-xdoctor-2008.png':620,'web-ritan-episode.png':590,'web-stochastic-episode.png':625,'web-sound-episode.png':640}[p.name]
        im.crop((202,46,774,end)).save(p)

d=fitz.open(ROOT/'analysis/official-logo-fourth/colored_xyz_logo_rgb.ai')
pix=d[0].get_pixmap(matrix=fitz.Matrix(3,3),alpha=True)
pix.save(A/'official-wordmark-fourth.png')
im=Image.open(A/'official-wordmark-fourth.png')
im.crop(im.getbbox()).save(A/'official-wordmark-fourth.png')

beats=json.loads((ROOT/'story/beats-third-edit.json').read_text())
replacement={
'discovery':"After X Doctor, I started following topics, then other shows. I'd finish an episode and search for something it mentioned. Sometimes I browse a programme's older episodes. Sometimes I just pick something from the discovery page. One episode mentioned Daqing, where I grew up. I wasn't looking for that. It just made me stop for a second.",
'listening':"Most of the time, the phone is back in my pocket anyway. There are ways back in without opening the full player. Little Universe's home-screen widgets have pause and rewind controls. The lock-screen widgets show episode shortcuts, too. Inside the app, a small player stays at the bottom while I browse. The conversation keeps going. If I miss a detail, I can go back fifteen seconds and catch it again.",
'comments':"And the conversation doesn't end with the hosts. I was at two minutes thirty-three when I took this screenshot. From the episode page, I can open the discussion, and the comment box keeps that playback time beside it. Here, one listener writes about being a student in 2008. Another remembers the earthquake in Chengdu. I'll read a few, go back, and keep listening. Those memories stay with me for the rest of the episode.",
'history':"My profile says I've listened for 128 hours and 27 minutes altogether. There are stickers too. This one marks a hundred hours with a single creator, which is a different count. I like seeing it on my profile. It reminds me which voices I've spent time with.",
'ending':"I still use other apps. Little Universe is where I go for the Chinese podcasts I follow. I came here for X Doctor. Now I come back for other shows, the photos in the notes, and the people in the discussion. When someone sends me an episode, this is usually where I open it."
}
for b in beats:
    b['text']=replacement.get(b['id'],b['text'])
    b.pop('startMs',None); b.pop('endMs',None)
(ROOT/'story/beats-fourth-edit.json').write_text(json.dumps(beats,indent=2),encoding='utf-8')
(ROOT/'story/narration-fourth-edit.md').write_text('# Fourth edit narration\n\n'+'\n\n'.join(b['text'] for b in beats)+'\n',encoding='utf-8')
src=(ROOT/'scripts/generate_voice_third.py').read_text()
src=src.replace('third','fourth').replace('from captions_fourth import','from captions_third import')
a=src.index("    for voice, slug in")
z=src.index('    # Andrew',a)
src=src[:a]+src[z:]
src=src.replace('info.length*1000+1250','info.length*1000+3300')
(ROOT/'scripts/generate_voice_fourth.py').write_text(src,encoding='utf-8')
(ROOT/'scripts/analyze_voice_fourth.py').write_text((ROOT/'scripts/analyze_voice_third.py').read_text().replace('third','fourth'),encoding='utf-8')
print('Fourth script words',sum(len(b['text'].split()) for b in beats))
print('Prepared 12 source views + official wordmark; third preservation recorded')
