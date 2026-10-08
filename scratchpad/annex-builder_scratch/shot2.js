const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1150,height:500},deviceScaleFactor:2});
await p.goto('file:///home/user/capstone_proposal/scratchpad/annex-builder_scratch/fig2.html');
await (await p.$('#w')).screenshot({path:'figures/figure2_beacon_pipeline.png'});await b.close();})();
