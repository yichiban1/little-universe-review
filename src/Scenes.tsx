import React from 'react';
import {Img, staticFile, useCurrentFrame} from 'remotion';
import {Base, C, Card, Connector, Label, Phone, Photo, Tag, Wave, clamp, drift, pop} from './Design';

type BeatProps={index:number;duration:number;start:number;total:number;title:string};
const P=(n:number)=>Math.round(n);
const local=(f:number,d:number)=>clamp(f/d);

const Hook:React.FC<{f:number;d:number}>=({f,d})=>{
 const p=local(f,d), a=pop(f,4,25), b=pop(f,95,24), c=pop(f,220,23);
 return <>
  <div style={{position:'absolute',left:1040,top:150,width:620,height:620,borderRadius:'50%',overflow:'hidden',opacity:.55*(1-pop(f,108,30))}}><Img src={staticFile('assets/train-listener-editorial.png')} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:'75% center',scale:1+f*.0006}}/></div>
  <div style={{position:'absolute',left:1040,top:150,width:620,height:620,border:`2px solid ${C.line}`,borderRadius:'50%',scale:1+drift(f)*.025}}/>
  <div style={{position:'absolute',left:1130,top:240,width:440,height:440,border:`2px dashed ${C.green}`,borderRadius:'50%',rotate:`${f*.12}deg`,opacity:.5}}/>
  <Img src={staticFile('assets/xdoctor-cover.jpg')} style={{position:'absolute',left:1150-250*a,top:395,width:280,height:280,borderRadius:35,boxShadow:'0 20px 35px #11452c35',scale:.55+.45*a}}/>
  <Connector x1={1165} y1={530} x2={1440} y2={530} grow={b}/>
  <Img src={staticFile('assets/little-universe-icon.png')} style={{position:'absolute',left:1400+80*(1-b),top:470,width:120,height:120,borderRadius:30,scale:.3+.7*b,opacity:b}}/>
  <Label x={115} y={205} size={27} weight={800} color={C.green} opacity={a}>A PERSONAL ENTRY POINT</Label>
  <Label x={112} y={278} size={92} width={990} opacity={a}>I came for<br/><span style={{color:C.green}}>one podcast.</span></Label>
  <Label x={112} y={540} size={45} width={780} weight={500} opacity={b}>I was looking for X Doctor.</Label>
  <Label x={112} y={665} size={62} width={840} opacity={c}>Then the world<br/>opened up.</Label>
  <div style={{position:'absolute',left:985,top:822,width:620,height:9,background:C.line,borderRadius:10}}><div style={{height:9,width:`${p*100}%`,background:C.green,borderRadius:10}}/></div>
 </>;
};

const Origin:React.FC<{f:number;d:number}>=({f,d})=>{
 const a=pop(f,0,22),b=pop(f,105,24),c=pop(f,235,22);
 const slide=92*(1-a);
 const handoff=pop(f,d-35,31);
 return <>
  <Card x={130-slide} y={205} w={720} h={530} opacity={1-handoff} style={{border:'8px solid #20382d',borderRadius:30,boxShadow:'0 25px 50px #09221830'}}>
    <div style={{height:385,background:'linear-gradient(130deg,#0c2920,#227456)',position:'relative'}}>
      <div style={{position:'absolute',left:55,top:44,color:'#aedbbf',fontSize:21,fontWeight:800,letterSpacing:3}}>X DOCTOR · VIDEO</div>
      <div style={{position:'absolute',left:50,top:125,fontSize:67,color:'white',fontWeight:800,width:540,lineHeight:1.07}}>The first voice<br/>I followed.</div>
      <div style={{position:'absolute',left:330,top:264,width:90,height:90,borderRadius:'50%',background:'white',display:'grid',placeItems:'center',fontSize:46,color:C.green}}>▶</div>
      <Wave x={52} y={320} w={600} h={44} phase={f} color="#b8e7ca" bars={45}/>
    </div>
    <div style={{padding:27,fontSize:24,fontWeight:700}}>Video was the beginning <span style={{float:'right',color:C.muted}}>01:42</span></div>
  </Card>
  <Connector x1={852} y1={470} x2={1095} y2={470} grow={b*(1-handoff)} stroke={5}/>
  <div style={{position:'absolute',left:850,top:425,width:105,height:105,borderRadius:'50%',background:C.yellow,display:'grid',placeItems:'center',fontSize:51,opacity:b,scale:.4+.6*b}}>→</div>
  <Phone src="assets/ui-player.jpg" x={1110-915*handoff} y={168-12*handoff} w={400} h={740} scale={.65+.35*b} opacity={b}/>
  <Label x={910} y={766} size={29} opacity={c}>One tap into audio.</Label>
  <Tag x={130} y={790} opacity={c}>FROM VIDEO</Tag><Tag x={340} y={790} filled opacity={c}>TO PODCAST</Tag>
 </>;
};

