from pathlib import Path
import math, wave, subprocess
import numpy as np

root=Path(__file__).resolve().parents[1]
seconds=184
rate=32000
count=seconds*rate
t=np.arange(count,dtype=np.float64)/rate
music=np.zeros(count,dtype=np.float64)

# Original low-key ambient score: gently repeating triads and sparse soft plucks.
chords=[(196,246.94,293.66),(174.61,220,261.63),(146.83,196,246.94),(164.81,207.65,261.63)]
for n,chord in enumerate(chords):
    start=n*12
    while start<seconds:
        end=min(start+13,seconds)
        j0=int(start*rate); j1=int(end*rate)
        tt=np.arange(j1-j0)/rate
        env=np.minimum(1,tt/2.5)*np.minimum(1,(end-start-tt)/2.5)
        env=np.maximum(env,0)
        pad=sum(np.sin(2*math.pi*freq*tt)*.25+np.sin(2*math.pi*freq*2.005*tt)*.06 for freq in chord)
        music[j0:j1]+=pad*env*.14
        start+=48
for beat in np.arange(0,seconds,2.7):
    j0=int(beat*rate); j1=min(count,j0+int(rate*.65))
    tt=np.arange(j1-j0)/rate
    freq=chords[int(beat//12)%4][int(beat//2.7)%3]*2
    music[j0:j1]+=np.sin(2*math.pi*freq*tt)*np.exp(-tt*7)*.08
fade=np.minimum(1,t/2.5)*np.minimum(1,(seconds-t)/4)
music=np.tanh(music*np.maximum(fade,0))*.54
wav=root/'public'/'audio'/'music.wav'
with wave.open(str(wav),'wb') as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(rate)
    w.writeframes((music*32767).astype('<i2').tobytes())
ffmpeg=root/'node_modules'/'@remotion'/'compositor-win32-x64-msvc'/'ffmpeg.exe'
subprocess.run([str(ffmpeg),'-y','-i',str(wav),'-c:a','libmp3lame','-b:a','128k',str(root/'public'/'audio'/'music.mp3')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
wav.unlink()
print('Original ambient music complete')
