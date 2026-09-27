import React from 'react';
import {AbsoluteFill,Easing,Img,interpolate,staticFile,useCurrentFrame} from 'remotion';
import {HeroPolishFilm} from './HeroPolishFilm';
import captions from './captions-fifth.json';

export const OPENING_END=577;
const C={dark:'#101820',deep:'#0a1319',cyan:'#25b7d8',ice:'#e6f8fa',white:'#f8fbfb',muted:'#94a9b0'};
type Box={x:number;y:number;w:number;h:number};
const p=(t:number,a:number,b:number)=>interpolate(t,[a,b],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp',easing:Easing.bezier(.42,0,.22,1)});
const lerp=(a:number,b:number,q:number)=>a+(b-a)*q;
const mix=(a:Box,b:Box,q:number):Box=>({x:lerp(a.x,b.x,q),y:lerp(a.y,b.y,q),w:lerp(a.w,b.w,q),h:lerp(a.h,b.h,q)});
const sq=(x:number,y:number,w:number):Box=>({x,y,w,h:w});
const dimensions:Record<string,[number,number]>={
 'xdoctor-cover-sixth.jpg':[1440,1440],'xdoctor-video-thumbnail.jpg':[1280,720],
 'web-xdoctor-programme-sixth.png':[600,900],'web-xdoctor-2008-sixth.png':[600,562],
 'xdoctor-episode-art-sixth.png':[1440,1440],'ui-player.jpg':[1206,2622],
 'ui-notes-photos.jpg':[1206,2622],'ui-comments-redacted.jpg':[1206,2622],
 'ui-listening-hours.jpg':[1100,440],'little-universe-icon.png':[1200,1200],
};
// Crops use original source pixels. Display bounds are checked on every frame.
const Raster:React.FC<{name:string;box:Box;crop?:[number,number,number,number];opacity?:number;reveal?:number;radius?:number}>=({name,box,crop,opacity=1,reveal=1,radius=0})=>{
 const [iw,ih]=dimensions[name];const [sx,sy,sw,sh]=crop??[0,0,iw,ih];const scale=box.w/sw;
 const limit=/^xdoctor-(cover|episode|video)/.test(name)?1.5:1.25;
 if(scale>limit+1e-6||sx<0||sy<0||sx+sw>iw||sy+sh>ih||box.h>sh*scale+.01)throw new Error(`Opening resolution: ${name} ${scale}x`);
 return <div style={{position:'absolute',left:box.x,top:box.y,width:box.w,height:box.h,overflow:'hidden',borderRadius:radius,opacity,clipPath:`inset(0 ${100*(1-reveal)}% 0 0)`}}><Img src={staticFile(`assets/${name}`)} style={{position:'absolute',left:-sx*scale,top:-sy*scale,width:iw*scale,height:ih*scale,maxWidth:'none'}}/></div>;
};
const Text:React.FC<{x:number;y:number;size:number;children:React.ReactNode;opacity?:number;color?:string;w?:number}>=({x,y,size,children,opacity=1,color=C.white,w=900})=><div style={{position:'absolute',left:x,top:y,width:w,fontFamily:size>=36?'Inter Tight, sans-serif':'Inter, sans-serif',fontSize:size,lineHeight:1.06,fontWeight:700,letterSpacing:size>=36?-1:0,color,opacity}}>{children}</div>;
// Exact supplied player crop: scale derives from the raster, not the phone border.
const initialPhone:Box={x:747,y:36,w:426,h:426*2622/1206};
const phoneArt=(b:Box)=>sq(b.x+164*b.w/1206,b.y+441*b.w/1206,876*b.w/1206);
const Phone:React.FC<{box:Box;opacity:number;reveal:number}>=({box,opacity,reveal})=><div style={{position:'absolute',left:box.x-5,top:box.y-5,width:box.w+10,height:box.h+10,border:'5px solid #29353b',borderRadius:36,overflow:'hidden',background:C.deep,opacity,boxShadow:'0 26px 75px #0006',clipPath:`inset(0 0 ${100*(1-reveal)}% 0)`}}>
 <div style={{position:'absolute',inset:0,clipPath:'polygon(evenodd,0% 0%,100% 0%,100% 100%,0% 100%,0% 0%,13.59% 16.82%,13.59% 50.23%,86.24% 50.23%,86.24% 16.82%,13.59% 16.82%)'}}><Raster name="ui-player.jpg" box={{x:0,y:0,w:box.w,h:box.h}}/></div>
 </div>;
const OpeningCaptions:React.FC=()=>{
 const ms=useCurrentFrame()/30*1000;const c=captions.find(x=>ms>=x.startMs-35&&ms<x.endMs+85);
 if(!c)return null;
 return <div style={{position:'absolute',left:220,right:220,bottom:44,zIndex:80,display:'flex',justifyContent:'center',pointerEvents:'none'}}><span style={{maxWidth:1400,padding:'8px 15px',background:'#08141bc9',color:'#fff',fontFamily:'Inter, sans-serif',fontWeight:500,fontSize:28,lineHeight:1.25,textAlign:'center',borderRadius:2,textShadow:'0 1px 2px #0006'}}>{c.text}</span></div>;
};
export const OpeningHero:React.FC=()=>{
 const t=useCurrentFrame()/30;
 const video=p(t,4.15,4.85),search=p(t,6.1,6.85),found=p(t,6.75,7.35),episode=p(t,7.99,8.75);
 const detach=p(t,9.1,10.05),enter=p(t,10.15,11.35),outward=p(t,14.3,15.15),collect=p(t,17.55,18.35),icon=p(t,18.0,18.5);
 const result=mix({x:700,y:300,w:650,h:340},{x:1060,y:150,w:650,h:609},episode);
 const cover=mix(mix(mix(sq(650,175,650),sq(315,215,560),p(t,0,.95)),sq(1390,700,166),video),sq(700+223*650/600,300+31*650/600,139*650/600),search);
 const programme=mix(cover,sq(result.x+333*650/600,result.y+133*650/600,31*650/600),episode);
 const webArt=sq(result.x+233*650/600,result.y+33*650/600,121*650/600);
 const phone=mix(mix(initialPhone,{x:740,y:90,w:370,h:370*2622/1206},outward),sq(500,440,30),collect);
 // Same high-resolution artwork travels from the real episode header into the phone.
 const art=mix(mix(webArt,sq(265,240,490),detach),phoneArt(initialPhone),enter);
 const finalArt=mix(mix(art,phoneArt({x:740,y:90,w:370,h:370*2622/1206}),outward),sq(500,440,30),collect);
 const rail=p(t,12.0,13.1),notes=p(t,14.458,15.05),comments=p(t,16.05,16.65),history=p(t,17.0,17.28);
 const timelineY=phone.y+1900*phone.w/1206;
 const dotX=lerp(lerp(initialPhone.x+96*initialPhone.w/1206,1500,rail),510,collect),dotY=lerp(timelineY,450,collect);
 const sheet=(b:Box)=>mix(b,{x:495,y:435,w:40,h:b.h/b.w*40},collect);
 return <AbsoluteFill style={{background:C.dark,overflow:'hidden',fontFamily:'Inter, sans-serif'}}>
  <div style={{position:'absolute',inset:0,background:C.ice,opacity:icon}}/>
  <div style={{opacity:(1-search)}}>
   <Raster name="web-xdoctor-programme-sixth.png" crop={[0,180,600,140]} box={{x:1060,y:355,w:650,h:151.667}} opacity={(1-video)*p(t,.3,1.15)}/>
   <Raster name="xdoctor-video-thumbnail.jpg" box={{x:lerp(955,250,video),y:lerp(240,115,video),w:lerp(450,1280,video),h:lerp(450,1280,video)*720/1280}} radius={18} reveal={video}/>
  </div>
  <div style={{position:'absolute',left:650,top:210,width:750*search,height:72,borderBottom:`3px solid ${C.cyan}`,overflow:'hidden',opacity:search*(1-episode),display:'flex',alignItems:'center',gap:20,color:C.white,fontSize:40,fontWeight:600}}><span>⌕</span><span>X Doctor</span></div>
  <div style={{position:'absolute',left:result.x,top:result.y,width:result.w,height:result.h*found,background:'#fff',borderRadius:12,overflow:'hidden',opacity:found*(1-enter)}}>
   <Raster name="web-xdoctor-programme-sixth.png" crop={[0,180,600,134]} box={{x:0,y:180*650/600,w:650,h:134*650/600}} opacity={1-episode}/>
   <Raster name="web-xdoctor-2008-sixth.png" crop={[0,172,600,390]} box={{x:0,y:172*650/600,w:650,h:390*650/600}} reveal={episode}/>
  </div>
  <Raster name="xdoctor-cover-sixth.jpg" box={programme} radius={lerp(18,3,episode)} opacity={1-p(t,9.0,9.4)}/>
  <Text x={1055} y={230} size={76} opacity={(1-video)*p(t,.3,1.15)}>X Doctor</Text>
  <Text x={lerp(265,1180,enter)} y={lerp(780,345,enter)} size={lerp(90,60,enter)} opacity={detach*(1-enter)}>2008.</Text>
  <Phone box={phone} opacity={enter*(1-icon)} reveal={enter}/>
  <svg width="1920" height="1080" style={{position:'absolute',inset:0,opacity:rail*(1-icon)}}>
   <path d={`M ${phone.x+96*phone.w/1206} ${dotY} H ${dotX}`} fill="none" stroke={C.cyan} strokeWidth="4"/>
   <path d={`M ${lerp(620,510,collect)} ${lerp(445,450,collect)} H ${lerp(650,510,collect)} V ${dotY} H ${dotX}`} fill="none" stroke={C.cyan} strokeWidth="2" opacity={notes*.55}/>
   <path d={`M ${lerp(1150,510,collect)} ${lerp(392,450,collect)} H ${lerp(1130,510,collect)} V ${dotY}`} fill="none" stroke={C.cyan} strokeWidth="2" opacity={comments*.55}/>
   <circle cx={dotX} cy={dotY} r={lerp(7,12,collect)} fill={C.cyan}/>
  </svg>
  <Raster name="ui-notes-photos.jpg" crop={[0,330,1206,1430]} box={sheet({x:160-35*(1-notes),y:240,w:440,h:1430*440/1206})} reveal={notes} opacity={1-icon} radius={12}/>
  <Raster name="ui-comments-redacted.jpg" crop={[0,280,1206,1050]} box={sheet({x:1190+35*(1-comments),y:230,w:475,h:1050*475/1206})} reveal={comments} opacity={1-icon} radius={12}/>
  <Raster name="ui-listening-hours.jpg" box={sheet({x:1185,y:675,w:490,h:196})} reveal={history} opacity={(1-icon)*.9} radius={8}/>
  <Raster name="xdoctor-episode-art-sixth.png" box={finalArt} opacity={episode*(1-icon)} radius={lerp(5,2,collect)}/>
  <Raster name="little-universe-icon.png" box={sq(245,232,535)} radius={105} opacity={icon}/>
  <Text x={850} y={300} size={100} color={C.dark} opacity={p(t,18.25,18.65)}>Little<br/>Universe</Text>
  <div style={{position:'absolute',left:852,top:545,width:690*p(t,18.4,18.8),height:12,background:C.cyan,borderRadius:12}}/>
 </AbsoluteFill>;
};
// Original film stays mounted: exact narration, music, SFX, caption timing and chapters.
// From frame 577 onwards this composition renders ONLY that original implementation.
export const OpeningHeroFilm:React.FC=()=>{
 const f=useCurrentFrame();return <AbsoluteFill><HeroPolishFilm/>{f<OPENING_END?<><OpeningHero/><OpeningCaptions/></>:null}</AbsoluteFill>;
};