const Interface:React.FC<{f:number;d:number}>=({f})=>{
 const a=pop(f,0,20),b=pop(f,78,20),c=pop(f,185,25),e=pop(f,315,22);
 return <>
  <Phone src="assets/ui-player.jpg" x={165+30*(1-a)} y={145} w={435} h={790} scale={.94+.06*a}/>
  <Label x={705} y={185} size={77} width={850} opacity={a}>Room to <span style={{color:C.green}}>listen.</span></Label>
  <Label x={711} y={302} size={29} weight={500} color={C.muted} opacity={a}>The interface stays calm while a story plays.</Label>
  <Connector x1={606} y1={446} x2={730} y2={446} grow={b}/>
  <Card x={750+55*(1-b)} y={386} w={790} h={138} opacity={b} fill="#fff"><div style={{display:'flex',height:'100%',alignItems:'center',gap:27,padding:'0 34px'}}><span style={{fontSize:45,color:C.green}}>◉</span><div><div style={{fontSize:27,fontWeight:800}}>Clear controls</div><div style={{fontSize:21,color:C.muted,marginTop:7}}>Play · seek · return</div></div></div></Card>
  <Card x={830-45*(1-c)} y={548} w={715} h={136} opacity={c} fill="#fff"><div style={{display:'flex',height:'100%',alignItems:'center',gap:27,padding:'0 34px'}}><span style={{fontSize:43,color:C.green}}>▤</span><div><div style={{fontSize:27,fontWeight:800}}>Cover and title first</div><div style={{fontSize:21,color:C.muted,marginTop:7}}>The episode stays in focus</div></div></div></Card>
  <Card x={915+65*(1-e)} y={706} w={625} h={126} opacity={e} fill={C.pale} border={C.green}><div style={{display:'flex',height:'100%',alignItems:'center',gap:22,padding:'0 30px',fontSize:27,fontWeight:800}}>↗ <span>Space to keep walking.</span></div></Card>
  <Wave x={719} y={857} w={806} h={40} phase={f} bars={65}/>
 </>;
};

const Discovery:React.FC<{f:number;d:number}>=({f})=>{
 const nodes=[['X DOCTOR',960,400,0],['FOLK CULTURE',1290,250,75],['PLACES',1500,460,145],['TRAVEL',1320,685,225],['PERSONAL STORIES',930,685,330]] as const;
 const base=pop(f,0,20);
 const search=pop(f,254,23),follow=pop(f,460,23);
 const remembered=pop(f,265,24)*(1-pop(f,444,26));
 return <>
  <Phone src="assets/appstore-3.jpg" x={155} y={155} w={415} h={760} scale={.9+.1*base} opacity={1-search}/>
  <Phone src="assets/appstore-6.jpg" x={155} y={155} w={415} h={760} scale={.9+.1*base} opacity={search*(1-follow)}/>
  <Phone src="assets/appstore-2.jpg" x={155} y={155} w={415} h={760} scale={.9+.1*base} opacity={follow}/>
  <Label x={680} y={167} size={71} width={1010} opacity={base}>One show became<br/><span style={{color:C.green}}>many doors.</span></Label>
  <div style={{position:'absolute',left:865,top:330,width:700,height:470,borderRadius:'50%',border:`2px dashed ${C.line}`,rotate:`${f*.03}deg`}}/>
  {nodes.slice(1).map(([,x,y,t],i)=><Connector key={'line'+i} x1={1040} y1={464} x2={x+30} y2={y+25} grow={pop(f,t,31)} color={i%2?C.green:'#86bd98'} stroke={2}/>)}
  {nodes.map(([label,x,y,t],i)=><Tag key={label} x={x+drift(f,i+1)*8} y={y+drift(f,i+2)*7} filled={i===0} opacity={pop(f,t,26)}>{label}</Tag>)}
  <div style={{position:'absolute',left:695+90*(1-remembered),top:335,width:950,height:460,background:'#fff',border:'9px solid white',borderRadius:28,boxShadow:'0 30px 55px #162d293c',overflow:'hidden',opacity:remembered}}>
   <Img src={staticFile('assets/listening-fieldnotes-illustration.png')} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:`${15+f*.025}% center`,scale:1.08}}/>
  </div>
  <Tag x={710} y={298} opacity={remembered}>A PLACE IN MY MEMORY · ILLUSTRATION</Tag>
  <Card x={681} y={824} w={980} h={86} fill="#e6f5eb" opacity={pop(f,350,24)}><div style={{padding:'24px 30px',fontSize:23,fontWeight:600}}>Daqing was one familiar place inside a much wider listening world.</div></Card>
 </>;
};

