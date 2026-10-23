#!/usr/bin/env python3
"""
AI KNYGOS KOMPILIATORIUS (Antigravity Studio Edition v4)
Sujungia visus skyrius is /chapters katalogo, pritaiko profesionalius leidybinius stilius,
automatiškai pažymi svarbiausius terminus ir asmenybes (Mini-Wikipedia žinynas),
įterpia Egzistencinius Vartus, 1 EUR mokėjimo simuliaciją, audio grotuvą su ADAM (ElevenLabs)
bei sugeneruoja galutinius HTML failus į /dist/index.html ir projekto šaknį /index.html.
"""

import os
import sys
import re
import json
import markdown

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
STYLES_DIR = os.path.join(BASE_DIR, "assets", "styles")
DIST_DIR = os.path.join(BASE_DIR, "dist")
GLOSSARY_PATH = os.path.join(BASE_DIR, "research", "glossary_data.json")

# Užkrauname žodyno duomenų bazę
with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    GLOSSARY_DATA = json.load(f)

# Žodžių atpažinimo šablonai
TERMS_PATTERNS = [
    ("singuliarumas", r"\b(Singuliarumo|Singuliarumą|Singuliarumas|Singuliarumui|Singuliarume|singuliarumo|singuliarumą|singuliarumas|singuliarumui|singuliarume)\b"),
    ("alan_turing", r"\b(Alano Turingo|Alanas Turingas|Alano Tiuringo|Alanas Tiuringas|Alan Turing|Alanu Turingu|Alanui Turingui|Tiuringo testas|Tiuringo testą)\b"),
    ("dartmouth_1956", r"\b(Dartmuto vasara|Dartmuto koledže|Dartmuto seminaras|Dartmuto|Dartmouth)\b"),
    ("agi", r"\b(AGI|Bendrasis Dirbtinis Intelektas|Bendrojo Dirbtinio Intelekto)\b"),
    ("asi", r"\b(ASI|Superintelekto|Superintelektas|Superintelektui|Superintelektą)\b"),
    ("tokenas", r"\b(tokenas|tokenai|tokenų|tokenams|tokenus|tokenais|Tokenas|Tokenai|Tokenų)\b"),
    ("embedding", r"\b(embedding|embeddingas|embeddingai|embeddingus|Embedding|Embeddingai)\b"),
    ("transformer", r"\b(transformeriai|transformerių|transformeriams|transformerių architektūra|Self-Attention|Transformer|Transformers)\b"),
    ("geoffrey_hinton", r"\b(Geoffrey Hinton|Geoffrey Hintono|Hintonas|Hintono|Hintonui)\b"),
    ("ilya_sutskever", r"\b(Ilya Sutskever|Ilyos Sutskeverio|Sutskeveris|Sutskeverio)\b"),
    ("demis_hassabis", r"\b(Demis Hassabis|Demio Hassabio|Hassabis|Hassabio)\b"),
    ("dario_amodei", r"\b(Dario Amodei|Dario Amodeiui|Amodei)\b"),
    ("sam_altman", r"\b(Sam Altman|Samo Altmano|Altmanas|Altmano)\b"),
    ("jensen_huang", r"\b(Jensen Huang|Jenseno Huango|Huangas|Huango)\b"),
    ("mo_gawdat", r"\b(Mo Gawdat|Mo Gawdato|Gawdatas|Gawdato)\b"),
    ("yuval_noah_harari", r"\b(Yuval Noah Harari|Hararis|Harario)\b"),
    ("nick_bostrom", r"\b(Nick Bostrom|Nicko Bostromo|Bostromas|Bostromo)\b"),
    ("roman_yampolskiy", r"\b(Roman Yampolskiy|Romano Yampolskio|Yampolskis|Yampolskio)\b"),
    ("sulaikymo_problema", r"\b(Sulaikymo problema|sulaikymo problema|Sulaikymo problemos|sulaikymo problemos|Sulaikymo problemą)\b"),
    ("instrumentine_konvergencija", r"\b(Instrumentinė konvergencija|instrumentinė konvergencija|Instrumentinės konvergencijos|instrumentinės konvergencijos)\b"),
    ("alignment_faking", r"\b(Alignment Faking|alignment faking|apsimestinis lygiavimas|apsimestinio lygiavimo)\b"),
    ("moraveco_paradoksas", r"\b(Moraveco paradoksas|moraveco paradoksas|Moraveco paradokso|moraveco paradokso)\b"),
    ("humanoidai", r"\b(humanoidai|humanoidų|humanoidams|humanoidus|Humanoidai|Humanoidų|Optimus|Figure 02)\b"),
    ("alphafold", r"\b(AlphaFold|AlphaFold 3|AlphaFold 2)\b"),
    ("yamanaka", r"\b(Yamanaka|Yamanakos faktoriai|OSKM faktoriai|epigenetinis laikrodis)\b"),
    ("asml", r"\b(ASML|EUV litografija|EUV)\b"),
    ("tsmc", r"\b(TSMC|Taivano puslaidininkių)\b"),
    ("dyson_sfera", r"\b(Dyson sfera|Dyson sferos|Dyson sferą|Dyson sferų|Dyson Swarm)\b"),
    ("computronium", r"\b(kompiutronis|kompiutronio|Computronium)\b"),
    ("didysis_filtras", r"\b(Didysis Filtras|Didysis filtras|Didžiojo Filtro|Didžiojo filtro)\b"),
    ("world_model", r"\b(Pasaulio modelis|Pasaulio modeliai|pasaulio modelis|pasaulio modeliai|World Model|World Models)\b"),
    ("ubi", r"\b(UBI|UBC|Visuotinės Bazinės Pajamos|bazinės pajamos|bazinių pajamų)\b"),
    ("mind_uploading", r"\b(Sąmonės perkėlimas|sąmonės perkėlimas|Sąmonės perkėlimo|sąmonės perkėlimo|Mind Uploading)\b"),
    ("karpathy_software", r"(Software 1\.0|Software 2\.0|Software 3\.0|Andrej Karpathy|Karpathy)"),
    ("one_person_unicorn", r"(1 zmogaus vienaragis|vienaragio|vienaragi|1 žmogaus vienaragis|vienaragio|One-person unicorn)"),
    ("backpropagation", r"(Backpropagation|atgalinė sklaida|atgalinės sklaidos|atgalinio sklidimo|atgaline sklaida)"),
    ("kardashev_scale", r"(Kardaševo skalė|Kardaševo skalės|Kardaševo skalę|Kardashev Scale|Kardasevo skale|Kardaševo II|II Kardashev)"),
    ("eliezeryudkowsky", r"(Eliezer Yudkowsky|Eliezerio Yudkowsky|Yudkowsky|Yudkowskis)"),
    ("eric_schmidt", r"(Eric Schmidt|Erico Schmidto|Schmidtas|Schmidto)"),
    ("david_baker", r"(David Baker|Davido Bakerio|Bakeris|Bakerio)"),
    ("daron_acemoglu", r"(Daron Acemoglu|Darono Acemoglu|Acemoglu)"),
    ("mustafa_suleyman", r"(Mustafa Suleyman|Mustafos Suleymano|Suleymanas)"),
    ("brett_adcock", r"(Brett Adcock|Bretto Adcocko|Adcockas)"),
    ("ship_of_theseus", r"(Tesėjo laivas|Tesėjo laivo|Tesėjo laivą|Tesejo laivas|Ship of Theseus)"),
    ("landauer_limit", r"(Landauerio riba|Landauerio ribos|Landauerio principas|Landauerio limitas)"),
    ("von_neumann_probes", r"(Von Neumanno zondai|Von Neumanno zondų|Von Neumanno zondas|Von Neumann probes)"),
    ("crispr", r"(CRISPR|Cas9|genų inžinerija|DNR redagavimas)"),
    ("longevity_escape_velocity", r"(pabėgimo greitis nuo senėjimo|Ilgaamžiškumo pabėgimo greitis|Longevity Escape Velocity)"),
    ("paperclip_maximizer", r"(sąvaržėlių maksimizatorius|sąvaržėlių maksimizatoriaus|Paperclip Maximizer)")
]

