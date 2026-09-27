// Render source frames, not UI automation. Compare frozen Hero to Polish at protected boundaries/chapters.
const {bundle}=require('@remotion/bundler');
const {getCompositions,openBrowser,renderStill}=require('@remotion/renderer');
const {enableTailwind}=require('@remotion/tailwind-v4');
const fs=require('node:fs');
const path=require('node:path');
const crypto=require('node:crypto');
const root=path.resolve(__dirname,'..');
const frames=[0,157,576,657,1017,1020,1021,1123,1390,1778,1900,2500,3000,3600,4200,4652,4906,5058,5480,5519];
const out=path.join(root,'analysis/hero-polish-preserved-frames');
fs.mkdirSync(out,{recursive:true});
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
(async()=>{
 const serveUrl=await bundle({entryPoint:path.join(root,'src/index.ts'),rspack:true,bundlerOverride:enableTailwind,outDir:path.join(root,'dist/hero-polish-frame-qa')});
 const browser=await openBrowser('chrome');
 try{
  const cs=await getCompositions({serveUrl,puppeteerInstance:browser,inputProps:{}});
  const old=cs.find(c=>c.id==='LittleUniverseReviewHero');
  const next=cs.find(c=>c.id==='LittleUniverseReviewHeroPolish');
  const results=[];
  for(const frame of frames){
   const files=[];
   for(const [name,composition] of [['hero',old],['polish',next]]){
    const output=path.join(out,`${name}-f${String(frame).padStart(4,'0')}.png`);
    await renderStill({serveUrl,composition,frame,output,imageFormat:'png',puppeteerInstance:browser,inputProps:{},logLevel:'error'});
    files.push(output);
   }
   const same=hash(files[0])===hash(files[1]);
   results.push({frame,time:frame/30,identicalPNG:same});
   if(!same)throw new Error(`Protected frame changed: ${frame}`);
  }
  fs.writeFileSync(path.join(root,'analysis/hero-polish-frame-preservation.json'),JSON.stringify({size:[1920,1080],frames:results},null,2));
  console.log(`${results.length} protected native frames byte-identical to Hero`);
 }finally{await browser.close({silent:true});}
})().catch(e=>{console.error(e);process.exitCode=1;});