const Intimacy:React.FC<{f:number;d:number}>=({f,d})=>{
 const a=pop(f,0,22),b=pop(f,90,22),c=pop(f,216,22),e=pop(f,330,20);
 return <>
  <Label x={118} y={183} size={80} width={810} opacity={a}>It sounds like<br/><span style={{color:C.green}}>old friends.</span></Label>
  <div style={{position:'absolute',left:920+100*(1-b),top:180,width:790,height:625,borderRadius:32,overflow:'hidden',opacity:b,boxShadow:'0 25px 55px #16332638',border:'9px solid white'}}>
   <Img src={staticFile('assets/train-listener-editorial.png')} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:`${62+f/d*8}% center`,scale:1+f/d*.07}}/>
  </div>
  <Tag x={1375} y={137} opacity={b}>A LISTENING MOMENT</Tag>
  <div style={{position:'absolute',left:98,top:575,width:1622,height:191,background:'linear-gradient(90deg,#f7f6f1e8,#f7f6f188)',borderRadius:35,opacity:c}}/>
  <Wave x={95} y={605} w={1600} h={160} phase={f} bars={105}/>
  <div style={{position:'absolute',left:155,top:815,width:1550,height:7,background:C.line,borderRadius:6}}><div style={{height:7,width:`${Math.min(f/d,1)*100}%`,background:C.green,borderRadius:6}}/></div>
  <div style={{position:'absolute',left:210+P(f/d*1220),top:781,width:70,height:70,background:C.green,borderRadius:'50%',border:'7px solid white',boxShadow:'0 8px 22px #12351e44'}}/>
  <Card x={670} y={288-40*(1-b)} w={250} h={83} opacity={b} fill="#fff"><div style={{padding:'22px 27px',fontSize:25,fontWeight:800}}>a pause</div></Card>
  <Card x={770} y={440-40*(1-c)} w={255} h={83} opacity={c} fill="#fff"><div style={{padding:'22px 27px',fontSize:25,fontWeight:800}}>a memory</div></Card>
  <Card x={1330} y={659-40*(1-e)} w={330} h={83} opacity={e} fill={C.pale}><div style={{padding:'22px 27px',fontSize:25,fontWeight:800}}>a shared joke</div></Card>
  <Label x={145} y={857} size={25} weight={500} color={C.muted} opacity={c}>Alone on a train. Still part of a conversation.</Label>
 </>;
};

const Notes:React.FC<{f:number;d:number}>=({f})=>{
 const a=pop(f,0,23),b=pop(f,95,24),c=pop(f,250,23),e=pop(f,415,24);
 const zoom=1+.04*clamp((f-95)/360);
 return <>
  <Phone src="assets/ui-notes-text.jpg" x={116-55*c} y={148} w={420} h={770} scale={.98} opacity={1-.25*e}/>
  <Label x={630} y={167} size={78} width={1050} opacity={a}>More than <span style={{color:C.green}}>audio.</span></Label>
  <Label x={633} y={277} size={27} color={C.muted} weight={500} opacity={a}>A reference becomes somewhere to explore.</Label>
  <Connector x1={554} y1={515} x2={780} y2={410} grow={b}/>
  <Photo src="assets/notes-beijing.jpg" x={810+100*(1-b)} y={360} w={460} h={284} opacity={b} rotate={-4+drift(f)*1.5} scale={zoom}/>
  <Tag x={938} y={322} opacity={b}>PHOTO</Tag>
  <Connector x1={555} y1={660} x2={1320} y2={740} grow={c}/>
  <Photo src="assets/notes-dvd.jpg" x={1278+120*(1-c)} y={608} w={444} h={290} opacity={c} rotate={3-drift(f,.7)} scale={zoom}/>
  <Tag x={1405} y={572} opacity={c}>PLACE</Tag>
  <Card x={669} y={700+80*(1-e)} w={520} h={170} opacity={e} fill={C.pale} border={C.green}><div style={{padding:28,fontSize:23,lineHeight:1.28}}><strong style={{fontSize:32}}>Audio → environment</strong><br/><span style={{color:C.muted}}>Photos, places, names, context.</span></div></Card>
 </>;
};

