from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,json,hashlib,shutil
import imageio_ffmpeg,numpy as np
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];A=R/'analysis';D=A/'hero-native';D.mkdir(exist_ok=True)
FF=imageio_ffmpeg.get_ffmpeg_exe();V=R/'out/little-universe-review-hero-edit.mp4'
def run(args):return subprocess.run([FF,*args],capture_output=True,check=True)
targets=[21.9,21.933,22.2,22.75,23.633,24.2,24.9,27.533,27.9,28.45,31.7,31.933,32.4,32.9,33.133,33.9,34.033,46.367,47.067,48.367,48.9,49.567,52.133,52.6,53.2,55.567,56.067,56.5,57.5,57.9,58.433,59.233,59.267,159.433,161.767,163.533,168.5]
def extract(t):
 n=round(t*30);p=D/f'f{n:04}.png'
 run(['-v','error','-y','-ss',str(n/30),'-i',str(V),'-frames:v','1',str(p)])
 return {'frame':n,'time':n/30,'file':p.name,'size':Image.open(p).size}
with ThreadPoolExecutor(max_workers=4) as pool: records=list(pool.map(extract,targets))
(D/'frames.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
windows=[('player-expand',21.9,22.8),('player-reduce',23.6,24.933),('player-page',27.3,28.5),('player-return',31.7,33.133),('discovery-detach',48.3,49.633),('discovery-browse',52.067,53.267),('discovery-branch',55.5,56.567),('discovery-episode',57.467,58.5)]
for name,start,end in windows:
 raw=run(['-v','error','-ss',str(start),'-i',str(V),'-t',str(end-start),'-vf','scale=320:180','-f','rawvideo','-pix_fmt','rgb24','pipe:1']).stdout
 frames=np.frombuffer(raw,dtype=np.uint8).reshape(-1,180,320,3)
 sheet=Image.new('RGB',(1920,((len(frames)+5)//6)*202),'#e9eeee');d=ImageDraw.Draw(sheet)
 for i,im in enumerate(frames):
  x=i%6*320;y=i//6*202;sheet.paste(Image.fromarray(im),(x,y));d.text((x+6,y+183),f'{start+i/30:.3f}s',fill='#111')
 sheet.save(A/f'hero-framebyframe-{name}.jpg',quality=94)
audio={}
for name in ['sixth','hero']:
 path=R/f'out/little-universe-review-{name}-edit.mp4'
 audio[name]=run(['-v','error','-i',str(path),'-map','0:a:0','-c','copy','-f','md5','-']).stdout.decode().strip()
assert audio['sixth']==audio['hero'],audio
decode=run(['-v','error','-i',str(V),'-f','null','-'])
assert not decode.stderr,decode.stderr
shutil.copyfile(R/'out/captions-sixth.srt',R/'out/captions-hero.srt')
probe=R/'node_modules/@remotion/compositor-win32-x64-msvc/ffprobe.exe'
meta=json.loads(subprocess.run([str(probe),'-v','error','-show_entries','stream=width,height,nb_frames,r_frame_rate','-show_entries','format=duration,size','-of','json',str(V)],capture_output=True,check=True).stdout)
assert meta['streams'][0]['nb_frames']=='5520',meta
assert meta['streams'][0]['width']==1920 and meta['streams'][0]['height']==1080,meta
result={'nativeFrames':len(records),'nativeSize':[1920,1080],'metadata':meta,'audioPayloadMD5':audio,'fullDecode':'passed','masterSHA256':hashlib.sha256(V.read_bytes()).hexdigest(),'captionsByteIdentical':True}
(A/'hero-technical-qa.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
