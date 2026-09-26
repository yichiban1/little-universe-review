import React from 'react';
import {AbsoluteFill,Audio,Sequence,staticFile,useCurrentFrame,interpolate} from 'remotion';
import './fifth-fonts';
import shots from './shots-fifth.json';
import timing from './timing-fifth.json';
import captions from './captions-fifth.json';
import {FifthShot} from './FifthEdit';

const FPS=30;
const frame=(ms:number)=>Math.round(ms/1000*FPS);
export const fifthTotalFrames=Math.ceil(timing.durationMs/1000*FPS);
const byId=(id:string)=>shots.find(s=>s.id===id);
const chapter=(id:string)=>shots.find(s=>s.chapter===id)!.startMs/1000;

const FifthCaptions:React.FC=()=>{
 const ms=useCurrentFrame()/FPS*1000;
 const c=captions.find(x=>ms>=x.startMs-35 && ms<x.endMs+85);
 if(!c)return null;
 return <div style={{position:'absolute',left:220,right:220,bottom:44,zIndex:80,display:'flex',justifyContent:'center',pointerEvents:'none'}}><span style={{maxWidth:1400,padding:'8px 15px',background:'#08141bc9',color:'#fff',fontFamily:'Inter, sans-serif',fontWeight:500,fontSize:28,lineHeight:1.25,textAlign:'center',borderRadius:2,textShadow:'0 1px 2px #0006'}}>{c.text}</span></div>;
};

const cues:{shot:string;offset:number;type:'click'|'page';volume:number}[]=[
 {shot:'open-search',offset:7,type:'click',volume:.20},
 {shot:'open-player',offset:11,type:'click',volume:.22},
 {shot:'player-rewind',offset:9,type:'click',volume:.18},
 {shot:'notes-open',offset:8,type:'click',volume:.17},
 {shot:'notes-olympic',offset:6,type:'page',volume:.28},
 {shot:'notes-dvd',offset:6,type:'page',volume:.28},
 {shot:'comments-open',offset:6,type:'click',volume:.18},
 {shot:'history-stickers',offset:4,type:'page',volume:.21},
];
const musicTimes=[0,18,20,chapter('listening')-1,chapter('listening')+1,chapter('notes')-1,chapter('notes')+1,chapter('comments')-1,chapter('comments')+1,chapter('history')-1,chapter('history')+1,chapter('critical')-1,chapter('critical')+1,chapter('ending'),chapter('ending')+2,timing.durationMs/1000];
const musicLevels=[.15,.15,.115,.115,.085,.085,.105,.105,.075,.075,.11,.11,.075,.075,.16,.16];

export const FifthFilm:React.FC=()=> <AbsoluteFill style={{background:'#101820'}}>
 {shots.map((s,i)=>{const from=frame(s.startMs),to=i===shots.length-1?fifthTotalFrames:frame(s.endMs);return <Sequence key={s.id} from={from} durationInFrames={Math.max(1,to-from)}><FifthShot id={s.id} duration={to-from} globalStart={from}/></Sequence>;})}
 <Audio src={staticFile('audio/music-third-original.mp3')} volume={f=>{
  const t=f/FPS,fadeIn=Math.min(1,t/2),fadeOut=Math.min(1,(fifthTotalFrames/FPS-t)/4);
  return Math.max(0,interpolate(t,musicTimes,musicLevels,{extrapolateLeft:'clamp',extrapolateRight:'clamp'})*Math.min(fadeIn,fadeOut));
 }}/>
 <Audio src={staticFile('audio/narration-fifth.mp3')} volume={1}/>
 {cues.map((cue,i)=>{const s=byId(cue.shot);return s?<Sequence key={i} from={frame(s.startMs)+cue.offset} durationInFrames={33}><Audio src={staticFile(`audio/sfx-third-${cue.type}.mp3`)} volume={()=>cue.volume}/></Sequence>:null;})}
 <FifthCaptions/>
 </AbsoluteFill>;

