"""Read frozen Hero; write only hero-polish artifacts. No Sixth/Hero QA builders."""
from pathlib import Path
import subprocess, json, hashlib, sys
import imageio_ffmpeg
import numpy as np
from PIL import Image, ImageDraw

R = Path(__file__).resolve().parents[1]
B = R.parent / 'little-universe-review'
A = R / 'analysis'
FF = imageio_ffmpeg.get_ffmpeg_exe()
segments = {'player': (657, 1019), 'discovery': (1391, 1777)}

def run(args):
    p = subprocess.run([FF, *map(str, args)], capture_output=True)
    if p.returncode:
        raise RuntimeError(p.stderr.decode(errors='replace'))
    return p.stdout

def sheet(video, dest, start, duration=None, every=15, label_start=None):
    args = ['-v', 'error', '-ss', start, '-i', video]
    if duration is not None:
        args += ['-t', duration]
    raw = run([*args, '-vf', f'select=not(mod(n\\,{every})),scale=320:180',
               '-fps_mode', 'vfr', '-f', 'rawvideo', '-pix_fmt', 'rgb24', 'pipe:1'])
    frames = np.frombuffer(raw, dtype=np.uint8).reshape(-1, 180, 320, 3)
    im = Image.new('RGB', (1920, ((len(frames)+5)//6)*202), '#e9eeee')
    d = ImageDraw.Draw(im)
    for i, f in enumerate(frames):
        x, y = i % 6 * 320, i // 6 * 202
        im.paste(Image.fromarray(f), (x, y))
        d.text((x+6, y+183), f'{(start if label_start is None else label_start)+i*every/30:.3f}s', fill='#111')
    im.save(dest, quality=94)

def previews():
    for name, (first, last) in segments.items():
        old = A / f'hero-polish-{name}-baseline.mp4'
        new = A / f'hero-polish-{name}-preview.mp4'
        final=R/'out/little-universe-review-hero-polish-edit.mp4'
        if final.exists():
            run(['-v','error','-y','-ss',first/30,'-i',final,
                 '-frames:v',last-first+1,'-c:v','libx264','-crf',16,'-c:a','aac',new])
        run(['-v','error','-y','-ss',first/30,'-i',B/'out/little-universe-review-hero-edit.mp4',
             '-frames:v',last-first+1,'-c:v','libx264','-crf',16,'-c:a','aac',old])
        sheet(new,A/f'hero-polish-{name}-strip.jpg',0,label_start=first/30)
        run(['-v','error','-y','-i',old,'-i',new,'-filter_complex',
             '[0:v]scale=960:540[a];[1:v]scale=960:540[b];[a][b]hstack=inputs=2[v]',
             '-map','[v]','-map','1:a','-c:v','libx264','-crf',18,
             A/f'hero-polish-{name}-comparison.mp4'])
        print(name, 'Hero left / Polish right', flush=True)
    windows = [('player-yield',26.9,28.7),('player-return',31.65,33.167),
               ('discovery-browse',52.05,53.267),('discovery-branch',54.9,56.567),
               ('discovery-episode',57.467,58.5),('discovery-resolve',58.75,59.267)]
    for name, start, end in windows:
        chapter = name.split('-')[0]
        first = segments[chapter][0]/30
        sheet(A/f'hero-polish-{chapter}-preview.mp4',A/f'hero-polish-framebyframe-{name}.jpg',
              start-first,end-start,1,label_start=start)
    D=A/'hero-polish-native'
    D.mkdir(exist_ok=True)
    targets=[22.75,24.9,27.2,27.4,27.6,27.9,28.45,28.7,31.7,32.2,32.6,32.9,33.1,
             48.9,49.567,52.4,52.8,53.2,55.3,55.65,55.8,56.0,56.5,57.8,58.4,59.2]
    for t in targets:
        chapter='player' if t<40 else 'discovery'
        n=round(t*30)
        run(['-v','error','-y','-ss',(n-segments[chapter][0])/30,
             '-i',A/f'hero-polish-{chapter}-preview.mp4','-frames:v',1,D/f'f{n:04}.png'])

def master():
    v=R/'out/little-universe-review-hero-polish-edit.mp4'
    probe=R/'node_modules/@remotion/compositor-win32-x64-msvc/ffprobe.exe'
    meta=json.loads(subprocess.check_output([str(probe),'-v','error','-show_entries',
        'stream=width,height,nb_frames,r_frame_rate','-show_entries','format=duration,size','-of','json',str(v)]))
    assert meta['streams'][0]['nb_frames']=='5520',meta
    assert (meta['streams'][0]['width'],meta['streams'][0]['height'])==(1920,1080),meta
    audio={name:run(['-v','error','-i',path,'-map','0:a:0','-c','copy','-f','md5','-']).decode().strip()
           for name,path in [('hero',B/'out/little-universe-review-hero-edit.mp4'),('polish',v)]}
    assert audio['hero']==audio['polish'],audio
    run(['-v','error','-i',v,'-f','null','-'])
    cap=(B/'out/captions-hero.srt').read_bytes()
    (R/'out/captions-hero-polish.srt').write_bytes(cap)
    saved=json.loads((A/'hero-polish-preservation.json').read_text())
    changed=[p for p,h in saved.items() if hashlib.sha256((B/p).read_bytes()).hexdigest()!=h]
    assert not changed,changed
    text_extensions={'.md','.json','.tsx','.ts','.css','.py','.mjs','.cjs','.txt'}
    def equal_checkout(p):
        a,b=(B/p).read_bytes(),(R/p).read_bytes()
        if a==b:
            return True
        if Path(p).suffix in text_extensions or p in {'.gitignore','.prettierrc'}:
            return a.replace(b'\r\n',b'\n')==b.replace(b'\r\n',b'\n')
        return False
    isolated=[p for p in saved if not p.startswith('out/') and not equal_checkout(p)]
    assert isolated==['.gitignore','src/Composition.tsx'],isolated
    # .gitignore in B was already a user edit at the snapshot; worktree keeps committed version.
    result={'metadata':meta,'audioPayloadMD5':audio,'decode':'passed','captionsByteIdentical':True,
            'originalFilesChecked':len(saved),'originalChanged':changed,
            'baselineWorktreeDiffIgnoringCheckoutLineEndings':isolated,'masterSHA256':hashlib.sha256(v.read_bytes()).hexdigest()}
    (A/'hero-polish-technical-qa.json').write_text(json.dumps(result,indent=2))
    sheet(v,A/'hero-polish-full-strip.jpg',0,every=120)
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    master() if '--master' in sys.argv else previews()
