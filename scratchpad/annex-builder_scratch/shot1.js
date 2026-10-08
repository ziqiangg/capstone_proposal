const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1100,height:900},deviceScaleFactor:2});
await p.goto('file:///home/user/capstone_proposal/benchtest/helpful_explanation/nemo-rails-explained.html');
await p.evaluate(()=>{document.querySelectorAll('section.overview svg text').forEach(t=>{if(/diagrams? \d/.test(t.textContent))t.remove();});});
const el=await p.$('section.overview figure svg');
await el.screenshot({path:'figures/figure1_guardrail_checkpoints.png'});await b.close();})();
