from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root=Path(__file__).resolve().parents[1]
target=root/'out'/'little-universe-review-project.zip'
keep=['README.md','package.json','package-lock.json','remotion.config.ts','tsconfig.json','eslint.config.mjs']
paths=[root/x for x in keep]
retired={'train-listener-editorial.png','listening-fieldnotes-illustration.png',
         'hook.mp3','origin.mp3','interface.mp3','discovery.mp3','intimacy.mp3',
         'notes.mp3','comments.mp3','memory.mp3','critique.mp3','ending.mp3','music.mp3'}
for folder in ['src','story','scripts','public']:
    paths.extend(p for p in (root/folder).rglob('*') if p.is_file() and p.name not in retired)
paths.extend((root/'analysis'/f'second-edit-sheet-{i}.jpg') for i in range(1,5))
for name in ['little-universe-review-second-edit.mp4','narration.mp3','narration.md','captions.srt']:
    paths.append(root/'out'/name)
with ZipFile(target,'w',ZIP_DEFLATED,compresslevel=6) as z:
    for path in paths:
        if path.exists(): z.write(path,path.relative_to(root))
print(target,round(target.stat().st_size/1024/1024,1),'MB')
