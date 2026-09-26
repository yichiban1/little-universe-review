"""Resolution-first sixth branch. Fifth source and output are read-only inputs."""
from pathlib import Path
import json,re
from PIL import Image
R=Path(__file__).resolve().parents[1]; A=R/'public/assets'; Q=R/'analysis/sixth-research'
for e in json.loads((Q/'acquisition.json').read_text(encoding='utf-8')):
    im=Image.open(Q/(e['name']+'-viewport.png')); rect=e['main']; x=round(rect['x']); y=round(rect['y'])
    im.crop((x,y,x+600,y+900)).save(A/('web-'+e['name']+'-sixth.png'))
Image.open(Q/'xdoctor-playing-raw.png').crop((652,60,1252,622)).save(A/'web-xdoctor-2008-sixth.png')
Image.open(Q/'xdoctor-playing-raw.png').crop((0,1002,1888,1071)).save(A/'web-xdoctor-controls-sixth.png')
Image.open(Q/'student-viewport.png').crop((699,485,1232,590)).save(A/'web-xdoctor-student-sixth.png')
s=(R/'src/FifthEdit.tsx').read_text(encoding='utf-8').replace('FifthShot','SixthShot')
s=s.replace(",filter:name==='ui-stickers.jpg'?'brightness(1.4)':undefined",'')
branches={
'open-cover':'''<Stage color={C.deep}><WebPage name="web-xdoctor-programme-sixth.png" x={1060-30*slow} y={85} w={650} h={820}/><Picture name="xdoctor-cover-sixth.jpg" x={210-35*slow} y={250} w={550} h={550} radius={24} shadow/><Line x={0} y={0} w={1920} h={10}/></Stage>''',
'open-result':'''<Stage color="#fff"><WebPage mode="borderless" name="web-xdoctor-2008-sixth.png" x={1070} y={125} w={650} h={760} opacity={entry}/><Words x={120} y={335} size={120} w={780} color={C.dark}>2008.</Words><Words x={125} y={505} size={40} color={C.dark} weight={500}>The episode I opened.</Words></Stage>''',
'player-art':'''<Stage><Picture name="xdoctor-episode-art-sixth.png" x={130} y={125} w={810} h={810} radius={14}/><Phone name="ui-player.jpg" x={1240} y={105} w={360}/><Tag>Artwork / the same episode</Tag></Stage>''',
'player-observation':'''<Stage color={C.ice}><Phone name="ui-player.jpg" x={1160} y={15} w={460}/><Picture name="xdoctor-episode-art-sixth.png" x={90} y={245} w={460} h={460} radius={18}/><Words x={615} y={360} size={64} w={500} color={C.dark}>A lot of cover.<br/>I look further down.</Words></Stage>''',
'player-title':'''<Stage color="#fff"><WebPage mode="borderless" name="web-xdoctor-2008-sixth.png" x={1150} y={160} w={620} h={700}/><Words x={110} y={300} size={112} w={900} color={C.dark}>2008.</Words><Words x={115} y={470} size={49} w={880} color={C.dark}>A memory, then a conversation.</Words><Tag color={C.dark}>The same episode</Tag></Stage>''',
'player-pocket':'''<Stage><Phone name="ui-player.jpg" x={1135} y={30} w={450}/><Words x={155} y={335} size={80} w={850}>Leave it playing.</Words><VoiceWave globalFrame={gf} x={160} y={550} w={780} h={120} bars={55}/></Stage>''',
'player-tap-hold':'''<Stage><Phone name="ui-player.jpg" x={1135} y={30} w={450}/><VoiceWave globalFrame={gf} x={160} y={465} w={780} h={145} bars={55}/></Stage>''',
'feed-topic':'''<Stage color={C.ice}><WebPage mode="borderless" name="web-ritan-topic-sixth.png" x={1080} y={55} w={650} h={900} pan={140+80*slow}/><Words x={105} y={265} size={95} w={850} color={C.dark}>Follow a topic.</Words><Words x={110} y={420} size={45} w={830} color={C.dark} weight={500}>History, through 日谈公园.</Words><Tag color={C.dark}>Following a topic</Tag></Stage>''',
'feed-programme':'''<Stage color="#fff"><WebPage mode="split" name="web-ritan-programme-sixth.png" x={230} y={65} w={650} h={880} pan={45*slow}/><WebPage mode="split" name="web-sound-programme-sixth.png" x={1050} y={65} w={650} h={880} opacity={entry} pan={35*slow}/></Stage>''',
'feed-discover':'''<Stage color="#fff"><WebPage mode="borderless" name="web-stochastic-programme-sixth.png" x={1080} y={70} w={650} h={890} pan={70+25*slow}/><Words x={110} y={325} size={80} w={800} color={C.dark}>Stochastic<br/>Volatility.</Words></Stage>''',
'feed-select':'''<Stage color="#fff"><WebPage mode="borderless" name="web-stochastic-episode-sixth.png" x={1080} y={70} w={650} h={890}/><Words x={110} y={325} size={85} w={820} color={C.dark}>Another story<br/>to open.</Words></Stage>''',
'listen-catch':'''<Stage><Phone name="ui-player.jpg" x={1190} y={35} w={440}/><Words x={155} y={275} size={83} w={900}>Catch a sentence.</Words><VoiceWave globalFrame={gf} x={160} y={490} w={800} h={155} bars={55}/></Stage>''',
'notes-enter':'''<Stage color={C.ice}><WebPage mode="borderless" name="web-xdoctor-2008-sixth.png" x={1120} y={140} w={650} h={760}/><Words x={110} y={315} size={102} w={900} color={C.dark}>Inside 2008.</Words><Words x={115} y={470} size={47} color={C.dark} weight={500}>The same conversation, in detail.</Words></Stage>''',
'notes-stadium':'''<Stage><Picture name="notes-stadium.png" x={165} y={310} w={500} h={333} radius={10} shadow scale={.88+.12*entry}/><Phone name="ui-notes-photos.jpg" x={745} y={25} w={480}/><Tag>Photographs</Tag></Stage>''',
'notes-dorm':'''<Stage><Picture name="notes-dorm.png" x={245} y={365} w={330} h={220} radius={10} shadow scale={.9+.1*entry}/><Phone name="ui-notes-photos.jpg" x={745} y={25} w={480}/><Tag>Photographs</Tag></Stage>''',
'comments-open':'''<Stage><WebPage mode="borderless" name="web-xdoctor-discussion.png" x={190} y={105} w={650} h={815} pan={130} opacity={1-.35*entry}/><Phone name="ui-comments-redacted.jpg" x={1050-70*entry} y={30} w={455} opacity={entry}/></Stage>''',
'comments-first':'''<Stage color="#fff"><Crop name="web-xdoctor-student-sixth.png" sx={0} sy={0} sw={533} sh={105} x={1160} y={420} w={635}/><Words x={105} y={255} size={30} color={C.dark} tracking={2}>LISTENER 01</Words><Words x={100} y={345} size={105} w={930} color={C.dark}>Student<br/>in 2008.</Words><Line x={105} y={640} w={700*entry}/></Stage>''',
'comments-second':'''<Stage><Crop name="ui-comments-redacted.jpg" sx={40} sy={1020} sw={1130} sh={860} x={1000} y={230+20*slow} w={850}/><Words x={105} y={255} size={30} tracking={2}>LISTENER 02</Words><Words x={100} y={345} size={112} w={850}>Chengdu.</Words><Line x={105} y={530} w={700*entry}/></Stage>''',
'history-hours':'''<Stage><Picture name="ui-listening-hours.jpg" x={750} y={350} w={1050} h={420}/><Words x={85} y={260} size={83} w={660}>128 h<br/>27 m</Words><Words x={90} y={545} size={30} tracking={2}>TOTAL LISTENING</Words></Stage>''',
'history-emphasis':'''<Stage><Picture name="ui-listening-hours.jpg" x={750} y={350} w={1050} h={420}/><Words x={85} y={260} size={83} w={660}>128 h<br/>27 m</Words><Words x={90} y={545} size={30} tracking={2}>TOTAL LISTENING</Words><Line x={90} y={650} w={530*entry}/></Stage>''',
'history-100':'''<Stage><Crop name="ui-stickers.jpg" sx={470} sy={360} sw={550} sh={720} x={1190} y={165} w={550}/><Words x={100} y={280} size={125} w={950}>100 h</Words><Words x={105} y={470} size={33} tracking={2}>WITH ONE CREATOR</Words></Stage>''',
'critical-web':'''<Stage color="#fff"><WebPage mode="borderless" name="web-xdoctor-2008-sixth.png" x={1090} y={100} w={650} h={650}/><Words x={110} y={290} size={88} w={850} color={C.dark}>Web listening<br/>works too.</Words><Crop name="web-xdoctor-controls-sixth.png" sx={0} sy={0} sw={1888} sh={69} x={0} y={835} w={1920}/></Stage>''',
'end-shows':'''<Stage color="#fff"><WebPage mode="split" name="web-ritan-episode-sixth.png" x={230} y={80} w={650} h={850}/><WebPage mode="split" name="web-stochastic-programme-sixth.png" x={1050} y={80} w={650} h={850}/></Stage>''',
'end-history':'''<Stage><Picture name="ui-listening-hours.jpg" x={750} y={350} w={1050} h={420}/><Words x={85} y={290} size={95} w={660}>128 h<br/>27 m</Words><Words x={90} y={565} size={30} tracking={2}>TOTAL LISTENING</Words></Stage>'''
}
for key,value in branches.items():
    pattern=r"if\(id==='"+key+r"'\)return .*?;(?=\s*\n)"
    s,n=re.subn(pattern,lambda m:f"if(id==='{key}')return {value};",s)
    assert n==1,(key,n)
