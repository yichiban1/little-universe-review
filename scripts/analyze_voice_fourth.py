"""Precompute a 30 Hz RMS envelope from the actual narration recording."""
import json
import subprocess
from pathlib import Path

import imageio_ffmpeg
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
raw = subprocess.run([ffmpeg,'-v','error','-i',str(ROOT/'public/audio/narration-fourth.mp3'),
                      '-f','f32le','-ac','1','-ar','24000','pipe:1'],capture_output=True,check=True).stdout
pcm = np.frombuffer(raw, dtype='<f4')
samples_per_frame = 800
envelope = []
for pos in range(0,len(pcm),samples_per_frame):
    window = pcm[pos:pos+samples_per_frame]
    envelope.append(float(np.sqrt(np.mean(window*window))) if len(window) else 0)
ceiling = float(np.quantile(envelope,.96)) or 1
levels = [round(min(1, (v/ceiling)**.64),3) for v in envelope]
(ROOT/'src/voice-envelope-fourth.json').write_text(json.dumps(levels),encoding='utf-8')
print(len(levels),'frames','median',np.median(levels),'peak',max(levels))
