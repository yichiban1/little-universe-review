from pathlib import Path
import json, shutil

root = Path(__file__).resolve().parents[1]
out = root / 'out'
out.mkdir(exist_ok=True)
captions = json.loads((root / 'src' / 'captions.json').read_text(encoding='utf-8'))


def stamp(ms):
    h, rem = divmod(int(ms), 3600000)
    m, rem = divmod(rem, 60000)
    s, rem = divmod(rem, 1000)
    return f'{h:02}:{m:02}:{s:02},{rem:03}'


(out / 'captions.srt').write_text('\n\n'.join(
    f"{i+1}\n{stamp(c['startMs'])} --> {stamp(c['endMs'])}\n{c['text']}"
    for i, c in enumerate(captions)) + '\n', encoding='utf-8')
shutil.copy2(root / 'public' / 'audio' / 'narration-master.mp3', out / 'narration.mp3')
shutil.copy2(root / 'story' / 'narration.md', out / 'narration.md')
print('Exported continuous narration, script, and SRT')