def auto_tag_glossary(html):
    parts = re.split(r"(<[^>]+>)", html)
    for key, pat in TERMS_PATTERNS:
        count = 0
        for i in range(len(parts)):
            if not parts[i].startswith("<") and count < 3:
                def repl(m):
                    nonlocal count
                    count += 1
                    word = m.group(0)
                    return f'<span class="wiki-term" onclick="openWikiModal(\'{key}\')" title="Spustelėkite analizei: {word}">{word}</span>'
                parts[i] = re.sub(pat, repl, parts[i], count=3 - count)
    return "".join(parts)

def get_chapter_files():
    files = [f for f in os.listdir(CHAPTERS_DIR) if f.endswith(".md")]
    files.sort()
    return [os.path.join(CHAPTERS_DIR, f) for f in files]

def read_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def extract_chapter_info(raw_text, basename):
    m_title = re.search(r'<h2 class="chapter-title">(.*?)</h2>', raw_text)
    if not m_title:
        m_title = re.search(r'#\s+(.*)', raw_text)
    title = m_title.group(1).strip() if m_title else basename.replace(".md", "").replace("_", " ").title()
    title_clean = re.sub(r'<[^>]+>', '', title).strip()
    
    m_num = re.search(r'<span class="chapter-number">(.*?)</span>', raw_text)
    num = m_num.group(1).strip() if m_num else ""
    num_clean = re.sub(r'<[^>]+>', '', num).strip()
    
    section_id = basename.replace(".md", "")
    return {
        "id": section_id,
        "title": title_clean,
        "number": num_clean,
        "label": f"{num_clean}: {title_clean}" if num_clean else title_clean
    }

