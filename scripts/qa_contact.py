"""Extract every two seconds and make readable four-page contact sheets."""
from pathlib import Path
import json, subprocess, time
import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

root=Path(__file__).resolve().parents[1]
src=root/'out'/'little-universe-review-second-edit.mp4'
folder=root/'analysis'/'second-edit-frames'
folder.mkdir(parents=True,exist_ok=True)
ffmpeg=imageio_ffmpeg.get_ffmpeg_exe()
started=time.time()
subprocess.run([ffmpeg,'-y','-i',str(src),'-vf','fps=1/2,scale=480:270',
                '-q:v','3',str(folder/'frame-%03d.jpg')],check=True,
               stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
duration=json.loads((root/'src'/'timing.json').read_text(encoding='utf-8'))['durationMs']
files=[p for p in sorted(folder.glob('frame-*.jpg')) if p.stat().st_mtime >= started-2]
if duration/1000-(len(files)-1)*2 > 1.5:
    final=folder/'frame-final.jpg'
    subprocess.run([ffmpeg,'-y','-ss',str((duration-800)/1000),'-i',str(src),
                    '-frames:v','1','-vf','scale=480:270','-q:v','3',str(final)],
                   check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    files.append(final)
font=ImageFont.truetype('arial.ttf',19)
for page in range((len(files)+23)//24):
    chosen=files[page*24:(page+1)*24]
    sheet=Image.new('RGB',(4*480,6*300),'#e9ece8')
    draw=ImageDraw.Draw(sheet)
    for i,path in enumerate(chosen):
        x=(i%4)*480;y=(i//4)*300
        with Image.open(path) as frame:
            sheet.paste(frame,(x,y))
        draw.text((x+8,y+272),f'{(page*24+i)*2:03d}s',fill='#172820',font=font)
    sheet.save(root/'analysis'/f'second-edit-sheet-{page+1}.jpg',quality=89)
print(len(files),'two-second frames,',page+1,'sheets')
