<span class="chapter-number">II DALIS · 4 SKYRIUS</span>
<h2 class="chapter-title">Paskutinis programuotojas ir rekursyvus savęs tobulinimas</h2>

<p class="chapter-lead">
  „Mokykitės programuoti“ – trisdešimt metų tai buvo auksinis bilietas į saugią ateitį. Tačiau programinės įrangos inžinerija pasirodė esanti pati pirmoji disciplina, kurioje mašinos ne tik prilygo žmogui, bet ir perėmė savo pačių kodo tobulinimo estafetę. Prasideda rekursyvaus savęs tobulinimo era.
</p>

<p class="drop-cap">
  2024 m. buvęs „OpenAI“ vyriausiasis mokslininkas <strong>Ilya Sutskeveris</strong> paskelbė paliekantis kompaniją ir kuriantis naują laboratoriją – <em>Safe Superintelligence (SSI)</em>. Jo pasitraukimas nebuvo susijęs su pinigais ar verslo nesutarimais. Sutskeveris suprato tai, ką Silicio slėnio elitas ilgai bandė sumenkinti: mes pasiekėme ribą, kuomet žmogus tampa lėčiausia, labiausiai stabdančia grandimi paties DI kūrimo procese.
</p>

<p>
  Iki šiol DI modelių kūrimas rėmėsi žmonių parašytais tekstais ir kodu iš „GitHub“ ar „Stack Overflow“. Tačiau šie duomenys baigėsi. Naujasis proveržio etapas, apie kurį laidoje <em>The Diary Of A CEO</em> kalbėjo ekspertai, remiasi dviem poliais: <strong>sintetiniais duomenimis</strong> ir <strong>modelių refleksija atliekant kodo optimizavimą</strong>.
</p>

<figure style="margin: 40px 0; border-radius: 14px; overflow: hidden; border: 1px solid var(--border-subtle);">
  <img src="../assets/images/ch03_recursive_code.jpg" alt="Rekursyvaus kodo matrica ir tuščia inžinieriaus kėdė" style="width: 100%; height: auto; display: block; object-fit: cover; max-height: 480px;">
  <figcaption style="padding: 12px 18px; font-family: var(--font-sans); font-size: 0.85rem; color: var(--text-muted); background: var(--bg-surface); text-align: center; border-top: 1px solid var(--border-subtle);">
    Paskutinio programuotojo pasitraukimas: algoritmai savarankiškai rašo, testuoja ir optimizuoja savo pačių naujos kartos architektūras, palikdami biologinį protą nuošalyje.
  </figcaption>
</figure>

<h3>Yannas LeCun ir „pasaulio modelių“ riba</h3>

<p>
  Tiesa, skeptiškasis „Meta“ DI vadovas <strong>Yannas LeCun</strong> Steveno Bartletto laidoje atkreipė dėmesį į esminę autoregresinių modelių silpnybę:
</p>

<blockquote class="expert-quote">
  „Dabartiniai kalbos modeliai nesupranta pagrindinių fizikos dėsnių. Jei jūs stumiate stalą, ant kurio stovi stiklinė, katė supranta, kad stiklinė nukris. Kalbos modelis to nežino, kol to neperskaitė tekste. Tačiau programavimas yra formali, matematiškai apibrėžta sistema. Čia taisyklės yra tobulai aiškios: kodas arba veikia ir kompiliuojasi, arba ne. Todėl programavime DI pasiekė dievišką lygį gerokai anksčiau nei bendrajame pasaulio supratime.“
  <cite>— Prof. Yann LeCun, <span>Turingo premijos laureatas, The Diary Of A CEO</span></cite>
</blockquote>

<p>
  Būtent programinis kodas tapo ta terpe, kurioje DI modeliai pradėjo taikyti <strong>stiprinamąjį mokymąsi (Reinforcement Learning)</strong>. Modelis sukuria milijoną programinio kodo variantų, juos paleidžia virtualioje aplinkoje, atrenka 0.1% greičiausių ir efektyviausių algoritmų ir mokosi iš šio rezultato be jokio žmogaus įsikišimo.
</p>

<h3>Leopoldo Aschenbrennerio manifestas: Šuolis į AGI iki 2027 m.</h3>

<p>
  Buvęs „OpenAI“ superderinimo (Superalignment) komandos narys <strong>Leopoldas Aschenbrenneris</strong> savo 165 puslapių analizėje <em>„Situational Awareness“</em> aprašė, kas nutinka, kai DI perima DI tyrėjo vaidmenį:
</p>

