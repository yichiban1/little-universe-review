"""Keep third motion vocabulary; replace selected source-led shots."""
import json,re
from pathlib import Path
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'public/assets'
# Mask from the saved screenshot's actual pixel coordinates (DOM coordinates
# were offset during the capture; do not treat them as pixel coordinates).
im=Image.open(ROOT/'analysis/fourth-research/web-xdoctor-discussion-raw.png')
draw=ImageDraw.Draw(im)
for box in [(218,80,350,121),(218,273,340,313),(218,356,345,396),(218,547,370,586),
            (258,150,755,249),(258,494,756,526)]: draw.rectangle(box,fill='#e1e4e5')
im.crop((202,66,774,844)).save(A/'web-xdoctor-discussion.png')

src=(ROOT/'src/ThirdEdit.tsx').read_text().replace('ThirdShot','FourthShot').replace('voice-envelope-third','voice-envelope-fourth')
dims={p.name:Image.open(p).size for p in A.iterdir() if p.suffix in ['.jpg','.png']}
src=re.sub(r'const dims:Record<string,\[number,number\]>=\{.*?\};', 'const dims:Record<string,[number,number]>='+json.dumps(dims)+';',src)
helper='''
// A captured product page, never a fabricated card or detached cover.
const WebPage:React.FC<{name:string;x:number;y:number;w:number;h?:number;pan?:number;opacity?:number}>=({name,x,y,w,h=820,pan=0,opacity=1})=><div style={{position:'absolute',left:x,top:y,width:w,height:h,overflow:'hidden',borderRadius:18,background:'#fff',boxShadow:'0 28px 65px #0005',opacity}}><Img src={asset(name)} style={{width:w,height:'auto',transform:`translateY(${-pan}px)`}}/></div>;
const Provenance:React.FC<{children:React.ReactNode;dark?:boolean}>=({children,dark=false})=><Words x={85} y={930} size={22} weight={500} color={dark?C.muted:'#5a737b'} tracking={0}>{children}</Words>;
'''
src=src.replace('export const FourthShot',helper+'\nexport const FourthShot')
branches={
'open-cover':'''<Stage color={C.deep}><WebPage name="web-xdoctor-programme.png" x={865-40*slow} y={85} w={780} h={820} opacity={.45+.55*entry}/><Picture name="xdoctor-cover.jpg" x={210-35*slow} y={280} w={440} h={440} radius={24} shadow/><Line x={0} y={0} w={1920} h={10}/></Stage>''',
'open-result':'''<Stage color={C.ice}><WebPage name="web-xdoctor-2008.png" x={705} y={95} w={870} h={820} opacity={entry}/><Words x={85} y={330} size={68} w={500} color={C.dark}>2008.</Words><Line x={88} y={470} w={360*entry}/></Stage>''',
'player-title':'''<Stage color={C.ice}><Crop name="web-xdoctor-2008.png" sx={0} sy={212} sw={572} sh={115} x={150} y={330} w={1620} radius={16} shadow/><Tag color={C.dark}>The same episode</Tag></Stage>''',
'player-pocket':'''<Stage color={C.ice}><Picture name="official-home-player.png" x={1050-45*entry} y={55} w={465} h={810} fit="contain"/><Words x={95} y={315} size={78} w={730} color={C.dark}>Leave it playing.</Words><Line x={98} y={500} w={680*entry}/><Provenance>Official player example</Provenance></Stage>''',
'player-tap-hold':'''<Stage><Crop name="appstore-4.jpg" sx={100} sy={840} sw={1025} sh={770} x={645} y={100} w={1000} radius={20}/><Words x={80} y={350} size={64} w={470}>One tap.<br/>Back a little.</Words><Provenance dark>Official player example</Provenance></Stage>''',
'feed-enter':'''<Stage color={C.ice}><Picture name="official-home-subscriptions.png" x={940-40*slow} y={25} w={510} h={1045} fit="contain"/><Words x={85} y={310} size={74} w={720} color={C.dark}>One show leads<br/>to another.</Words><Provenance>Official subscriptions example</Provenance></Stage>''',
'feed-topic':'''<Stage color={C.ice}><WebPage name="web-ritan-topic.png" x={690} y={70} w={1000} h={820} pan={40*slow}/><Tag color={C.dark}>Topics</Tag></Stage>''',
'feed-programme':'''<Stage color={C.ice}><WebPage name="web-ritan-programme.png" x={115+20*entry} y={65} w={770} h={830} pan={60*slow}/><WebPage name="web-sound-programme.png" x={990} y={65} w={770} h={830} opacity={entry} pan={40*slow}/></Stage>''',
'feed-discover':'''<Stage color={C.ice}><WebPage name="web-stochastic-programme.png" x={225} y={55} w={865} h={840} pan={55*slow}/><Words x={1190} y={370} size={64} w={620} color={C.dark}>An episode list.<br/>A new direction.</Words></Stage>''',
'feed-select':'''<Stage color={C.ice}><WebPage name="web-stochastic-episode.png" x={605} y={55} w={1020} h={850}/><Tag color={C.dark}>From programme to episode</Tag></Stage>''',
'feed-daqing':'''<Stage color={C.deep}><Words x={180} y={315} size={118} w={1500}>Daqing.</Words><Words x={184} y={470} size={42} color={C.muted} weight={500}>The place I grew up.</Words><Line x={185} y={620} w={850*entry}/></Stage>''',
'feed-hold':'''<Stage color={C.deep}><Words x={185} y={330} size={77} w={1450}>I wasn't expecting that.</Words><Line x={185} y={620} w={850} /></Stage>''',
'listen-widgets':'''<Stage color={C.ice}><Picture name="appstore-1.jpg" x={980-45*slow} y={-40} w={610} h={1085} fit="contain" radius={18}/><Words x={85} y={280} size={78} w={710} color={C.dark}>The phone can<br/>stay in my pocket.</Words><Provenance>Official widget examples</Provenance></Stage>''',
'listen-controls':'''<Stage color={C.ice}><Crop name="appstore-1.jpg" sx={0} sy={980} sw={1242} sh={570} x={230} y={155} w={1460} radius={24} shadow/><Tag color={C.dark}>Home-screen widgets</Tag></Stage>''',
'listen-lock':'''<Stage color={C.ice}><Picture name="appstore-7.jpg" x={835} y={-115-50*slow} w={720} h={1280} fit="contain" radius={20}/><Words x={85} y={330} size={72} w={660} color={C.dark}>An episode.<br/>One shortcut away.</Words><Provenance>Official lock-screen examples</Provenance></Stage>''',
'listen-mini':'''<Stage><Phone name="ui-notes-text.jpg" x={1080-45*slow} y={-30} w={500}/><Words x={85} y={325} size={74} w={780}>Still playing<br/>while I browse.</Words><Line x={88} y={545} w={650*entry}/></Stage>''',
'listen-mini-detail':'''<Stage><Crop name="ui-notes-text.jpg" sx={0} sy={2340} sw={1206} sh={265} x={215} y={415} w={1490} radius={16} shadow/><Words x={85} y={165} size={67}>A small player at the bottom.</Words><VoiceWave globalFrame={gf} x={480} y={805} w={960} h={70}/></Stage>''',
'listen-back':'''<Stage><Crop name="appstore-1.jpg" sx={400} sy={1010} sw={842} sh={560} x={275} y={150} w={1340} radius={20}/><Words x={95} y={820} size={50}>Catch that detail again.</Words><Provenance dark>Official widget controls</Provenance></Stage>''',
'comments-feature':'''<Stage color={C.ice}><Picture name="appstore-5.jpg" x={840} y={-70-35*slow} w={655} h={1165} fit="contain" radius={20}/><Words x={85} y={320} size={77} w={660} color={C.dark}>More voices<br/>below the audio.</Words><Provenance>Official discussion example</Provenance></Stage>''',
'comments-context':'''<Stage color={C.ice}><WebPage name="web-xdoctor-2008.png" x={85} y={105} w={690} h={750}/><Crop name="ui-player.jpg" sx={35} sy={1610} sw={1130} sh={690} x={890} y={205} w={900} radius={18} shadow/><Words x={890} y={790} size={64} w={850} color={C.dark}>02:33</Words></Stage>''',
'comments-open':'''<Stage><WebPage name="web-xdoctor-discussion.png" x={100-70*entry} y={95} w={720} h={790} opacity={1-.35*entry}/><Phone name="ui-comments-redacted.jpg" x={1030-70*entry} y={30} w={455} opacity={entry}/></Stage>''',
'comments-player':'''<Stage color={C.ice}><Crop name="web-xdoctor-discussion.png" sx={45} sy={290} sw={510} sh={485} x={430} y={45} w={940} radius={18} shadow/><Tag color={C.dark}>Listener memories</Tag></Stage>''',
'comments-first':'''<Stage color={C.ice}><Crop name="web-xdoctor-discussion.png" sx={45} sy={330} sw={510} sh={95} x={235} y={315} w={1430} radius={15} shadow/><Tag color={C.dark}>Listener 01</Tag></Stage>''',
'history-stickers':'''<Stage><Picture name="ui-stickers.jpg" x={665} y={-50} w={620} h={852} radius={22}/><Tag>Sticker shelf</Tag></Stage>''',
'history-board':'''<Stage><Picture name="ui-stickers.jpg" x={670} y={-55} w={630} h={866} radius={22} shadow/><Words x={85} y={320} size={66} w={540}>Voices I've<br/>spent time with.</Words></Stage>''',
'end-feed':'''<Stage color={C.ice}><WebPage name="web-sound-episode.png" x={690} y={45} w={1020} h={850}/><Words x={85} y={360} size={65} w={530} color={C.dark}>I come back.</Words></Stage>''',
'end-catalogue':'''<Stage color={C.ice}><Picture name="official-home-subscriptions.png" x={870} y={-30} w={560} h={1120} fit="contain"/><Words x={85} y={340} size={73} w={720} color={C.dark}>Something else<br/>to open.</Words></Stage>''',
'end-xdoctor':'''<Stage><WebPage name="web-xdoctor-programme.png" x={855} y={70} w={820} h={810}/><Picture name="xdoctor-cover.jpg" x={200} y={270} w={450} h={450} radius={22}/></Stage>''',
'end-shows':'''<Stage color={C.ice}><WebPage name="web-ritan-episode.png" x={115} y={65} w={760} h={820}/><WebPage name="web-stochastic-programme.png" x={1010} y={65} w={760} h={820}/></Stage>''',
'end-notes':'''<Stage color={C.ice}><Picture name="notes-dvd.jpg" x={315} y={85} w={1280} h={840} radius={18} shadow/></Stage>''',
'end-comments':'''<Stage><Phone name="ui-comments-redacted.jpg" x={750} y={25} w={460}/></Stage>''',
'end-icon':'''<Stage color={C.ice}><Picture name="little-universe-icon.png" x={790} y={150} w={340} h={340} radius={74} shadow scale={.91+.09*entry}/><Words x={250} y={545} w={1420} color={C.dark} size={94} align="center">Little Universe</Words><Picture name="official-wordmark-fourth.png" x={750} y={700} w={420} h={111} fit="contain" opacity={move(f,15,24)}/><Line x={610} y={850} w={700*entry} h={9}/></Stage>'''
}
for sid,jsx in branches.items():
    line=f' if(id===\'{sid}\')return {jsx};'
    pattern=r" if\(id==='"+re.escape(sid)+r"'\)return .*?;(?=\n)"
    if re.search(pattern,src): src=re.sub(pattern,lambda m:line,src)
    else: src=src.replace(' return <Stage>{null}</Stage>;',line+'\n return <Stage>{null}</Stage>;')
