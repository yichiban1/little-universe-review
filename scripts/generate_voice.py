import asyncio
import json
from pathlib import Path
import edge_tts
from mutagen.mp3 import MP3

root = Path(__file__).resolve().parents[1]
beats = json.loads((root / 'story' / 'beats.json').read_text(encoding='utf-8'))
out = root / 'public' / 'audio'
out.mkdir(parents=True, exist_ok=True)

async def make_one(beat):
    voice = edge_tts.Communicate(beat['text'], voice='en-US-JennyNeural', rate='+0%', boundary='WordBoundary')
    audio = bytearray()
    words = []
    async for packet in voice.stream():
        if packet['type'] == 'audio':
            audio.extend(packet['data'])
        elif packet['type'] == 'WordBoundary':
            words.append({'text': packet['text'], 'startMs': packet['offset']/10000,
                          'endMs': (packet['offset']+packet['duration'])/10000})
    target = out / f"{beat['id']}.mp3"
    target.write_bytes(audio)
    return {'id':beat['id'], 'title':beat['title'], 'text':beat['text'],
            'durationMs':round(MP3(target).info.length*1000), 'words':words}

async def main():
    results=[]
    for beat in beats:
        r=await make_one(beat)
        results.append(r)
        print(beat['id'],r['durationMs'],len(r['words']),flush=True)
    cursor=0
    captions=[]
    for r in results:
        r['startMs']=cursor
        source_words=r['text'].split()
        if len(source_words)==len(r['words']):
            for spoken,original in zip(r['words'],source_words):
                spoken['text']=original
        # Group actual spoken-word boundaries into readable 2-3 second caption blocks.
        group=[]
        for word in r['words']:
            if group and (word['endMs']-group[0]['startMs']>2800 or len(group)>=8):
                captions.append({'text':' '.join(x['text'] for x in group),
                    'startMs':round(cursor+group[0]['startMs']),
                    'endMs':round(cursor+group[-1]['endMs']),
                    'timestampMs':None,'confidence':None})
                group=[]
            group.append(word)
        if group:
            captions.append({'text':' '.join(x['text'] for x in group),
                'startMs':round(cursor+group[0]['startMs']),
                'endMs':round(cursor+group[-1]['endMs']),
                'timestampMs':None,'confidence':None})
        cursor += r['durationMs']+500
    total=cursor+1200
    timing={'durationMs':total,'beats':results}
    (root/'src'/'timing.json').write_text(json.dumps(timing,indent=2),encoding='utf-8')
    (root/'src'/'captions.json').write_text(json.dumps(captions,indent=2),encoding='utf-8')
    (root/'story'/'narration.md').write_text('# Final English narration\n\n'+'\n\n'.join(r['text'] for r in results)+'\n',encoding='utf-8')
    print('Total seconds:',round(total/1000,2),flush=True)

asyncio.run(main())