<p>
  „Šiandien prie pažangiausių modelių dirba keli šimtai talentingiausių pasaulio inžinierių. Tačiau iki 2027 metų mes turėsime sistemas, prilygstančias geriausiam DI tyrėjui. Užuot turėję kelis šimtus žmonių, laboratorijos paleis <strong>100 000 automatizuotų DI mokslininkų spiečių</strong>, dirbančių 24 valandas per parą, 7 dienas per savaitę, 100 kartų greitesniu nei žmogaus tempu. Tai, kas anksčiau užtrukdavo dešimtmetį tyrimų, bus atlikta per kelis mėnesius.“
</p>

<div class="warning-box">
  <h4>Rekursyvaus tobulėjimo spąstai</h4>
  <p>
    Kai mašina pati rašo kodą savo kitai versijai, žmogus nebegali patikrinti kodo eilučių. Algoritmai tampa per gilūs, per daugiasluoksniai ir pernelyg abstraktūs biologinėms smegenims. Paskutinis žmogus-programuotojas nustoja būti kūrėju ir tampa tiesiog stebėtoju, kurio vienintelis darbas – patvirtinti galutinius sistemos parametrus.
  </p>
</div>

<!-- INFOGRAFIKAS 4: Rekursyvus tobulėjimo ciklas -->
<div class="infographic-wrapper">
  <div class="infographic-header">
    <span class="badge">Uždaros Kilpos Architektūra</span>
    <h3>Rekursyvusis Savęs Tobulinimas (Recursive Self-Improvement)</h3>
    <p>Kaip DI perima programinės įrangos evoliuciją ir pašalina žmogaus kognityvinius apribojimus.</p>
  </div>

  <svg viewBox="0 0 800 360" fill="none" xmlns="http://www.w3.org/2000/svg">
    <!-- Circle nodes -->
    <!-- 1. Modelis N -->
    <rect x="60" y="140" width="180" height="80" rx="12" fill="#181e2b" stroke="#38bdf8" stroke-width="2"/>
    <text x="150" y="175" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="13" text-anchor="middle">ESAMAS DI MODELIS</text>
    <text x="150" y="198" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" text-anchor="middle">Bazinė architektūra (N)</text>

    <!-- Arrow 1 -> 2 -->
    <path d="M240 180 L310 180" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>

    <!-- 2. Kodo generavimas ir optimizavimas -->
    <rect x="310" y="140" width="200" height="80" rx="12" fill="#181e2b" stroke="#10b981" stroke-width="2"/>
    <text x="410" y="172" fill="#10b981" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="13" text-anchor="middle">AUTOMATINIS KODAVIMAS</text>
    <text x="410" y="192" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" text-anchor="middle">Milijonai sintetinių kodo testų</text>
    <text x="410" y="206" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" text-anchor="middle">Greitesnės matricos ir branduoliai</text>

    <!-- Arrow 2 -> 3 -->
    <path d="M510 180 L580 180" stroke="#10b981" stroke-width="2"/>

    <!-- 3. Naujas Modelis N+1 -->
    <rect x="580" y="140" width="180" height="80" rx="12" fill="#181e2b" stroke="#a855f7" stroke-width="2"/>
    <text x="670" y="175" fill="#a855f7" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="13" text-anchor="middle">NAUJAS MODELIS (N+1)</text>
    <text x="670" y="198" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" text-anchor="middle">+300% Intelekto tankis</text>

    <!-- Feedback loop (The recursion) -->
    <path d="M670 140 C670 60, 150 60, 150 140" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="5" fill="none"/>
    <text x="410" y="75" fill="#f43f5e" font-family="'Plus Jakarta Sans', sans-serif" font-weight="700" font-size="12" text-anchor="middle">REKURSYVUS GRĮŽTAMASIS RYŠYS (Žmogus pašalintas iš ciklo)</text>
    
    <!-- Human sideline -->
    <rect x="330" y="270" width="160" height="50" rx="8" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <text x="410" y="295" fill="#64748b" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" text-anchor="middle">Žmogus-inžinierius</text>
    <text x="410" y="310" fill="#f43f5e" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">(Per lėtas kognityvinis butelio kaklelis)</text>
    <path d="M410 270 L410 220" stroke="#475569" stroke-width="1.5" stroke-dasharray="3"/>
  </svg>
</div>

<h3>Programinės įrangos savikainos griūtis iki nulio: „Software is Dead“</h3>

<p>
  Ką tai reiškia verslui, kūrėjams ir visuomenei? Tai reiškia reiškinį, kurį Silicio slėnio rizikos kapitalistai jau atvirai vadina **tradicinės programinės įrangos mirtimi**.
</p>

