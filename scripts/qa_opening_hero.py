from pathlib import Path
import subprocess,json,hashlib
import imageio_ffmpeg
import numpy as np
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1];A=R/'analysis';FF=imageio_ffmpeg.get_ffmpeg_exe()
def run(args):
 p=subprocess.run([FF,*map(str,args)],capture_output=True)
 if p.returncode:raise RuntimeError(p.stderr.decode(errors='replace'))
 return p.stdout

def sheet(video,dest,first,last,step=1):
 raw=run(['-v','error','-i',video,'-vf',f'select=between(n\\,{first}\\,{last})*not(mod(n-{first}\\,{step})),scale=320:180','-fps_mode','vfr','-f','rawvideo','-pix_fmt','rgb24','pipe:1'])
 frames=np.frombuffer(raw,dtype=np.uint8).reshape(-1,180,320,3)
 im=Image.new('RGB',(1920,((len(frames)+5)//6)*202),'#e9eeee');d=ImageDraw.Draw(im)
 for i,f in enumerate(frames):
  x=i%6*320;y=i//6*202;im.paste(Image.fromarray(f),(x,y));d.text((x+6,y+183),f'f{first+i*step:03d} {(first+i*step)/30:.3f}s',fill='#111')
 im.save(dest,quality=94)

def main():
 old=A/'opening-hero-baseline.mp4';new=A/'opening-hero-preview.mp4'
 run(['-v','error','-y','-i',old,'-i',new,'-filter_complex','[0:v]scale=960:540[a];[1:v]scale=960:540[b];[a][b]hstack=inputs=2[v]','-map','[v]','-map','0:a','-c:v','libx264','-crf',18,'-c:a','copy',A/'opening-hero-comparison.mp4'])
 sheet(new,A/'opening-hero-strip.jpg',0,576,15)
 for name,first,last in [('xdoctor-search',180,225),('search-2008',235,272),('2008-phone',300,345),('phone-surfaces',430,523),('title-reveal',526,570)]:
  sheet(new,A/f'opening-hero-framebyframe-{name}.jpg',first,last)
 probe=R/'node_modules/@remotion/compositor-win32-x64-msvc/ffprobe.exe'
 meta={name:json.loads(subprocess.check_output([str(probe),'-v','error','-show_entries','stream=width,height,nb_frames,r_frame_rate','-show_entries','format=duration,size','-of','json',str(path)])) for name,path in [('baseline',old),('preview',new)]}
 for value in meta.values():
  v=value['streams'][0];assert (v['width'],v['height'],v['nb_frames'],v['r_frame_rate'])==(1920,1080,'577','30/1'),v
 audio={name:run(['-v','error','-i',path,'-map','0:a:0','-c','copy','-f','md5','-']).decode().strip() for name,path in [('baseline',old),('preview',new)]}
 assert audio['baseline']==audio['preview'],audio
 for path in [old,new,A/'opening-hero-comparison.mp4']:run(['-v','error','-i',path,'-f','null','-'])
 # Original tracked files may differ in checkout newline only. No original source edit allowed.
 baseline=R.parent/'little-universe-review'
 files=subprocess.check_output(['git','ls-files','-z'],cwd=baseline).decode().split('\0')[:-1]
 preserve={};diff=[];text_ext={'.md','.json','.tsx','.ts','.css','.py','.mjs','.cjs','.txt','.html','.srt'}
 for name in files:
  original=(baseline/name).read_bytes();preserve[name]=hashlib.sha256(original).hexdigest()
  other=(R/name).read_bytes()
  if name=='src/Composition.tsx':continue
  if original!=other:
   if Path(name).suffix in text_ext or name in ['.gitignore','.prettierrc']:
    if original.replace(b'\r\n',b'\n')==other.replace(b'\r\n',b'\n'):continue
   diff.append(name)
 assert not diff,diff
 master=baseline.parent/'little-universe-review-hero-polish-edit.mp4'
 preserve[str(master)]=hashlib.sha256(master.read_bytes()).hexdigest()
 (A/'opening-hero-original-hashes.json').write_text(json.dumps(preserve,indent=2),encoding='utf-8')
 (A/'opening-hero-technical-qa.json').write_text(json.dumps({'metadata':meta,'audioPayloadMD5':audio,'decode':'passed','protectedOriginalFiles':len(preserve),'crossCheckoutChangedExceptComposition':diff,'frameBoundary':577,'totalCompositionFrames':5520,'noNewAssets':True},indent=2),encoding='utf-8')
 print('A/B, five every-frame strips, audio identity, decode and original-source preservation passed',flush=True)
if __name__=='__main__':main()
