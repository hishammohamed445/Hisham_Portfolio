from pathlib import Path
from textwrap import dedent

ROOT = Path('/mnt/data/hisham_portfolio')
AS = ROOT/'assets'
WORK = ROOT/'work'

projects = [
    {
        'slug':'vision-decision',
        'eyebrow':'FOUNDER / EDGE AI / INDUSTRIAL SAFETY',
        'title':'VISION & DECISION',
        'subtitle':'Turning existing cameras into reviewable safety intelligence.',
        'summary':'A working pre-pilot industrial computer-vision platform for PPE, falls, forklift-person proximity and restricted-zone events, built around a human-in-the-loop workflow.',
        'status':'Working MVP · Pre-pilot',
        'role':'Co-Founder · Acting CEO · Technical Product Lead',
        'stack':'Python · PyTorch · YOLO · OpenCV · ByteTrack · FastAPI · PostgreSQL · Redis · Docker · WebSockets',
        'metrics':[('87.22%','mAP@0.5 on forklift/person model'),('~15 FPS','multi-model runtime on RTX 4050'),('43/43','edge tests passing in the verified CV snapshot')],
        'accent':'#ff1a1a',
        'github':None,
        'body':[('The problem','Industrial cameras record enormous amounts of footage, but safety teams still need timely, reviewable events instead of raw video.'),('What I built','I worked across product direction, backend platform, pilot metrics, customer discovery and partnerships while co-building an edge-first perception pipeline that turns detections into evidence-backed incidents.'),('System thinking','The runtime combines object detection, tracking, temporal rules, zone logic and event aggregation, then pushes incidents through FastAPI, PostgreSQL, Redis and WebSockets to operational interfaces.'),('Design principle','Human-in-the-loop by default: the system supports safety teams with evidence and workflow, while final decisions remain with authorized HSE professionals.')],
        'visual':'vd'
    },
    {
        'slug':'factory-vision',
        'eyebrow':'IN PROGRESS / COMPUTER VISION / OPERATIONS',
        'title':'Factory Vision',
        'subtitle':'Truck, pallet and warehouse movement intelligence.',
        'summary':'An implementation program for vehicle entry, license-plate reading, pallet counting and warehouse movement tracking across a camera-rich factory environment.',
        'status':'Engineering in progress',
        'role':'System Design · CV Architecture · Data Preparation',
        'stack':'RT-DETRv2 · ByteTrack · PaddleOCR · FastAPI · PostgreSQL · JetStream · Object Storage · ERP/WMS integration',
        'metrics':[('5,097','validated LOCO images'),('151,428','matched bounding boxes'),('2,820 / 2,277','train / validation split')],
        'accent':'#3b5bff',
        'github':None,
        'body':[('The goal','Connect every truck visit to verified visual evidence, count pallet movements without double-counting, and carry those events into warehouse and ERP workflows.'),('Architecture','Cameras and readers feed edge inference and tracking workers; an event engine writes durable events, evidence and review state into the application zone and data layer.'),('Current evidence','Public logistics data has been cleaned and validated for a detection baseline. Factory-specific movement, identity and acceptance data is still awaiting site collection.'),('Integrity gate','No trained model is represented as complete yet. Plate data with unresolved usage terms is isolated from training until permission is documented.')],
        'visual':'factory'
    },
    {
        'slug':'donut-invoice-intelligence',
        'eyebrow':'DOCUMENT AI / TRANSFORMERS / FASTAPI',
        'title':'Donut Invoice Intelligence',
        'subtitle':'OCR-free structured extraction from receipts and invoices.',
        'summary':'A document-understanding pipeline that fine-tunes Donut to produce structured fields directly from pixels, with training, batch inference and an API layer.',
        'status':'Public engineering project',
        'role':'ML Engineering · Training · API Delivery',
        'stack':'Python · PyTorch · PyTorch Lightning · Hugging Face · Donut · FastAPI',
        'metrics':[('973','SROIE receipt images prepared'),('778 / 97 / 98','train / validation / test split'),('0.7747','best validation loss in the CV training run')],
        'accent':'#3b5bff',
        'github':'https://github.com/hishammohamed445/Donut-Invoice-Intelligence',
        'body':[('Why Donut','Traditional extraction often chains OCR, layout analysis and field rules. Donut treats the task as image-to-sequence generation and emits structured tokens directly.'),('Pipeline','The repository covers preprocessing, target sequence generation, training, checkpointing, early stopping, mixed precision, single/batch inference and a lightweight browser client.'),('API delivery','The FastAPI layer supports structured JSON responses and keeps model inference separated from the training code.'),('Evaluation honesty','The public repository intentionally does not claim accuracy/F1 until a reproducible held-out evaluation report is versioned. Training metrics are not presented as production quality.')],
        'visual':'donut'
    },
    {
        'slug':'agripheno-fusion',
        'eyebrow':'AGRI AI / MULTIMODAL / COMPUTER VISION',
        'title':'AgriPheno Fusion',
        'subtitle':'RGB + NIR + sensor fusion for crop-trait extraction.',
        'summary':'A tested engineering MVP for image quality checks, vegetation traits, NDVI statistics and weather/soil feature fusion, delivered by CLI and FastAPI.',
        'status':'Public MVP',
        'role':'Computer Vision · Sensor Fusion · API Engineering',
        'stack':'Python · OpenCV · NumPy · Pydantic · FastAPI · Docker · GitHub Actions',
        'metrics':[('10','automated tests passing'),('RGB + NIR','aligned image inputs'),('JSON','deterministic structured output')],
        'accent':'#3b5bff',
        'github':'https://github.com/hishammohamed445/AgriPheno-Fusion',
        'body':[('What it measures','Canopy cover, NDVI distribution, vegetation fractions, image-quality indicators, vapor-pressure deficit and canopy-air temperature delta.'),('Engineering choices','Inputs are validated aggressively; RGB and NIR dimensions must match; quality warnings remain visible instead of silently discarding data.'),('Reproducibility','Synthetic fixtures make the repository testable without bundling a large or ambiguously licensed dataset.'),('Boundary','The current stress score is explicitly labelled heuristic. Production use still requires calibrated geospatial inputs, stronger registration and ground-truth validation.')],
        'visual':'agri'
    },
    {
        'slug':'olist-recommender',
        'eyebrow':'RECOMMENDATION / NLP FEATURES / DATA SCIENCE',
        'title':'Olist Recommendation Engine',
        'subtitle':'Content-based discovery for a real e-commerce catalogue.',
        'summary':'A product recommendation system using TF-IDF, cosine similarity and Nearest Neighbors, evaluated with ranking metrics rather than only anecdotal examples.',
        'status':'Portfolio ML project',
        'role':'Data Preparation · Retrieval · Evaluation',
        'stack':'Python · Pandas · Scikit-learn · TF-IDF · Cosine Similarity · Nearest Neighbors',
        'metrics':[('Precision@K','ranking evaluation'),('Recall@K','coverage-oriented evaluation'),('NDCG@K','position-aware relevance')],
        'accent':'#3b5bff',
        'github':None,
        'body':[('Approach','Represent product content with TF-IDF, retrieve nearest items in vector space, and rank recommendations by semantic/content similarity.'),('Why this matters','Recommendation quality is measured as a ranking problem, not just by showing a few plausible neighbors.'),('Evaluation','Precision@K, Recall@K and NDCG@K provide complementary views of relevance, coverage and rank position.'),('Next step','A production version would combine content signals with behavioral interactions, cold-start handling and online experiment metrics.')],
        'visual':'olist'
    },
    {
        'slug':'alhana-erp',
        'eyebrow':'ENTERPRISE SOFTWARE / BACKEND / RELEASE ENGINEERING',
        'title':'ALHANA ERP Engineering',
        'subtitle':'Production-minded ERP architecture, controls and release readiness.',
        'summary':'Enterprise ERP engineering work spanning backend contracts, auditability, idempotency, data integrity, reporting semantics, operational recovery and release gates.',
        'status':'Private / enterprise work',
        'role':'Backend Engineering · Architecture · Production Readiness',
        'stack':'Python · FastAPI · PostgreSQL · Alembic · Monitoring · Audit/Event Patterns · Testing',
        'metrics':[('80','backend tests in a verified remediation snapshot'),('Audit-first','traceable business operations'),('Release gates','security, recovery and data integrity')],
        'accent':'#3b5bff',
        'github':None,
        'body':[('Scope','The work focuses on production controls around ERP behavior: authoritative transactions, versioning, approvals, audit trails, reporting definitions and recovery readiness.'),('Backend discipline','API contracts use validation, idempotency, optimistic concurrency and explicit state transitions to prevent silent business-state corruption.'),('Analytics discipline','KPIs and reports are treated as governed business definitions, with visible cutoffs and no unsupported aggregation across incompatible units or currencies.'),('Disclosure','Implementation details are intentionally limited here because parts of the engineering documentation are private/confidential.')],
        'visual':'erp'
    },
    {
        'slug':'mini-agent',
        'eyebrow':'AGENTIC AI / RAG / BACKEND',
        'title':'Mini Agent',
        'subtitle':'A compact foundation for RAG and agent workflows.',
        'summary':'A small public codebase used to practice the core engineering loop behind AI-agent systems: environment setup, FastAPI routing and minimal RAG/agent structure.',
        'status':'Learning / exploration project',
        'role':'AI Engineering · Backend Foundations',
        'stack':'Python · FastAPI · Environment Configuration · RAG / Agent Concepts',
        'metrics':[('FastAPI','service foundation'),('RAG','retrieval-oriented exploration'),('Git','iterative engineering workflow')],
        'accent':'#3b5bff',
        'github':'https://github.com/hishammohamed445/mini-agent',
        'body':[('Purpose','A deliberately small environment for understanding the moving parts of agentic systems before adding orchestration complexity.'),('Foundation','The repository establishes a runnable FastAPI project and a minimal structure for retrieval/agent experiments.'),('Learning direction','The broader focus is production-ready agent workflows that connect LLM reasoning to APIs, databases, calendars, documents and automation tools.'),('Why it belongs here','Not every portfolio project needs to be large. Small, focused repositories show how I learn, isolate problems and build reusable engineering foundations.')],
        'visual':'agent'
    },
]

