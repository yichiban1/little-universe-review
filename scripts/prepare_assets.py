from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

root = Path(__file__).resolve().parents[1]
out = root / 'public' / 'assets'
source = Path(r'C:\Users\Fy\AppData\Local\Temp')
files = {
    'player': '3fa306f2-204a-4a02-84b5-167fe00499d3',
    'notes_photos': '09d12701-f7e2-4cae-bb55-b094a16f25f9',
    'notes_text': '80e91197-49b4-4017-9cd5-cfc3b81cd6c5',
    'comments': 'b6897055-d2a9-428b-9dd9-82443f119db8',
    'profile': '5be53983-0efb-4077-8260-9546486e8e45',
    'stickers': '904ffed7-0a3b-463a-8cbb-bbc9d5c54a8f',
}
imgs = {k: Image.open(source / f'codex-clipboard-{v}.jpg').convert('RGB') for k,v in files.items()}

# Source screenshots stay outside the project. Copy only selected, redacted regions.
imgs['player'].save(out / 'ui-player.jpg', quality=91)
imgs['notes_photos'].save(out / 'ui-notes-photos.jpg', quality=91)
imgs['notes_text'].save(out / 'ui-notes-text.jpg', quality=91)
imgs['profile'].crop((52, 1075, 1152, 1515)).save(out / 'ui-listening-hours.jpg', quality=92)
imgs['stickers'].crop((15, 200, 1150, 1760)).save(out / 'ui-stickers.jpg', quality=92)

im = imgs['comments'].copy()
# Mask other listeners' identifying information while retaining their real comments.
draw = ImageDraw.Draw(im)
for box in [(45,420,495,560), (45,1120,515,1260),
            (150,945,680,1050), (120,1865,1150,2255)]:
    draw.rounded_rectangle(box, radius=24, fill=(31,30,31))
im.save(out / 'ui-comments-redacted.jpg', quality=91)

# Documentary images already embedded in the supplied Show Notes screenshot.
photos = imgs['notes_photos']
photos.crop((60, 314, 1147, 827)).save(out / 'notes-beijing.jpg', quality=92)
photos.crop((60, 1025, 1147, 1738)).save(out / 'notes-dvd.jpg', quality=92)
print('Prepared 9 authentic screenshot assets')