const Comments:React.FC<{f:number;d:number}>=({f,d})=>{
 const a=pop(f,0,22),b=pop(f,100,23),c=pop(f,220,23),e=pop(f,345,23);
 return <>
  <Phone src="assets/ui-comments-redacted.jpg" x={130} y={165} w={420} h={740} scale={.92+.08*a}/>
  <Label x={677} y={177} size={74} width={1110} opacity={a}>The same moment,<br/><span style={{color:C.green}}>many listeners.</span></Label>
  <div style={{position:'absolute',left:685,top:437,width:980,height:7,borderRadius:5,background:C.line}}><div style={{height:7,background:C.green,width:`${Math.min(f/d,1)*100}%`,borderRadius:5}}/></div>
  <Tag x={820} y={394} opacity={b}>02:33</Tag>
  <div style={{position:'absolute',left:888,top:428,width:25,height:25,background:C.green,borderRadius:'50%',opacity:b}}/>
  <Connector x1={900} y1={455} x2={790} y2={565} grow={b}/>
  <Connector x1={900} y1={455} x2={1230} y2={590} grow={c}/>
  <Connector x1={900} y1={455} x2={1420} y2={720} grow={e}/>
  <Card x={681} y={570} w={340} h={94} opacity={b}><div style={{padding:29,fontSize:27,fontWeight:800}}>a memory</div></Card>
  <Card x={1110} y={608} w={390} h={94} opacity={c}><div style={{padding:29,fontSize:27,fontWeight:800}}>a reaction</div></Card>
  <Card x={1350} y={753} w={340} h={94} opacity={e} fill={C.pale}><div style={{padding:29,fontSize:27,fontWeight:800}}>a reply</div></Card>
  <Label x={683} y={829} size={21} weight={500} color={C.muted} opacity={e}>Graphic labels summarize the interaction; the phone shows the real comments page.</Label>
 </>;
};

const Memory:React.FC<{f:number;d:number}>=({f})=>{
 const a=pop(f,0,24),b=pop(f,120,25),c=pop(f,265,24),e=pop(f,410,25);
 const num=Math.round(100*clamp((f-120)/125));
 return <>
  <Label x={120} y={170} size={72} width={990} opacity={a}>Listening leaves<br/><span style={{color:C.green}}>a trail.</span></Label>
  <Card x={105} y={455} w={765} h={316} opacity={a} fill="#242525" border="#242525"><Img src={staticFile('assets/ui-listening-hours.jpg')} style={{width:'100%',height:'100%',objectFit:'contain'}}/></Card>
  <Tag x={115} y={792} opacity={a}>TOTAL APP LISTENING</Tag>
  <Connector x1={875} y1={619} x2={1090} y2={619} grow={b}/>
  <Card x={1110} y={217+60*(1-b)} w={602} h={602} opacity={b} fill="#202124" border="#202124"><Img src={staticFile('assets/ui-stickers.jpg')} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:'center 40%'}}/></Card>
  <Card x={935} y={749} w={740} h={124} opacity={c} fill={C.pale} border={C.green}><div style={{display:'flex',alignItems:'center',height:'100%',padding:'0 30px',gap:28}}><span style={{fontSize:57,fontWeight:800,color:C.green}}>{num}</span><div><div style={{fontSize:24,fontWeight:800}}>HOURS WITH ONE CREATOR</div><div style={{fontSize:18,color:C.muted}}>A sticker can appear on the profile</div></div></div></Card>
  <div style={{position:'absolute',left:1070,top:890,width:580,height:8,background:C.line,borderRadius:6,opacity:e}}><div style={{width:`${num}%`,height:8,background:C.green,borderRadius:6}}/></div>
 </>;
};