(ROOT/'src/FourthEdit.tsx').write_text(src,encoding='utf-8')

spec=[]
third=json.loads((ROOT/'src/shots-third.json').read_text())
for s in third:
    if s['chapter'] in ['opening','player','notes']:spec.append((s['anchor'],s['id'],s['chapter']))
# Insert discovery/listening before notes; retain word anchors in all retained chapters.
idx=next(i for i,s in enumerate(spec) if s[2]=='notes')
spec[idx:idx]=[
('After X Doctor','feed-enter','discovery'),('following topics','feed-topic','discovery'),
("I'd finish an episode",'feed-search','discovery'),('Sometimes I browse','feed-programme','discovery'),
("Sometimes I just",'feed-discover','discovery'),('the discovery page','feed-select','discovery'),
('One episode mentioned Daqing','feed-daqing','discovery'),("I wasn't looking",'feed-hold','discovery'),
('Most of the time','listen-widgets','listening'),('There are ways','listen-controls','listening'),
('The lock-screen','listen-lock','listening'),('Inside the app','listen-mini','listening'),
('The conversation keeps','listen-mini-detail','listening'),('If I miss a detail','listen-back','listening')]
spec += [
('And the conversation','comments-feature','comments'),('I was at','comments-context','comments'),
('I can open the discussion','comments-open','comments'),
('comment box keeps','comments-link','comments'),('one listener writes','comments-first','comments'),
('Another remembers','comments-second','comments'),("I'll read a few",'comments-return','comments'),
('Those memories stay','comments-player','comments'),
('My profile says','history-hours','history'),('There are stickers too','history-stickers','history'),
('This one marks','history-100','history'),('I like seeing','history-board','history'),
('I still use other apps','end-feed','ending'),('Little Universe is where','end-catalogue','ending'),('I came here','end-xdoctor','ending'),
('Now I come back','end-shows','ending'),('the photos in the notes','end-notes','ending'),
('the people in the discussion','end-comments','ending'),('When someone sends','end-icon','ending')]
words=json.loads((ROOT/'src/words-fourth.json').read_text())
timing=json.loads((ROOT/'src/timing-fourth.json').read_text())
timing['durationMs']=185000
(ROOT/'src/timing-fourth.json').write_text(json.dumps(timing,indent=2))
speech=' '.join(w['text'] for w in words); starts=[];cursor=0
for word in words:starts.append(cursor);cursor+=len(word['text'])+1
shots=[];search=0
for phrase,sid,chapter in spec:
    pos=speech.lower().find(phrase.lower(),search)
    if pos<0:raise ValueError(phrase)
    wi=max(i for i,s in enumerate(starts) if s<=pos)
    shots.append(dict(id=sid,chapter=chapter,anchor=phrase,wordIndex=wi,startMs=words[wi]['startMs']))
    search=pos+len(phrase)
