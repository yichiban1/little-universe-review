"""Render fourth-edit voice samples, a master, and actual word alignment."""
import asyncio
import json
import subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg
import numpy as np
from mutagen.mp3 import MP3

ROOT = Path(__file__).resolve().parents[1]
BEATS = json.loads((ROOT / 'story/beats-fourth-edit.json').read_text(encoding='utf-8'))
OUT = ROOT / 'public/audio'
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
SAMPLE_TEXT = "I downloaded Little Universe because X Doctor had a podcast. I'd watched their videos for ages, then searched the name here."


async def synth(text, voice, rate='+0%'):
    audio, words = bytearray(), []
    async for part in edge_tts.Communicate(text, voice=voice, rate=rate, boundary='WordBoundary').stream():
        if part['type'] == 'audio':
            audio.extend(part['data'])
        elif part['type'] == 'WordBoundary':
            words.append({'text': part['text'], 'startMs': part['offset']/10000,
                          'endMs': (part['offset']+part['duration'])/10000})
    return bytes(audio), words


def decode(data):
    raw = subprocess.run([FFMPEG, '-v', 'error', '-i', 'pipe:0', '-f', 's16le',
                          '-ac', '1', '-ar', '24000', 'pipe:1'], input=data,
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype='<i2')


def encode(pcm, path):
    subprocess.run([FFMPEG, '-y', '-v', 'error', '-f', 's16le', '-ac', '1', '-ar', '24000',
                    '-i', 'pipe:0', '-c:a', 'libmp3lame', '-b:a', '160k', str(path)],
                   input=pcm.tobytes(), check=True)


async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    # Andrew is conversational rather than the brighter Jenny read used in edit 2.
    voice = 'en-US-AndrewNeural'
    script = '\n\n'.join(b['text'] for b in BEATS)
    data, words = await synth(script, voice, rate='-10%')
    originals = script.split()
    print('raw words', len(words), 'script words', len(originals))
    from difflib import SequenceMatcher
    origin_to_word = {}
    for tag, i, j, k, l in SequenceMatcher(None, [w.lower().strip('.,:;') for w in originals], [w['text'].lower().strip('.,:;') for w in words]).get_opcodes():
        if tag == 'equal':
            for oi, wi in zip(range(i,j), range(k,l)):
                origin_to_word[oi] = wi
                words[wi]['text'] = originals[oi]
        elif tag == 'replace' and l-k == 1 and j-i == 2:
            origin_to_word[i] = origin_to_word[i+1] = k
            words[k]['text'] = ' '.join(originals[i:j])
        else:
            raise RuntimeError(f'Unexpected voice tokenization: {tag} {originals[i:j]} {[w["text"] for w in words[k:l]]}')

    pcm = decode(data)
    raw_duration = len(pcm)/24000
    print('raw duration', round(raw_duration, 2))
    # Retain spontaneous breathing room, trimming only the very long Edge TTS
    # paragraph rests. This cut list is measured in audio time, then applied to
    # both PCM and word boundaries. It is not tied to section fractions.
    beat_ends = []
    count = 0
    for beat in BEATS:
        count += len(beat['text'].split())
        beat_ends.append(origin_to_word[count-1])
    cuts = []
    for i, (prev, following) in enumerate(zip(words, words[1:])):
        gap = (following['startMs'] - prev['endMs'])/1000
        allowed = .90 if i in beat_ends else (.64 if prev['text'].endswith(('.', '?', '!')) else .42)
        if gap > allowed + .12:
            surplus = gap-allowed
            center = (prev['endMs']+following['startMs'])/2000
            cuts.append((center-surplus/2, center+surplus/2))
    pieces, cursor = [], 0
    for start, end in cuts:
        a, b = round(start*24000), round(end*24000)
        pieces.append(pcm[cursor:a]); cursor = b
    pieces.append(pcm[cursor:])
    edited = np.concatenate(pieces)
    target = OUT / 'narration-fourth.mp3'
    encode(edited, target)
    for word in words:
        for key in ('startMs', 'endMs'):
            old = word[key]/1000
            word[key] = round((old-sum(b-a for a,b in cuts if b <= old))*1000)
    duration_ms = 185000
    count = 0
    for beat in BEATS:
        n = len(beat['text'].split())
        beat['startMs'] = words[origin_to_word[count]]['startMs']
        beat['endMs'] = words[origin_to_word[count+n-1]]['endMs']
        count += n
    from captions_third import build_captions
    captions = build_captions(words)
    (ROOT/'src/words-fourth.json').write_text(json.dumps(words,indent=2), encoding='utf-8')
    (ROOT/'src/timing-fourth.json').write_text(json.dumps({'durationMs':duration_ms,'beats':BEATS},indent=2), encoding='utf-8')
    (ROOT/'src/captions-fourth.json').write_text(json.dumps(captions,indent=2), encoding='utf-8')
    (ROOT/'story/narration-fourth-edit.md').write_text('# Fourth edit narration\n\n'+ '\n\n'.join(b['text'] for b in BEATS)+'\n', encoding='utf-8')
    print('final', duration_ms/1000, 'cuts', len(cuts), 'voice', voice)
    for beat in BEATS:
        print(beat['id'], beat['startMs']/1000, beat['endMs']/1000)


asyncio.run(main())
