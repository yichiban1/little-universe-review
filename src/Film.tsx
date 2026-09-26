import React from 'react';
import {AbsoluteFill, Audio, Sequence, staticFile, useCurrentFrame} from 'remotion';
import timing from './timing.json';
import captions from './captions.json';
import {BeatScene} from './SecondEdit';

const FPS=30;
const frameOf=(ms:number)=>Math.round(ms/1000*FPS);
export const totalFrames=Math.ceil(timing.durationMs/1000*FPS);

const CaptionLayer:React.FC=()=>{
 const ms=useCurrentFrame()/FPS*1000;
 const caption=captions.find(c=>ms>=c.startMs-60&&ms<c.endMs+120);
 if(!caption)return null;
 return <div style={{position:'absolute',left:290,right:290,bottom:44,zIndex:50,display:'flex',justifyContent:'center',pointerEvents:'none'}}><div style={{background:'#0a2019a8',color:'#fff',padding:'5px 13px',font:'600 27px/1.18 Arial, Helvetica, sans-serif',textAlign:'center',borderRadius:5,textShadow:'0 1px 3px #0009',maxWidth:1130}}>{caption.text}</div></div>;
};

const sfx:{beat:string;fraction:number;kind:string;volume:number}[]=[
 {beat:'hook',fraction:.20,kind:'swipe',volume:.7},{beat:'hook',fraction:.40,kind:'tap',volume:.8},{beat:'hook',fraction:.60,kind:'riser',volume:.5},
 {beat:'player',fraction:.20,kind:'tap',volume:.48},{beat:'player',fraction:.40,kind:'cue',volume:.35},{beat:'player',fraction:.60,kind:'tap',volume:.45},
 {beat:'discovery',fraction:.20,kind:'swipe',volume:.35},{beat:'discovery',fraction:.60,kind:'cue',volume:.34},
 {beat:'intimacy',fraction:.40,kind:'riser',volume:.22},
 {beat:'notes',fraction:.20,kind:'swipe',volume:.34},{beat:'notes',fraction:.40,kind:'paper',volume:.58},{beat:'notes',fraction:.80,kind:'paper',volume:.55},
 {beat:'comments',fraction:.20,kind:'tap',volume:.45},{beat:'comments',fraction:.40,kind:'cue',volume:.22},{beat:'comments',fraction:.80,kind:'tap',volume:.37},
 {beat:'history',fraction:.20,kind:'cue',volume:.4},{beat:'history',fraction:.60,kind:'cue',volume:.36},
 {beat:'judgement',fraction:.42,kind:'swipe',volume:.28},{beat:'judgement',fraction:.70,kind:'riser',volume:.28}
];

export const Film:React.FC=()=> <AbsoluteFill>
 {timing.beats.map((beat,index)=>{
  const start=frameOf(beat.startMs);
  const duration=(index===timing.beats.length-1?totalFrames:frameOf(timing.beats[index+1].startMs))-start;
  return <Sequence key={beat.id} from={start} durationInFrames={duration}><BeatScene index={index} duration={duration}/></Sequence>;
 })}
 <Audio src={staticFile('audio/music-second-edit.mp3')} volume={(f)=>f<45?.33: f>totalFrames-105?.43:.25}/>
 <Audio src={staticFile('audio/narration-master.mp3')} volume={1}/>
 {sfx.map((cue,i)=>{const index=timing.beats.findIndex(b=>b.id===cue.beat);if(index<0)return null;const start=frameOf(timing.beats[index].startMs),end=index===timing.beats.length-1?totalFrames:frameOf(timing.beats[index+1].startMs);return <Sequence key={i} from={start+Math.round((end-start)*cue.fraction)}><Audio src={staticFile(`audio/sfx-${cue.kind}.mp3`)} volume={()=>cue.volume}/></Sequence>})}
 <CaptionLayer/>
 </AbsoluteFill>;
