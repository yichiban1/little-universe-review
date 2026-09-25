import React from 'react';
import {AbsoluteFill, Audio, Sequence, staticFile} from 'remotion';
import timing from './timing.json';
import captions from './captions.json';
import {BeatScene} from './Scenes';
import {CaptionLayer} from './Design';

const FPS=30;
export const totalFrames=Math.ceil(timing.durationMs/1000*FPS);
const frameOf=(ms:number)=>Math.round(ms/1000*FPS);

export const Film:React.FC=()=> <AbsoluteFill>
  {timing.beats.map((beat,index)=>{
   const start=frameOf(beat.startMs);
   const duration=(index===timing.beats.length-1?totalFrames:frameOf(timing.beats[index+1].startMs))-start;
   return <Sequence key={beat.id} from={start} durationInFrames={duration}>
     <BeatScene index={index} duration={duration} start={start} total={totalFrames} title={beat.title}/>
     <Audio src={staticFile(`audio/${beat.id}.mp3`)} volume={1}/>
   </Sequence>;
  })}
  <Audio src={staticFile('audio/music.mp3')} volume={.23}/>
  <CaptionLayer captions={captions}/>
 </AbsoluteFill>;