# ---------- SVG assets ----------

def write(name, text):
    (AS/name).write_text(dedent(text).strip()+"\n", encoding='utf-8')

write('favicon.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#0a0a0a"/><path d="M15 17v30h7V35h20v12h7V17h-7v12H22V17z" fill="#fff"/><circle cx="50" cy="14" r="5" fill="#3b5bff"/></svg>
''')

write('hero-brush.svg', '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 240" fill="none"><path d="M31 169C142 47 296 31 420 82c88 36 158 105 240 51" stroke="#3B5BFF" stroke-width="34" stroke-linecap="round" opacity=".95"/><path d="M48 196c120-62 246-67 369-23 90 32 142 17 210-8" stroke="#3B5BFF" stroke-width="8" stroke-linecap="round" opacity=".45"/></svg>
''')

covers = {
'vd': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 720"><rect width="1200" height="720" fill="#090909"/><g stroke="#252525" stroke-width="1"><path d="M0 120h1200M0 240h1200M0 360h1200M0 480h1200M0 600h1200"/><path d="M200 0v720M400 0v720M600 0v720M800 0v720M1000 0v720"/></g><rect x="118" y="128" width="428" height="410" rx="28" fill="#121212" stroke="#343434"/><rect x="655" y="158" width="330" height="260" rx="12" fill="none" stroke="#ff1a1a" stroke-width="5"/><path d="M821 130v58M626 288h58M956 288h58M821 388v58" stroke="#ff1a1a" stroke-width="4"/><circle cx="820" cy="288" r="84" fill="#1b1b1b"/><circle cx="820" cy="288" r="28" fill="#ff1a1a"/><path d="M340 280h150M340 332h120M340 384h170" stroke="#d9d9d9" stroke-width="20" stroke-linecap="round"/><rect x="146" y="174" width="100" height="24" rx="12" fill="#ff1a1a"/><text x="118" y="610" fill="#fff" font-family="Arial" font-size="38" font-weight="700">SEE → UNDERSTAND → DECIDE → ACT</text></svg>''',
'factory': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 720"><rect width="1200" height="720" fill="#f0eee8"/><g stroke="#c9c6be" stroke-width="2"><path d="M80 160h1040M80 360h1040M80 560h1040"/><path d="M220 80v560M500 80v560M780 80v560M1060 80v560"/></g><path d="M150 510C340 510 317 254 520 254s160 236 370 236 171-198 264-198" fill="none" stroke="#3b5bff" stroke-width="14" stroke-linecap="round"/><g fill="#0a0a0a"><rect x="112" y="430" width="160" height="74" rx="18"/><circle cx="150" cy="518" r="24"/><circle cx="235" cy="518" r="24"/><rect x="510" y="205" width="110" height="90" rx="16"/><rect x="905" y="454" width="74" height="74" rx="8"/><rect x="1000" y="454" width="74" height="74" rx="8"/></g><g fill="#3b5bff"><circle cx="520" cy="254" r="18"/><circle cx="890" cy="490" r="18"/><circle cx="1154" cy="292" r="18"/></g><text x="90" y="110" fill="#0a0a0a" font-family="Arial" font-size="34" font-weight="700">GATE / DOCK / WAREHOUSE EVENT FLOW</text></svg>''',
'donut': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 720"><rect width="1200" height="720" fill="#0a0a0a"/><rect x="130" y="90" width="390" height="540" rx="24" fill="#fff"/><path d="M190 184h250M190 240h180M190 338h250M190 394h220M190 500h140" stroke="#b7b7b7" stroke-width="18" stroke-linecap="round"/><rect x="178" y="288" width="292" height="138" rx="12" fill="none" stroke="#3b5bff" stroke-width="6"/><path d="M560 356h145" stroke="#3b5bff" stroke-width="12" stroke-linecap="round"/><path d="m685 326 36 30-36 30" fill="none" stroke="#3b5bff" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/><rect x="755" y="205" width="340" height="310" rx="22" fill="#151515" stroke="#3b3b3b"/><text x="795" y="270" fill="#8ea2ff" font-family="monospace" font-size="30">{</text><text x="835" y="322" fill="#fff" font-family="monospace" font-size="24">"company": ...</text><text x="835" y="372" fill="#fff" font-family="monospace" font-size="24">"date": ...</text><text x="835" y="422" fill="#fff" font-family="monospace" font-size="24">"total": ...</text><text x="795" y="474" fill="#8ea2ff" font-family="monospace" font-size="30">}</text></svg>''',
'agri': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 720"><rect width="1200" height="720" fill="#f0eee8"/><rect x="90" y="110" width="460" height="460" rx="28" fill="#0a0a0a"/><path d="M314 468c-6-150 56-265 168-296-17 151-68 259-168 296Z" fill="#3b5bff"/><path d="M314 468c-38-111-110-175-203-177 18 108 85 175 203 177Z" fill="#8ea2ff"/><path d="M314 470c18-121 81-215 170-287M314 470c-43-91-111-145-198-167" fill="none" stroke="#f0eee8" stroke-width="8" stroke-linecap="round"/><g fill="#0a0a0a"><rect x="640" y="125" width="430" height="88" rx="20"/><rect x="640" y="244" width="430" height="88" rx="20"/><rect x="640" y="363" width="430" height="88" rx="20"/><rect x="640" y="482" width="430" height="88" rx="20"/></g><g fill="#fff" font-family="Arial" font-size="24" font-weight="700"><text x="685" y="180">CANOPY COVER</text><text x="685" y="299">NDVI DISTRIBUTION</text><text x="685" y="418">IMAGE QC</text><text x="685" y="537">SENSOR FUSION</text></g></svg>''',
'olist': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 720"><rect width="1200" height="720" fill="#0a0a0a"/><g stroke="#494949" stroke-width="3"><path d="M240 356 490 190 760 275 1000 154M240 356 500 500 760 275 1000 530M490 190 500 500M760 275 1000 530"/></g><g fill="#f0eee8"><circle cx="240" cy="356" r="68"/><circle cx="490" cy="190" r="48"/><circle cx="500" cy="500" r="48"/><circle cx="760" cy="275" r="58"/><circle cx="1000" cy="154" r="44"/><circle cx="1000" cy="530" r="44"/></g><circle cx="240" cy="356" r="24" fill="#3b5bff"/><path d="M120 620h960" stroke="#3b5bff" stroke-width="10" stroke-linecap="round"/><text x="120" y="110" fill="#fff" font-family="Arial" font-size="38" font-weight="700">VECTOR SPACE → NEIGHBORS → RANKING</text></svg>''',
'erp': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 720"><rect width="1200" height="720" fill="#f0eee8"/><rect x="90" y="90" width="1020" height="540" rx="28" fill="#fff" stroke="#d2cfc7"/><rect x="90" y="90" width="1020" height="86" rx="28" fill="#0a0a0a"/><circle cx="142" cy="133" r="10" fill="#3b5bff"/><circle cx="176" cy="133" r="10" fill="#696969"/><circle cx="210" cy="133" r="10" fill="#696969"/><g fill="#0a0a0a"><rect x="140" y="235" width="260" height="66" rx="10"/><rect x="140" y="330" width="260" height="66" rx="10"/><rect x="140" y="425" width="260" height="66" rx="10"/></g><g fill="#d9dcff"><rect x="470" y="235" width="560" height="48" rx="8"/><rect x="470" y="313" width="460" height="48" rx="8"/><rect x="470" y="391" width="520" height="48" rx="8"/><rect x="470" y="469" width="380" height="48" rx="8"/></g><path d="M140 560h890" stroke="#3b5bff" stroke-width="8" stroke-linecap="round"/></svg>''',
'agent': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 720"><rect width="1200" height="720" fill="#0a0a0a"/><g fill="#151515" stroke="#3a3a3a" stroke-width="2"><rect x="90" y="250" width="250" height="150" rx="30"/><rect x="475" y="90" width="250" height="150" rx="30"/><rect x="475" y="480" width="250" height="150" rx="30"/><rect x="860" y="250" width="250" height="150" rx="30"/></g><g stroke="#3b5bff" stroke-width="10" stroke-linecap="round"><path d="M340 325h160M600 240v240M725 165h135M725 555h135"/></g><g fill="#fff" font-family="Arial" font-size="28" font-weight="700"><text x="142" y="340">PROMPT</text><text x="520" y="178">RETRIEVE</text><text x="530" y="568">TOOLS</text><text x="910" y="340">ANSWER</text></g><circle cx="600" cy="355" r="62" fill="#3b5bff"/><text x="565" y="367" fill="#fff" font-family="Arial" font-size="28" font-weight="700">AI</text></svg>'''
}
for k,v in covers.items(): write(f'cover-{k}.svg', v)

