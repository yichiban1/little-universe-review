"""Create one continuous narration master and word-aligned sequence/caption timing."""
import asyncio
import json
import subprocess
from pathlib import Path

import edge_tts
import imageio_ffmpeg
from mutagen.mp3 import MP3
import numpy as np

root = Path(__file__).resolve().parents[1]
beats = json.loads((root / 'story' / 'beats.json').read_text(encoding='utf-8'))
out = root / 'public' / 'audio'
out.mkdir(parents=True, exist_ok=True)
ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()


async def main():
    script = '\n\n'.join(beat['text'] for beat in beats)
    source_words = script.split()
    audio = bytearray()
    words = []
    stream = edge_tts.Communicate(script, voice='en-US-JennyNeural', rate='+0%', boundary='WordBoundary')
    async for packet in stream.stream():
        if packet['type'] == 'audio':
            audio.extend(packet['data'])
        elif packet['type'] == 'WordBoundary':
            words.append({'text': packet['text'], 'startMs': packet['offset'] / 10000,
                          'endMs': (packet['offset'] + packet['duration']) / 10000})
    if len(source_words) != len(words):
        raise RuntimeError(f'Voice boundaries {len(words)} != source words {len(source_words)}')
    for item, original in zip(words, source_words):
        item['text'] = original

    # Edge leaves an almost identical ~1s silence after most periods. Preserve
    # punctuation but vary the actual rest: brisk short fragments, a normal
    # sentence breath, and a longer transition between sequences.
    beat_ends = set()
    word_cursor = 0
    for beat in beats:
        word_cursor += len(beat['text'].split())
        beat_ends.add(word_cursor - 1)
    cuts = []
    sentence_length = 0
    for i, (prev, following) in enumerate(zip(words, words[1:])):
        sentence_length += 1
        gap = (following['startMs'] - prev['endMs']) / 1000
        if gap > .72:
            if i in beat_ends:
                target_gap = .89
            elif sentence_length <= 4:
                target_gap = .44
            else:
                target_gap = .66 + (i % 3) * .045
            if gap > target_gap:
                remove = gap - target_gap
                center = (prev['endMs'] + following['startMs']) / 2000
                cuts.append((center - remove / 2, center + remove / 2))
        if prev['text'].endswith(('.', '?', '!')):
            sentence_length = 0

    decoded = subprocess.run([str(ffmpeg), '-v', 'error', '-i', 'pipe:0',
                              '-f', 's16le', '-ac', '1', '-ar', '24000', 'pipe:1'],
                             input=bytes(audio), capture_output=True, check=True).stdout
    pcm = np.frombuffer(decoded, dtype='<i2')
    pieces = []
    cursor_sample = 0
    for start, end in cuts:
        a = round(start * 24000); b = round(end * 24000)
        pieces.append(pcm[cursor_sample:a])
        cursor_sample = b
    pieces.append(pcm[cursor_sample:])
    edited = np.concatenate(pieces)
    target = out / 'narration-master.mp3'
    subprocess.run([str(ffmpeg), '-y', '-v', 'error', '-f', 's16le', '-ac', '1',
                    '-ar', '24000', '-i', 'pipe:0', '-c:a', 'libmp3lame', '-b:a', '160k',
                    str(target)], input=edited.tobytes(), check=True)
    for item in words:
        old_start = item['startMs'] / 1000
        old_end = item['endMs'] / 1000
        removed_start = sum(end-start for start, end in cuts if end <= old_start)
        removed_end = sum(end-start for start, end in cuts if end <= old_end)
        item['startMs'] = (old_start - removed_start) * 1000
        item['endMs'] = (old_end - removed_end) * 1000

    # Word boundary durations do not fully describe the acoustic silence in
    # this voice. A second PCM pass trims remaining long quiet runs directly.
    measured = subprocess.run([str(ffmpeg), '-v', 'info', '-f', 's16le',
                               '-ac', '1', '-ar', '24000', '-i', 'pipe:0',
                               '-af', 'silencedetect=noise=-40dB:d=0.78',
                               '-f', 'null', 'NUL'], input=edited.tobytes(),
                              capture_output=True, check=True).stderr.decode(errors='replace')
    second_cuts = []
    silence_start = None
    for line in measured.splitlines():
        if 'silence_start:' in line:
            silence_start = float(line.split('silence_start:')[1].split()[0])
        elif 'silence_end:' in line and silence_start is not None:
            silence_end = float(line.split('silence_end:')[1].split()[0])
            transition = any(j + 1 < len(words) and
                             abs(words[j + 1]['startMs'] / 1000 - silence_end) < .38
                             for j in beat_ends)
            desired = .88 if transition else (.66 if silence_start < 18 else .75)
            length = silence_end - silence_start
            if length > desired + .04:
                remove = length - desired
                mid = (silence_start + silence_end) / 2
                second_cuts.append((mid - remove / 2, mid + remove / 2))
            silence_start = None
    if second_cuts:
        pieces = []
        cursor_sample = 0
        for start, end in second_cuts:
            a = round(start * 24000); b = round(end * 24000)
            pieces.append(edited[cursor_sample:a])
            cursor_sample = b
        pieces.append(edited[cursor_sample:])
        edited = np.concatenate(pieces)
        subprocess.run([str(ffmpeg), '-y', '-v', 'error', '-f', 's16le', '-ac', '1',
                        '-ar', '24000', '-i', 'pipe:0', '-c:a', 'libmp3lame',
                        '-b:a', '160k', str(target)], input=edited.tobytes(), check=True)
        for item in words:
            old_start = item['startMs'] / 1000
            old_end = item['endMs'] / 1000
            item['startMs'] = (old_start - sum(end-start for start, end in second_cuts if end <= old_start)) * 1000
            item['endMs'] = (old_end - sum(end-start for start, end in second_cuts if end <= old_end)) * 1000

    cursor = 0
    for beat in beats:
        beat_words = beat['text'].split()
        first = words[cursor]
        last = words[cursor + len(beat_words) - 1]
        beat['startMs'] = round(first['startMs'])
        beat['endMs'] = round(last['endMs'])
        cursor += len(beat_words)

    captions = []
    group = []
    for word in words:
        if group and (word['endMs'] - group[0]['startMs'] > 2300 or len(group) >= 7):
            captions.append({'text': ' '.join(x['text'] for x in group),
                             'startMs': round(group[0]['startMs']),
                             'endMs': round(group[-1]['endMs'])})
            group = []
        group.append(word)
    if group:
        captions.append({'text': ' '.join(x['text'] for x in group),
                         'startMs': round(group[0]['startMs']),
                         'endMs': round(group[-1]['endMs'])})

    total = round(MP3(target).info.length * 1000 + 1300)
    (root / 'src' / 'timing.json').write_text(json.dumps({'durationMs': total, 'beats': beats}, indent=2), encoding='utf-8')
    (root / 'src' / 'captions.json').write_text(json.dumps(captions, indent=2), encoding='utf-8')
    (root / 'story' / 'narration.md').write_text('# Final English narration — second edit\n\n' +
                                               '\n\n'.join(x['text'] for x in beats) + '\n', encoding='utf-8')
    print(f'{len(words)} words, {total/1000:.2f}s, continuous master voice; {len(cuts)+len(second_cuts)} pauses re-timed')
    for beat in beats:
        print(f"{beat['id']}: {beat['startMs']/1000:.2f}–{beat['endMs']/1000:.2f}s")


asyncio.run(main())
