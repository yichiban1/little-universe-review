import React from 'react';
import {AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame, interpolate} from 'remotion';
import shots from './shots-third.json';
import timing from './timing-third.json';
import captions from './captions-third.json';
import {ThirdShot} from './ThirdEdit';

const FPS=30;
const frame=(ms:number)=>Math.round(ms/1000*FPS);
export const thirdTotalFrames=Math.ceil(timing.durationMs/1000*FPS);
const shotById=(id:string)=>shots.find(s=>s.id===id);

const Caption:React.FC=()=>{
 const f=useCurrentFrame(), ms=f/FPS*1000;
 const line=captions.find(c=>ms>=c.startMs-40 && ms<c.endMs+110);
 if(!line)return null;
 return <div style={{position:'absolute',left:180,right:180,bottom:32,zIndex:80,display:'flex',justifyContent:'center',pointerEvents:'none'}}><span style={{display:'inline-block',maxWidth:1510,padding:'7px 15px',background:'#08141bd9',color:'#fff',font:'600 30px/1.16 Arial, Helvetica, sans-serif',textAlign:'center',borderRadius:6,textShadow:'0 1px 2px #0008'}}>{line.text}</span></div>;
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

export const ThirdFilm:React.FC=()=> <AbsoluteFill style={{background:'#101820'}}>
 {shots.map((s,i)=>{
   const from=frame(s.startMs), to=i===shots.length-1?thirdTotalFrames:frame(s.endMs);
   return <Sequence key={s.id} from={from} durationInFrames={Math.max(1,to-from)}><ThirdShot id={s.id} duration={to-from} globalStart={from}/></Sequence>;
 })}
 <Audio src={staticFile('audio/music-third-original.mp3')} volume={(f)=>{
   const t=f/FPS;
   const fadeIn=Math.min(1,t/2),fadeOut=Math.min(1,(thirdTotalFrames/FPS-t)/4);
   const level=interpolate(t,[0,18,20,60,62,71,74,106,108,135,138,154,158,179],[.15,.15,.115,.115,.085,.085,.105,.105,.075,.075,.11,.11,.16,.16],{extrapolateLeft:'clamp',extrapolateRight:'clamp'});
   return Math.max(0,level*Math.min(fadeIn,fadeOut));
 }}/>
 <Audio src={staticFile('audio/narration-third.mp3')} volume={1}/>
 {cues.map((cue,i)=>{const shot=shotById(cue.shot);if(!shot)return null;return <Sequence key={i} from={frame(shot.startMs)+cue.offset} durationInFrames={33}><Audio src={staticFile(`audio/sfx-third-${cue.type}.mp3`)} volume={()=>cue.volume}/></Sequence>})}
 <Caption/>
 </AbsoluteFill>;
