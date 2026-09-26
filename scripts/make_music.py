"""Original, evolving 3-phase score and short editorial action cues."""
from pathlib import Path
import json, math, subprocess, wave
import numpy as np

root = Path(__file__).resolve().parents[1]
timing = json.loads((root / 'src' / 'timing.json').read_text(encoding='utf-8'))
seconds = math.ceil(timing['durationMs'] / 1000) + 1
middle_start = timing['beats'][2]['startMs'] / 1000
ending_start = timing['beats'][-1]['startMs'] / 1000
rate = 32000
count = seconds * rate
music = np.zeros(count, dtype=np.float64)
ffmpeg = root / 'node_modules' / '@remotion' / 'compositor-win32-x64-msvc' / 'ffmpeg.exe'
out = root / 'public' / 'audio'


def place(start, signal, gain=1.0, target=music):
    pos = int(start * rate)
    if pos >= len(target):
        return
    n = min(len(signal), len(target) - pos)
    target[pos:pos + n] += signal[:n] * gain


def tone(freq, duration, decay=2.0, soft=0.03):
    t = np.arange(int(duration * rate)) / rate
    env = (1 - np.exp(-t / soft)) * np.exp(-t * decay)
    return (np.sin(2 * np.pi * freq * t) + .22 * np.sin(2 * np.pi * 2 * freq * t)) * env


def pad(start, duration, chord, amp):
    t = np.arange(int(duration * rate)) / rate
    env = np.maximum(0, np.minimum(1, t / 2.4) * np.minimum(1, (duration - t) / 2.4))
    signal = sum(np.sin(2 * np.pi * f * t) + .15 * np.sin(2 * np.pi * 2.004 * f * t)
                 for f in chord) / len(chord)
    place(start, signal * env, amp)


chords = [(164.81, 196, 246.94), (174.61, 220, 261.63),
          (146.83, 196, 246.94), (164.81, 207.65, 293.66)]
for i, start in enumerate(np.arange(0, seconds, 10.5)):
    pad(start, min(12, seconds - start), chords[i % len(chords)], .17)

# Curiosity: open, sparse mallet notes and a quiet pulse.
for i, start in enumerate(np.arange(0, middle_start, 2.35)):
    place(start, tone([392, 493.88, 587.33, 493.88][i % 4], .9, 5), .075)
    if i % 2 == 0:
        place(start + 1.17, tone(196, .3, 11), .025)

# Exploration: a slightly quicker pattern and gentle high counterline.
for i, start in enumerate(np.arange(middle_start, ending_start, 1.6)):
    place(start, tone([392, 440, 493.88, 587.33, 493.88, 440][i % 6], .8, 5.5), .07)
    if i % 4 == 0:
        place(start + .8, tone(784, .55, 7), .025)
    if i % 2 == 0:
        place(start, tone(130.81, .25, 13), .022)

# Resolution: lower pulse fades away, wider chord and a repeated closing figure.
for i, start in enumerate(np.arange(ending_start, seconds - 1, 2.4)):
    place(start, tone([392, 493.88, 587.33, 783.99][i % 4], 1.15, 3.1), .085)
resolution_start=max(ending_start+9,seconds-16)
pad(resolution_start, min(17, seconds - resolution_start), (164.81, 196, 246.94, 329.63), .12)

t = np.arange(count) / rate
fade = np.maximum(0, np.minimum(1, t / 1.6) * np.minimum(1, (seconds - t) / 3))
music = np.tanh(music * fade) * .69


def export(name, samples):
    wav = out / f'{name}.wav'
    with wave.open(str(wav), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
        w.writeframes((np.clip(samples, -1, 1) * 32767).astype('<i2').tobytes())
    subprocess.run([str(ffmpeg), '-y', '-i', str(wav), '-c:a', 'libmp3lame', '-b:a', '160k', str(out / f'{name}.mp3')],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    wav.unlink()


export('music-second-edit', music)
rng = np.random.default_rng(75)
for kind in ['tap', 'swipe', 'paper', 'cue', 'riser']:
    dur = {'tap': .22, 'swipe': .47, 'paper': .63, 'cue': .52, 'riser': .75}[kind]
    tt = np.arange(int(dur * rate)) / rate
    noise = rng.normal(0, 1, len(tt))
    if kind == 'tap':
        signal = (np.sin(2*np.pi*880*tt) + .15*noise) * np.exp(-tt*31) * .35
    elif kind == 'swipe':
        smooth = np.convolve(noise, np.ones(75)/75, 'same')
        signal = smooth * np.sin(np.pi*tt/dur)**2 * .37
    elif kind == 'paper':
        smooth = np.convolve(noise, np.ones(12)/12, 'same')
        signal = smooth * np.exp(-tt*4) * .14
    elif kind == 'cue':
        signal = (np.sin(2*np.pi*660*tt)+.45*np.sin(2*np.pi*990*tt)) * np.exp(-tt*7) * .23
    else:
        smooth = np.convolve(noise, np.ones(90)/90, 'same')
        signal = smooth * np.sin(np.pi*tt/dur)**2 * .32
    export(f'sfx-{kind}', signal)
print('Three-phase original music and five original editorial cues ready')
