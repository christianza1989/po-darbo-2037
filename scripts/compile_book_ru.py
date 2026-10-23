#!/usr/bin/env python3
"""
KOMPILIATORIUS RUSŲ KALBA (Antigravity Studio Edition - Russian Edition)
Sujungia visus skyrius is /chapters_ru katalogo,
sukuria pilną rusišką monografijos versiją: /dist/index_ru.html ir /index_ru.html,
integruoja rusiškus Egzistencinius Vartus, 1 € apmokėjimą, audio grotuvą su Dmitry (RU)
ir kalbos perjungiklį į lietuvių kalbą.
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
CHAPTERS_RU_DIR = os.path.join(BASE_DIR, "chapters_ru")
STYLES_DIR = os.path.join(BASE_DIR, "assets", "styles")
DIST_DIR = os.path.join(BASE_DIR, "dist")
GLOSSARY_PATH = os.path.join(BASE_DIR, "research", "glossary_data.json")

with open(GLOSSARY_PATH, "r", encoding="utf-8") as f:
    GLOSSARY_DATA = json.load(f)

def get_chapter_files():
    files = [f for f in os.listdir(CHAPTERS_RU_DIR) if f.endswith(".md")]
    files.sort()
    return [os.path.join(CHAPTERS_RU_DIR, f) for f in files]

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

def compile_book_ru():
    os.makedirs(DIST_DIR, exist_ok=True)
    css_path = os.path.join(STYLES_DIR, "book.css")
    css_content = read_file(css_path) if os.path.exists(css_path) else ""

    chapter_files = get_chapter_files()
    rendered_chapters = []
    chapter_options = []

    print(f"Rasta RU skyriu: {len(chapter_files)}")

    for cpath in chapter_files:
        raw_text = read_file(cpath)
        raw_text = re.sub(r'src="\.\./assets/images/', 'src="assets/images/', raw_text)

        basename = os.path.basename(cpath)
        info = extract_chapter_info(raw_text, basename)
        print(f" -> Apdorojamas RU: {basename} ({info['title']})")
        
        chapter_options.append(f'<option value="#{info["id"]}">{info["label"]}</option>')

        html = markdown.markdown(
            raw_text,
            extensions=["tables", "fenced_code", "nl2br", "sane_lists"]
        )
        rendered_chapters.append(f'<section class="chapter" id="{info["id"]}">{html}</section>')

    select_html = chr(10).join(chapter_options)
    glossary_json_str = json.dumps(GLOSSARY_DATA, ensure_ascii=False)

    full_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ПОСЛЕ РАБОТЫ: Как ИИ к 2037 году перестроит экономику, государства и человека</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>⚡</text></svg>">
  <meta name="description" content="Стратегическая и аналитическая монография об эпохе искусственного сверхинтеллекта и автономной робототехники (2027–2037 гг.)">
  <style>
{css_content}
  .lang-toggle {{
    display: inline-flex;
    align-items: center;
    background: rgba(15, 23, 42, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 20px;
    padding: 2px 4px;
    margin-right: 8px;
  }}
  .lang-btn {{
    font-family: var(--font-mono);
    font-size: 0.75rem;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 16px;
    color: #94a3b8;
    text-decoration: none;
    transition: all 0.2s ease;
  }}
  .lang-btn.active {{
    background: var(--accent-cyan);
    color: #05070e;
  }}
  .voice-select {{
    background: rgba(15, 23, 42, 0.9);
    border: 1px solid rgba(56, 189, 248, 0.3);
    color: #38bdf8;
    font-family: var(--font-mono);
    font-size: 0.8rem;
    padding: 4px 8px;
    border-radius: 16px;
    cursor: pointer;
  }}
  </style>
</head>
<body class="theme-dark gate-active">

  <!-- ==========================================================================
       ЭКЗИСТЕНЦИАЛЬНЫЕ ВРАТА (Live Worldometer & 1 € Gateway)
       ========================================================================== -->
  <section id="existentialGate" class="existential-gate">
    <div style="display: flex; justify-content: flex-end; width: 100%; max-width: 900px; margin-bottom: 12px;">
      <div class="lang-toggle">
        <a href="index.html" class="lang-btn">🇱🇹 LT</a>
        <a href="index_ru.html" class="lang-btn active">🇷🇺 RU</a>
      </div>
    </div>

    <div class="existential-live-badge">
      <span class="live-pulse-dot"></span>
      ПРЯМАЯ ТРАНСЛЯЦИЯ ЦИВИЛИЗАЦИИ • КОНЕЦ 2026 ГОДА • КРИВАЯ ПОД 90°
    </div>

    <h1 class="existential-hero-title">ПОСЛЕ РАБОТЫ</h1>
    <p class="existential-hero-subtitle">
      Вы упустили слишком многое. Мы исследовали 1 500+ часов отчетов ведущих лабораторий мира, свидетельств нобелевских лауреатов и инсайдеров, чтобы открыть вам глаза перед великим переломом.
    </p>

    <!-- Worldometer Grid -->
    <div class="worldometer-grid">
      <div class="worldometer-card card-danger">
        <div class="worldometer-label">Население Земли</div>
        <div class="worldometer-value" id="counterPopulation">8,188,419,250</div>
        <div class="worldometer-desc">99,99% населения планеты прямо сейчас не понимают АБСОЛЮТНО НИЧЕГО.</div>
      </div>

      <div class="worldometer-card card-warning">
        <div class="worldometer-label">Умерло Сегодня</div>
        <div class="worldometer-value" id="counterDeaths">146,820</div>
        <div class="worldometer-desc">Эти люди не дожили до того, что предстоит пережить вам.</div>
      </div>

      <div class="worldometer-card card-success">
        <div class="worldometer-label">Родилось Сегодня</div>
        <div class="worldometer-value" id="counterBirths">371,430</div>
        <div class="worldometer-desc">Их мир будет полностью неузнаваем — мир без человеческого труда.</div>
      </div>

      <div class="worldometer-card card-purple">
        <div class="worldometer-label">Подключились / Проснулись</div>
        <div class="worldometer-value" id="counterAwakened">13,345,493</div>
        <div class="worldometer-desc">Присоединяйтесь к тем, кто снял розовые очки и готовится сейчас.</div>
      </div>
    </div>

    <!-- Pantheon of Architects -->
    <div class="authority-showcase">
      <div class="authority-title">Монография основана на свидетельствах главных архитекторов мирового разума:</div>
      <div class="authority-badges">
        <span class="auth-chip">🏆 <strong>Джеффри Хинтон</strong> (Нобель 2024)</span>
        <span class="auth-chip">🏆 <strong>Демис Хассабис</strong> (DeepMind, Нобель 2024)</span>
        <span class="auth-chip">🏆 <strong>Дэвид Бейкер</strong> (Нобель 2024)</span>
        <span class="auth-chip">🏆 <strong>Дарон Аджемоглу</strong> (Нобель 2024)</span>
        <span class="auth-chip">🧬 <strong>Дарио Амодеи</strong> (Anthropic)</span>
        <span class="auth-chip">🧠 <strong>Илья Суцкевер</strong> (SSI)</span>
        <span class="auth-chip">⚡ <strong>Дженсен Хуанг</strong> (NVIDIA)</span>
        <span class="auth-chip">👁️ <strong>Мо Гавдат</strong> (Google [X])</span>
        <span class="auth-chip">📜 <strong>Юваль Ной Харари</strong></span>
        <span class="auth-chip">⏳ <strong>Ник Бостром</strong> (Оксфорд)</span>
        <span class="auth-chip">🛡️ <strong>Роман Ямпольский</strong></span>
        <span class="auth-chip">💡 <strong>Сэм Альтман</strong> (OpenAI)</span>
      </div>
    </div>

    <!-- 1 € Paywall Box -->
    <div class="paywall-cta-box">
      <button class="btn-unlock-super" onclick="startPaymentSimulation()">
        ⚡ РАЗБЛОКИРОВАТЬ И НАЧАТЬ ЧТЕНИЕ (1 €)
      </button>

      <div class="fund-promise">
        🕊️ 100% собранных средств направляются в фонд Безопасного Сверхинтеллекта (Safe ASI) и Защиты Человечества.
      </div>

      <div>
        <button class="demo-unlock-link" onclick="quickDemoUnlock()">
          [Демонстрационный режим: Прямая разблокировка]
        </button>
      </div>

      <!-- Viral Share Bar -->
      <div class="viral-share-bar">
        <span style="font-size: 0.8rem; color: #64748b; margin-right: 4px;">Поделиться правдой:</span>
        <button class="btn-share" onclick="shareBook('telegram')">✈️ Telegram</button>
        <button class="btn-share" onclick="shareBook('whatsapp')">💬 WhatsApp</button>
        <button class="btn-share" onclick="shareBook('x')">𝕏 Twitter</button>
        <button class="btn-share" onclick="shareBook('facebook')">📘 Facebook</button>
        <button class="btn-share" onclick="shareBook('copy')">📋 Скопировать ссылку</button>
      </div>
    </div>
  </section>

  <!-- 1 EUR Payment Modal -->
  <div id="paymentModalOverlay" class="payment-modal-overlay">
    <div class="payment-modal-card">
      <div class="pay-modal-top">
        <div class="pay-secure-tag">
          🔒 ЗАШИФРОВАННАЯ МИКРО-ТРАНЗАКЦИЯ
        </div>
        <div class="pay-amount-pill">
          1,00 €
        </div>
      </div>

      <div class="pay-fund-target">
        <div class="pay-fund-label">Назначение платежа и получатель:</div>
        <div class="pay-fund-name">Safe ASI & Humanity Alignment Reserve</div>
        <div class="pay-fund-sub">100% средств направляются на независимые исследования проблемы удержания ИИ</div>
      </div>

      <div class="sim-steps-list" id="simStepsContainer">
        <div class="sim-step-item active" id="simStep1">
          <div class="sim-step-circle"></div>
          <div>Подключение к безопасному платежному шлюзу (Apple Pay / Visa)...</div>
        </div>

        <div class="sim-step-item" id="simStep2">
          <div class="sim-step-circle"></div>
          <div>Резервирование взноса 1,00 € в фонд Safe ASI...</div>
        </div>

        <div class="sim-step-item" id="simStep3">
          <div class="sim-step-circle"></div>
          <div>Генерация персонального зашифрованного ключа #ASI-2026-99...</div>
        </div>
      </div>

      <div class="sim-success-banner" id="simSuccessBanner" style="display: none;">
        <div class="success-badge-icon">✓</div>
        <h3 class="success-title">ПЛАТЕЖ ПОДТВЕРЖДЕН</h3>
        <p class="success-sub">
          1,00 € успешно переведены в резерв Safe ASI.<br>
          <strong>Поздравляем с пробуждением.</strong> Доступ ко всей монографии и аналитике активирован.
        </p>
        <button class="btn-proceed-reading" onclick="finalizeBookUnlock()">
          НАЧАТЬ ЧТЕНИЕ И АНАЛИТИКУ ➔
        </button>
      </div>
    </div>
  </div>

  <!-- Bespoke Wiki Modal -->
  <div id="wikiModalOverlay" class="wiki-modal-overlay" onclick="closeWikiModalOnBackdrop(event)">
    <div class="wiki-modal-card" id="wikiModalCard">
      <div id="wikiModalDynamicBody"></div>
    </div>
  </div>

  <!-- Top Navigation Toolbar -->
  <header class="reader-toolbar" id="mainToolbar" style="display: none;">
    <div class="reader-progress-track">
      <div class="reader-progress-bar" id="progressBar"></div>
    </div>
    
    <div class="reader-brand">
      <span>ПОСЛЕ РАБОТЫ</span>
      <span class="pill-badge" style="background: rgba(16, 185, 129, 0.2); border-color: rgba(16, 185, 129, 0.4); color: #10b981;">
        🟢 ДОСТУП АКТИВЕН (1 €)
      </span>
    </div>

    <div class="reader-controls">
      <div class="lang-toggle">
        <a href="index.html" class="lang-btn">🇱🇹 LT</a>
        <a href="index_ru.html" class="lang-btn active">🇷🇺 RU</a>
      </div>

      <select class="chapter-select" id="chapterNav" onchange="navigateToChapter(this.value)">
        <option value="">-- Выберите главу --</option>
        {select_html}
      </select>

      <button class="btn-pill" onclick="toggleAudioReadAlong()" id="audioBtn" style="border-color: var(--accent-cyan); color: var(--accent-cyan);" title="Слушать профессиональную озвучку">
        🎧 Слушать (Аудио)
      </button>

      <select class="voice-select" id="voiceSelect" onchange="changeVoice(this.value)" title="Выбрать голос озвучки">
        <option value="ru" selected>🇷🇺 Дмитрий (RU)</option>
        <option value="lt">🇱🇹 Леонас (LT)</option>
      </select>

      <button class="btn-pill" onclick="cycleTheme()" id="themeBtn" title="Сменить тему">
        🌓 Тема
      </button>

      <span class="drm-badge" title="Контент защищен от несанкционированного копирования и экспорта">
        🔒 DRM Защита
      </span>
    </div>

    <audio id="bookAudioPlayer" preload="auto">
      <source src="assets/audio/ru/00_prologas.mp3" type="audio/mpeg">
      <source src="../assets/audio/ru/00_prologas.mp3" type="audio/mpeg">
    </audio>
  </header>

  <!-- Main Content -->
  <main class="book-container" id="bookContent" style="display: none;">
    {chr(10).join(rendered_chapters)}
  </main>

  <div id="toastNotification" class="toast-notification">
    <span>🔒 Копирование, печать и экспорт в PDF отключены для защиты авторских прав.</span>
  </div>

  <script>
    const GLOSSARY_DB = {glossary_json_str};
    let currentVoice = "ru";

    function changeVoice(voice) {{
      currentVoice = voice;
      updateAudioTrackForCurrentChapter();
      if (isPlayingAudio) {{
        const audio = document.getElementById("bookAudioPlayer");
        if (audio) audio.play().catch(e => console.log(e));
      }}
    }}

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
              <div class="wiki-category-badge ${{data.badge_color || 'cyan'}}">${{data.category || 'КОГНИТИВНЫЙ СПРАВОЧНИК'}}</div>
              <h2 class="wiki-title">${{data.title}}</h2>
              <div class="wiki-en-title">${{data.en_title || ''}}</div>
            </div>
            <button class="wiki-btn-close" onclick="closeWikiModal()" title="Закрыть (ESC)">✕</button>
          </div>
          <div class="wiki-bespoke-content">
            ${{data.custom_html}}
          </div>
          <div class="wiki-modal-footer">
            <span class="wiki-footer-hint">ПОСЛЕ РАБОТЫ • Когнитивная энциклопедия</span>
            <button class="wiki-btn-dismiss" onclick="closeWikiModal()">Понятно ➔</button>
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

    // Worldometer & Paywall Logic
    let popVal = 8188419250;
    let deathVal = 146820;
    let birthVal = 371430;
    let awakenVal = 13345493;

    function initWorldometer() {{
      setInterval(() => {{
        popVal += Math.floor(Math.random() * 3) + 1;
        deathVal += (Math.random() > 0.4 ? 1 : 0);
        birthVal += Math.floor(Math.random() * 3) + 1;
        if (Math.random() > 0.6) awakenVal += 1;

        const elPop = document.getElementById("counterPopulation");
        const elDeath = document.getElementById("counterDeaths");
        const elBirth = document.getElementById("counterBirths");
        const elAwk = document.getElementById("counterAwakened");

        if (elPop) elPop.textContent = popVal.toLocaleString("ru-RU");
        if (elDeath) elDeath.textContent = deathVal.toLocaleString("ru-RU");
        if (elBirth) elBirth.textContent = birthVal.toLocaleString("ru-RU");
        if (elAwk) elAwk.textContent = awakenVal.toLocaleString("ru-RU");
      }}, 1200);
    }}

    function playSciFiChime(type) {{
      try {{
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        if (type === 'unlock') {{
          osc.type = 'sine';
          osc.frequency.setValueAtTime(440, ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.3);
          gain.gain.setValueAtTime(0.15, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.6);
          osc.start();
          osc.stop(ctx.currentTime + 0.6);
        }} else if (type === 'step') {{
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(520, ctx.currentTime);
          gain.gain.setValueAtTime(0.08, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.15);
          osc.start();
          osc.stop(ctx.currentTime + 0.15);
        }} else if (type === 'wiki') {{
          osc.type = 'sine';
          osc.frequency.setValueAtTime(660, ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(1100, ctx.currentTime + 0.2);
          gain.gain.setValueAtTime(0.1, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
          osc.start();
          osc.stop(ctx.currentTime + 0.3);
        }}
      }} catch (e) {{}}
    }}

    function startPaymentSimulation() {{
      const overlay = document.getElementById("paymentModalOverlay");
      if (!overlay) return;
      overlay.classList.add("active");
      playSciFiChime('step');

      setTimeout(() => {{
        const s2 = document.getElementById("simStep2");
        if (s2) s2.classList.add("active");
        playSciFiChime('step');
      }}, 1200);

      setTimeout(() => {{
        const s3 = document.getElementById("simStep3");
        if (s3) s3.classList.add("active");
        playSciFiChime('step');
      }}, 2400);

      setTimeout(() => {{
        const steps = document.getElementById("simStepsContainer");
        const banner = document.getElementById("simSuccessBanner");
        if (steps) steps.style.display = "none";
        if (banner) banner.style.display = "block";
        playSciFiChime('unlock');
      }}, 3600);
    }}

    function finalizeBookUnlock() {{
      const overlay = document.getElementById("paymentModalOverlay");
      if (overlay) overlay.classList.remove("active");
      unlockBookView();
    }}

    function quickDemoUnlock() {{
      playSciFiChime('unlock');
      unlockBookView();
    }}

    function unlockBookView() {{
      document.body.classList.remove("gate-active");
      const gate = document.getElementById("existentialGate");
      const toolbar = document.getElementById("mainToolbar");
      const content = document.getElementById("bookContent");

      if (gate) gate.style.display = "none";
      if (toolbar) toolbar.style.display = "flex";
      if (content) content.style.display = "block";

      localStorage.setItem("po_darbo_unlocked_ru", "true");
      updateProgressBar();
    }}

    const chapterAudioMapRu = {{
      "00_prologas": "assets/audio/ru/00_prologas.mp3",
      "01_tyloje_kylantis_dievas": "assets/audio/ru/01_tyloje_kylantis_dievas.mp3",
      "02_baltuju_apykakliu_saulelydis": "assets/audio/ru/02_baltuju_apykakliu_saulelydis.mp3",
      "03_kas_yra_agi_ir_asi": "assets/audio/ru/03_kas_yra_agi_ir_asi.mp3",
      "04_paskutinis_programuotojas": "assets/audio/ru/04_paskutinis_programuotojas.mp3",
      "05_silicio_ir_energijos_karai": "assets/audio/ru/05_silicio_ir_energijos_karai.mp3",
      "06_sulaikymo_problema": "assets/audio/ru/06_sulaikymo_problema.mp3",
      "07_instrumentine_konvergencija": "assets/audio/ru/07_instrumentine_konvergencija.mp3",
      "08_humanoidu_banga": "assets/audio/ru/08_humanoidu_banga.mp3",
      "09_biologijos_nulauzimas": "assets/audio/ru/09_biologijos_nulauzimas.mp3",
      "10_dvi_ateitys_utopija_pries_distopija": "assets/audio/ru/10_dvi_ateitys_utopija_pries_distopija.mp3",
      "11_ekonomika_be_algu": "assets/audio/ru/11_ekonomika_be_algu.mp3",
      "12_kas_lieka_zmogui": "assets/audio/ru/12_kas_lieka_zmogui.mp3",
      "13_samones_perkelimas_ir_nemirtingumas": "assets/audio/ru/13_samones_perkelimas_ir_nemirtingumas.mp3",
      "14_dyson_sferos_ir_zvaigzdziu_inzinerija": "assets/audio/ru/14_dyson_sferos_ir_zvaigzdziu_inzinerija.mp3",
      "15_didysis_filtras_ir_fermi_paradoksas": "assets/audio/ru/15_didysis_filtras_ir_fermi_paradoksas.mp3",
      "16_praktinis_manifestas": "assets/audio/ru/16_praktinis_manifestas.mp3"
    }};

    const chapterAudioMapLt = {{
      "00_prologas": "assets/audio/lt/00_prologas.mp3",
      "01_tyloje_kylantis_dievas": "assets/audio/lt/01_tyloje_kylantis_dievas.mp3",
      "02_baltuju_apykakliu_saulelydis": "assets/audio/lt/02_baltuju_apykakliu_saulelydis.mp3",
      "03_kas_yra_agi_ir_asi": "assets/audio/lt/03_kas_yra_agi_ir_asi.mp3",
      "04_paskutinis_programuotojas": "assets/audio/lt/04_paskutinis_programuotojas.mp3",
      "05_silicio_ir_energijos_karai": "assets/audio/lt/05_silicio_ir_energijos_karai.mp3",
      "06_sulaikymo_problema": "assets/audio/lt/06_sulaikymo_problema.mp3",
      "07_instrumentine_konvergencija": "assets/audio/lt/07_instrumentine_konvergencija.mp3",
      "08_humanoidu_banga": "assets/audio/lt/08_humanoidu_banga.mp3",
      "09_biologijos_nulauzimas": "assets/audio/lt/09_biologijos_nulauzimas.mp3",
      "10_dvi_ateitys_utopija_pries_distopija": "assets/audio/lt/10_dvi_ateitys_utopija_pries_distopija.mp3",
      "11_ekonomika_be_algu": "assets/audio/lt/11_ekonomika_be_algu.mp3",
      "12_kas_lieka_zmogui": "assets/audio/lt/12_kas_lieka_zmogui.mp3",
      "13_samones_perkelimas_ir_nemirtingumas": "assets/audio/lt/13_samones_perkelimas_ir_nemirtingumas.mp3",
      "14_dyson_sferos_ir_zvaigzdziu_inzinerija": "assets/audio/lt/14_dyson_sferos_ir_zvaigzdziu_inzinerija.mp3",
      "15_didysis_filtras_ir_fermi_paradoksas": "assets/audio/lt/15_didysis_filtras_ir_fermi_paradoksas.mp3",
      "16_praktinis_manifestas": "assets/audio/lt/16_praktinis_manifestas.mp3"
    }};

    function getActiveChapterId() {{
      const chapters = document.querySelectorAll(".chapter");
      let activeId = "00_prologas";
      const scrollPos = window.scrollY + 120;
      chapters.forEach(ch => {{
        if (ch.offsetTop <= scrollPos) {{
          activeId = ch.id;
        }}
      }});
      return activeId;
    }}

    function updateAudioTrackForCurrentChapter() {{
      const audio = document.getElementById("bookAudioPlayer");
      if (!audio) return;
      const chId = getActiveChapterId();
      const map = (currentVoice === "ru") ? chapterAudioMapRu : chapterAudioMapLt;
      const track = map[chId] || "assets/audio/ru/00_prologas.mp3";
      if (!audio.src.endsWith(track)) {{
        const wasPlaying = isPlayingAudio;
        audio.src = track;
        if (wasPlaying) {{
          audio.play().catch(e => console.log(e));
        }}
      }}
    }}

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
        btn.innerHTML = "⏸️ Пауза";
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
        btn.innerHTML = "🎧 Слушать (Аудио)";
        btn.style.background = "";
        btn.style.color = "var(--accent-cyan)";
        document.querySelectorAll(".active-reading-chunk").forEach(el => {{
          el.classList.remove("active-reading-chunk");
        }});
      }}
    }}

    function navigateToChapter(hash) {{
      if (!hash) return;
      const target = document.querySelector(hash);
      if (target) {{
        target.scrollIntoView({{ behavior: "smooth" }});
        setTimeout(updateAudioTrackForCurrentChapter, 500);
      }}
    }}

    function updateProgressBar() {{
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
      const pbar = document.getElementById("progressBar");
      if (pbar) pbar.style.width = scrolled + "%";

      const nav = document.getElementById("chapterNav");
      if (nav) {{
        const activeId = getActiveChapterId();
        if (nav.value !== "#" + activeId) {{
          nav.value = "#" + activeId;
        }}
      }}
    }}

    function cycleTheme() {{
      const b = document.body;
      if (b.classList.contains("theme-dark")) {{
        b.classList.remove("theme-dark");
        b.classList.add("theme-sepia");
      }} else if (b.classList.contains("theme-sepia")) {{
        b.classList.remove("theme-sepia");
        b.classList.add("theme-light");
      }} else {{
        b.classList.remove("theme-light");
        b.classList.add("theme-dark");
      }}
    }}

    function shareBook(platform) {{
      const url = window.location.href;
      const text = "«ПОСЛЕ РАБОТЫ: Как ИИ к 2037 году перестроит экономику, государства и человека» — экзистенциальная монография эпохи ASI.";
      if (platform === 'telegram') {{
        window.open(`https://t.me/share/url?url=${{encodeURIComponent(url)}}&text=${{encodeURIComponent(text)}}`, '_blank');
      }} else if (platform === 'whatsapp') {{
        window.open(`https://api.whatsapp.com/send?text=${{encodeURIComponent(text + ' ' + url)}}`, '_blank');
      }} else if (platform === 'x') {{
        window.open(`https://twitter.com/intent/tweet?text=${{encodeURIComponent(text)}}&url=${{encodeURIComponent(url)}}`, '_blank');
      }} else if (platform === 'facebook') {{
        window.open(`https://www.facebook.com/sharer/sharer.php?u=${{encodeURIComponent(url)}}`, '_blank');
      }} else if (platform === 'copy') {{
        navigator.clipboard.writeText(url).then(() => showToast("Ссылка скопирована в буфер!"));
      }}
    }}

    function showToast(msg) {{
      const t = document.getElementById("toastNotification");
      if (!t) return;
      if (msg) t.querySelector("span").textContent = msg;
      t.classList.add("show");
      setTimeout(() => t.classList.remove("show"), 3500);
    }}

    window.addEventListener("scroll", updateProgressBar);
    window.addEventListener("load", () => {{
      initWorldometer();
      if (localStorage.getItem("po_darbo_unlocked_ru") === "true") {{
        unlockBookView();
      }}
    }});

    // DRM Protection
    document.addEventListener("contextmenu", e => {{
      e.preventDefault();
      showToast("🔒 Копирование текста отключено для защиты авторских прав.");
    }});

    document.addEventListener("keydown", e => {{
      if ((e.ctrlKey || e.metaKey) && ['c', 'p', 's', 'u'].includes(e.key.toLowerCase())) {{
        e.preventDefault();
        showToast("🔒 Экспорт и копирование отключены.");
      }}
      if (e.key === "F12") {{
        e.preventDefault();
      }}
      if (e.key === "Escape") {{
        closeWikiModal();
      }}
    }});
  </script>
</body>
</html>"""

    out_dist = os.path.join(DIST_DIR, "index_ru.html")
    with open(out_dist, "w", encoding="utf-8") as f:
        f.write(full_html)

    out_root = os.path.join(BASE_DIR, "index_ru.html")
    with open(out_root, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"\n[SEKME] Rusiska knyga sekmingai sukompiliuota i: {out_dist}")
    print(f"[SEKME] Sakninis failas sukompiliuotas i: {out_root}")

if __name__ == "__main__":
    compile_book_ru()