const Critique:React.FC<{f:number;d:number}>=({f})=>{
 const a=pop(f,0,22),b=pop(f,145,22),c=pop(f,310,24),e=pop(f,470,22);
 return <>
  <Label x={116} y={175} size={77} width={1100} opacity={a}>Where it <span style={{color:C.green}}>fits.</span></Label>
  <Card x={130} y={320} w={790} h={420} opacity={a} fill="#fff"><div style={{padding:46}}><div style={{fontSize:24,fontWeight:800,color:C.green,letterSpacing:2}}>MY EXPERIENCE</div><div style={{fontSize:48,fontWeight:800,lineHeight:1.15,marginTop:34}}>A home for Chinese-language podcast discovery.</div><div style={{fontSize:24,color:C.muted,marginTop:26}}>That focus is part of why I like it.</div></div></Card>
  <Card x={1040} y={320} w={710} h={420} opacity={b} fill="#fff"><div style={{padding:46}}><div style={{fontSize:24,fontWeight:800,color:C.green,letterSpacing:2}}>A PERSONAL LIMIT</div><div style={{fontSize:46,fontWeight:800,lineHeight:1.15,marginTop:34}}>English-first listeners may need a different mix.</div><div style={{fontSize:24,color:C.muted,marginTop:26}}>It depends on what they listen to.</div></div></Card>
  <Connector x1={926} y1={529} x2={1038} y2={529} grow={b}/>
  <Tag x={390} y={801} opacity={c}>WEB LISTENING EXISTS</Tag>
  <Tag x={895} y={801} filled opacity={c}>I STILL REACH FOR THE PHONE</Tag>
  <div style={{position:'absolute',left:134,top:878,width:1570,height:3,background:C.line,opacity:e}}><div style={{height:3,width:`${Math.max(0,(f-470)/160)*100}%`,maxWidth:'100%',background:C.green}}/></div>
  <Label x={686} y={889} size={19} weight={600} color={C.muted} opacity={e}>A preference, not an absent feature.</Label>
 </>;
};

const Ending:React.FC<{f:number;d:number}>=({f})=>{
 const a=pop(f,0,18),c=pop(f,215,22),e=pop(f,340,24);
 const orbit=[['FOLK CULTURE',1150,260,95],['TRAVEL',1520,415,154],['PLACES',1320,765,230],['STORIES',920,720,297]] as const;
 return <>
  <div style={{position:'absolute',left:920,top:210,width:680,height:680,borderRadius:'50%',overflow:'hidden',opacity:.22*a}}><Img src={staticFile('assets/train-listener-editorial.png')} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:'75% center',scale:1+f*.0003}}/></div>
  <div style={{position:'absolute',left:920,top:210,width:680,height:680,border:`2px dashed ${C.line}`,borderRadius:'50%',rotate:`${f*.08}deg`}}/>
  <Img src={staticFile('assets/xdoctor-cover.jpg')} style={{position:'absolute',left:1200,top:468,width:170,height:170,borderRadius:32,opacity:a,scale:.7+.3*a}}/>
  {orbit.map(([name,x,y,t],i)=><React.Fragment key={name}><Connector x1={1285} y1={548} x2={x+35} y2={y+22} grow={pop(f,t,27)} stroke={2}/><Tag x={x+drift(f,i+1)*8} y={y+drift(f,i+2)*8} opacity={pop(f,t,24)}>{name}</Tag></React.Fragment>)}
  <Label x={118} y={260} size={68} width={850} opacity={a}>I came for<br/><span style={{color:C.green}}>one podcast.</span></Label>
  <Label x={118} y={516} size={70} width={900} opacity={c}>I stayed for<br/><span style={{color:C.green}}>many more.</span></Label>
  <Img src={staticFile('assets/little-universe-icon.png')} style={{position:'absolute',left:1150,top:430,width:270,height:270,borderRadius:58,opacity:e,scale:.6+.4*e,boxShadow:'0 25px 55px #164b2e3f'}}/>
  <Label x={120} y={805} size={24} weight={500} color={C.muted} opacity={e}>Little Universe · 小宇宙</Label>
 </>;
};

const visuals=[Hook,Origin,Interface,Discovery,Intimacy,Notes,Comments,Memory,Critique,Ending];
export const BeatScene:React.FC<BeatProps>=({index,duration,start,total,title})=>{
 const f=useCurrentFrame(); const Visual=visuals[index];
 const push=clamp(f/duration);
 return <Base section={title} index={index} progress={(start+f)/total}>
  <div style={{position:'absolute',inset:0,transform:`translate(${(index%2?1:-1)*push*9}px,${-push*9}px) scale(${1+push*.018})`,transformOrigin:'center center'}}><Visual f={f} d={duration}/></div>
 </Base>;
};
