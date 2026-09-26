"""Fifth-only editorial changes. Never write fourth source or assets."""
import json,re
from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parents[1]
s=(R/'src/FourthEdit.tsx').read_text().replace('FourthShot','FifthShot').replace('voice-envelope-fourth','voice-envelope-fifth')
s=s.replace("import React from 'react';","import React from 'react';\nimport './fifth-fonts';")
s=s.replace("fontFamily:'Arial, Helvetica, sans-serif'","fontFamily:'Inter, sans-serif'")
s=s.replace("color,fontSize:size,fontWeight:weight", "color,fontFamily:size>=36?'Inter Tight, sans-serif':'Inter, sans-serif',fontSize:size,fontWeight:weight")
dims={p.name:Image.open(p).size for p in (R/'public/assets').iterdir() if p.suffix in ['.jpg','.png']}
s=re.sub(r'const dims:Record<string,\[number,number\]>=\{.*?\};','const dims:Record<string,[number,number]>='+json.dumps(dims)+';',s)
helper="""const WebPage:React.FC<{name:string;x:number;y:number;w:number;h?:number;pan?:number;opacity?:number;mode?:'card'|'borderless'|'fullBleed'|'edgeCrop'|'split'|'largeDetail'}>=({name,x,y,w,h=820,pan=0,opacity=1,mode='card'})=>{
 const card=mode==='card';
 const left=mode==='fullBleed'?0:x,top=mode==='fullBleed'?0:y,width=mode==='fullBleed'?1920:w,height=mode==='fullBleed'?1080:h;
 return <div style={{position:'absolute',left,top,width,height,overflow:'hidden',borderRadius:card?18:0,background:'#fff',boxShadow:card?'0 28px 65px #0005':undefined,opacity}}><Img src={asset(name)} style={{width,height:'auto',transform:`translateY(${-pan}px)`}}/></div>;
};"""
s=re.sub(r'const WebPage:React.FC<.*?;(?=\nconst Provenance)',lambda m:helper,s,flags=re.S)
branches={
'open-result':'''<Stage color="#fff"><WebPage mode="edgeCrop" name="web-xdoctor-2008.png" x={610} y={-90} w={1310} h={1170} opacity={entry}/><Words x={85} y={375} size={100} w={440} color={C.dark}>2008.</Words></Stage>''',
'player-art':'''<Stage><Crop name="ui-player.jpg" sx={140} sy={345} sw={930} sh={925} x={-60} y={-280+40*slow} w={2020}/><Tag>Artwork</Tag></Stage>''',
'player-observation':'''<Stage color={C.deep}><Words x={155} y={320} size={86} w={1550}>A lot of cover.<br/>I look further down.</Words><Line x={158} y={590} w={720*entry}/></Stage>''',
'player-title':'''<Stage color="#fff"><Crop name="web-xdoctor-2008.png" sx={0} sy={220} sw={572} sh={103} x={65} y={340} w={1790}/><Tag color={C.dark}>The same episode</Tag></Stage>''',
'player-pocket':'''<Stage color={C.deep}><VoiceWave globalFrame={gf} x={160} y={465} w={1600} h={145} bars={95}/><Words x={155} y={275} size={80}>Leave it playing.</Words></Stage>''',
'player-tap-hold':'''<Stage><VoiceWave globalFrame={gf} x={185} y={470} w={1550} h={180} bars={85}/></Stage>''',
'feed-topic':'''<Stage color="#fff"><WebPage mode="fullBleed" name="web-ritan-topic.png" x={0} y={0} w={1920} pan={430+170*slow}/><div style={{position:'absolute',left:0,top:0,width:1920,height:140,background:'#ffffffee'}}/><Tag color={C.dark}>Following a topic</Tag></Stage>''',
'feed-programme':'''<Stage color="#fff"><WebPage mode="split" name="web-ritan-programme.png" x={0} y={-80} w={945} h={1160} pan={55*slow}/><WebPage mode="split" name="web-sound-programme.png" x={975} y={-80} w={945} h={1160} opacity={entry} pan={35*slow}/></Stage>''',
'feed-discover':'''<Stage color="#fff"><WebPage mode="borderless" name="web-stochastic-programme.png" x={465} y={-30} w={1120} h={1110} pan={160+25*slow}/></Stage>''',
'feed-select':'''<Stage color="#fff"><WebPage mode="edgeCrop" name="web-stochastic-episode.png" x={465} y={-30} w={1120} h={1110}/></Stage>''',
'feed-daqing':'''<Stage color={C.deep}><Words x={180} y={340} size={116} w={1500}>Daqing.</Words><Words x={185} y={492} size={40} color={C.muted} weight={500}>My hometown. Unexpected.</Words></Stage>''',
'listen-widgets':'''<Stage color={C.ice}><Picture name="appstore-1.jpg" x={665} y={-185} w={610} h={1085} fit="contain"/><Provenance>Official widget examples</Provenance></Stage>''',
'listen-controls':'''<Stage color={C.ice}><Crop name="appstore-1.jpg" sx={0} sy={980} sw={1242} sh={570} x={-35} y={140} w={1990}/><Provenance>Official widget controls</Provenance></Stage>''',
'listen-lock':'''<Stage color={C.ice}><Picture name="appstore-7.jpg" x={580} y={-150-40*slow} w={760} h={1351} fit="contain"/><Provenance>Official lock-screen shortcuts</Provenance></Stage>''',
'listen-mini':'''<Stage><Phone name="ui-notes-text.jpg" x={750} y={-30} w={485}/><Tag>Browsing the same episode</Tag></Stage>''',
'listen-mini-detail':'''<Stage><Crop name="ui-notes-text.jpg" sx={0} sy={2340} sw={1206} sh={265} x={0} y={330} w={1920}/><VoiceWave globalFrame={gf} x={300} y={795} w={1320} h={80}/></Stage>''',
'listen-back':'''<Stage><Crop name="ui-player.jpg" sx={15} sy={1810} sw={1160} sh={590} x={175} y={110} w={1570}/><Tap x={600} y={545} f={f} start={16} size={170}/><Words x={85} y={875} size={38}>15 seconds back.</Words></Stage>''',
'listen-catch':'''<Stage color={C.deep}><Words x={155} y={280} size={83} w={1550}>Catch a sentence.</Words><VoiceWave globalFrame={gf} x={160} y={490} w={1600} h={155} bars={90}/></Stage>''',
'notes-enter':'''<Stage><Crop name="web-xdoctor-2008.png" sx={0} sy={220} sw={572} sh={103} x={100} y={270} w={1720}/><Tag>Inside the 2008 episode</Tag></Stage>''',
'notes-player-return':'''<Stage><Crop name="ui-notes-text.jpg" sx={0} sy={2340} sw={1206} sh={265} x={0} y={335} w={1920}/><Tag>The same episode keeps its references</Tag></Stage>''',
'comments-context':'''<Stage color="#fff"><WebPage mode="split" name="web-xdoctor-2008.png" x={0} y={-50} w={790} h={1130}/><Crop name="ui-player.jpg" sx={35} sy={1610} sw={1130} sh={690} x={820} y={125} w={1100}/><Words x={840} y={830} size={78} w={1000} color={C.dark}>02:33</Words></Stage>''',
'comments-open':'''<Stage><WebPage mode="edgeCrop" name="web-xdoctor-discussion.png" x={0} y={-60} w={890} h={1140} pan={130} opacity={1-.35*entry}/><Phone name="ui-comments-redacted.jpg" x={1050-70*entry} y={30} w={455} opacity={entry}/></Stage>''',
'comments-first':'''<Stage color="#fff"><Crop name="web-xdoctor-discussion.png" sx={45} sy={330} sw={510} sh={95} x={70} y={340} w={1780}/><Tag color={C.dark}>Listener 01 / student in 2008</Tag></Stage>''',
'comments-second':'''<Stage><Crop name="ui-comments-redacted.jpg" sx={40} sy={1020} sw={1130} sh={860} x={0} y={-150+30*slow} w={1920}/><div style={{position:'absolute',left:0,right:0,top:0,height:120,background:'#101820'}}/><Tag>Listener 02 / Chengdu</Tag></Stage>''',
'history-hours':'''<Stage><Picture name="ui-listening-hours.jpg" x={0} y={140} w={1920} h={768}/><Tag>All listening</Tag></Stage>''',
'history-emphasis':'''<Stage><Crop name="ui-listening-hours.jpg" sx={70} sy={178} sw={355} sh={170} x={200} y={135} w={1520}/><Tag>Total listening / 128h27</Tag></Stage>''',
'history-stickers':'''<Stage><Picture name="ui-stickers.jpg" x={640} y={-45} w={640} h={880}/><Tag>One creator</Tag></Stage>''',
'history-100':'''<Stage><Crop name="ui-stickers.jpg" sx={470} sy={360} sw={550} sh={720} x={570} y={-125} w={830}/><Words x={85} y={870} size={40}>100 hours with one creator</Words></Stage>''',
'history-return':'''<Stage><Picture name="ui-listening-hours.jpg" x={40} y={265} w={1050} h={420}/><Picture name="ui-stickers.jpg" x={1240} y={45} w={520} h={715}/><Tag>Two different counts</Tag></Stage>''',
'critical-personal':'''<Stage color={C.deep}><Words x={155} y={270} size={91} w={1530}>I don't use it<br/>for everything.</Words><Words x={160} y={565} size={40} weight={500} color={C.muted}>Most of my English listening happens elsewhere.</Words></Stage>''',
'critical-web':'''<Stage color="#fff"><WebPage mode="borderless" name="web-xdoctor-playing-page-fifth.png" x={0} y={-230} w={1250} h={1240}/><Words x={1360} y={275} size={67} w={470} color={C.dark}>Web listening<br/>works too.</Words><Crop name="web-xdoctor-playing-controls-fifth.png" sx={0} sy={0} sw={974} sh={69} x={0} y={805} w={1920}/></Stage>''',
'critical-phone':'''<Stage><Phone name="ui-player.jpg" x={740} y={25} w={470}/><Tag>How I use it</Tag><Words x={85} y={375} size={65} w={560}>I still reach<br/>for my phone.</Words></Stage>''',
'critical-fit':'''<Stage color={C.deep}><Picture name="little-universe-icon.png" x={210} y={325} w={340} h={340} radius={70}/><Words x={700} y={365} size={87} w={1100}>The Chinese<br/>podcasts I follow.</Words></Stage>''',
'end-xdoctor':'''<Stage><Picture name="xdoctor-cover.jpg" x={685} y={245} w={550} h={550} radius={22}/></Stage>''',
'end-shows':'''<Stage color="#fff"><WebPage mode="split" name="web-ritan-episode.png" x={0} y={-100} w={945} h={1180}/><WebPage mode="split" name="web-stochastic-programme.png" x={975} y={-100} w={945} h={1180}/></Stage>''',
'end-notes':'''<Stage color={C.ice}><Picture name="notes-dvd.jpg" x={0} y={-190} w={1920} h={1260}/></Stage>''',
'end-comments':'''<Stage><Crop name="ui-comments-redacted.jpg" sx={40} sy={1020} sw={1130} sh={860} x={230} y={-60} w={1460}/></Stage>''',
'end-history':'''<Stage><Picture name="ui-listening-hours.jpg" x={0} y={155} w={1920} h={768}/></Stage>'''
}
for sid,jsx in branches.items():
 line=f" if(id==='{sid}')return {jsx};"
 pattern=r" if\(id==='"+re.escape(sid)+r"'\)return .*?;(?=\n)"
 if re.search(pattern,s):s=re.sub(pattern,lambda m:line,s)
 else:s=s.replace(' return <Stage>{null}</Stage>;',line+'\n return <Stage>{null}</Stage>;')