# ---------- Shared HTML ----------
nav = '''
<header class="site-header" data-header>
  <a class="brand" href="{root}index.html" aria-label="Hisham Mohamed home"><span>HM</span><i></i></a>
  <button class="menu-toggle" data-menu-toggle aria-expanded="false" aria-controls="site-nav"><span></span><span></span></button>
  <nav class="site-nav" id="site-nav" data-nav>
    <a href="{root}index.html#work">Work</a>
    <a href="{root}index.html#profile">Profile</a>
    <a href="{root}index.html#stack">Stack</a>
    <a href="{root}index.html#journey">Journey</a>
    <a href="{root}index.html#contact">Contact</a>
  </nav>
  <a class="header-cta" href="{root}assets/Hisham_Mohamed_CV.pdf" target="_blank" rel="noopener">Resume <span>↗</span></a>
</header>
'''

footer = '''
<footer class="site-footer">
  <div class="footer-top"><p>Have a hard AI problem?</p><a href="mailto:hishamelbaaly@gmail.com">Let’s talk <span>↗</span></a></div>
  <div class="footer-grid">
    <div><strong>Hisham Mohamed</strong><span>AI Engineer · Computer Vision · Applied ML</span></div>
    <div><span>Cairo, Egypt</span><span>2026</span></div>
    <div><a href="https://github.com/hishammohamed445" target="_blank" rel="noopener">GitHub ↗</a><a href="https://www.linkedin.com/in/hisham-mohamed0" target="_blank" rel="noopener">LinkedIn ↗</a></div>
  </div>
</footer>
'''