# The original DVD file carries enough pixels for the protected existing choreography.
s=s.replace('name="notes-dvd.jpg"','name="notes-dvd-sixth.png"').replace('name="xdoctor-cover.jpg"','name="xdoctor-cover-sixth.jpg"')
s=s.replace('name="notes-beijing.jpg"','name="notes-beijing-sixth.png"')
s=s.replace('x={770-270*entry} y={125+59*entry} w={430+890*entry} h={203+420*entry}', 'x={770-195*entry} y={125+85*entry} w={430+395*entry} h={286+263*entry}')
s=s.replace('x={500-405*back} y={184-9*back} w={1320-980*back} h={623-462*back}', 'x={575-480*back} y={210-35*back} w={825-485*back} h={549-323*back}')
changes={
'player-timeline': [('x={170}','x={280}'),('w={1580}','w={1360}')],
'player-rewind': [('x={130}','x={240}'),('w={1640}','w={1440}'),('Tap x={575} y={620}','Tap x={631} y={565}')],
'listen-controls': [('x={-35}','x={210}'),('w={1990}','w={1500}')],
'listen-mini-detail': [('x={0}','x={215}'),('w={1920}','w={1490}')],
'listen-back': [('x={175}','x={240}'),('w={1570}','w={1440}'),('Tap x={600} y={545}','Tap x={613} y={509}')],
'notes-outline': [('w={1450}','w={1360}'),('y={95-600*slow}','y={95-555*slow}')],
'notes-player-return': [('x={0}','x={215}'),('w={1920}','w={1490}')],
'comments-context': [('name="web-xdoctor-2008.png"','name="web-xdoctor-2008-sixth.png"'),('x={0}','x={95}'),('y={-50}','y={75}'),('w={790}','w={650}'),('h={1130}','h={820}')],
'end-comments': [('x={230}','x={285}'),('w={1460}','w={1350}'),('y={-60}','y={20}')],
}
for key,reps in changes.items():
    pat=r"if\(id==='"+key+r"'\)return .*?;(?=\s*\n)"
    def replace(m):
        t=m[0]
        for old,new in reps:
            assert old in t,(key,old)
            t=re.sub(r'(?<![a-zA-Z])'+re.escape(old),lambda _:new,t)
        return t
    s=re.sub(pat,replace,s)