def compile_book():
    os.makedirs(DIST_DIR, exist_ok=True)
    css_path = os.path.join(STYLES_DIR, "book.css")
    css_content = read_file(css_path) if os.path.exists(css_path) else ""

    chapter_files = get_chapter_files()
    rendered_chapters = []
    chapter_options = []

    print(f"Rasta skyriu: {len(chapter_files)}")

    for cpath in chapter_files:
        raw_text = read_file(cpath)
        raw_text = re.sub(r'src="\.\./assets/images/', 'src="assets/images/', raw_text)

        basename = os.path.basename(cpath)
        info = extract_chapter_info(raw_text, basename)
        print(f" -> Apdorojamas: {basename} ({info['title']})")
        
        chapter_options.append(f'<option value="#{info["id"]}">{info["label"]}</option>')

        # Markdown to HTML konversija
        html = markdown.markdown(
            raw_text,
            extensions=["tables", "fenced_code", "nl2br", "sane_lists"]
        )
        
        # Pritaiko kognityvinį terminų ženklinimą
        html = auto_tag_glossary(html)
        
        rendered_chapters.append(f'<section class="chapter" id="{info["id"]}">{html}</section>')

    select_html = chr(10).join(chapter_options)
    glossary_json_str = json.dumps(GLOSSARY_DATA, ensure_ascii=False)

    full_html = f"""<!DOCTYPE html>
<html lang="lt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PO DARBO: Kaip AI iki 2037 m. perkurs ekonomiką, valstybes ir žmogų</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
  <meta name="description" content="Išsami strateginė ir analitinė monografija apie dirbtinio superintelekto ir autonominės robotikos erą (2027–2037 m.)">
  <style>
{css_content}
  </style>
</head>
<body class="theme-dark gate-active">

  <!-- ==========================================================================
       EGZISTENCINIAI VARTAI (Live Worldometer & 1 € Paywall Gateway)
       ========================================================================== -->
  <section id="existentialGate" class="existential-gate">
    <div class="existential-live-badge">
      <span class="live-pulse-dot"></span>
      TIESIOGINĖ CIVILIZACIJOS TRANSMISIJA • 2026 M. PABAIGA • KREIVĖ TIES 90°
    </div>

    <h1 class="existential-hero-title">PO DARBO</h1>
    <p class="existential-hero-subtitle">
      Tu praleidai labai daug. Mes ištyrėme 1 500+ valandų didžiausių pasaulio laboratorijų ataskaitų, Nobelio laureatų ir insiderių liudijimų, kad atvertume tau akis prieš didįjį lūžį.
    </p>

    <!-- Pasaulinis Egzistencinis Skaitiklis (Worldometer Matrix) -->
    <div class="worldometer-grid">
      <div class="worldometer-card card-danger">
        <div class="worldometer-label">Pasaulio Populiacija</div>
        <div class="worldometer-value" id="counterPopulation">8,188,419,250</div>
        <div class="worldometer-desc">99,99% pasaulio gyventojų šiuo metu nesupranta VISIŠKAI NIEKO.</div>
      </div>

      <div class="worldometer-card card-warning">
        <div class="worldometer-label">Šiandien Mirę Žmonės</div>
        <div class="worldometer-value" id="counterDeaths">146,820</div>
        <div class="worldometer-desc">Šie žmonės neišgyveno to, ką netrukus išgyvensi tu.</div>
      </div>

      <div class="worldometer-card card-success">
        <div class="worldometer-label">Šiandien Gimę Kūdikiai</div>
        <div class="worldometer-value" id="counterBirths">371,430</div>
        <div class="worldometer-desc">Jie taip pat neišgyvens to, ką išgyvensi tu – jų pasaulis bus neatpažįstamas.</div>
      </div>

      <div class="worldometer-card card-purple">
        <div class="worldometer-label">Prisijungę / Prabudę</div>
        <div class="worldometer-value" id="counterAwakened">13,345,493</div>
        <div class="worldometer-desc">Prisijunk prie tų, kurie atsisakė rožinių akinių ir ruošiasi dabar.</div>
      </div>
    </div>

    <!-- Proto Architektų Panteonas -->
    <div class="authority-showcase">
      <div class="authority-title">Monografija parengta remiantis pasaulio proto architektų liudijimais:</div>
      <div class="authority-badges">
        <span class="auth-chip">🏆 <strong>Geoffrey Hinton</strong> (Nobel 2024)</span>
        <span class="auth-chip">🏆 <strong>Demis Hassabis</strong> (DeepMind, Nobel 2024)</span>
        <span class="auth-chip">🏆 <strong>David Baker</strong> (Nobel 2024)</span>
        <span class="auth-chip">🏆 <strong>Daron Acemoglu</strong> (Nobel 2024)</span>
        <span class="auth-chip">🧬 <strong>Dario Amodei</strong> (Anthropic)</span>
        <span class="auth-chip">🧠 <strong>Ilya Sutskever</strong> (SSI)</span>
        <span class="auth-chip">⚡ <strong>Jensen Huang</strong> (NVIDIA)</span>
        <span class="auth-chip">👁️ <strong>Mo Gawdat</strong> (Google [X])</span>
        <span class="auth-chip">📜 <strong>Yuval Noah Harari</strong></span>
        <span class="auth-chip">⏳ <strong>Nick Bostrom</strong> (Oksfordas)</span>
        <span class="auth-chip">🛡️ <strong>Roman Yampolskiy</strong></span>
        <span class="auth-chip">💡 <strong>Sam Altman</strong> (OpenAI)</span>
      </div>
    </div>

    <!-- 1 € Paywall CTA Dėžutė -->
    <div class="paywall-cta-box">
      <button class="btn-unlock-super" onclick="startPaymentSimulation()">
        ⚡ ATRAKINTI IR PRADĖTI SKAITYMĄ (1 €)
      </button>

      <div class="fund-promise">
        🕊️ 100% visų surinktų lėšų skiriama nepriklausomam Saugaus Superintelekto (Safe ASI) ir Žmonijos Apsaugos fondui.
      </div>

      <div>
        <button class="demo-unlock-link" onclick="quickDemoUnlock()">
          [Demonstracinis režimas: Tiesioginis atrakinimas]
        </button>
      </div>

      <!-- Viral Share Skydelis -->
      <div class="viral-share-bar">
        <span style="font-size: 0.8rem; color: #64748b; margin-right: 4px;">Pasidalink tiesa:</span>
        <button class="btn-share" onclick="shareBook('telegram')">✈️ Telegram</button>
        <button class="btn-share" onclick="shareBook('whatsapp')">💬 WhatsApp</button>
        <button class="btn-share" onclick="shareBook('x')">𝕏 Twitter</button>
        <button class="btn-share" onclick="shareBook('facebook')">📘 Facebook</button>
        <button class="btn-share" onclick="shareBook('copy')">📋 Kopijuoti nuorodą</button>
      </div>
    </div>
  </section>

  <!-- ==========================================================================
       1 EUR MOKĖJIMO SIMULIACIJOS MODALAS
       ========================================================================== -->
  <div id="paymentModalOverlay" class="payment-modal-overlay">
    <div class="payment-modal-card">
      <div class="pay-modal-top">
        <div class="pay-secure-tag">
          🔒 ŠIFRUOTA MIKRO-TRANSAKCIJA
        </div>
        <div class="pay-amount-pill">
          1,00 €
        </div>
      </div>

      <div class="pay-fund-target">
        <div class="pay-fund-label">Paskirtis ir Paramos Gavėjas:</div>
        <div class="pay-fund-name">Safe ASI & Humanity Alignment Reserve</div>
        <div class="pay-fund-sub">100% lėšų skiriama nepriklausomiems AI sulaikymo problemos tyrimams</div>
      </div>

      <!-- Live Transakcijos Žingsniai -->
      <div class="sim-steps-list" id="simStepsContainer">
        <div class="sim-step-item active" id="simStep1">
          <div class="sim-step-circle"></div>
          <div>Jungiamasi prie saugaus atsiskaitymo šliuzo (Apple Pay / Visa)...</div>
        </div>

        <div class="sim-step-item" id="simStep2">
          <div class="sim-step-circle"></div>
          <div>Rezervuojamas 1,00 € įnašas į Safe ASI fondą...</div>
        </div>

        <div class="sim-step-item" id="simStep3">
          <div class="sim-step-circle"></div>
          <div>Generuojamas asmeninis šifruotas raktas #ASI-2026-99...</div>
        </div>
      </div>

      <!-- Sėkmės Pranešimas -->
      <div class="sim-success-banner" id="simSuccessBanner" style="display: none;">
        <div class="success-badge-icon">✓</div>
        <h3 class="success-title">MOKĖJIMAS PATVIRTINTAS</h3>
        <p class="success-sub">
          1,00 € sėkmingai pervesta į Safe ASI rezervą.<br>
          <strong>Sveikiname atmerkus akis.</strong> Tavo prieiga prie visos monografijos ir analitikos yra aktyvuota.
        </p>
        <button class="btn-proceed-reading" onclick="finalizeBookUnlock()">
          PRADĖTI SKAITYMĄ IR ANALITIKĄ ➔
        </button>
      </div>
    </div>
  </div>

  <!-- ==========================================================================
       MINI-WIKIPEDIA KOGNITYVINIS ŽINYNAS (MODALAS) - DINAMINIS BESPOKE MAKETAS
       ========================================================================== -->
  <div id="wikiModalOverlay" class="wiki-modal-overlay" onclick="closeWikiModalOnBackdrop(event)">
    <div class="wiki-modal-card" id="wikiModalCard">
      <!-- Dinamiškai sugeneruojamas unikalus kiekvieno termino/asmens turinys -->
      <div id="wikiModalDynamicBody"></div>
    </div>
  </div>

  <!-- ==========================================================================
       VIRŠUTINIS INTERAKTYVUS VALDYMO SKYDELIS
       ========================================================================== -->
  <header class="reader-toolbar" id="mainToolbar" style="display: none;">
    <div class="reader-progress-track">
      <div class="reader-progress-bar" id="progressBar"></div>
    </div>
    
    <div class="reader-brand">
      <span>PO DARBO</span>
      <span class="pill-badge" style="background: rgba(16, 185, 129, 0.2); border-color: rgba(16, 185, 129, 0.4); color: #10b981;">
        🟢 PRABUDĘS (1 € Apmokėta)
      </span>
    </div>

    <div class="reader-controls">
      <select class="chapter-select" id="chapterNav" onchange="navigateToChapter(this.value)">
        <option value="">-- Pasirinkite Skyrių --</option>
        {select_html}
      </select>

      <button class="btn-pill" onclick="toggleAudioReadAlong()" id="audioBtn" style="border-color: var(--accent-cyan); color: var(--accent-cyan);" title="Klausytis autentiško ElevenLabs (Adam) įgarsinimo">
        🎧 Klausytis (Audio)
      </button>

      <button class="btn-pill" onclick="cycleTheme()" id="themeBtn" title="Keisti spalvų temą">
        🌓 Tema
      </button>

      <span class="drm-badge" title="Turinys apsaugotas nuo neteisėto kopijavimo ir PDF eksporto">
        🔒 DRM Apsaugota
      </span>
    </div>

    <!-- Nematomas Audio Grotuvas su ElevenLabs Adam įgarsinimu -->
    <audio id="bookAudioPlayer" preload="auto">
      <source src="assets/audio/00_prologas.mp3" type="audio/mpeg">
      <source src="../assets/audio/00_prologas.mp3" type="audio/mpeg">
    </audio>
  </header>

  <!-- ==========================================================================
       PAGRINDINIS KNYGOS TURINYS
       ========================================================================== -->
  <main class="book-container" id="bookContent" style="display: none;">
    {chr(10).join(rendered_chapters)}
  </main>

  <!-- DRM Įspėjamasis Pranešimas (Toast) -->
  <div id="toastNotification" class="toast-notification">
    <span>🔒 Kopijavimas, spausdinimas ir PDF eksportas yra išjungti autorių teisių apsaugai.</span>
  </div>

  <!-- ==========================================================================
       INTERAKTYVŪS SKRIPTAI (Worldometer, Paywall, Audio, Wiki, DRM)
       ========================================================================== -->
  <script>
    // 0. MINI-WIKIPEDIA DUOMENŲ BAZĖ
    const GLOSSARY_DB = {glossary_json_str};

    function openWikiModal(termKey) {{
      const modal = document.getElementById("wikiModalOverlay");
      const dynamicBody = document.getElementById("wikiModalDynamicBody");
      const data = GLOSSARY_DB[termKey];
      if (!modal || !data || !dynamicBody) return;

      playSciFiChime('wiki');

      if (data.custom_html) {{
        dynamicBody.innerHTML = `
          <div class="wiki-modal-header">
            <div class="wiki-header-left">
              <div class="wiki-category-badge ${{data.badge_color || 'cyan'}}">${{data.category || 'KOGNITYVINIS ŽINYNAS'}}</div>
              <h2 class="wiki-title">${{data.title}}</h2>
              <div class="wiki-en-title">${{data.en_title || ''}}</div>
            </div>
            <button class="wiki-btn-close" onclick="closeWikiModal()" title="Uždaryti langą (ESC)">✕</button>
          </div>
          <div class="wiki-bespoke-content">
            ${{data.custom_html}}
          </div>
          <div class="wiki-modal-footer">
            <span class="wiki-footer-hint">PO DARBO • Kognityvinė Enciklopedija</span>
            <button class="wiki-btn-dismiss" onclick="closeWikiModal()">Supratau ➔</button>
          </div>
        `;
      }} else {{
        dynamicBody.innerHTML = `
          <div class="wiki-modal-header">
            <div class="wiki-header-left">
              <div class="wiki-category-badge ${{data.badge_color || 'cyan'}}">${{data.category || 'KOGNITYVINIS TERMINAS'}}</div>
              <h2 class="wiki-title">${{data.title}}</h2>
              <div class="wiki-en-title">${{data.en_title || ''}}</div>
            </div>
            <button class="wiki-btn-close" onclick="closeWikiModal()" title="Uždaryti langą (ESC)">✕</button>
          </div>
          <div class="wiki-summary-box">${{data.summary || ''}}</div>
          <div class="wiki-modal-footer">
            <span class="wiki-footer-hint">PO DARBO • Kognityvinė Enciklopedija</span>
            <button class="wiki-btn-dismiss" onclick="closeWikiModal()">Supratau ➔</button>
          </div>
        `;
      }}

      modal.classList.add("active");
    }}

    function closeWikiModal() {{
      const modal = document.getElementById("wikiModalOverlay");
      if (modal) modal.classList.remove("active");
    }}

    function closeWikiModalOnBackdrop(e) {{
      if (e.target && e.target.id === "wikiModalOverlay") {{
        closeWikiModal();
      }}
    }}

    // 1. WORLDOMETER REAL-TIME TIKINIMO LOGIKA
    let popVal = 8188419250;
    let deathsVal = 146820;
    let birthsVal = 371430;
    let awakenedVal = 13345493;

    function formatNumber(num) {{
      return num.toLocaleString('lt-LT');
    }}

    function updateWorldometer() {{
      popVal += Math.floor(Math.random() * 3) + 1;
      deathsVal += (Math.random() > 0.4 ? 1 : 0);
      birthsVal += Math.floor(Math.random() * 3) + 1;
      if (Math.random() > 0.6) awakenedVal += 1;

      const elPop = document.getElementById("counterPopulation");
      const elDeaths = document.getElementById("counterDeaths");
      const elBirths = document.getElementById("counterBirths");
      const elAwakened = document.getElementById("counterAwakened");

      if (elPop) elPop.textContent = formatNumber(popVal);
      if (elDeaths) elDeaths.textContent = formatNumber(deathsVal);
      if (elBirths) elBirths.textContent = formatNumber(birthsVal);
      if (elAwakened) elAwakened.textContent = formatNumber(awakenedVal);
    }}

    setInterval(updateWorldometer, 700);

    // 2. FUTURISTINIAI GARSO EFEKTAI (Web Audio API)
    function playSciFiChime(type) {{
      try {{
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (!AudioContext) return;
        const ctx = new AudioContext();

        if (type === 'start') {{
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(440, ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.2);
          gain.gain.setValueAtTime(0.12, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.3);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.3);
        }} else if (type === 'wiki') {{
          const osc = ctx.createOscillator();
          const gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(987.77, ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(1318.51, ctx.currentTime + 0.1);
          gain.gain.setValueAtTime(0.08, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.18);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.18);
        }} else if (type === 'success') {{
          const freqs = [523.25, 659.25, 783.99, 1046.50];
          freqs.forEach((f, idx) => {{
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(f, ctx.currentTime + idx * 0.08);
            gain.gain.setValueAtTime(0.15, ctx.currentTime + idx * 0.08);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + idx * 0.08 + 0.6);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(ctx.currentTime + idx * 0.08);
            osc.stop(ctx.currentTime + idx * 0.08 + 0.6);
          }});
        }}
      }} catch (e) {{}}
    }}

    // 3. 1 EUR MOKĖJIMO SIMULIACIJOS SISTEMA
    function startPaymentSimulation() {{
      playSciFiChime('start');
      const modal = document.getElementById("paymentModalOverlay");
      if (modal) modal.classList.add("active");

      const s1 = document.getElementById("simStep1");
      const s2 = document.getElementById("simStep2");
      const s3 = document.getElementById("simStep3");
      const banner = document.getElementById("simSuccessBanner");

      s1.className = "sim-step-item active";
      s1.querySelector(".sim-step-circle").textContent = "";
      s2.className = "sim-step-item";
      s2.querySelector(".sim-step-circle").textContent = "";
      s3.className = "sim-step-item";
      s3.querySelector(".sim-step-circle").textContent = "";
      banner.style.display = "none";

      setTimeout(() => {{
        s1.className = "sim-step-item done";
        s1.querySelector(".sim-step-circle").textContent = "✓";
        s2.className = "sim-step-item active";
      }}, 600);

      setTimeout(() => {{
        s2.className = "sim-step-item done";
        s2.querySelector(".sim-step-circle").textContent = "✓";
        s3.className = "sim-step-item active";
      }}, 1300);

      setTimeout(() => {{
        s3.className = "sim-step-item done";
        s3.querySelector(".sim-step-circle").textContent = "✓";
        playSciFiChime('success');
        banner.style.display = "block";
      }}, 2000);
    }}

    function finalizeBookUnlock() {{
      const modal = document.getElementById("paymentModalOverlay");
      if (modal) modal.classList.remove("active");
      
      showSecurityToast("🎉 1,00 € įnašas patvirtintas! Prieiga pilnai suteikta.");
      unlockGateAnimation();
    }}

    function quickDemoUnlock() {{
      showSecurityToast("✨ Demonstracinis režimas: Knyga sėkmingai atrakinta!");
      unlockGateAnimation();
    }}

    function unlockGateAnimation() {{
      const gate = document.getElementById("existentialGate");
      const toolbar = document.getElementById("mainToolbar");
      const content = document.getElementById("bookContent");

      if (gate) {{
        gate.style.transition = "opacity 0.6s ease, transform 0.6s ease";
        gate.style.opacity = "0";
        gate.style.transform = "translateY(-40px)";
        setTimeout(() => {{
          gate.style.display = "none";
          if (toolbar) toolbar.style.display = "flex";
          if (content) content.style.display = "block";
          document.body.classList.remove("gate-active");
          window.scrollTo({{ top: 0, behavior: "smooth" }});
        }}, 600);
      }}
    }}

    // 4. VIRAL SHARE SISTEMA
    function shareBook(platform) {{
      const text = encodeURIComponent("Ar tu supranti, kas vyksta? 99,99% žmonių miega. Aš ką tik perskaičiau 'PO DARBO' monografiją... Nemiegokite:");
      const url = encodeURIComponent(window.location.href || "https://dontbeafoolandopenyoureyesrightnow-project.com");

      if (platform === 'telegram') {{
        window.open(`https://t.me/share/url?url=${{url}}&text=${{text}}`, '_blank');
      }} else if (platform === 'whatsapp') {{
        window.open(`https://api.whatsapp.com/send?text=${{text}}%20${{url}}`, '_blank');
      }} else if (platform === 'x') {{
        window.open(`https://twitter.com/intent/tweet?text=${{text}}&url=${{url}}`, '_blank');
      }} else if (platform === 'facebook') {{
        window.open(`https://www.facebook.com/sharer/sharer.php?u=${{url}}`, '_blank');
      }} else if (platform === 'copy') {{
        try {{
          navigator.clipboard.writeText(decodeURIComponent(text) + " " + decodeURIComponent(url));
          showSecurityToast("📋 Nuoroda nukopijuota į iškarpinę!");
        }} catch(e) {{
          showSecurityToast("📋 Nukopijuota: dontbeafoolandopenyoureyesrightnow-project.com");
        }}
      }}
    }}

    function showSecurityToast(msg) {{
      const toast = document.getElementById("toastNotification");
      if (toast) {{
        if (msg) toast.querySelector("span").textContent = msg;
        toast.classList.add("show");
        clearTimeout(window._toastTimeout);
        window._toastTimeout = setTimeout(() => {{
          toast.classList.remove("show");
        }}, 3400);
      }}
    }}

    // 5. TURINIO APSAUGOS SKYDAS (Anti-Copy / Anti-PDF DRM-Lite)
    document.addEventListener('contextmenu', e => {{
      e.preventDefault();
      showSecurityToast("🔒 Dešinysis pelės klavišas išjungtas siekiant apsaugoti autorių teises.");
    }});

    window.addEventListener('beforeprint', e => {{
      e.preventDefault();
      showSecurityToast("🚫 Spausdinimas ir PDF eksportas yra visiškai blokuojami!");
      return false;
    }});

    document.addEventListener('keydown', e => {{
      if (e.key === "Escape") {{
        closeWikiModal();
      }}
      const k = e.key.toLowerCase();
      if ((e.ctrlKey || e.metaKey) && ['c', 'u', 's', 'p', 'a'].includes(k)) {{
        e.preventDefault();
        if (k === 'p') {{
          showSecurityToast("🚫 Knygos PDF spausdinimas yra išjungtas siekiant išvengti nelegalių kopijų.");
        }} else if (k === 'c' || k === 'a') {{
          showSecurityToast("🔒 Teksto žymėjimas ir kopijavimas yra apsaugoti.");
        }} else {{
          showSecurityToast("🔒 Puslapio kodo peržiūra ir išsaugojimas yra apriboti.");
        }}
        return false;
      }}
      if (e.key === 'F12' || ((e.ctrlKey || e.metaKey) && e.shiftKey && ['i', 'j', 'c'].includes(k))) {{
        e.preventDefault();
        showSecurityToast("🔒 Inspekcijos įrankiai yra išjungti.");
        return false;
      }}
    }});

    // 6. SKAITYMO PROGRESO SEKIMAS IR AUDIO TAKELIŲ VALDYMAS
    window.addEventListener('scroll', () => {{
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      const pBar = document.getElementById("progressBar");
      if (pBar) {{
        pBar.style.width = scrolled + "%";
      }}
    }});

    function navigateToChapter(hash) {{
      if (hash) {{
        window.location.hash = hash;
        setTimeout(updateAudioTrackForCurrentChapter, 150);
      }}
    }}

    // Skyrių audio takelių žemėlapis
    const chapterAudioMap = {{
      "00_prologas": "assets/audio/00_prologas.mp3",
      "01_tyloje_kylantis_dievas": "assets/audio/01_tyloje_kylantis_dievas.mp3",
      "02_baltuju_apykakliu_saulelydis": "assets/audio/02_baltuju_apykakliu_saulelydis.mp3",
      "03_kas_yra_agi_ir_asi": "assets/audio/03_kas_yra_agi_ir_asi.mp3",
      "04_paskutinis_programuotojas": "assets/audio/04_paskutinis_programuotojas.mp3",
      "05_silicio_ir_energijos_karai": "assets/audio/05_silicio_ir_energijos_karai.mp3",
      "06_sulaikymo_problema": "assets/audio/06_sulaikymo_problema.mp3",
      "07_instrumentine_konvergencija": "assets/audio/07_instrumentine_konvergencija.mp3",
      "08_humanoidu_banga": "assets/audio/08_humanoidu_banga.mp3",
      "09_biologijos_nulauzimas": "assets/audio/09_biologijos_nulauzimas.mp3"
    }};

    function getActiveChapterId() {{
      const hash = window.location.hash.replace("#", "");
      if (hash && chapterAudioMap[hash]) return hash;
      const sections = document.querySelectorAll(".chapter");
      let currentId = "00_prologas";
      const scrollPos = window.scrollY + 160;
      sections.forEach(sec => {{
        if (sec.offsetTop <= scrollPos) {{
          currentId = sec.id;
        }}
      }});
      return currentId;
    }}

    function updateAudioTrackForCurrentChapter() {{
      const audio = document.getElementById("bookAudioPlayer");
      if (!audio) return;
      const chId = getActiveChapterId();
      const track = chapterAudioMap[chId] || "assets/audio/00_prologas.mp3";
      if (!audio.src.endsWith(track)) {{
        const wasPlaying = isPlayingAudio;
        audio.src = track;
        if (wasPlaying) {{
          audio.play().catch(e => console.log(e));
        }}
      }}
    }}

    // 7. REALUS AUDIO GROTUVAS SU BĖGANČIU TEKSTU
    let isPlayingAudio = false;
    let audioTimer = null;
    let currentParagraphIdx = 0;

    function toggleAudioReadAlong() {{
      const btn = document.getElementById("audioBtn");
      const audio = document.getElementById("bookAudioPlayer");
      const paragraphs = document.querySelectorAll(".book-container p:not(.book-subtitle), .book-container blockquote");
      
      updateAudioTrackForCurrentChapter();

      if (!isPlayingAudio) {{
        isPlayingAudio = true;
        btn.innerHTML = "⏸️ Pauzė";
        btn.style.background = "var(--accent-cyan)";
        btn.style.color = "#000";

        if (audio) {{
          audio.play().catch(e => console.log("Audio autoplay note:", e));
        }}

        audioTimer = setInterval(() => {{
          document.querySelectorAll(".active-reading-chunk").forEach(el => {{
            el.classList.remove("active-reading-chunk");
          }});

          if (currentParagraphIdx < paragraphs.length) {{
            const activeEl = paragraphs[currentParagraphIdx];
            activeEl.classList.add("active-reading-chunk");
            activeEl.scrollIntoView({{ behavior: "smooth", block: "center" }});
            currentParagraphIdx++;
          }} else {{
            toggleAudioReadAlong();
          }}
        }}, 4500);
      }} else {{
        isPlayingAudio = false;
        clearInterval(audioTimer);
        if (audio) {{
          audio.pause();
        }}
        btn.innerHTML = "🎧 Klausytis (Audio)";
        btn.style.background = "";
        btn.style.color = "var(--accent-cyan)";
        document.querySelectorAll(".active-reading-chunk").forEach(el => {{
          el.classList.remove("active-reading-chunk");
        }});
      }}
    }}

    // 8. TEMŲ PERJUNGIMAS
    const themes = ['theme-dark', 'theme-light', 'theme-sepia'];
    let currentThemeIdx = 0;

    function cycleTheme() {{
      currentThemeIdx = (currentThemeIdx + 1) % themes.length;
      document.body.className = themes[currentThemeIdx];
      const labels = ['🌙 Tamsi', '☀️ Šviesi', '📜 Sepija'];
      const btn = document.getElementById("themeBtn");
      if (btn) btn.innerHTML = labels[currentThemeIdx];
      try {{
        localStorage.setItem('book_theme', themes[currentThemeIdx]);
      }} catch (e) {{}}
    }}

    try {{
      const saved = localStorage.getItem('book_theme');
      if (saved && themes.includes(saved)) {{
        document.body.className = saved;
        currentThemeIdx = themes.indexOf(saved);
        const labels = ['🌙 Tamsi', '☀️ Šviesi', '📜 Sepija'];
        const btn = document.getElementById("themeBtn");
        if (btn) btn.innerHTML = labels[currentThemeIdx];
      }}
    }} catch(e) {{}}
  </script>
</body>
</html>
"""

    dist_output_path = os.path.join(DIST_DIR, "index.html")
    with open(dist_output_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"\n[SEKME] Knyga sekmingai sukompiliuota i: {dist_output_path}")

    root_output_path = os.path.join(BASE_DIR, "index.html")
    with open(root_output_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[SEKME] Sakninis failas sukompiliuotas i: {root_output_path}")

if __name__ == "__main__":
    compile_book()
