<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Social Media Agent — Content Ideas & Daily Planner</title>
  <style>
    :root{
      --bg:#0f1724; --card:#0b1220; --muted:#94a3b8; --accent:#7c3aed; --glass: rgba(255,255,255,0.04);
      --glass-2: rgba(255,255,255,0.03);
      --radius:14px;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
    }
    *{box-sizing:border-box}
    html,body{height:100%;margin:0;background:linear-gradient(180deg,#071127 0%, #0b1220 60%);color:#e6eef8}
    .container{max-width:1200px;margin:28px auto;padding:20px}

    header{display:flex;gap:18px;align-items:center;margin-bottom:18px}
    .logo{display:flex;align-items:center;gap:12px}
    .logo .mark{width:48px;height:48px;border-radius:12px;background:linear-gradient(135deg,var(--accent),#06b6d4);display:flex;align-items:center;justify-content:center;font-weight:700}
    h1{margin:0;font-size:20px}
    p.lead{margin:0;color:var(--muted);font-size:13px}

    .grid{display:grid;grid-template-columns:320px 1fr 320px;gap:18px}

    .card{background:linear-gradient(180deg,var(--card), rgba(255,255,255,0.02));border-radius:var(--radius);padding:16px;box-shadow:0 6px 18px rgba(2,6,23,0.6);}
    .section-title{font-size:13px;color:var(--muted);display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
    label{display:block;font-size:13px;margin-bottom:6px;color:var(--muted)}
    select,input,textarea{width:100%;padding:10px;border-radius:10px;border:1px solid rgba(255,255,255,0.03);background:var(--glass);color:inherit;font-size:14px}
    textarea{min-height:90px;resize:vertical}
    .btn{display:inline-flex;align-items:center;gap:8px;padding:10px 12px;border-radius:10px;border:none;background:linear-gradient(90deg,var(--accent),#06b6d4);color:white;cursor:pointer;font-weight:600}
    .btn.ghost{background:transparent;border:1px solid rgba(255,255,255,0.05)}

    .chip{display:inline-block;padding:6px 10px;border-radius:999px;background:var(--glass-2);border:1px solid rgba(255,255,255,0.02);font-size:13px;margin:6px 6px 0 0;cursor:pointer}

    .ideas-list{display:flex;flex-direction:column;gap:12px}
    .idea{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));padding:12px;border-radius:10px;border:1px solid rgba(255,255,255,0.02)}
    .idea h3{margin:0;font-size:15px}
    .meta{font-size:12px;color:var(--muted);margin-top:6px}
    .actions{display:flex;gap:8px;margin-top:10px}

    /* planner */
    .planner-day{padding:10px;border-radius:10px;background:linear-gradient(180deg, rgba(255,255,255,0.02), transparent);border:1px solid rgba(255,255,255,0.02);min-height:88px}
    .planner-grid{display:grid;grid-template-columns:repeat(1,1fr);gap:8px}
    .day-head{display:flex;align-items:center;justify-content:space-between;font-size:13px}
    .small{font-size:12px;color:var(--muted)}

    footer{margin-top:16px;color:var(--muted);font-size:13px;text-align:center}

    /* responsive */
    @media (max-width:980px){.grid{grid-template-columns:1fr;}.container{padding:12px}}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">
        <div class="mark">SM</div>
        <div>
          <h1>Social Media Agent</h1>
          <p class="lead">Generate content ideas, captions and a weekly posting plan — all in one page.</p>
        </div>
      </div>
      <div style="margin-left:auto;display:flex;gap:10px;align-items:center">
        <button class="btn" id="autoFill">Auto-fill 7-day plan</button>
        <button class="btn ghost" id="exportBtn">Export CSV</button>
      </div>
    </header>

    <div class="grid">
      <!-- Left: Controls -->
      <aside class="card">
        <div class="section-title"><strong>Create</strong><span class="small">Settings</span></div>

        <label for="platform">Platform</label>
        <select id="platform">
          <option>Instagram</option>
          <option>Facebook</option>
          <option>Twitter / X</option>
          <option>TikTok</option>
          <option>LinkedIn</option>
        </select>

        <label for="contentType">Content Type</label>
        <select id="contentType">
          <option>Reel / Short</option>
          <option>Carousel</option>
          <option>Single Image</option>
          <option>Story</option>
          <option>Text Post</option>
        </select>

        <label for="tone">Tone</label>
        <select id="tone">
          <option>Casual & Friendly</option>
          <option>Educational</option>
          <option>Inspiring</option>
          <option>Humorous</option>
          <option>Professional</option>
        </select>

        <label for="nIdeas">Ideas to generate</label>
        <input id="nIdeas" type="number" min="1" max="20" value="6" />

        <label for="keywords">Keywords / Hashtags (comma)</label>
        <input id="keywords" placeholder="#college, #project, tutorial" />

        <div style="margin-top:12px;display:flex;gap:8px">
          <button class="btn" id="generateBtn">Generate Ideas</button>
          <button class="btn ghost" id="clearBtn">Clear</button>
        </div>

        <hr style="margin:14px 0;border:none;border-top:1px solid rgba(255,255,255,0.03)" />
        <div class="section-title"><span>Quick Templates</span></div>
        <div id="templates">
          <div class="chip" data-template="howto">How-to / Tutorial</div>
          <div class="chip" data-template="beforeafter">Before & After</div>
          <div class="chip" data-template="story">Personal Story</div>
          <div class="chip" data-template="myth">Myth-busting</div>
          <div class="chip" data-template="list">Top 5 / List</div>
        </div>
      </aside>

      <!-- Center: Ideas -->
      <main class="card">
        <div class="section-title"><strong>Generated Ideas</strong><span class="small">Click an idea to copy / add to planner</span></div>
        <div id="ideas" class="ideas-list">
          <!-- ideas inserted here -->
        </div>
      </main>

      <!-- Right: Planner -->
      <aside class="card">
        <div class="section-title"><strong>Weekly Planner</strong><span class="small">Drag ideas → day or click "Add"</span></div>
        <div id="planner" class="planner-grid">
          <!-- 7 day slots -->
        </div>
        <div style="margin-top:12px;display:flex;gap:8px">
          <input id="planTitle" placeholder="Campaign / Week label" />
          <button class="btn" id="savePlan">Save</button>
        </div>
      </aside>
    </div>

    <footer>Made with ♥ — modify templates & copy tones to match your brand. Want CSV/JSON export? Use Export.</footer>
  </div>

  <script>
    // small local generator — uses templates and user settings
    const templates = {
      howto: (kw, platform, tone) => `How to ${kw} — a step-by-step guide for ${platform}. Write short steps and a CTA.`,
      beforeafter: (kw) => `Before & After: ${kw} results. Show transition with a quick caption.`,
      story: (kw) => `A short personal story about ${kw}. End with a question to increase comments.`,
      myth: (kw) => `Myth vs Fact about ${kw}. Bust a common misconception with data.`,
      list: (kw) => `Top 5 ${kw} tips — quick bullets, save for later.`
    };

    function uid(){return Math.random().toString(36).slice(2,9)}

    function pickTemplate(t, kw, platform, tone){
      if(templates[t]) return templates[t](kw, platform, tone)
      // default mix
      return `Talk about ${kw} for ${platform} in a ${tone} tone.`
    }

    function generateIdeas(){
      const n = Number(document.getElementById('nIdeas').value) || 6
      const platform = document.getElementById('platform').value
      const tone = document.getElementById('tone').value
      const type = document.getElementById('contentType').value
      const kwRaw = document.getElementById('keywords').value || ''
      const keywords = kwRaw.split(',').map(s=>s.trim()).filter(Boolean)

      const chosen = []
      const templateKeys = Object.keys(templates)
      for(let i=0;i<n;i++){
        const kw = keywords[i % Math.max(1,keywords.length)] || ['branding','college project','tutorial','life hack','behind the scenes'][i%5]
        const t = templateKeys[i % templateKeys.length]
        const ideaText = pickTemplate(t, kw, platform, tone)
        const caption = generateCaption(ideaText, platform, tone)
        chosen.push({id:uid(), idea:ideaText, caption, type, platform, tone})
      }
      renderIdeas(chosen)
    }

    function generateCaption(ideaText, platform, tone){
      // small set of caption patterns — feel free to expand
      const openers = {
        'Casual & Friendly':['Quick tip:','Pro tip:','PSA:','Hey —'],
        'Educational':['Did you know?','Quick breakdown:','Here’s how:','Summary:'],
        'Inspiring':['From small beginnings:','You can too —','Believe it:','Inspiration:'],
        'Humorous':['Plot twist:','When you realize...','Not clickbait:','Storytime:'],
        'Professional':['Insights:','A quick case study:','Research shows:','Key takeaway:']
      }
      const closers = ['What do you think?', 'Save this for later ✨', 'Tag someone who needs this.', 'Share your thoughts below.']
      const toneKeys = Object.keys(openers)
      let picks = openers[tone] || openers['Casual & Friendly']
      const opener = picks[Math.floor(Math.random()*picks.length)]
      const closer = closers[Math.floor(Math.random()*closers.length)]
      // keep captions short for platform suitability
      let caption = `${opener} ${ideaText.split('.').slice(0,1).join('.')} ${closer}`
      if(platform.includes('TikTok') || platform.includes('Reel')) caption += ' #shorts'
      return caption
    }

    function renderIdeas(items){
      const container = document.getElementById('ideas')
      container.innerHTML = ''
      items.forEach(it=>{
        const el = document.createElement('div')
        el.className = 'idea'
        el.draggable = true
        el.innerHTML = `
          <h3>${escapeHtml(it.idea)}</h3>
          <div class="meta">Type: ${it.type} • Platform: ${it.platform} • Tone: ${it.tone}</div>
          <div class="meta">Caption: <em id="cap-${it.id}">${escapeHtml(it.caption)}</em></div>
          <div class="actions">
            <button class="btn" data-id="${it.id}" onclick='copyCaption("${it.id}")'>Copy Caption</button>
            <button class="btn ghost" onclick='addToToday("${escapeHtml(it.idea).replace(/"/g,'')}", "${escapeHtml(it.caption).replace(/"/g,'')}")'>Add to Today</button>
          </div>
        `
        // drag handlers
        el.addEventListener('dragstart', e=>{ e.dataTransfer.setData('text/plain', JSON.stringify(it)) })
        container.appendChild(el)
      })
    }

    function escapeHtml(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}

    function copyCaption(id){
      const el = document.getElementById('cap-'+id)
      if(!el) return
      navigator.clipboard.writeText(el.textContent).then(()=>{
        alert('Caption copied to clipboard')
      })
    }

    // Planner logic — simple week starting today
    function getWeekDays(){
      const days = []
      const now = new Date();
      for(let i=0;i<7;i++){
        const d = new Date(now)
        d.setDate(now.getDate()+i)
        days.push(d)
      }
      return days
    }

    function renderPlanner(){
      const container = document.getElementById('planner')
      container.innerHTML = ''
      const days = getWeekDays()
      days.forEach(d=>{
        const dayBox = document.createElement('div')
        dayBox.className = 'planner-day'
        dayBox.dataset.date = d.toISOString().slice(0,10)
        dayBox.innerHTML = `
          <div class="day-head"><strong>${d.toLocaleDateString(undefined,{weekday:'short'})} ${d.getDate()}</strong><span class="small">${d.toLocaleDateString()}</span></div>
          <div class="day-items" style="margin-top:8px;display:flex;flex-direction:column;gap:6px" ondragover="event.preventDefault()" ondrop="handleDrop(event)"></div>
        `
        container.appendChild(dayBox)
      })
    }

    function handleDrop(e){
      e.preventDefault()
      try{
        const data = JSON.parse(e.dataTransfer.getData('text/plain'))
        const target = e.target.closest('.planner-day')
        if(target) addIdeaToDay(target.dataset.date, data)
      }catch(err){console.warn(err)}
    }

    function addIdeaToDay(dateStr, ideaObj){
      const day = document.querySelector(`[data-date='${dateStr}'] .day-items`)
      if(!day) return
      const it = document.createElement('div')
      it.style.padding='8px';it.style.borderRadius='8px';it.style.background='rgba(255,255,255,0.02)';it.style.border='1px solid rgba(255,255,255,0.02)'
      it.innerHTML = `<strong style="font-size:13px">${escapeHtml(ideaObj.idea)}</strong><div class="small">${escapeHtml(ideaObj.caption)}</div>`
      day.appendChild(it)
    }

    function addToToday(idea, caption){
      const dateStr = new Date().toISOString().slice(0,10)
      addIdeaToDay(dateStr, {idea, caption})
    }

    // Auto-fill with generated ideas across the week
    function autofillWeek(){
      generateIdeas()
      const ideasEls = Array.from(document.querySelectorAll('#ideas .idea'))
      const days = document.querySelectorAll('#planner .planner-day')
      ideasEls.forEach((el,i)=>{
        const data = {
          idea: el.querySelector('h3').textContent,
          caption: el.querySelector('[id^="cap-"]').textContent
        }
        const day = days[i % days.length]
        addIdeaToDay(day.dataset.date, data)
      })
    }

    // Export planner as CSV
    function exportCSV(){
      const rows = [['date','idea','caption']]
      document.querySelectorAll('#planner .planner-day').forEach(day=>{
        const date = day.dataset.date
        const items = day.querySelectorAll('.day-items > div')
        items.forEach(it=>{
          const idea = it.querySelector('strong').textContent.replace(/\n/g,' ')
          const cap = it.querySelector('.small').textContent.replace(/\n/g,' ')
          rows.push([date, idea, cap])
        })
      })
      const csv = rows.map(r=>r.map(c=>`"${String(c).replace(/"/g,'""')}"`).join(',')).join('\n')
      const blob = new Blob([csv],{type:'text/csv'})
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `sma_plan_${new Date().toISOString().slice(0,10)}.csv`
      a.click()
      URL.revokeObjectURL(url)
    }

    // UI wiring
    document.getElementById('generateBtn').addEventListener('click', generateIdeas)
    document.getElementById('autoFill').addEventListener('click', autofillWeek)
    document.getElementById('clearBtn').addEventListener('click', ()=>{document.getElementById('ideas').innerHTML='';})
    document.getElementById('exportBtn').addEventListener('click', exportCSV)
    document.getElementById('savePlan').addEventListener('click', ()=>{alert('Plan saved locally (demo). You can export as CSV.')})

    // template chips
    document.querySelectorAll('#templates .chip').forEach(ch=>{
      ch.addEventListener('click', e=>{
        const t = e.currentTarget.dataset.template
        const kw = prompt('Enter a keyword or subject to use with this template', 'your topic') || 'your topic'
        const platform = document.getElementById('platform').value
        const tone = document.getElementById('tone').value
        const idea = pickTemplate(t, kw, platform, tone)
        const caption = generateCaption(idea, platform, tone)
        renderIdeas([{id:uid(), idea, caption, type:document.getElementById('contentType').value, platform, tone}])
      })
    })

    // initial render
    renderPlanner()
    generateIdeas()
  </script>
</body>
</html>