dims={p.name:Image.open(p).size for p in A.iterdir() if p.suffix.lower() in ['.jpg','.png']}
s=re.sub(r'const dims:Record<string,\[number,number\]>=\{.*?\};','const dims:Record<string,[number,number]>='+json.dumps(dims)+';',s)
# Guard actual animated values on every rendered frame, in addition to the usage audit.
guard="""const pixelGate=(name:string,factor:number)=>{const photo=/^(notes-|xdoctor-cover|xdoctor-episode-art|xdoctor-video|discovery-|commute-|train-|listening-fieldnotes)/.test(name);const limit=photo?1.5:1.25;if(!dims[name]||!Number.isFinite(factor)||factor>limit+1e-6)throw new Error(`Source pixel budget exceeded: ${name} ${factor.toFixed(3)}x > ${limit}x`);};\n"""
s=s.replace('const Crop:React.FC',guard+'const Crop:React.FC')
s=s.replace('const s=w/sw;return','const s=w/sw;pixelGate(name,s);if(sx<0||sy<0||sx+sw>iw||sy+sh>ih)throw new Error(`Crop outside source: ${name}`);return')
s=s.replace("})=><div style={{position:'absolute',left:x,top:y,width:w,height:h,overflow:'hidden'", "})=>{const [iw,ih]=dims[name];pixelGate(name,(fit==='contain'?Math.min(w/iw,h/ih):Math.max(w/iw,h/ih))*scale);return <div style={{position:'absolute',left:x,top:y,width:w,height:h,overflow:'hidden'",1)
s=s.replace("objectPosition:pos}}/></div>;", "objectPosition:pos}}/></div>};",1)
s=s.replace('const h=w*2622/1206;return','const h=w*2622/1206;pixelGate(name,w/1206*scale);return')
s=s.replace("height=mode==='fullBleed'?1080:h;", "height=mode==='fullBleed'?1080:h;pixelGate(name,width/dims[name][0]);")
used={v['id'] for v in json.loads((R/'src/shots-fifth.json').read_text(encoding='utf-8'))}
s='\n'.join(line for line in s.splitlines() if not (m:=re.search(r"if\(id==='([^']+)'\)",line)) or m[1] in used)+'\n'
(R/'src/SixthEdit.tsx').write_text(s,encoding='utf-8')
film=(R/'src/FifthFilm.tsx').read_text(encoding='utf-8').replace('Fifth','Sixth').replace('fifthTotalFrames','sixthTotalFrames')
# Timings, captions, RMS waveform and sound mix deliberately reference the preserved fifth data.
(R/'src/SixthFilm.tsx').write_text(film,encoding='utf-8')
p=R/'src/Composition.tsx'; c=p.read_text(encoding='utf-8')
if "from './SixthFilm'" not in c:
    c=c.replace("export const MyComposition", "import {SixthFilm,sixthTotalFrames} from './SixthFilm';\nexport const MyComposition")
    c=c.replace(' </>;', ' <Composition id="LittleUniverseReviewSixth" component={SixthFilm} durationInFrames={sixthTotalFrames} fps={30} width={1920} height={1080}/>\n </>;')
    p.write_text(c,encoding='utf-8')
print('Sixth branch created; timing and continuous fifth sound unchanged.')
