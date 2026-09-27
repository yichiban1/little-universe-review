import React from 'react';
import {AbsoluteFill, Img, Easing, interpolate, staticFile, useCurrentFrame} from 'remotion';
import {SixthShot} from './SixthEdit';
import envelope from './voice-envelope-fifth.json';

const C={dark:'#101820',deep:'#0a1319',cyan:'#25b7d8',ice:'#e6f8fa',white:'#f8fbfb',muted:'#94a9b0'};
const dims:Record<string,[number,number]>={
 'xdoctor-episode-art-sixth.png':[1440,1440],'ui-player.jpg':[1206,2622],
 'web-xdoctor-2008-sixth.png':[600,562],'web-xdoctor-controls-sixth.png':[1888,69],
 'web-ritan-topic-sixth.png':[600,900],'web-ritan-programme-sixth.png':[600,900],
 'web-sound-programme-sixth.png':[600,900],'web-stochastic-programme-sixth.png':[600,900],
 'web-stochastic-episode-sixth.png':[600,900],
 'hero-stochastic-programme.jpg':[3000,3000],'discovery-ritan.jpg':[1400,1400],'discovery-stochastic.jpg':[3000,3000],
 'little-universe-icon.png':[1200,1200],
};
type Box={x:number;y:number;w:number;h:number};
const progress=(t:number,a:number,b:number,small=false)=>interpolate(t,[a,b],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp',easing:small?Easing.bezier(.2,.7,.25,1):Easing.bezier(.42,0,.22,1)});
const lerp=(a:number,b:number,p:number)=>a+(b-a)*p;
const mix=(a:Box,b:Box,p:number):Box=>({x:lerp(a.x,b.x,p),y:lerp(a.y,b.y,p),w:lerp(a.w,b.w,p),h:lerp(a.h,b.h,p)});
const square=(x:number,y:number,w:number):Box=>({x,y,w,h:w});
// Every rendered frame checks actual source crops and scale. Masks never excuse enlargement.
const Raster:React.FC<{name:string;box:Box;crop?:[number,number,number,number];opacity?:number;radius?:number;reveal?:number}>=({name,box,crop,opacity=1,radius=0,reveal=1})=>{
 const [iw,ih]=dims[name];const [sx,sy,sw,sh]=crop??[0,0,iw,ih];
 const s=box.w/sw;const limit=/^(hero-stochastic|discovery-|xdoctor-episode)/.test(name)?1.5:1.25;
 if(s>limit+1e-6||sx<0||sy<0||sx+sw>iw||sy+sh>ih||box.h>sh*s+.01)throw new Error(`Hero pixel gate: ${name} ${s}x crop ${crop}`);
 return <div style={{position:'absolute',left:box.x,top:box.y,width:box.w,height:box.h,overflow:'hidden',borderRadius:radius,opacity,clipPath:`inset(0 0 ${100*(1-reveal)}% 0)`}}><Img src={staticFile(`assets/${name}`)} style={{position:'absolute',left:-sx*s,top:-sy*s,width:iw*s,height:ih*s,maxWidth:'none'}}/></div>;
};
const Text:React.FC<{children:React.ReactNode;x:number;y:number;w?:number;size?:number;color?:string;opacity?:number;weight?:number}>=({children,x,y,w=850,size=64,color=C.white,opacity=1,weight=700})=><div style={{position:'absolute',left:x,top:y,width:w,fontFamily:size>=36?'Inter Tight, sans-serif':'Inter, sans-serif',fontSize:size,lineHeight:1.06,fontWeight:weight,letterSpacing:size>=36?-1:0,color,opacity,whiteSpace:'pre-line'}}>{children}</div>;
const Frame:React.FC<{box:Box;p:number;children:React.ReactNode}>=({box,p,children})=><div style={{position:'absolute',left:box.x,top:box.y,width:box.w,height:box.h,overflow:'hidden',borderRadius:lerp(8,36,p),border:`5px solid ${p>.5?'#29353b':'#94a9b0'}`,background:p>.5?C.deep:'#fff',boxShadow:'0 26px 75px #0006'}}>{children}</div>;
const Stage:React.FC<{children:React.ReactNode;light?:boolean}>=({children,light=false})=><AbsoluteFill style={{background:light?C.ice:C.dark,overflow:'hidden',fontFamily:'Inter, sans-serif'}}>{children}</AbsoluteFill>;
const phone:Box={x:740,y:30,w:468,h:468*2622/1206};
// Match Sixth's border-box phone and object-fit:cover, including its five-pixel border.
const phoneScale=(phone.h-10)/2622;
const phoneArt=square(745+164*phoneScale-(1206*phoneScale-458)/2,35+441*phoneScale,876*phoneScale);
const artHole='polygon(evenodd, 0% 0%, 100% 0%, 100% 100%, 0% 100%, 0% 0%, 12.7% 16.3%, 12.7% 51%, 87.5% 51%, 87.5% 16.3%, 12.7% 16.3%)';
const Mobile:React.FC<{box:Box;reveal?:number;hole?:boolean}>=({box,reveal=1,hole=false})=>{
 if(Math.max((box.w-10)/1206,(box.h-10)/2622)>1.25)throw new Error('Hero mobile pixel gate');
 return <div style={{position:'absolute',inset:0,clipPath:hole?artHole:undefined}}><div style={{position:'absolute',inset:0,clipPath:`inset(0 0 ${100*(1-reveal)}% 0)`}}><Img src={staticFile('assets/ui-player.jpg')} style={{width:'100%',height:'100%',objectFit:'cover'}}/></div></div>;
};
const ReturnWave:React.FC<{t:number;opacity:number}>=({t,opacity})=><div style={{position:'absolute',left:105,top:700,width:500,height:120,display:'flex',alignItems:'center',gap:3,opacity}}>{Array.from({length:70},(_,i)=>{const gf=Math.round(t*30),frame=Math.round(gf-60+i*120/69),v=envelope[Math.max(0,Math.min(envelope.length-1,frame))]??0;return <div key={i} style={{height:4+v*120*.92,width:500/70-3,background:C.cyan,borderRadius:4,opacity:frame<=gf?1:.35}}/>;})}</div>;

const Player:React.FC<{t:number}>=({t})=>{
 const expand=progress(t,21.917,22.75),reduce=progress(t,23.625,24.9),page=progress(t,27.55,28.45),back=progress(t,31.708,32.92);
 const huge=square(130,125,810),held=square(175,245,460);
 const art=mix(mix(mix(phoneArt,huge,expand),held,reduce),phoneArt,back);
 return <Stage>
  <div style={{opacity:1-expand}}><Frame box={phone} p={1}><Mobile box={{x:0,y:0,w:468,h:phone.h}} hole/></Frame></div>
  <Text x={82} y={65} size={22} color={C.cyan} opacity={1-back}>ARTWORK / THE SAME EPISODE</Text>
  <div style={{position:'absolute',inset:0,clipPath:`inset(0 ${100*(1-page)}% 0 0)`,opacity:1-back}}>
   <Text x={760} y={155} size={112}>2008.</Text>
   <Text x={765} y={298} size={49}>A memory, then a conversation.</Text>
   <Raster name="web-xdoctor-2008-sixth.png" crop={[0,172,600,390]} box={{x:1065,y:405,w:650,h:422.5}}/>
  </div>
  <Text x={760} y={370} size={64} w={970} opacity={reduce*(1-progress(t,27.3,27.55,true))*(1-back)}>A lot of cover.{'\n'}I look further down.</Text>
  <div style={{opacity:back}}><Frame box={phone} p={1}><Mobile box={{x:0,y:0,w:468,h:phone.h}} reveal={back} hole={t<32.92}/></Frame></div>
  <Raster name="xdoctor-episode-art-sixth.png" box={art} radius={lerp(14,6,back)} opacity={1-progress(t,32.94,33.14,true)}/>
  <ReturnWave t={t} opacity={back}/>
 </Stage>;
};

const Discovery:React.FC<{t:number}>=({t})=>{
 const select=progress(t,46.75,47.05,true),detach=progress(t,48.35,49.55),browse=progress(t,52.1,53.2),branch=progress(t,55.55,56.5),episode=progress(t,57.486,58.42);
 const pageX=lerp(1080,1030,detach);
 const row=mix({x:1080,y:331,w:650,h:99.667},{x:130,y:700,w:650,h:99.667},detach);
 const cover=mix(square(1095.17,342.5,67.17),square(170,245,390),detach);
 const ritan=mix(cover,square(115,135,100),branch);
 const blue=mix(square(170,245,390),square(250,330,290),episode);
 return <Stage light>
  <Text x={105} y={65} size={22} color={C.dark}>FOLLOWING A TOPIC</Text>
  <Text x={105} y={145} size={95} color={C.dark} opacity={1-detach}>Follow a topic.</Text>
  <Text x={110} y={265} size={45} color={C.dark} opacity={1-detach} weight={500}>History, through 日谈公园.</Text>
  <div style={{opacity:1-detach}}><Raster name="web-ritan-topic-sixth.png" box={{x:1080,y:55,w:650,h:900}}/></div>
  <div style={{position:'absolute',left:row.x-4,top:row.y-4,width:row.w+8,height:row.h+8,border:`3px solid ${C.cyan}`,borderRadius:6,opacity:select*(1-branch)}}/>
  <Raster name="web-ritan-topic-sixth.png" crop={[0,255,600,92]} box={row} opacity={1-branch}/>
  <div style={{position:'absolute',inset:0,clipPath:`inset(${100*(1-detach)}% 0 0 0)`}}>
   <Raster name="web-ritan-programme-sixth.png" crop={[0,178,600,722]} box={{x:pageX,y:180,w:650,h:782.167}} opacity={1-branch}/>
  </div>
  <div style={{position:'absolute',inset:0,clipPath:`inset(0 0 0 ${100*(1-browse)}%)`,opacity:1-branch}}>
   <Raster name="web-sound-programme-sixth.png" crop={[0,180,600,620]} box={{x:lerp(1940,1060,browse),y:210,w:650,h:671.667}}/>
  </div>
  <Text x={650} y={330} w={340} size={54} color={C.dark} opacity={detach*(1-browse)}>Search what{'\n'}comes up next.</Text>
  <Text x={140} y={840} size={30} color={C.dark} opacity={browse*(1-branch)}>日谈公园 → 声东击西</Text>
  <Raster name="discovery-ritan.jpg" box={ritan} radius={lerp(10,8,branch)}/>
  <div style={{position:'absolute',inset:0,clipPath:`inset(0 ${100*(1-branch)}% 0 0)`}}>
   <Text x={245} y={169} size={30} color={C.dark}>→</Text>
   <Text x={310} y={140} size={54} w={700} color={C.dark}>Stochastic Volatility.</Text>
   <Raster name="web-stochastic-programme-sixth.png" crop={[0,180,600,720]} box={{x:lerp(1720,1080,branch),y:180,w:650,h:780}} opacity={1-episode}/>
   <Raster name="web-stochastic-episode-sixth.png" box={{x:1080,y:lerp(960,70,episode),w:650,h:890}} reveal={episode}/>
   <Raster name="hero-stochastic-programme.jpg" box={blue} radius={10}/>
   <Text x={175} y={680} size={65} w={820} color={C.dark} opacity={episode}>Another story to open.</Text>
  </div>
 </Stage>;
};

const Critical:React.FC<{t:number}>=({t})=>{
 const p=progress(t,161.45,162.75),fit=progress(t,163.514,164.55);
 const b=mix({x:1080,y:150,w:650,h:650},{...phone,y:25},p);
 const art=mix(square(1080+5+233*650/600,150+5+33*650/600,121*650/600),{...phoneArt,y:phoneArt.y-5},p);
 const exit=mix(b,{x:240,y:240,w:225,h:489.18},fit);
 return <Stage>
  <Text x={110} y={290} size={88} opacity={1-p}>Web listening{'\n'}works too.</Text>
  <Text x={85} y={375} size={65} w={560} opacity={p*(1-fit)}>I still reach{'\n'}for my phone.</Text>
  <div style={{opacity:1-fit}}><Frame box={exit} p={p}>
   <Raster name="web-xdoctor-2008-sixth.png" box={{x:0,y:0,w:650,h:608.833}} opacity={1-p}/>
   <Mobile box={{x:0,y:0,w:exit.w,h:exit.w*2622/1206}} reveal={p} hole={t<162.75}/>
  </Frame></div>
  <Raster name="web-xdoctor-controls-sixth.png" box={{x:lerp(0,phone.x,p),y:lerp(835,825,p),w:lerp(1920,468,p),h:lerp(1920,468,p)*69/1888}} opacity={1-p}/>
  <Raster name="xdoctor-episode-art-sixth.png" box={art} radius={4} opacity={1-progress(t,162.65,162.9,true)}/>
  <Raster name="little-universe-icon.png" box={square(210,325,340)} radius={70} reveal={fit}/>
  <Text x={700} y={365} size={87} w={1100} opacity={fit}>The Chinese{'\n'}podcasts I follow.</Text>
 </Stage>;
};

export const HeroShot:React.FC<{id:string;duration:number;globalStart:number}>=({id,duration,globalStart})=>{
 const f=useCurrentFrame(),t=(globalStart+f)/30;
 if(['player-art','player-observation','player-title','player-return'].includes(id)&&t<33.9)return <Player t={t}/>;
 if(['feed-topic','feed-search','feed-programme','feed-discover','feed-select'].includes(id))return <Discovery t={t}/>;
 // Critical experiment did not earn inclusion; final Hero preserves Sixth here.
 return <SixthShot id={id} duration={duration} globalStart={globalStart}/>;
};

export const HeroExperimentShot:React.FC<{id:string;duration:number;globalStart:number}>=props=>{
 const t=(props.globalStart+useCurrentFrame())/30;
 if(['critical-web','critical-phone','critical-fit'].includes(props.id)&&t<168.5)return <Critical t={t}/>;
 return <HeroShot {...props}/>;
};