head = '''
<head>
  <meta charset="utf-8" />\n  <script>document.documentElement.classList.add(\'js\')</script>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#f3f1ec" />
  <meta name="description" content="Hisham Mohamed — AI Engineer focused on computer vision, applied machine learning, backend AI systems and agentic workflows." />
  <link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root}styles.css" />
  <title>{title}</title>
</head>
'''

brush = '''<svg class="brush-svg" viewBox="0 0 700 240" aria-hidden="true" style="color:var(--accent)"><path class="brush-main" fill="none" stroke="#3b5bff" d="M31 169C142 47 296 31 420 82c88 36 158 105 240 51"/><path class="brush-ghost" fill="none" stroke="#3b5bff" d="M48 196c120-62 246-67 369-23 90 32 142 17 210-8"/></svg>'''

# ---------- Homepage ----------
project_cards=[]
for i,p in enumerate(projects):
    cls = 'project-card project-card--hero' if i==0 else 'project-card'
    link = f'work/{p["slug"]}.html'
    project_cards.append(f'''
      <article class="{cls} reveal" style="--project-accent:{p['accent']}">
        <a class="project-visual" href="{link}" aria-label="Read {p['title']} case study"><img src="assets/cover-{p['visual']}.svg" alt="" loading="lazy" /></a>
        <div class="project-copy">
          <div class="project-meta"><span>{p['eyebrow']}</span><span>{p['status']}</span></div>
          <h3><a href="{link}">{p['title']}</a></h3>
          <p>{p['summary']}</p>
          <div class="project-actions"><a class="text-link" href="{link}">View case study <span>→</span></a>{f'<a class="text-link secondary" href="{p["github"]}" target="_blank" rel="noopener">GitHub ↗</a>' if p['github'] else ''}</div>
        </div>
      </article>
    ''')

