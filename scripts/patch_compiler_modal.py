import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

compile_script_path = os.path.join(os.path.dirname(__file__), "compile_book.py")

with open(compile_script_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Pakeičiame statinį modal HTML į dinaminį
old_modal_chunk = """  <!-- ==========================================================================
       MINI-WIKIPEDIA KOGNITYVINIS ŽINYNAS (MODALAS)
       ========================================================================== -->
  <div id="wikiModalOverlay" class="wiki-modal-overlay" onclick="closeWikiModalOnBackdrop(event)">
    <div class="wiki-modal-card" id="wikiModalCard">
      <div class="wiki-modal-header">
        <div class="wiki-header-left">
          <div class="wiki-category-badge cyan" id="wikiBadge">KOGNITYVINIS TERMINAS</div>
          <h2 class="wiki-title" id="wikiTitle">Technologinis Singuliarumas</h2>
          <div class="wiki-en-title" id="wikiEnTitle">Technological Singularity</div>
        </div>
        <button class="wiki-btn-close" onclick="closeWikiModal()" title="Uždaryti langą (ESC)">✕</button>
      </div>

      <div class="wiki-summary-box" id="wikiSummary">
        Hipotetinis civilizacijos taškas...
      </div>

      <div class="wiki-grid">
        <div class="wiki-card-item what">
          <div class="wiki-item-label">🔍 Kas tai yra? (Esmė paprastai / Level 1)</div>
          <div class="wiki-item-text" id="wikiWhat">...</div>
        </div>

        <div class="wiki-card-item how">
          <div class="wiki-item-label">⚙️ Kaip tai veikia? (Gilus mechanizmas / Level 99)</div>
          <div class="wiki-item-text" id="wikiHow">...</div>
        </div>

        <div class="wiki-card-item impact">
          <div class="wiki-item-label">💥 Kodėl tai lemia tavo ateitį? (Egzistencinis poveikis)</div>
          <div class="wiki-item-text" id="wikiImpact">...</div>
        </div>

        <div class="wiki-card-item when">
          <div class="wiki-item-label">⏳ Kada tai įvyks? (Insiderių prognozė)</div>
          <div class="wiki-item-text" id="wikiWhen">...</div>
        </div>
      </div>

      <div class="wiki-modal-footer">
        <span class="wiki-footer-hint">PO DARBO • Kognityvinė Enciklopedija</span>
        <button class="wiki-btn-dismiss" onclick="closeWikiModal()">Supratau ➔</button>
      </div>
    </div>
  </div>"""

new_modal_chunk = """  <!-- ==========================================================================
       MINI-WIKIPEDIA KOGNITYVINIS ŽINYNAS (MODALAS) - DINAMINIS BESPOKE MAKETAS
       ========================================================================== -->
  <div id="wikiModalOverlay" class="wiki-modal-overlay" onclick="closeWikiModalOnBackdrop(event)">
    <div class="wiki-modal-card" id="wikiModalCard">
      <!-- Dinamiškai sugeneruojamas unikalus kiekvieno termino/asmens turinys -->
      <div id="wikiModalDynamicBody"></div>
    </div>
  </div>"""

# 2. Pakeičiame openWikiModal funkciją
old_func_chunk = """    function openWikiModal(termKey) {{
      const modal = document.getElementById("wikiModalOverlay");
      const data = GLOSSARY_DB[termKey];
      if (!modal || !data) return;

      playSciFiChime('wiki');

      const badge = document.getElementById("wikiBadge");
      badge.textContent = data.category || "KOGNITYVINIS TERMINAS";
      badge.className = "wiki-category-badge " + (data.badge_color || "cyan");

      document.getElementById("wikiTitle").textContent = data.title;
      document.getElementById("wikiEnTitle").textContent = data.en_title || "";
      document.getElementById("wikiSummary").textContent = data.summary;
      document.getElementById("wikiWhat").textContent = data.what;
      document.getElementById("wikiHow").textContent = data.how;
      document.getElementById("wikiImpact").textContent = data.impact;
      document.getElementById("wikiWhen").textContent = data.when;

      modal.classList.add("active");
    }}"""

new_func_chunk = """    function openWikiModal(termKey) {{
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
    }}"""

def norm(s):
    return s.replace("\r\n", "\n")

norm_code = norm(code)
norm_old_modal = norm(old_modal_chunk)
norm_new_modal = norm(new_modal_chunk)
norm_old_func = norm(old_func_chunk)
norm_new_func = norm(new_func_chunk)

if norm_old_modal in norm_code:
    norm_code = norm_code.replace(norm_old_modal, norm_new_modal)
    print("Sekmingai atnaujintas modal HTML!")
else:
    print("ISPEJIMAS: norm_old_modal nerastas kode.")

if norm_old_func in norm_code:
    norm_code = norm_code.replace(norm_old_func, norm_new_func)
    print("Sekmingai atnaujinta openWikiModal JS funkcija!")
else:
    print("ISPEJIMAS: norm_old_func nerastas kode.")

with open(compile_script_path, "w", encoding="utf-8") as f:
    f.write(norm_code)

print("compile_book.py sekmingai atnaujintas!")
