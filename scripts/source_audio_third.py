"""Fetch verified CC0 recorded sound and music for the third edit."""
import subprocess
from pathlib import Path
import requests
import imageio_ffmpeg

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public/audio'
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
OUT.mkdir(parents=True, exist_ok=True)

MUSIC = 'https://files.freemusicarchive.org/storage-freemusicarchive-org/tracks/gpJhOdSsQGabjtoXYifAqHDHJqPQ52nAyTUyR8qt.mp3'
music = requests.get(MUSIC, timeout=60)
music.raise_for_status()
(OUT/'music-third-original.mp3').write_bytes(music.content)

for title, stem in [('File:Turning a page.ogg', 'page'), ('File:Clicker sound.ogg', 'click')]:
    item = 'https://commons.wikimedia.org/wiki/Special:Redirect/file/' + title.removeprefix('File:').replace(' ', '_')
    response = requests.get(item, timeout=30, headers={'User-Agent':'Mozilla/5.0'})
    response.raise_for_status()
    (OUT/f'sfx-third-{stem}-original.ogg').write_bytes(response.content)

# The source page turn lasts 3.4 s; use a short tactile part. The clicker has
# an accidental first noise, so trim to the main physical click and soften it.
subprocess.run([FFMPEG,'-y','-v','error','-ss','1.38','-t','1.03','-i',str(OUT/'sfx-third-page-original.ogg'),
                '-af','highpass=f=120,lowpass=f=6500,volume=8','-c:a','libmp3lame','-b:a','160k',
                str(OUT/'sfx-third-page.mp3')], check=True)
subprocess.run([FFMPEG,'-y','-v','error','-ss','0.84','-t','0.35','-i',str(OUT/'sfx-third-click-original.ogg'),
                '-af','highpass=f=130,lowpass=f=5000,volume=1.2','-c:a','libmp3lame','-b:a','160k',
                str(OUT/'sfx-third-click.mp3')], check=True)
print('music',len(music.content),'page', (OUT/'sfx-third-page.mp3').stat().st_size,
      'click',(OUT/'sfx-third-click.mp3').stat().st_size)