index = f'''<!doctype html>
<html lang="en">
{head.format(root='', title='Hisham Mohamed — AI Engineer')}
<body class="home">
<div class="noise" aria-hidden="true"></div>
{nav.format(root='')}
<main>
  <section class="hero shell" id="top">
    <div class="hero-copy">
      <div class="kicker reveal"><span class="status-dot"></span> AI ENGINEER · COMPUTER VISION · APPLIED ML</div>
      <h1 class="hero-title"><span class="line"><span>I build AI systems</span></span><span class="line"><span>that <em>see</em>, reason,</span></span><span class="line"><span>and ship.</span></span></h1>
      <p class="hero-deck reveal">From model training and evaluation to FastAPI services, real-time computer vision, data pipelines and production-minded product systems.</p>
      <div class="hero-actions reveal"><a class="btn btn-dark" href="#work">See the work <span>↓</span></a><a class="btn btn-ghost" href="https://github.com/hishammohamed445" target="_blank" rel="noopener">GitHub ↗</a></div>
      <div class="hero-note reveal"><span>Based in Cairo, Egypt</span><span>B.Sc. Artificial Intelligence · ERU · 2026</span></div>
    </div>
    <div class="hero-media reveal">
      <div class="portrait-frame"><img src="assets/hisham-headshot.webp" alt="Professional portrait of Hisham Mohamed" /></div>
      {brush}
      <div class="portrait-label"><strong>HISHAM MOHAMED</strong><span>AI / ML / CV</span></div>
    </div>
  </section>

  <section class="stats-strip" aria-label="Selected project metrics">
    <div class="shell stats-grid">
      <div class="stat reveal"><strong data-count="87.22" data-suffix="%">87.22%</strong><span>mAP@0.5 · forklift/person CV model</span></div>
      <div class="stat reveal"><strong data-count="15" data-prefix="~" data-suffix=" FPS">~15 FPS</strong><span>multi-model safety runtime · RTX 4050</span></div>
      <div class="stat reveal"><strong data-count="973">973</strong><span>SROIE receipt images · Donut project</span></div>
      <div class="stat reveal"><strong data-count="10">10</strong><span>automated tests · AgriPheno Fusion</span></div>
    </div>
  </section>

  <section class="section shell" id="work">
    <div class="section-head reveal"><div><span class="section-no">01</span><span class="section-kicker">SELECTED WORK</span></div><h2>Systems, not demos.</h2><p>I like projects where models have to survive contact with APIs, data, users, latency, testing and real operational constraints.</p></div>
    <div class="projects-grid">{''.join(project_cards)}</div>
    <div class="more-work reveal"><span>More experiments, utilities and earlier builds live on GitHub.</span><a class="btn btn-light" href="https://github.com/hishammohamed445?tab=repositories" target="_blank" rel="noopener">Browse all repositories ↗</a></div>
  </section>

  <section class="section profile-section" id="profile">
    <div class="shell split-editorial">
      <div class="section-label reveal"><span class="section-no">02</span><span class="section-kicker">PROFILE</span></div>
      <div class="profile-copy">
        <h2 class="reveal">I care about the part <em>after</em> the model works.</h2>
        <p class="lead reveal">I’m an Artificial Intelligence graduate and AI Engineer focused on computer vision, applied ML and production-ready AI services. I build across the lifecycle: data, training, evaluation, APIs, backend integration, testing and deployment.</p>
        <div class="profile-grid">
          <div class="profile-block reveal"><span>NOW</span><strong>Co-Founder & Technical Product Lead</strong><p>VISION & DECISION (V&D) — edge-first industrial safety intelligence using existing CCTV.</p></div>
          <div class="profile-block reveal"><span>EDUCATION</span><strong>B.Sc. Artificial Intelligence</strong><p>Egyptian Russian University (ERU), July 2026.</p></div>
          <div class="profile-block reveal"><span>FOCUS</span><strong>Computer Vision → AI Systems</strong><p>Real-time perception, document AI, recommendation, multimodal pipelines and agentic workflows.</p></div>
          <div class="profile-block reveal"><span>WORKING STYLE</span><strong>Measure before claim.</strong><p>I prefer explicit limits, reproducible tests and honest evaluation over inflated demo metrics.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section inverse" id="stack">
    <div class="shell">
      <div class="section-head light reveal"><div><span class="section-no">03</span><span class="section-kicker">STACK</span></div><h2>Model to product.</h2><p>A broad stack, organized around the job the system needs to do.</p></div>
      <div class="stack-grid">
        <div class="stack-card reveal"><span>01</span><h3>Computer Vision</h3><p>PyTorch · YOLO · OpenCV · ByteTrack · object detection · pose logic · tracking · zones · video analytics</p></div>
        <div class="stack-card reveal"><span>02</span><h3>ML & Data</h3><p>Scikit-learn · Pandas · NumPy · EDA · feature engineering · recommendation systems · model evaluation</p></div>
        <div class="stack-card reveal"><span>03</span><h3>Document & GenAI</h3><p>Hugging Face · Donut · NLP · TF-IDF · spaCy · prompt engineering · RAG · agent foundations</p></div>
        <div class="stack-card reveal"><span>04</span><h3>Backend & Delivery</h3><p>FastAPI · REST · WebSockets · PostgreSQL · Redis · Docker · Git/GitHub · Linux · API integration</p></div>
      </div>
    </div>
  </section>

  <section class="section shell" id="journey">
    <div class="section-head reveal"><div><span class="section-no">04</span><span class="section-kicker">JOURNEY</span></div><h2>Built by learning in public.</h2><p>Training that strengthened the engineering behind the projects.</p></div>
    <div class="timeline">
      <div class="timeline-row reveal"><time>2026</time><div><strong>B.Sc. in Artificial Intelligence</strong><span>Egyptian Russian University · July 2026</span></div></div>
      <div class="timeline-row reveal"><time>2026</time><div><strong>Deep Learning Course</strong><span>Egyptian Russian University · Jan–Feb 2026</span></div></div>
      <div class="timeline-row reveal"><time>2025</time><div><strong>Building LLM Applications with Prompt Engineering</strong><span>NVIDIA · Sep 2025</span></div></div>
      <div class="timeline-row reveal"><time>2025</time><div><strong>Big Data Analysis</strong><span>ITIDA & National Telecommunication Institute · 120 hours · Score 90%</span></div></div>
      <div class="timeline-row reveal"><time>2024–25</time><div><strong>Machine Learning Engineer Track</strong><span>Digital Egypt Pioneers Initiative (DEPI), MCIT · Nov 2024–May 2025</span></div></div>
    </div>
  </section>

  <section class="contact-section" id="contact">
    <div class="shell contact-inner">
      <span class="section-kicker reveal">05 · CONTACT</span>
      <h2 class="reveal">Let’s build something<br><em>useful.</em></h2>
      <p class="reveal">AI engineering, computer vision, applied ML, production AI systems — or a hard technical problem that needs structured thinking.</p>
      <div class="contact-actions reveal"><a class="btn btn-dark" href="mailto:hishamelbaaly@gmail.com">Email me ↗</a><a class="btn btn-ghost" href="https://www.linkedin.com/in/hisham-mohamed0" target="_blank" rel="noopener">LinkedIn ↗</a></div>
    </div>
  </section>
</main>
{footer}
<script src="script.js"></script>
</body>
</html>
'''
(ROOT/'index.html').write_text(index, encoding='utf-8')

# ---------- Project case study pages ----------
for p in projects:
    metric_html=''.join([f'<div class="case-metric"><strong>{a}</strong><span>{b}</span></div>' for a,b in p['metrics']])
    body_html=''.join([f'<div class="case-block reveal"><span>{i+1:02d}</span><div><h3>{h}</h3><p>{t}</p></div></div>' for i,(h,t) in enumerate(p['body'])])
    external = f'<a class="btn btn-dark" href="{p["github"]}" target="_blank" rel="noopener">Open GitHub ↗</a>' if p['github'] else '<a class="btn btn-dark" href="../index.html#contact">Discuss the project ↗</a>'
    page=f'''<!doctype html>
<html lang="en">
{head.format(root='../', title=p['title']+' — Hisham Mohamed')}
<body class="case-page" style="--case-accent:{p['accent']}">
<div class="noise" aria-hidden="true"></div>
{nav.format(root='../')}
<main>
  <section class="case-hero shell">
    <div class="case-title">
      <div class="kicker reveal">{p['eyebrow']}</div>
      <h1><span class="line"><span>{p['title']}</span></span></h1>
      <p class="reveal">{p['subtitle']}</p>
      <div class="case-actions reveal">{external}<a class="btn btn-ghost" href="../index.html#work">Back to work ←</a></div>
    </div>
    <div class="case-facts reveal"><div><span>STATUS</span><strong>{p['status']}</strong></div><div><span>ROLE</span><strong>{p['role']}</strong></div><div><span>STACK</span><strong>{p['stack']}</strong></div></div>
  </section>
  <section class="case-cover shell reveal"><img src="../assets/cover-{p['visual']}.svg" alt="Abstract visual for {p['title']}" /></section>
  <section class="case-summary shell"><div class="section-label reveal"><span class="section-no">01</span><span class="section-kicker">OVERVIEW</span></div><div><h2 class="reveal">{p['summary']}</h2><div class="case-metrics reveal">{metric_html}</div></div></section>
  <section class="case-story shell"><div class="section-label reveal"><span class="section-no">02</span><span class="section-kicker">CASE STUDY</span></div><div class="case-blocks">{body_html}</div></section>
  <section class="case-next"><div class="shell"><span class="section-kicker reveal">NEXT</span><h2 class="reveal">Back to the full body of work.</h2><a class="btn btn-light reveal" href="../index.html#work">Explore all projects →</a></div></section>
</main>
{footer}
<script src="../script.js"></script>
</body>
</html>'''
    (WORK/f'{p["slug"]}.html').write_text(page, encoding='utf-8')

