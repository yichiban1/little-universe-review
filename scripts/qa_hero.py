"""Only writes hero artifacts. Sixth assets and QA stay read-only."""
from pathlib import Path
import subprocess,json,hashlib,re
import imageio_ffmpeg,numpy as np
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1]; A=R/'analysis'; FF=imageio_ffmpeg.get_ffmpeg_exe()
segments={'player':(657,1020),'discovery':(1391,1777),'critical':(4652,5058)}
def run(args):return subprocess.run([FF,*args],capture_output=True,check=True).stdout
def strip(path,target,start):
 raw=run(['-v','error','-i',str(path),'-vf',r'select=not(mod(n\,15)),scale=320:180','-fps_mode','vfr','-f','rawvideo','-pix_fmt','rgb24','pipe:1'])
 frames=np.frombuffer(raw,dtype=np.uint8).reshape(-1,180,320,3)
 sheet=Image.new('RGB',(1920,((len(frames)+5)//6)*205),'#e9eeee'); d=ImageDraw.Draw(sheet)
 for i,f in enumerate(frames):
  x=i%6*320;y=i//6*205;sheet.paste(Image.fromarray(f),(x,y));d.text((x+6,y+184),f'{start+i/2:.3f}s',fill='#111')
 sheet.save(target,quality=93)
for name,(first,last) in segments.items():
 hero=A/f'hero-{name}-preview.mp4';old=A/f'hero-sixth-{name}-preview.mp4'
 master=R/'out/little-universe-review-hero-edit.mp4'
 if master.exists():
  run(['-v','error','-y','-ss',str(first/30),'-i',str(master),'-t',str((last-first+1)/30),'-c:v','libx264','-crf','16','-c:a','aac',str(hero)])
 run(['-v','error','-y','-ss',str(first/30),'-i',str(R/'out/little-universe-review-sixth-edit.mp4'),'-t',str((last-first+1)/30),'-c:v','libx264','-crf','16','-c:a','aac',str(old)])
 strip(hero,A/f'hero-{name}-strip.jpg',first/30)
 strip(old,A/f'hero-sixth-{name}-strip.jpg',first/30)
 run(['-v','error','-y','-i',str(old),'-i',str(hero),'-filter_complex','[0:v]scale=960:540[a];[1:v]scale=960:540[b];[a][b]hstack=inputs=2[v]','-map','[v]','-map','1:a','-c:v','libx264','-crf','18',str(A/f'hero-{name}-comparison.mp4')])
 print(name,'strips and Sixth-left / Hero-right comparison',flush=True)
strip(A/'hero-critical-experiment.mp4',A/'hero-critical-experiment-strip.jpg',4652/30)
saved=json.loads((A/'hero-preservation.json').read_text(encoding='utf-8'))
changed=[p for p,v in saved.items() if hashlib.sha256((R/p).read_bytes()).hexdigest()!=v]
assert changed==['src/Composition.tsx'],changed
(A/'hero-preservation-result.json').write_text(json.dumps({'files':len(saved),'onlyChanged':'src/Composition.tsx','sixthUnchanged':True},indent=2),encoding='utf-8')
print('Preservation verified:',len(saved),'files; only Hero registration changed')
page=A/'hero-review.html';master=R/'out/little-universe-review-hero-edit.mp4'
if page.exists() and master.exists():
 revision=hashlib.sha256(master.read_bytes()).hexdigest()[:16]
 page.write_text(re.sub(r"const revision='[^']+'",f"const revision='{revision}'",page.read_text(encoding='utf-8')),encoding='utf-8')
