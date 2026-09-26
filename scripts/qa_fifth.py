"""Review artifacts from an actual encode; no composition screenshots substituted."""
import sys,json,subprocess,hashlib
from pathlib import Path
import imageio_ffmpeg,numpy as np
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1];AN=ROOT/'analysis'
VIDEO=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'out/little-universe-review-fifth-edit.mp4')
PREFIX='fifth' if len(sys.argv)<3 else sys.argv[2]
FF=imageio_ffmpeg.get_ffmpeg_exe()
def run(args):return subprocess.run([FF,*args],capture_output=True,check=True)
def frames(path,fps=0.5,width=320):
    height=width*9//16
    raw=run(['-v','error','-i',str(path),'-vf',f'fps={fps},scale={width}:{height}','-f','rawvideo','-pix_fmt','rgb24','pipe:1']).stdout
    return np.frombuffer(raw,dtype=np.uint8).reshape(-1,height,width,3)
fr=frames(VIDEO)
for page,start in enumerate(range(0,len(fr),24),1):
    sheet=Image.new('RGB',(1920,840),'#e9eeee');draw=ImageDraw.Draw(sheet)
    for i,f in enumerate(fr[start:start+24]):
        x=i%6*320;y=i//6*210;sheet.paste(Image.fromarray(f),(x,y))
        draw.text((x+8,y+186),f'{(start+i)*2+1:05.1f}s',fill='#111')
    sheet.save(AN/f'{PREFIX}-edit-sheet-{page}.jpg',quality=93)
shots=json.loads((ROOT/'src/shots-fifth.json').read_text())
for chapter in ['opening','player','discovery','listening','notes','comments','history','critical','ending']:
    group=[s for s in shots if s['chapter']==chapter]
    start=group[0]['startMs']/1000;length=(group[-1]['endMs']-group[0]['startMs'])/1000
    clip=AN/f'{PREFIX}-motion-{chapter}.mp4'
    run(['-v','error','-y','-ss',str(start),'-i',str(VIDEO),'-t',str(length),'-vf','scale=960:540','-c:v','libx264','-crf','20','-preset','fast','-c:a','aac','-b:a','160k',str(clip)])
    frs=frames(clip,fps=2)
    sheet=Image.new('RGB',(1920,((len(frs)+5)//6)*205),'#e9eeee');draw=ImageDraw.Draw(sheet)
    for i,f in enumerate(frs):
        x=i%6*320;y=i//6*205;sheet.paste(Image.fromarray(f),(x,y));draw.text((x+6,y+184),f'{start+i/2:.2f}s',fill='#111')
    sheet.save(AN/f'{PREFIX}-motion-{chapter}-strip.jpg',quality=91)
    print(chapter,round(start,2),round(length,2),flush=True)
stats=run(['-hide_banner','-i',str(VIDEO),'-vn','-af','volumedetect','-f','null','-'])
info=stats.stderr.decode('utf-8',errors='replace')
(AN/f'{PREFIX}-encode-audio-check.txt').write_text(info,encoding='utf-8')
print('\n'.join(line for line in info.splitlines() if any(k in line for k in ['Duration:','Video:','Audio:','mean_volume:','max_volume:'])))
captions=json.loads((ROOT/'src/captions-fifth.json').read_text())
def stamp(ms):
    ms=int(ms);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(ROOT/'out/captions-fifth.srt').write_text('\n\n'.join(f'{i}\n{stamp(c["startMs"])} --> {stamp(c["endMs"])}\n{c["text"]}' for i,c in enumerate(captions,1))+'\n',encoding='utf-8')
saved=json.loads((AN/'fifth-research/fourth-preservation.json').read_text())
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==v for p,v in saved.items()),'Fourth changed'
print('Fourth source/assets/audio/export hashes unchanged')