shots[0]['startMs']=0
for i,s in enumerate(shots):
    s['endMs']=shots[i+1]['startMs'] if i+1<len(shots) else timing['durationMs']
    s['durationMs']=s['endMs']-s['startMs']
    assert s['durationMs']>0
(ROOT/'src/shots-fourth.json').write_text(json.dumps(shots,indent=2))
film=(ROOT/'src/ThirdFilm.tsx').read_text().replace('third','fourth').replace('Third','Fourth')
film=film.replace('audio/music-fourth-original.mp3','audio/music-third-original.mp3').replace('audio/sfx-fourth-','audio/sfx-third-')
film=film.replace("{shot:'history-stickers',offset:4,type:'page',volume:.21}","{shot:'history-stickers',offset:4,type:'page',volume:.21}")
film=film.replace('[0,18,20,60,62,71,74,106,108,135,138,154,158,179]','[0,18,20,61,63,87,89,122,124,149,151,165,169,185]')
(ROOT/'src/FourthFilm.tsx').write_text(film,encoding='utf-8')
p=ROOT/'src/Composition.tsx';c=p.read_text()
if "import {FourthFilm" not in c:
    c=c.replace("export const MyComposition", "import {FourthFilm,fourthTotalFrames} from './FourthFilm';\nexport const MyComposition")
    c=c.replace(' </>;', ' <Composition id="LittleUniverseReviewFourth" component={FourthFilm} durationInFrames={fourthTotalFrames} fps={30} width={1920} height={1080}/>\n </>;')
p.write_text(c,encoding='utf-8')
for s in shots:print(f"{s['startMs']/1000:.2f}-{s['endMs']/1000:.2f} {s['id']}")
