"""Make motion checkpoint strips from rendered diagnostic clips."""
import subprocess
from pathlib import Path

import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
AN=ROOT/'analysis'
ff=imageio_ffmpeg.get_ffmpeg_exe()
for title in ('opening','player','discovery','notes','comments','ending'):
    path=AN/f'third-motion-{title}.mp4'
    if not path.exists(): continue
    fps=2 if title in ('opening','notes','comments') else 1.5
    raw=subprocess.run([ff,'-v','error','-i',str(path),'-vf',f'fps={fps},scale=320:180',
                        '-f','rawvideo','-pix_fmt','rgb24','pipe:1'],capture_output=True,check=True).stdout
    frames=np.frombuffer(raw,dtype=np.uint8).reshape(-1,180,320,3)
    rows=(len(frames)+7)//8
    sheet=Image.new('RGB',(2560,rows*205),'#e9eeee')
    draw=ImageDraw.Draw(sheet)
    for i,frame in enumerate(frames):
        x=(i%8)*320; y=(i//8)*205
        sheet.paste(Image.fromarray(frame),(x,y))
        draw.text((x+5,y+183),f'{i/fps:04.1f}s',fill='#111')
    sheet.save(AN/f'third-motion-{title}-strip.jpg',quality=89)
    print(title,len(frames))
