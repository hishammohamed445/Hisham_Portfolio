const header=document.querySelector('[data-header]');
const menuBtn=document.querySelector('[data-menu-toggle]');
const nav=document.querySelector('[data-nav]');
const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function onScroll(){header?.classList.toggle('scrolled',window.scrollY>24)}
onScroll(); window.addEventListener('scroll',onScroll,{passive:true});
menuBtn?.addEventListener('click',()=>{const open=nav.classList.toggle('open');menuBtn.setAttribute('aria-expanded',String(open));document.body.style.overflow=open?'hidden':''});
nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menuBtn?.setAttribute('aria-expanded','false');document.body.style.overflow=''}));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav?.classList.contains('open')){nav.classList.remove('open');menuBtn?.setAttribute('aria-expanded','false');document.body.style.overflow='';menuBtn?.focus();}});
const reveals=[...document.querySelectorAll('.reveal')];
if(reduced){reveals.forEach(el=>el.classList.add('in-view'));}else{
  const io=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in-view');io.unobserve(e.target)}}),{threshold:.14,rootMargin:'0px 0px -40px 0px'});
  reveals.forEach(el=>io.observe(el));
}
const counters=[...document.querySelectorAll('[data-count]')];
if(!reduced && counters.length){
  const cio=new IntersectionObserver(entries=>entries.forEach(e=>{if(!e.isIntersecting)return; const el=e.target; const target=Number(el.dataset.count); const prefix=el.dataset.prefix||''; const suffix=el.dataset.suffix||''; const decimals=(String(target).split('.')[1]||'').length; const start=performance.now(); const dur=900; function tick(t){const p=Math.min(1,(t-start)/dur); const eased=1-Math.pow(1-p,3); const v=(target*eased).toFixed(decimals); el.textContent=prefix+v+suffix; if(p<1)requestAnimationFrame(tick)} requestAnimationFrame(tick); cio.unobserve(el)}),{threshold:.6});
  counters.forEach(c=>cio.observe(c));
}

// Premium interaction layer
const progressBar=document.querySelector('[data-scroll-progress]');
function updateProgress(){
  if(!progressBar)return;
  const max=document.documentElement.scrollHeight-window.innerHeight;
  const p=max>0?Math.min(1,Math.max(0,window.scrollY/max)):0;
  progressBar.style.transform=`scaleX(${p})`;
}
updateProgress();window.addEventListener('scroll',updateProgress,{passive:true});window.addEventListener('resize',updateProgress,{passive:true});

// Highlight current homepage section in the fixed navigation.
const navAnchors=[...document.querySelectorAll('.site-nav a[href*="#"]')];
const sectionPairs=navAnchors.map(a=>{
  const id=a.getAttribute('href').split('#')[1];
  return [a,document.getElementById(id)];
}).filter(([,section])=>section);
if(sectionPairs.length){
  const sio=new IntersectionObserver(entries=>{
    const visible=entries.filter(e=>e.isIntersecting).sort((a,b)=>b.intersectionRatio-a.intersectionRatio)[0];
    if(!visible)return;
    navAnchors.forEach(a=>a.classList.remove('is-active'));
    const pair=sectionPairs.find(([,s])=>s===visible.target);
    pair?.[0].classList.add('is-active');
  },{rootMargin:'-25% 0px -55% 0px',threshold:[0,.08,.2,.4,.6]});
  sectionPairs.forEach(([,s])=>sio.observe(s));
}

// Project imagery: subtle parallax, live spotlight and follow-cursor action bubble.
if(!reduced && window.matchMedia('(pointer:fine)').matches){
  document.querySelectorAll('[data-project-visual]').forEach(stage=>{
    const cursor=stage.querySelector('.project-cursor');
    const img=stage.querySelector('img');
    stage.addEventListener('pointermove',e=>{
      const r=stage.getBoundingClientRect();
      const x=e.clientX-r.left, y=e.clientY-r.top;
      const nx=(x/r.width-.5), ny=(y/r.height-.5);
      stage.style.setProperty('--mx',`${x}px`);
      stage.style.setProperty('--my',`${y}px`);
      stage.style.setProperty('--img-x',`${(-nx*7).toFixed(2)}px`);
      stage.style.setProperty('--img-y',`${(-ny*7).toFixed(2)}px`);
      if(cursor){cursor.style.left=`${x}px`;cursor.style.top=`${y}px`;}
    });
    stage.addEventListener('pointerleave',()=>{
      stage.style.setProperty('--mx','50%');stage.style.setProperty('--my','50%');
      stage.style.setProperty('--img-x','0px');stage.style.setProperty('--img-y','0px');
    });
  });
}

// Hero portrait responds gently to pointer position, while remaining still for touch/reduced-motion users.
const portraitStage=document.querySelector('[data-portrait-stage]');
if(portraitStage && !reduced && window.matchMedia('(pointer:fine)').matches){
  portraitStage.addEventListener('pointermove',e=>{
    const r=portraitStage.getBoundingClientRect();
    const nx=(e.clientX-r.left)/r.width-.5;
    const ny=(e.clientY-r.top)/r.height-.5;
    portraitStage.style.setProperty('--hero-x',`${(nx*10).toFixed(2)}px`);
    portraitStage.style.setProperty('--hero-y',`${(ny*8).toFixed(2)}px`);
  });
  portraitStage.addEventListener('pointerleave',()=>{
    portraitStage.style.setProperty('--hero-x','0px');portraitStage.style.setProperty('--hero-y','0px');
  });
}

// Light magnetic response on primary actions; intentionally very small.
if(!reduced && window.matchMedia('(pointer:fine)').matches){
  document.querySelectorAll('.btn').forEach(btn=>{
    btn.dataset.magnetic='';
    btn.addEventListener('pointermove',e=>{
      const r=btn.getBoundingClientRect();
      const x=(e.clientX-r.left-r.width/2)*.08;
      const y=(e.clientY-r.top-r.height/2)*.10;
      btn.style.transform=`translate3d(${x}px,${y}px,0)`;
    });
    btn.addEventListener('pointerleave',()=>{btn.style.transform='';});
  });
}