# ---------- CSS ----------
css = r'''
:root{
  --black:#090909;--white:#fff;--sand:#f3f1ec;--accent:#3b5bff;--muted:rgba(9,9,9,.60);--line:rgba(9,9,9,.12);
  --radius-sm:12px;--radius-md:22px;--radius-lg:34px;--radius-xl:48px;
  --max:1320px;--ease:cubic-bezier(.16,1,.3,1);--fast:180ms;--base:280ms;--slow:720ms;
}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--sand);color:var(--black);font-family:"Nunito",system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased}a{color:inherit;text-decoration:none}img{max-width:100%;display:block}button{font:inherit}.shell{width:min(var(--max),calc(100% - 96px));margin-inline:auto}.noise{position:fixed;inset:0;pointer-events:none;z-index:9999;opacity:.035;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.65'/%3E%3C/svg%3E")}
.site-header{height:78px;position:fixed;top:0;left:0;right:0;z-index:100;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:0 max(32px,calc((100vw - var(--max))/2));transition:background var(--base) var(--ease),border-color var(--base) var(--ease);border-bottom:1px solid transparent}.site-header.scrolled{background:rgba(243,241,236,.88);backdrop-filter:blur(18px);border-color:var(--line)}.brand{font-size:21px;font-weight:800;display:inline-flex;align-items:flex-start;gap:4px;width:max-content}.brand i{width:7px;height:7px;border-radius:50%;background:var(--accent);margin-top:3px}.site-nav{display:flex;gap:30px;font-size:14px;font-weight:700}.site-nav a{position:relative}.site-nav a:after{content:"";position:absolute;left:0;right:100%;bottom:-6px;height:2px;background:var(--black);transition:right var(--base) var(--ease)}.site-nav a:hover:after,.site-nav a:focus-visible:after{right:0}.header-cta{justify-self:end;font-weight:800;font-size:14px}.header-cta span,.text-link span{display:inline-block;transition:transform var(--base) var(--ease)}.header-cta:hover span,.text-link:hover span{transform:translate(4px,-2px)}.menu-toggle{display:none;border:0;background:transparent;width:46px;height:46px;align-items:center;justify-content:center;flex-direction:column;gap:6px}.menu-toggle span{width:24px;height:2px;background:var(--black)}
.hero{min-height:100vh;padding-top:138px;padding-bottom:72px;display:grid;grid-template-columns:1.08fr .92fr;gap:64px;align-items:center}.kicker,.section-kicker{font-size:12px;font-weight:800;letter-spacing:.10em}.status-dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--accent);margin-right:10px}.hero-title{font-size:clamp(58px,6.4vw,104px);line-height:.91;letter-spacing:-.055em;margin:30px 0 30px;max-width:850px}.hero-title .line,.case-title h1 .line{display:block;overflow:hidden;padding-bottom:.07em}.hero-title .line>span,.case-title h1 .line>span{display:block;transform:translateY(110%);animation:titleIn 900ms var(--ease) forwards}.hero-title .line:nth-child(2)>span{animation-delay:90ms}.hero-title .line:nth-child(3)>span{animation-delay:180ms}@keyframes titleIn{to{transform:translateY(0)}}em{font-style:normal;color:var(--accent)}.hero-deck{font-size:20px;line-height:1.55;max-width:650px;color:var(--muted)}.hero-actions,.contact-actions,.case-actions{display:flex;gap:12px;margin-top:32px;flex-wrap:wrap}.btn{min-height:54px;padding:0 24px;border-radius:999px;display:inline-flex;align-items:center;justify-content:center;gap:16px;font-size:15px;font-weight:800;border:1px solid transparent;transition:transform var(--fast) var(--ease),background var(--fast),color var(--fast),border-color var(--fast)}.btn:hover{transform:translateY(-2px)}.btn-dark{background:var(--black);color:var(--white)}.btn-dark:hover{background:var(--accent)}.btn-ghost{border-color:rgba(9,9,9,.22)}.btn-ghost:hover{border-color:var(--black);background:#fff}.btn-light{background:#fff;color:#090909}.hero-note{display:flex;gap:24px;margin-top:58px;font-size:12px;font-weight:700;color:rgba(9,9,9,.5)}.hero-media{position:relative;min-height:650px;display:flex;align-items:flex-end;justify-content:center}.portrait-frame{position:relative;width:min(100%,520px);aspect-ratio:4/5;border-radius:42px;overflow:hidden;background:#fff;z-index:2;border:1px solid rgba(9,9,9,.08);clip-path:inset(100% 0 0 0 round 42px);animation:portraitIn 1s 140ms var(--ease) forwards}@keyframes portraitIn{to{clip-path:inset(0 0 0 0 round 42px)}}.portrait-frame img{width:100%;height:100%;object-fit:cover;object-position:50% 20%}.brush-svg{position:absolute;z-index:1;width:120%;left:-18%;bottom:13%;overflow:visible}.brush-main,.brush-ghost{fill:none;stroke:var(--accent);stroke-linecap:round;stroke-dasharray:1100;stroke-dashoffset:1100;animation:draw 1.4s .45s var(--ease) forwards}.brush-main{stroke-width:34}.brush-ghost{stroke-width:8;opacity:.45;animation-delay:.65s}@keyframes draw{to{stroke-dashoffset:0}}.portrait-label{position:absolute;z-index:3;right:0;bottom:40px;background:var(--black);color:#fff;padding:16px 18px;border-radius:16px;display:flex;flex-direction:column;font-size:11px;letter-spacing:.08em;box-shadow:0 16px 48px rgba(0,0,0,.14)}.portrait-label span{color:#9ca6ff;margin-top:4px}
.stats-strip{background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.stats-grid{display:grid;grid-template-columns:repeat(4,1fr)}.stat{padding:36px 28px;border-right:1px solid var(--line)}.stat:first-child{padding-left:0}.stat:last-child{border-right:0}.stat strong{display:block;font-size:42px;letter-spacing:-.05em}.stat span{font-size:12px;color:var(--muted);line-height:1.5}
.section{padding:140px 0}.section-head{display:grid;grid-template-columns:1.1fr 1fr;gap:60px;align-items:end;margin-bottom:72px}.section-head>div{grid-column:1/-1;display:flex;gap:18px}.section-no{font-size:12px;font-weight:800;color:var(--accent)}.section-head h2{font-size:clamp(48px,5vw,78px);line-height:.96;letter-spacing:-.045em;margin:0}.section-head p{font-size:18px;line-height:1.6;color:var(--muted);max-width:540px;margin:0}.projects-grid{display:grid;grid-template-columns:1fr 1fr;gap:28px}.project-card{background:#fff;border-radius:var(--radius-lg);overflow:hidden;border:1px solid rgba(9,9,9,.09)}.project-card--hero{grid-column:1/-1;display:grid;grid-template-columns:1.18fr .82fr;min-height:630px}.project-visual{display:block;overflow:hidden;background:#111}.project-card:not(.project-card--hero) .project-visual{aspect-ratio:16/10}.project-visual img{width:100%;height:100%;object-fit:cover;transition:transform 700ms var(--ease)}.project-card:hover .project-visual img{transform:scale(1.025)}.project-copy{padding:34px;display:flex;flex-direction:column}.project-card--hero .project-copy{padding:52px}.project-meta{display:flex;justify-content:space-between;gap:12px;font-size:10px;font-weight:800;letter-spacing:.08em;color:var(--muted)}.project-copy h3{font-size:36px;line-height:1;letter-spacing:-.035em;margin:60px 0 18px}.project-card--hero .project-copy h3{font-size:56px;margin-top:auto}.project-copy p{font-size:16px;line-height:1.6;color:var(--muted);margin:0 0 28px}.project-actions{display:flex;gap:18px;margin-top:auto}.text-link{font-size:14px;font-weight:800;display:inline-flex;gap:8px;align-items:center}.text-link.secondary{color:var(--muted)}.more-work{margin-top:32px;padding:32px 0;border-top:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:24px}.more-work span{font-size:15px;color:var(--muted)}
.profile-section{background:#fff}.split-editorial{display:grid;grid-template-columns:1fr 3fr;gap:90px}.section-label{display:flex;gap:15px;align-items:flex-start;padding-top:10px}.profile-copy h2{font-size:clamp(50px,5vw,82px);line-height:.95;letter-spacing:-.05em;margin:0 0 42px;max-width:900px}.profile-copy .lead{font-size:25px;line-height:1.5;max-width:900px;color:rgba(9,9,9,.72)}.profile-grid{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);margin-top:70px;border:1px solid var(--line)}.profile-block{background:#fff;padding:34px}.profile-block>span{font-size:10px;font-weight:800;letter-spacing:.1em;color:var(--accent)}.profile-block strong{display:block;font-size:21px;margin:22px 0 8px}.profile-block p{font-size:14px;line-height:1.6;color:var(--muted);margin:0}
.inverse{background:var(--black);color:#fff}.section-head.light p{color:rgba(255,255,255,.6)}.section-head.light .section-no{color:#8ea2ff}.stack-grid{display:grid;grid-template-columns:repeat(2,1fr);border-top:1px solid rgba(255,255,255,.16);border-left:1px solid rgba(255,255,255,.16)}.stack-card{padding:48px;border-right:1px solid rgba(255,255,255,.16);border-bottom:1px solid rgba(255,255,255,.16);min-height:260px}.stack-card>span{font-size:12px;color:#8ea2ff}.stack-card h3{font-size:34px;letter-spacing:-.03em;margin:54px 0 14px}.stack-card p{font-size:16px;line-height:1.65;color:rgba(255,255,255,.64);max-width:530px}
.timeline{border-top:1px solid var(--line)}.timeline-row{display:grid;grid-template-columns:150px 1fr;padding:28px 0;border-bottom:1px solid var(--line);align-items:start}.timeline-row time{font-size:12px;font-weight:800;color:var(--accent)}.timeline-row div{display:flex;justify-content:space-between;gap:30px}.timeline-row strong{font-size:18px}.timeline-row span{font-size:14px;color:var(--muted);text-align:right}
.contact-section{background:var(--accent);padding:130px 0}.contact-inner h2{font-size:clamp(64px,8vw,126px);line-height:.86;letter-spacing:-.06em;margin:38px 0;color:#fff}.contact-inner h2 em{color:#090909}.contact-inner p{font-size:20px;line-height:1.55;max-width:650px;color:rgba(255,255,255,.82)}.contact-section .btn-ghost{border-color:rgba(255,255,255,.5);color:#fff}.contact-section .btn-ghost:hover{background:#fff;color:#090909}.site-footer{background:#090909;color:#fff;padding:80px max(32px,calc((100vw - var(--max))/2)) 36px}.footer-top{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:72px;border-bottom:1px solid rgba(255,255,255,.18)}.footer-top p{font-size:16px;color:rgba(255,255,255,.55);margin:0}.footer-top a{font-size:clamp(44px,6vw,88px);line-height:.9;letter-spacing:-.05em;font-weight:800}.footer-grid{padding-top:28px;display:grid;grid-template-columns:2fr 1fr 1fr;gap:30px;font-size:12px;color:rgba(255,255,255,.55)}.footer-grid div{display:flex;flex-direction:column;gap:6px}.footer-grid strong,.footer-grid a{color:#fff}
.reveal{opacity:0;transform:translateY(24px);transition:opacity 750ms var(--ease),transform 750ms var(--ease)}.reveal.in-view{opacity:1;transform:none}
/* Case studies */
.case-page{--accent:var(--case-accent,#3b5bff)}.case-hero{min-height:86vh;padding-top:160px;padding-bottom:78px;display:grid;grid-template-columns:1.35fr .65fr;gap:70px;align-items:end}.case-title h1{font-size:clamp(72px,9vw,140px);line-height:.82;letter-spacing:-.065em;margin:28px 0 34px;max-width:1000px}.case-title p{font-size:24px;line-height:1.45;max-width:720px;color:var(--muted)}.case-facts{align-self:end;border-top:1px solid var(--line)}.case-facts>div{padding:20px 0;border-bottom:1px solid var(--line)}.case-facts span{display:block;font-size:10px;font-weight:800;letter-spacing:.1em;color:var(--accent);margin-bottom:9px}.case-facts strong{font-size:14px;line-height:1.55}.case-cover{border-radius:40px;overflow:hidden;background:#111}.case-cover img{width:100%;aspect-ratio:16/8.5;object-fit:cover}.case-summary,.case-story{padding:130px 0;display:grid;grid-template-columns:1fr 3fr;gap:90px}.case-summary h2{font-size:clamp(44px,4.8vw,74px);line-height:1;letter-spacing:-.045em;margin:0 0 64px;max-width:980px}.case-metrics{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid var(--line);border-left:1px solid var(--line)}.case-metric{padding:28px;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}.case-metric strong{font-size:34px;display:block;letter-spacing:-.035em}.case-metric span{font-size:12px;line-height:1.5;color:var(--muted)}.case-story{background:#fff;width:100%;max-width:none;padding-left:max(48px,calc((100vw - var(--max))/2));padding-right:max(48px,calc((100vw - var(--max))/2))}.case-blocks{border-top:1px solid var(--line)}.case-block{display:grid;grid-template-columns:80px 1fr;gap:22px;padding:36px 0;border-bottom:1px solid var(--line)}.case-block>span{font-size:12px;color:var(--accent);font-weight:800}.case-block h3{font-size:28px;margin:0 0 10px;letter-spacing:-.02em}.case-block p{font-size:17px;line-height:1.7;color:var(--muted);margin:0;max-width:820px}.case-next{padding:120px 0;background:var(--black);color:#fff}.case-next h2{font-size:clamp(52px,6vw,90px);letter-spacing:-.05em;margin:28px 0 42px;max-width:860px}
@media (max-width:1024px){.shell{width:min(var(--max),calc(100% - 56px))}.site-header{padding-inline:28px}.hero{grid-template-columns:1fr;min-height:auto;padding-top:140px}.hero-media{min-height:600px}.stats-grid{grid-template-columns:1fr 1fr}.stat:nth-child(2){border-right:0}.stat:nth-child(-n+2){border-bottom:1px solid var(--line)}.project-card--hero{grid-template-columns:1fr;min-height:0}.project-card--hero .project-visual{aspect-ratio:16/9}.project-card--hero .project-copy h3{margin-top:60px}.split-editorial,.case-summary,.case-story{grid-template-columns:1fr;gap:46px}.case-hero{grid-template-columns:1fr;padding-top:150px;min-height:auto}.case-facts{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:var(--line);border:1px solid var(--line)}.case-facts>div{background:var(--sand);padding:18px;border:0}.case-story{padding-left:28px;padding-right:28px}}
@media (max-width:760px){.shell{width:calc(100% - 40px)}.site-header{height:68px;grid-template-columns:1fr auto;padding-inline:20px}.header-cta{display:none}.menu-toggle{display:flex;justify-self:end}.site-nav{position:fixed;inset:68px 0 auto 0;background:var(--sand);border-bottom:1px solid var(--line);padding:26px 20px 34px;display:flex;flex-direction:column;gap:0;transform:translateY(-120%);opacity:0;pointer-events:none;transition:transform 420ms var(--ease),opacity 250ms}.site-nav.open{transform:none;opacity:1;pointer-events:auto}.site-nav a{font-size:30px;padding:11px 0;letter-spacing:-.03em}.hero{padding-top:110px;padding-bottom:48px;gap:26px}.hero-title{font-size:clamp(48px,15vw,72px);margin-top:22px}.hero-deck{font-size:17px}.hero-note{flex-direction:column;gap:7px;margin-top:38px}.hero-media{min-height:470px}.portrait-frame{width:100%;max-width:430px;border-radius:28px}.portrait-label{right:8px;bottom:25px}.stats-grid{grid-template-columns:1fr}.stat,.stat:first-child{padding:26px 0;border-right:0;border-bottom:1px solid var(--line)}.stat:last-child{border-bottom:0}.section{padding:90px 0}.section-head{grid-template-columns:1fr;gap:24px;margin-bottom:46px}.section-head>div{grid-column:auto}.section-head h2{font-size:48px}.section-head p{font-size:16px}.projects-grid{grid-template-columns:1fr}.project-card--hero{grid-column:auto}.project-card--hero .project-copy,.project-copy{padding:26px}.project-card--hero .project-copy h3,.project-copy h3{font-size:34px;margin-top:44px}.project-meta{flex-direction:column}.more-work{align-items:flex-start;flex-direction:column}.split-editorial{gap:34px}.profile-copy h2{font-size:50px}.profile-copy .lead{font-size:20px}.profile-grid{grid-template-columns:1fr}.stack-grid{grid-template-columns:1fr}.stack-card{padding:30px;min-height:220px}.stack-card h3{margin-top:42px}.timeline-row{grid-template-columns:1fr;gap:14px}.timeline-row div{flex-direction:column;gap:6px}.timeline-row span{text-align:left}.contact-section{padding:90px 0}.contact-inner h2{font-size:64px}.footer-top{align-items:flex-start;flex-direction:column;gap:30px}.footer-grid{grid-template-columns:1fr;gap:20px}.case-hero{padding-top:120px;gap:42px}.case-title h1{font-size:64px}.case-title p{font-size:19px}.case-facts{grid-template-columns:1fr}.case-cover{width:calc(100% - 40px);border-radius:24px}.case-summary,.case-story{padding-top:90px;padding-bottom:90px}.case-summary h2{font-size:44px}.case-metrics{grid-template-columns:1fr}.case-block{grid-template-columns:44px 1fr}.case-block h3{font-size:24px}.case-next{padding:90px 0}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}*,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important}.reveal{opacity:1;transform:none}}
:focus-visible{outline:3px solid var(--accent);outline-offset:4px}
'''
(ROOT/'styles.css').write_text(dedent(css).strip()+"\n", encoding='utf-8')