(R/'src/FifthEdit.tsx').write_text(s,encoding='utf-8')

# Anchors follow actual word alignment; durations are never section fractions.
old=json.loads((R/'src/shots-fourth.json').read_text())
spec=[(x['anchor'],x['id'],x['chapter']) for x in old if x['chapter'] in ['opening','player','notes']]
idx=next(i for i,x in enumerate(spec) if x[1]=='player-title')
spec.insert(idx,('With that much space','player-observation','player'))
idx=next(i for i,x in enumerate(spec) if x[2]=='notes')
spec[idx:idx]=[
('After X Doctor','feed-enter','discovery'),('following topics','feed-topic','discovery'),("I'd finish an episode",'feed-search','discovery'),('Sometimes I browse','feed-programme','discovery'),('Sometimes I just','feed-discover','discovery'),('the discovery page','feed-select','discovery'),('Daqing','feed-daqing','discovery'),
('Most of the time','listen-widgets','listening'),('If I need','listen-controls','listening'),("there's usually a shortcut",'listen-lock','listening'),("I don't need the full",'listen-mini','listening'),('The little player','listen-mini-detail','listening'),('And if I missed','listen-catch','listening'),('Fifteen seconds back','listen-back','listening')]
spec += [('And the conversation','comments-feature','comments'),('I was at','comments-context','comments'),('I can open the discussion','comments-open','comments'),('comment box keeps','comments-link','comments'),('one listener writes','comments-first','comments'),('Another remembers','comments-second','comments'),("I'll read a few",'comments-return','comments'),
('My profile shows','history-hours','history'),('128 hours','history-emphasis','history'),('This sticker is different','history-stickers','history'),('a hundred hours','history-100','history'),('I like seeing','history-return','history'),
("I don't use it for everything",'critical-personal','critical'),('Web listening works','critical-web','critical'),('I still reach','critical-phone','critical'),('For the Chinese podcasts','critical-fit','critical'),
('I came here','end-xdoctor','ending'),('Now I come back','end-shows','ending'),('the photos in the notes','end-notes','ending'),('the people in the discussion','end-comments','ending'),("There's a history",'end-history','ending'),('When someone sends','end-icon','ending')]
words=json.loads((R/'src/words-fifth.json').read_text());t=json.loads((R/'src/timing-fifth.json').read_text())
speech=' '.join(w['text'] for w in words);starts=[];cursor=0
for word in words:starts.append(cursor);cursor+=len(word['text'])+1
shots=[];search=0
for phrase,sid,chapter in spec:
 pos=speech.lower().find(phrase.lower(),search)
 if pos<0:raise ValueError(phrase)
 wi=max(i for i,x in enumerate(starts) if x<=pos)
 shots.append(dict(id=sid,chapter=chapter,anchor=phrase,wordIndex=wi,startMs=words[wi]['startMs']))
 search=pos+len(phrase)