<p>
  Trisdešimt metų technologijų verslas rėmėsi viena auksine taisykle: *„Sukurk sudėtingą kodą vieną kartą, apgaubk jį patentais ar slaptais serveriais ir pardavinėk mėnesines prenumeratas (SaaS) su 85% pelno marža“*. Ši tvirtovė subyrėjo per kelis mėnesius.
</p>

<h3>Andrejaus Karpathy evoliucija: Nuo „Software 1.0“ iki „Software 3.0“</h3>

<p>
  Buvęs „Tesla AI“ direktorius ir vienas iš „OpenAI“ įkūrėjų <strong>Andrejus Karpathy</strong> aprašė fundamentalų posūkį kompiuterijos istorijoje:
</p>

<ul style="padding-left: 28px; margin-bottom: 24px; color: var(--text-secondary);">
  <li style="margin-bottom: 10px;"><strong>Software 1.0 (Žmogaus kodas):</strong> Programuotojas rankiniu būdu rašo taisykles C++, Python ar Java kalbomis. Kiekviena logika, kiekviena išimtis turi būti apgalvota žmogaus. Ši era baigėsi.</li>
  <li style="margin-bottom: 10px;"><strong>Software 2.0 (Diferencijuojami svoriai):</strong> Kodą rašo ne žmogus, o neuroninio tinklo optimizavimo algoritmas (gradientinis nusileidimas). Programa yra ne tekstas, o milijardai plaukiojančio kablelio skaičių (svorių).</li>
  <li style="margin-bottom: 10px;"><strong>Software 3.0 (Agentų simfonija):</strong> Programavimo kalba tampa natūrali žmogaus šneka. Vartotojas nurodo norimą rezultatą, o autonominių agentų spiečius realiuoju laiku sugeneruoja, ištestuoja, paleidžia ir prireikus sunaikina reikiamą programinę infrastruktūrą.</li>
</ul>

<h3>Erico Schmidto nutekintas patarimas ir intelektinės nuosavybės mirtis</h3>

<p>
  2024 m. pabaigoje internete sprogo slapta nufilmuota buvusio „Google“ vadovo <strong>Erico Schmidto</strong> paskaita Stenfordo universiteto studentams. Schmidtas atvirai rėžė tai, ką Silicio slėnio teisininkai bando nutylėti:
</p>

<blockquote class="expert-quote">
  „Silicio slėnis dešimtmečius meldėsi intelektinei nuosavybei ir patentams. Šiandien sakau jums atvirai: jei esate startuolio įkūrėjas, pamirškite autorines teises. Paimkite konkurentų duomenis, suklonuokite jų sistemą naudodami DI per savaitgalį, paleiskite produktą į rinką ir užkariaukite vartotojus. O jei jie jus paduos į teismą – pasamdykite geriausius advokatus tada, kai būsite uždirbę milijardus. Nes jei elgsitės pagal senąsias taisykles ir lauksite licencijų – jūs būsite mirę anksčiau, nei pradėsite.“
  <cite>— Eric Schmidt, <span>buvęs „Google“ vadovas, nutekinta Stenfordo paskaita</span></cite>
</blockquote>

<h3>GitHub REA banga: Kaip moksleivis per vakarą klonuoja 100 mln. $ imperiją</h3>

<p>
  Atvirojo kodo bendruomenėje sprogo reiškinys, žinomas kaip **REA (Reverse Engineer Anything – Grįžtamoji bet kurios sistemos inžinerija)**:
</p>

<p>
  Šiuolaikiniai autonominiai kodo agentai neberašo kodo nuo tuščio lapo. Prijungti prie naršyklės automatizavimo ir binarinių failų inspektorių (tokių kaip „Ghidra“), agentai savarankiškai „apeina“ bet kurį komercinį produktą. Jie analizuoja duomenų bazių schemas, API užklausų struktūras, naudotojo sąsajos logiką ir per **kelias valandas sugeneruoja pilnavertį, identiškai veikiantį atvirojo kodo pakaitalą**.
</p>

<div class="concept-card">
  <h4>Kūrybinių monopolijų griūtis: Nuo „Adobe“ iki „Figma“</h4>
  <p>
    Dešimtmečius tokie gigantai kaip „Adobe“ reikalavo šimtų eurų metinių prenumeratų už „Photoshop“, „Premiere“ ar „Illustrator“. Šiandien bet kuris technologijomis besidomintis paauglys gali pasinaudoti atvirojo kodo modeliais („ComfyUI“, „WebGPU“ varikliais ir lokaliais agentais), kad savo asmeniniame kompiuteryje be jokių mokesčių paleistų profesionalią vaizdų redagavimo ir generavimo studiją, kuri veikia greičiau, neturi korporacinės cenzūros ir idealiai prisitaiko prie jo asmeninių poreikių. <strong>Uždaro kodo gynybinis griovys (angl. <em>Moat</em>) išgaravo.</strong>
  </p>
