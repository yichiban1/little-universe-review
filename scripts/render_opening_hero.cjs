const {bundle}=require('@remotion/bundler');
const {getCompositions,openBrowser,renderMedia,renderStill}=require('@remotion/renderer');
const {enableTailwind}=require('@remotion/tailwind-v4');
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..'),a=path.join(root,'analysis');
(async()=>{
 const serveUrl=await bundle({entryPoint:path.join(root,'src/index.ts'),rspack:true,bundlerOverride:enableTailwind,outDir:path.join(root,'dist/opening-hero')});
 const browser=await openBrowser('chrome');
 try{
  const comps=await getCompositions({serveUrl,puppeteerInstance:browser});
  const baseline=comps.find(c=>c.id==='LittleUniverseReviewHeroPolish'),next=comps.find(c=>c.id==='LittleUniverseReviewOpeningHero');
  if(process.argv.includes('--stills')){
   const d=path.join(a,'opening-hero-native');fs.mkdirSync(d,{recursive:true});
   for(const frame of [0,124,155,195,215,240,265,285,310,342,405,450,490,520,538,550,570])await renderStill({serveUrl,composition:next,frame,output:path.join(d,`f${String(frame).padStart(4,'0')}.png`),imageFormat:'png',puppeteerInstance:browser,logLevel:'error'});
   console.log('17 native frame checks complete');return;
  }
  if(process.argv.includes('--preserve')){
   const d=path.join(a,'opening-hero-preserved-frames');fs.mkdirSync(d,{recursive:true});const results=[];
   const hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
   for(const frame of [577,578,657,1020,1391,1778,1900,2500,3000,3600,4200,4652,5058,5519]){
    const files=[];
    for(const [tag,composition] of [['baseline',baseline],['opening',next]]){
     const output=path.join(d,`${tag}-f${frame}.png`);files.push(output);await renderStill({serveUrl,composition,frame,output,imageFormat:'png',puppeteerInstance:browser,logLevel:'error'});
    }
    const identical=hash(files[0])===hash(files[1]);results.push({frame,identical});if(!identical)throw new Error(`Protected frame changed ${frame}`);
   }
   fs.writeFileSync(path.join(a,'opening-hero-frame-preservation.json'),JSON.stringify({boundary:577,frames:results},null,2));console.log('14 protected frames PNG-byte-identical');return;
  }
  for(const [name,composition] of (process.argv.includes('--preview')?[['preview',next]]:[['baseline',baseline],['preview',next]])){
   await renderMedia({serveUrl,composition,codec:'h264',crf:16,imageFormat:'png',outputLocation:path.join(a,`opening-hero-${name}.mp4`),frameRange:[0,576],concurrency:4,puppeteerInstance:browser,logLevel:'error'});
   console.log(`${name} rendered: 577 frames at 1920x1080`);
  }
 }finally{await browser.close({silent:true});}
})().catch(e=>{console.error(e);process.exitCode=1;});
