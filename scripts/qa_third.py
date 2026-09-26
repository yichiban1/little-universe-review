"""Inspect the delivered encode and regenerate review artifacts from that encode."""
import json
import subprocess
from pathlib import Path

import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
AN = ROOT / 'analysis'
OUT = ROOT / 'out'
VIDEO = OUT / 'little-universe-review-third-edit.mp4'
FF = imageio_ffmpeg.get_ffmpeg_exe()

def run(args):
    return subprocess.run([FF, *args], capture_output=True, check=True)

raw = run(['-v', 'error', '-i', str(VIDEO), '-vf', 'fps=1/2,scale=320:180',
           '-f', 'rawvideo', '-pix_fmt', 'rgb24', 'pipe:1']).stdout
frames = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 180, 320, 3)
for page, start in enumerate(range(0, len(frames), 24), 1):
    sheet = Image.new('RGB', (1920, 840), '#e9eeee')
    draw = ImageDraw.Draw(sheet)
    for offset, frame in enumerate(frames[start:start + 24]):
        x, y = offset % 6 * 320, offset // 6 * 210
        sheet.paste(Image.fromarray(frame), (x, y))
        draw.text((x + 8, y + 186), f'{(start + offset) * 2 + 1:05.1f}s', fill='#111')
    sheet.save(AN / f'third-edit-sheet-{page}.jpg', quality=92)

clips = {'opening': (0, 19.22), 'player': (19.22, 21.50),
         'discovery': (40.72, 20.53), 'notes': (72.69, 34.38),
         'comments': (107.07, 29.35), 'ending': (155.97, 22.98)}
for name, (start, length) in clips.items():
    run(['-v', 'error', '-y', '-ss', str(start), '-i', str(VIDEO), '-t', str(length),
         '-vf', 'scale=960:540', '-c:v', 'libx264', '-crf', '21', '-preset', 'fast',
         '-c:a', 'aac', '-b:a', '160k', str(AN / f'third-motion-{name}.mp4')])
    print('Review clip:', name, flush=True)

for time in [7.5, 17.8, 35.3, 79.5, 86.8, 88, 89.5, 95.5, 118.5, 122.5, 148, 175.5]:
    run(['-v', 'error', '-y', '-ss', str(time), '-i', str(VIDEO), '-frames:v', '1',
         str(AN / f'third-final-{time:.1f}s.jpg')])

raw = run(['-v', 'error', '-ss', '86.4', '-i', str(VIDEO), '-t', '10',
           '-vf', 'fps=6,scale=320:180', '-f', 'rawvideo', '-pix_fmt', 'rgb24', 'pipe:1']).stdout
detail = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 180, 320, 3)
sheet = Image.new('RGB', (2560, ((len(detail) + 7) // 8) * 205), '#e9eeee')
draw = ImageDraw.Draw(sheet)
for i, frame in enumerate(detail):
    x, y = i % 8 * 320, i // 8 * 205
    sheet.paste(Image.fromarray(frame), (x, y))
    draw.text((x + 6, y + 183), f'{86.4 + i / 6:.2f}s', fill='#111')
sheet.save(AN / 'third-notes-final-transition-6fps.jpg', quality=92)

stats = run(['-hide_banner', '-i', str(VIDEO), '-vn', '-af', 'volumedetect', '-f', 'null', '-'])
info = stats.stderr.decode('utf-8', errors='replace')
(AN / 'third-encode-audio-check.txt').write_text(info, encoding='utf-8')
print('\n'.join(line for line in info.splitlines() if any(key in line for key in
      ('Duration:', 'Video:', 'Audio:', 'mean_volume:', 'max_volume:'))))

captions = json.loads((ROOT / 'src/captions-third.json').read_text(encoding='utf-8'))
def timestamp(ms):
    ms = int(ms)
    return f'{ms // 3600000:02}:{ms // 60000 % 60:02}:{ms // 1000 % 60:02},{ms % 1000:03}'
(OUT / 'captions-third.srt').write_text('\n\n'.join(
    f'{i}\n{timestamp(c["startMs"])} --> {timestamp(c["endMs"])}\n{c["text"]}'
    for i, c in enumerate(captions, 1)) + '\n', encoding='utf-8')
print('Contact sheets:', (len(frames) + 23) // 24)
