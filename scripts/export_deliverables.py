from pathlib import Path
import json, subprocess, wave, array
import imageio_ffmpeg

root=Path(__file__).resolve().parents[1]
out=root/'out'
out.mkdir(exist_ok=True)
ffmpeg=imageio_ffmpeg.get_ffmpeg_exe()
timing=json.loads((root/'src'/'timing.json').read_text(encoding='utf-8'))
captions=json.loads((root/'src'/'captions.json').read_text(encoding='utf-8'))
rate=24000
samples=array.array('h')
for beat in timing['beats']:
    path=root/'public'/'audio'/f"{beat['id']}.mp3"
    raw=subprocess.check_output([str(ffmpeg),'-v','error','-i',str(path),'-f','s16le','-ac','1','-ar',str(rate),'-'])
    part=array.array('h');part.frombytes(raw)
    samples.extend(part)
    expected=int((beat['startMs']+beat['durationMs']+500)/1000*rate)
    if len(samples)<expected:
        samples.extend([0]*(expected-len(samples)))
wav=out/'narration.wav'
with wave.open(str(wav),'wb') as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(rate);w.writeframes(samples.tobytes())
subprocess.run([str(ffmpeg),'-y','-i',str(wav),'-c:a','libmp3lame','-b:a','160k',str(out/'narration.mp3')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
wav.unlink()

def stamp(ms):
    n=int(ms)
    h,n=divmod(n,3600000);m,n=divmod(n,60000);s,n=divmod(n,1000)
    return f'{h:02}:{m:02}:{s:02},{n:03}'
srt='\n\n'.join(f"{i+1}\n{stamp(c['startMs'])} --> {stamp(c['endMs'])}\n{c['text']}" for i,c in enumerate(captions))+'\n'
(out/'captions.srt').write_text(srt,encoding='utf-8')
(out/'narration.md').write_text((root/'story'/'narration.md').read_text(encoding='utf-8'),encoding='utf-8')
print('Exported narration audio, script, and SRT')