</div>

<h3>„Vienkartinė programinė įranga“ (Disposable Software)</h3>

<p>
  Atsiranda visiškai nauja vartojimo paradigma – <strong>vienkartinės aplikacijos</strong>.
</p>

<p>
  Praeityje, jei jums reikėjo suorganizuoti specifinį renginį ar atlikti specifinę duomenų analizę, jūs pirkote brangią platformą metams. Šiandien jūs tiesiog ištariate komandą: <em>„Sukurk man įrankį, kuris išanalizuoja šiuos 50 failų, sugeneruoja interaktyvų 3D grafiką ir suderina sąskaitas su mano banku“</em>. Agentas per 45 sekundes sugeneruoja pilnavertį kodą, paleidžia jį naršyklėje, jūs atliekate darbą ir… <strong>kodą išmetate</strong>.
</p>

<p>
  Programinė įranga nustojo būti ilgalaikiu vertingu turtu. Ji tapo momentine, vienkartine minties išraiška – lyg elektros kibirkštis ar žodinis sakinys.
</p>

<h3>Žaidimų be variklių epocha: „Oasis“, „Google Genie“ ir „Neural GTA 6“</h3>

<p>
  Tačiau pati radikaliausia šios revoliucijos banga ritasi per 200 milijardų dolerių vertės vaizdo žaidimų ir skaitmeninių pasaulių industriją.
</p>

<p>
  Iki šiol kiekvienas žaidimas – nuo „Minecraft“ iki „Grand Theft Auto“ – rėmėsi griežtais trimačiais varikliais („Unreal Engine“, „Unity“). Šimtai programuotojų dešimtmetį rankiniu būdu kodavo fizikos dėsnius: gravitaciją, šviesos atspindžius, susidūrimų geometriją ir personažų dialogus.
</p>

<p>
  2024 m. pabaigoje startuolis „Decart“ kartu su „Etched“ pristatė <strong>„Oasis“</strong> – pirmąjį pasaulyje žaidžiamą **neuroninį žaidimų variklį (Neural Game Engine)**.
</p>

<blockquote class="expert-quote">
  „'Oasis' žaidime nėra nė vienos kodo eilutės apie žaidimo taisykles. Nėra jokio trimačio modelio, jokio fizikos variklio. Tai yra grynasis difuzinis transformerių modelis (DiT), kuris buvo apmokytas stebint milijonus valandų žaidimo vaizdo įrašų. Kai žaidėjas spaudžia klavišus W-A-S-D, modelis kadras po kadro (20 kadrų per sekundę) tiesiog nuspėja, kaip turi atrodyti kiti pikseliai. Modelis 'išmoko' gravitaciją, blokų griovimą ir šviesą vien iš vaizdo stebėjimo.“
  <cite>— Decart AI & Etched tyrimų ataskaita</cite>
</blockquote>

<p>
  Palyginkite tai su tuo, kas laukia artimiausiais metais, pasirodžius tokiems grandams kaip „GTA 6“.
</p>

<div class="warning-box">
  <h4>Kiekvieno žaidėjo asmeninis GTA: Begalinių fantazijų pasauliai</h4>
  <p>
    Tradicinė studija („Rockstar Games“) išleidžia milijardą dolerių ir dešimt metų, kad sukurtų fiksuotą, statišką virtualų Majamį. Tačiau neuroninių pasaulio modelių (tokių kaip „Google Genie 2“ ir realaus laiko vaizdo generatorių) eroje žaidėjas nebebus pasyvus vartotojas.
    <br><br>
    Jau 2027 metais žaidėjas galės ištarti: <em>„Pakeisk šį žaidimą: noriu, kad veiksmas vyktų 2099 m. post-apokaliptiniame Vilniuje su skraidančiais automobiliais, o mano personažo bendrakeleivis turėtų tikrą nepriklausomą intelektą, prisimintų visas mūsų keliones ir kalbėtų mano mėgstamo filmo herojaus balsu“</em>. Ir modelis realiuoju laiku transformuos žaidimą. Žaidimų kūrimas nustoja būti korporacijų privilegija – kiekvienas žmogus tampa dievu savo asmeninėje matricoje.
  </p>
</div>

<p>
  Kai kodas tampa nemokamas, o virtualūs pasauliai generuojami iš vaizduotės – kas lieka tikroji vertė? Vertė persikelia į fizinį pamatą: **į elektrą, silicio lustus ir branduolinius reaktorius**, maitinančius šį sapną. Apie tai – kitame skyriuje.
</p>