shots[0]['startMs']=0

# Primary visual grammar, deliberately broader than CSS implementation details.
family={
'full-bleed crop':['player-art','history-hours','notes-dvd-hold','feed-topic','comments-second','end-notes','end-history'],
'detail crop':['player-title','player-timeline','player-rewind','listen-controls','listen-mini-detail','listen-back','notes-outline','notes-outline-return','comments-link','notes-enter','notes-player-return','comments-first','history-emphasis','history-100','end-comments'],
'split-screen':['feed-programme','comments-context','end-shows'],
'floating object':['open-title','listen-widgets','listen-lock','history-stickers','critical-fit','end-xdoctor','end-icon'],
'page/card':['open-cover','open-video','feed-search','feed-enter','feed-discover','comments-feature'],
'typographic interlude':['player-observation','player-pocket','player-tap-hold','feed-daqing','critical-personal','listen-catch'],
'phone-in-space':['open-player','player-full','player-return','listen-mini','notes-open','critical-phone'],
'two-source comparison':['history-return'],
'object transformation':['open-search','open-notes','open-comments','notes-stadium','notes-dorm','notes-olympic','notes-dvd','notes-return','comments-open','comments-return'],
'edge crop':['open-result','feed-select','critical-web']}
for i,x in enumerate(shots):
 x['endMs']=shots[i+1]['startMs'] if i+1<len(shots) else t['durationMs'];x['durationMs']=x['endMs']-x['startMs']
 assert x['durationMs']>0
 x['composition']=next((k for k,v in family.items() if x['id'] in v),None)
 assert x['composition'],x['id']
(R/'src/shots-fifth.json').write_text(json.dumps(shots,indent=2))
for x in shots:print(f"{x['startMs']/1000:.2f}–{x['endMs']/1000:.2f} {x['id']} [{x['composition']}]")