# ---------- JS ----------
js = r'''
const header=document.querySelector('[data-header]');
const menuBtn=document.querySelector('[data-menu-toggle]');
const nav=document.querySelector('[data-nav]');
const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
function onScroll(){header?.classList.toggle('scrolled',window.scrollY>24)}
onScroll(); window.addEventListener('scroll',onScroll,{passive:true});
menuBtn?.addEventListener('click',()=>{const open=nav.classList.toggle('open');menuBtn.setAttribute('aria-expanded',String(open));document.body.style.overflow=open?'hidden':''});
nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menuBtn?.setAttribute('aria-expanded','false');document.body.style.overflow=''}));
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
'''
(ROOT/'script.js').write_text(dedent(js).strip()+"\n", encoding='utf-8')

# ---------- README ----------
readme = '''# Hisham Mohamed Portfolio\n\nStatic multi-page portfolio built around a ZEN-inspired editorial design grammar, adapted into an original personal visual identity.\n\n## Pages\n- `index.html` — home, profile, stack, journey and project index\n- `work/*.html` — seven project case-study pages\n\n## Local preview\n```bash\npython -m http.server 8000\n```\nThen open `http://localhost:8000`.\n\n## Deployment\nThis is a dependency-free static site. Deploy the folder to Vercel, Netlify, GitHub Pages, Cloudflare Pages or any static host.\n'''
(ROOT/'README.md').write_text(readme, encoding='utf-8')

print('generated', len(projects), 'project pages')
