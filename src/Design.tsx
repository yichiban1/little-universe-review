import React from 'react';
import {AbsoluteFill, Img, staticFile, useCurrentFrame} from 'remotion';

export const C = {paper:'#f7f6f1', ink:'#152821', green:'#199a69', pale:'#e2f3e9', muted:'#788780', line:'#c9d8ce', yellow:'#f0c95c'};
export const clamp=(n:number,a=0,b=1)=>Math.min(b,Math.max(a,n));
export const ease=(n:number)=>1-Math.pow(1-clamp(n),3);
export const pop=(frame:number,at:number,d=16)=>ease((frame-at)/d);
export const drift=(frame:number,speed=1)=>Math.sin(frame*.025*speed);

export const Base:React.FC<{section:string; index:number; progress:number; children:React.ReactNode}> = ({section,index,progress,children})=>{
 const frame=useCurrentFrame();
 return <AbsoluteFill style={{background:C.paper,color:C.ink,fontFamily:'Arial, Helvetica, sans-serif',overflow:'hidden'}}>
   <div style={{position:'absolute',inset:0,backgroundImage:'radial-gradient(#d5ded3 1px, transparent 1px)',backgroundSize:'42px 42px',opacity:.25,translate:`${drift(frame)*8}px ${drift(frame,.7)*5}px`}}/>
   <div style={{position:'absolute',width:710,height:710,borderRadius:'50%',background:'#d6efe2',filter:'blur(115px)',opacity:.48,left:1050+drift(frame)*70,top:-300}}/>
   <div style={{position:'absolute',left:62,top:44,display:'flex',alignItems:'center',gap:14,zIndex:20}}>
     <Img src={staticFile('assets/little-universe-icon.png')} style={{width:45,height:45,borderRadius:12}}/>
     <span style={{fontSize:23,fontWeight:800,letterSpacing:-.7}}>Little Universe</span>
   </div>
   <div style={{position:'absolute',right:64,top:52,zIndex:20,fontSize:14,fontWeight:800,letterSpacing:2,color:C.muted}}>{String(index+1).padStart(2,'0')} / 10&nbsp; {section.toUpperCase()}</div>
   <div style={{position:'absolute',left:64,right:64,top:106,height:2,background:C.line,zIndex:20}}><div style={{height:'100%',width:`${progress*100}%`,background:C.green}}/></div>
   {children}
   <div style={{position:'absolute',left:66,bottom:27,fontSize:13,color:C.muted,letterSpacing:2,zIndex:20}}>A PERSONAL APP REVIEW</div>
   <div style={{position:'absolute',right:66,bottom:27,fontSize:13,color:C.muted,letterSpacing:2,zIndex:20}}>RMIT · 2026</div>
 </AbsoluteFill>;
};

export const Phone:React.FC<{src:string;x?:number;y?:number;w?:number;h?:number;scale?:number;rotate?:number;opacity?:number; imagePosition?:string}> = ({src,x=130,y=150,w=440,h=780,scale=1,rotate=0,opacity=1,imagePosition='center top'}) => <div style={{position:'absolute',left:x,top:y,width:w,height:h,borderRadius:50,padding:9,background:'#17221e',boxShadow:'0 34px 75px #12251e35, 0 7px 18px #12251e30',transform:`scale(${scale}) rotate(${rotate}deg)`,transformOrigin:'center center',opacity,zIndex:3}}>
 <div style={{width:'100%',height:'100%',borderRadius:42,overflow:'hidden',position:'relative',background:'#111'}}>
  <Img src={staticFile(src)} style={{width:'100%',height:'100%',objectFit:'cover',objectPosition:imagePosition}}/>
  <div style={{position:'absolute',top:10,left:'41%',width:'18%',height:17,borderRadius:20,background:'#101311'}}/>
 </div>
 </div>;

