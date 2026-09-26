"""Native 1920x1080 paused frames from the final MP4, never upsampled sheets."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json,subprocess,html,hashlib
import imageio_ffmpeg
R=Path(__file__).resolve().parents[1]; D=R/'analysis/sixth-native';D.mkdir(exist_ok=True)
shots=json.loads((R/'src/shots-fifth.json').read_text(encoding='utf-8'));ff=imageio_ffmpeg.get_ffmpeg_exe()
def extract(s):
    t=max(s['startMs']/1000+.08,s['endMs']/1000-.16)
    p=D/(s['id']+'.png')
    subprocess.run([ff,'-v','error','-y','-ss',str(t),'-i',str(R/'out/little-universe-review-sixth-edit.mp4'),'-frames:v','1',str(p)],check=True)
    return {'shot':s['id'],'chapter':s['chapter'],'time':round(t,3),'frame':round(t*30),'file':str(p.relative_to(R)).replace('\\','/')}
with ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(extract,shots))
(D/'frames.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
buttons=''.join(f'<button data-index="{i}" onclick="seek({i})">{html.escape(v["shot"])}</button>' for i,v in enumerate(records))
page='''<!doctype html><meta charset="utf-8"><title>Sixth native 1080p QA</title>
<style>html,body{margin:0;overflow:hidden;background:#101820}video{display:block;width:1920px;height:1080px;object-fit:contain}nav{position:fixed;top:0;left:0;right:0;z-index:2;background:#fff9;display:flex;gap:8px;font:12px Arial;height:25px;align-items:center}button{font-size:12px}#list{display:none;position:fixed;z-index:3;top:25px;background:white;max-width:1000px}#list button{margin:3px}</style>
<video id="v" preload="auto" src="../out/little-universe-review-sixth-edit.mp4"></video>
<nav><button onclick="v.currentTime=0;v.play();document.querySelector('#list').style.display='none'">Play full master</button><button onclick="v.pause()">Pause</button><button onclick="document.querySelector('#list').style.display='block'">Shot list</button><button onclick="seek(Math.min(index+1,shots.length-1))">Next paused shot</button><span id="label">1920 × 1080 / native pixels</span></nav>
<div id="list">BUTTONS</div><script>const shots=RECORDS;const v=document.querySelector('#v');let index=-1;function seek(i){index=i;v.pause();v.currentTime=shots[i].time;document.querySelector('#label').textContent=shots[i].shot+' / '+shots[i].time+'s / native 1080p';document.querySelector('#list').style.display='none';}v.onended=()=>document.querySelector('#label').textContent='Ended / '+v.currentTime+'s / '+v.playbackRate+'x';</script>'''
(R/'analysis/sixth-native-review.html').write_text(page.replace('BUTTONS',buttons).replace('RECORDS',json.dumps(records)).replace('sixth-edit.mp4','sixth-edit.mp4?v='+hashlib.sha256((R/'out/little-universe-review-sixth-edit.mp4').read_bytes()).hexdigest()),encoding='utf-8')
print('Extracted',len(records),'native encoded frames; browser QA page created.')