export const Card:React.FC<{x:number;y:number;w:number;h:number;children:React.ReactNode; rotate?:number; opacity?:number; fill?:string; border?:string; style?:React.CSSProperties}> = ({x,y,w,h,children,rotate=0,opacity=1,fill='#fff',border=C.line,style})=><div style={{position:'absolute',left:x,top:y,width:w,height:h,boxSizing:'border-box',background:fill,border:`1px solid ${border}`,borderRadius:25,boxShadow:'0 20px 45px #23382a18',overflow:'hidden',transform:`rotate(${rotate}deg)`,opacity,...style}}>{children}</div>;

export const Label:React.FC<{x:number;y:number;children:React.ReactNode;size?:number;weight?:number;color?:string;opacity?:number;width?:number;lineHeight?:number}> = ({x,y,children,size=30,weight=700,color=C.ink,opacity=1,width,lineHeight=1.06})=><div style={{position:'absolute',left:x,top:y,fontSize:size,fontWeight:weight,color,opacity,width,lineHeight,letterSpacing:size>55?-2:-.6}}>{children}</div>;

export const Tag:React.FC<{x:number;y:number;children:React.ReactNode;filled?:boolean;opacity?:number}> = ({x,y,children,filled=false,opacity=1})=><div style={{position:'absolute',left:x,top:y,padding:'11px 16px',background:filled?C.green:'#fff',border:`1px solid ${filled?C.green:C.line}`,color:filled?'white':C.ink,borderRadius:14,fontSize:18,fontWeight:800,letterSpacing:1,opacity}}>{children}</div>;

export const Photo:React.FC<{src:string;x:number;y:number;w:number;h:number;opacity?:number;rotate?:number;scale?:number}> = ({src,x,y,w,h,opacity=1,rotate=0,scale=1}) => <div style={{position:'absolute',left:x,top:y,width:w,height:h,padding:10,boxSizing:'border-box',borderRadius:22,background:'white',boxShadow:'0 22px 48px #12291b30',transform:`rotate(${rotate}deg) scale(${scale})`,opacity}}><Img src={staticFile(src)} style={{width:'100%',height:'100%',objectFit:'cover',borderRadius:12}}/></div>;

export const Connector:React.FC<{x1:number;y1:number;x2:number;y2:number;grow?:number;color?:string;stroke?:number}> = ({x1,y1,x2,y2,grow=1,color=C.green,stroke=3})=> <svg style={{position:'absolute',inset:0,pointerEvents:'none',overflow:'visible'}} width="1920" height="1080"><line x1={x1} y1={y1} x2={x1+(x2-x1)*grow} y2={y1+(y2-y1)*grow} stroke={color} strokeWidth={stroke} strokeLinecap="round"/><circle cx={x1+(x2-x1)*grow} cy={y1+(y2-y1)*grow} r="6" fill={color}/></svg>;

export const Wave:React.FC<{x:number;y:number;w:number;h:number;phase:number;color?:string;bars?:number}> = ({x,y,w,h,phase,color=C.green,bars=60})=><div style={{position:'absolute',left:x,top:y,width:w,height:h,display:'flex',alignItems:'center',justifyContent:'space-between',gap:3}}>{Array.from({length:bars},(_,i)=>{const q=Math.abs(Math.sin(i*.68+phase*.11)+.45*Math.sin(i*1.83-phase*.07)); return <div key={i} style={{flex:1,height:`${13+q*37}%`,background:color,borderRadius:10,opacity:.35+.55*Math.abs(Math.sin(i*.11+phase*.04))}}/>})}</div>;

export const CaptionLayer:React.FC<{captions:{text:string;startMs:number;endMs:number}[]}> = ({captions})=>{
 const frame=useCurrentFrame(); const ms=frame/30*1000;
 const caption=captions.find(c=>ms>=c.startMs-50&&ms<c.endMs+100);
 if(!caption)return null;
 return <div style={{position:'absolute',bottom:74,left:340,right:340,minHeight:64,zIndex:40,display:'flex',justifyContent:'center',alignItems:'center',pointerEvents:'none'}}><div style={{background:'#14251fdf',color:'white',fontSize:29,fontWeight:600,lineHeight:1.23,padding:'10px 22px',borderRadius:12,textAlign:'center',boxShadow:'0 6px 20px #17271c22'}}>{caption.text}</div></div>;
};
