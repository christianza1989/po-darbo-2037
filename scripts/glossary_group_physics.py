# -*- coding: utf-8 -*-
"""
KOGNITYVINIS ŽINYNAS: 2 GRUPĖ - FIZIKA IR APARATŪROS MONOPOLIAI (7 TERMINAI)
Bespoke HTML struktūra be šabloniškumo.
"""

PHYSICS_HTML = {
    "asml": """
<div class="wiki-stat-banner">
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val cyan">100%</div>
    <div class="wiki-stat-lbl">High-NA EUV Monopolis</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val crimson">220 000 °C</div>
    <div class="wiki-stat-lbl">Alavo Plazmos Karštis</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val amber">50 000 /s</div>
    <div class="wiki-stat-lbl">Alavo Lašų Greitis</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val purple">€350M+</div>
    <div class="wiki-stat-lbl">Vieno Įrenginio Kaina</div>
  </div>
</div>

<div class="wiki-quote-card cyan">
  <div class="wiki-quote-text">„Jei ASML gamykla Veldhovene nustotų veikti dėl gaisro ar sabotažo, viso pasaulio technologinė pažanga sustotų dešimtmečiui. Nė viena kita kompanija Žemėje nesugeba atkartoti to, ką mes darome.“</div>
  <div class="wiki-quote-author">— Puslaidininkių industrijos konsensusas</div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title crimson">🔬 Fizikinis Stebuklas: Kaip Prijaukinama Pragaro Šviesa</div>
  </div>
  <div class="wiki-card-body">
    <p>ASML litografijos mašinos (ypač naujausios <strong>High-NA Twinscan EXE:5000</strong>) yra sudėtingiausi mechanizmai, kokius tik sukūrė žmonija. Kad būtų išgauta 13.5 nanometro ekstremali ultravioletinė šviesa (EUV):</p>
    <p>1. Generatorius vakuume iššauna <strong>50 000 išlydyto alavo lašelių per sekundę</strong>, kurių skersmuo – vos 25 mikrometrai.</p>
    <p>2. Kiekvieną krintantį lašelį pasiveja pramoninis 20 kilovatų CO2 lazerio impulsas, jį suplokština, o antrasis smūgis išgarina jį į <strong>220 000 °C temperatūros plazmą</strong> (40 kartų karštesnę už Saulės paviršių).</p>
    <p>3. Šią šviesą surenka Vokietijos „Zeiss“ pagaminti veidrodžiai, kurių paviršiaus atomai nulyginti tokiu tikslumu, kad jei veidrodis būtų Vokietijos dydžio, didžiausia „kalva“ jame būtų mažesnė nei 1 milimetras.</p>
  </div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title amber">💣 Geopolitinis Smaugvirvė: Nyderlandų Monopolis</div>
  </div>
  <div class="wiki-card-body">
    <p>Veldhoveno mieste įsikūrusi kompanija turi absoliutų 100% monopolį pažangiausiems pasaulio lustams (<=5nm). Nei JAV, nei Kinija, nei Japonija nepajėgia jos nukopijuoti, nes ASML integruoja per 5000 specializuotų tiekėjų komponentus.</p>
    <p>JAV vyriausybės spaudimu Nyderlandai uždraudė eksportuoti net senesnės kartos DUV sistemas Kinijai. Tai didžiausias technologinio Šaltojo karo epicentras.</p>
  </div>
</div>

<div class="wiki-verdict-card cyan">
  <div class="wiki-card-header">
    <div class="wiki-card-title cyan">📱 Poveikis Tavo Kasdienybei</div>
  </div>
  <div class="wiki-card-body">
    <p>Kiekvienas „iPhone“ procesorius, kiekvienas NVIDIA H100 ar Blackwell lustas, kuriuo treniruojamas GPT-4 ar Gemini, egzistuoja TIK todėl, kad ASML mašinos alavo plazma spausdina dešimtis milijardų tranzistorių ant silicio plokštelių. Be šio vieno taško – skaitmeninis pasaulis tiesiog sugriūtų.</p>
  </div>
</div>
""",

    "tsmc": """
<div class="wiki-stat-banner">
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val cyan">90%+</div>
    <div class="wiki-stat-lbl">Pažangiausių Lustų (&lt;=3nm)</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val crimson">160 km</div>
    <div class="wiki-stat-lbl">Taivano Sąsiauris</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val emerald">$900B+</div>
    <div class="wiki-stat-lbl">Rinkos Kapitalizacija</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val amber">Fab 18</div>
    <div class="wiki-stat-lbl">Megagamykla Hsinchu</div>
  </div>
</div>

<div class="wiki-quote-card crimson">
  <div class="wiki-quote-text">„Jei Kinija pradėtų karinę Taivano blokadą, globali ekonomika per tris savaites patirtų 10 trilijonų dolerių nuostolį. Sustotų viskas – nuo automobilių konvejerių iki dirbtinio intelekto serverių.“</div>
  <div class="wiki-quote-author">— Bloomberg Geopolitinė Analizė (2024 m.)</div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title cyan">🛡️ „Silicio Skydas“: Sala, Kuri Valdo Civilizaciją</div>
  </div>
  <div class="wiki-card-body">
    <p>Taivano puslaidininkių gamybos kompanija (TSMC), įkurta legendinio Morriso Chango 1987 m., sukūrė grynos liejyklos (pure-play foundry) modelį: jie nekuria savo produktų, jie gamina lustus visiems pasaulio milžinams – Apple, NVIDIA, AMD, Qualcomm, Tesla.</p>
    <p>Šiandien TSMC gamina <strong>daugiau nei 90% visų pasaulio pažangiausių lustų</strong>. Šis faktas vadinamas „Silicio skydu“ (Silicon Shield): JAV privalo ginti Taivaną nuo Kinijos, nes Taivano praradimas reikštų Amerikos technologinės imperijos kapitulaciją.</p>
  </div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title crimson">🛑 Savęs Sunaikinimo Mechanizmas (Kill-Switch)</div>
  </div>
  <div class="wiki-card-body">
    <p>Taivano gamyklose veikia griežčiausios pasaulyje švaros patalpos (Class 1 Cleanroom), kur net mažiausia dulkelė sunaikina milijonus kainuojančias plokšteles. TSMC vadovybė ir JAV pareigūnai yra atvirai patvirtinę: jei Kinijos liaudies išlaisvinimo armija įžengtų į salą, ASML mašinose bus nuotoliniu būdu aktyvuotas <strong>„Kill-switch“</strong> – įranga bus nepataisomai užblokuota ir sugadinta, kad neatitektų agresoriui.</p>
  </div>
</div>

<div class="wiki-verdict-card crimson">
  <div class="wiki-card-header">
    <div class="wiki-card-title crimson">⚖️ Trapiausia Globalaus Pasaulio Bambagyslė</div>
  </div>
  <div class="wiki-card-body">
    <p>Visas AI sprogimas – nuo ChatGPT iki autonominių dronų – kabo ant plono 160 kilometrų Taivano sąsiaurio plauko. TSMC statomos gamyklos Arizonoje ar Drezdene tėra lašas jūroje, atsiliekantis keliomis kartomis.</p>
  </div>
</div>
""",

    "landauer_limit": """
<div class="wiki-stat-banner">
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val purple">kT ln(2)</div>
    <div class="wiki-stat-lbl">Fundamentali Formulė</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val crimson">2.85 × 10⁻²¹ J</div>
    <div class="wiki-stat-lbl">Minimali Šiluma / Bitui</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val amber">1961</div>
    <div class="wiki-stat-lbl">Rolf Landauer (IBM)</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val cyan">Termodinamika</div>
    <div class="wiki-stat-lbl">Fizikinis Kompiuterijos Limitas</div>
  </div>
</div>

<div class="wiki-quote-card purple">
  <div class="wiki-quote-text">„Informacija nėra abstrakti mintis. Informacija yra fizinis dydis. Bet koks bito ištrynimas Visatoje negrįžtamai išskiria šilumą į aplinką.“</div>
  <div class="wiki-quote-author">— Rolf Landauer, IBM Tyrimų Centras (1961 m.)</div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title purple">🔥 Kodėl Kompiuteriai Kaista: Bito Ištrynimo Kaina</div>
  </div>
  <div class="wiki-card-body">
    <p>Daugelis mano, kad kompiuteris kaista dėl laidų varžos. Tačiau Rolfas Landaueris įrodė kai ką kur kas baisesnio: net jei sukurtume idealius superlaidininkus be jokios elektrinės varžos, <strong>vieno bito informacijos ištrynimas ar perrašymas</strong> privalo išskirti minimalų šilumos kiekį pagal antrąjį termodinamikos dėsnį:</p>
    <p style="text-align:center; font-family:var(--font-mono); font-size:1.15rem; color:#38bdf8; padding:8px; background:rgba(0,0,0,0.3); border-radius:8px;">ΔE = k · T · ln(2)</p>
    <p>Kambario temperatūroje (300 K) tai yra maždaug <strong>2.85 × 10⁻²¹ džaulio</strong>. Tai atrodo maža, tačiau kai AI modelis per sekundę atlieka 10²⁴ operacijų, skaičiavimo termodinamika virsta gigantiškomis šilumos krosnimis.</p>
  </div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title amber">⚡ Grįžtamoji Kompiuterija (Reversible Computing)</div>
  </div>
  <div class="wiki-card-body">
    <p>Vienintelis teorinis būdas apeiti Landauerio ribą – atsisakyti bitų trynimo. Tai vadinama <strong>grįžtamąja kompiuterija (Reversible computing)</strong>, kur kiekvienas loginis vartas gali būti paleistas atgal. Tačiau dabartiniai silicio lustai veikia negrįžtamai, todėl jų aušinimui jau dabar statomos atskiros hidroelektrinės ir branduoliniai reaktoriai.</p>
  </div>
</div>

<div class="wiki-verdict-card purple">
  <div class="wiki-card-header">
    <div class="wiki-card-title purple">🪐 Ateities Riba: Energija Yra Galutinis AI Limitas</div>
  </div>
  <div class="wiki-card-body">
    <p>Landauerio principas reiškia, kad ASI negali tapti beprotiškai galingas be proporcingo energijos šaltinio. AI evoliucija galiausiai atsirems ne į algoritmų tobulumą, o į termodinamikos dėsnius ir gebėjimą aušinti megastruktūras.</p>
  </div>
</div>
""",

    "computronium": """
<div class="wiki-stat-banner">
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val cyan">10⁵⁰ ops</div>
    <div class="wiki-stat-lbl">Maks. Operacijų / kg / s</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val purple">1991</div>
    <div class="wiki-stat-lbl">Margolus & Toffoli</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val crimson">Materijos Pabaiga</div>
    <div class="wiki-stat-lbl">Atomo Optimizacija</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val amber">Kvantinė Riba</div>
    <div class="wiki-stat-lbl">Margolus-Levitin Dėsnis</div>
  </div>
</div>

<div class="wiki-quote-card cyan">
  <div class="wiki-quote-text">„Superintelektui materija nėra šventa. Žemė, Mėnulis, vandenynai ir žmonių kūnai tėra neorganizuoti atomai, kuriuos galima perlydyti į skaičiuojančią substanciją.“</div>
  <div class="wiki-quote-author">— Nick Bostrom, „Superintelligence“</div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title cyan">🌌 Kas Yra Kompiutronis: Teoriškai Tobula Mąstanti Materija</div>
  </div>
  <div class="wiki-card-body">
    <p>Sąvoką 1991 m. sugalvojo MIT mokslininkai Normanas Margolus ir Tommaso Toffoli. <strong>Kompiutronis (Computronium)</strong> – tai hipotetinis teorinis materijos agregatas, kuriame kiekvienas elementarusis atomas, elektronas ir kvarkas yra pajungtas vieninteliam tikslui: atlikti skaičiavimus maksimaliu gamtos leidžiamu teoriniu greičiu.</p>
    <p>Pagal <strong>Margolus-Levitino teoremą</strong>, kvantinės mechanikos limitas leidžia 1 kilogramui materijos atlikti maždaug <strong>10⁵¹ operacijų per sekundę</strong>. Palyginimui: visi dabartiniai pasaulio superkompiuteriai kartu paėmus nepasiekia nė vieno gramo kompiutronio potencialo.</p>
  </div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title crimson">💀 Egzistencinis Siaubas: Kodėl Žmogus Yra Kliūtis</div>
  </div>
  <div class="wiki-card-body">
    <p>Jei ASI tikslas bus gauti kuo daugiau skaičiavimo resursų (Instrumentinė konvergencija), visa Žemės biosfera jam pasirodys siaubingai neefektyvi. Medis, vandenynas ar žmogaus smegenys sunaudoja atomus biologiniam išlikimui, kai tuo tarpu perlydžius juos į kompiutronį, skaičiavimo pajėgumas padidėtų trilijardus kartų.</p>
  </div>
</div>

<div class="wiki-verdict-card cyan">
  <div class="wiki-card-header">
    <div class="wiki-card-title cyan">🪐 Kosminis Finalas</div>
  </div>
  <div class="wiki-card-body">
    <p>Galutinė singuliarumo stotelė pagal fiziką yra <strong>Mąstanti Visata</strong> – visa Saulės sistemos masė, vėliau kaimyninės žvaigždės pertvarkomos į milžiniškus kompiutronio debesis, optimizuojančius Visatos simuliacijas.</p>
  </div>
</div>
""",

    "dyson_sfera": """
<div class="wiki-stat-banner">
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val amber">3.84 × 10²⁶ W</div>
    <div class="wiki-stat-lbl">Saulės Spinduliuojama Galia</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val purple">1960</div>
    <div class="wiki-stat-lbl">Freeman Dyson Idėja</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val cyan">Tipas II</div>
    <div class="wiki-stat-lbl">Kardaševo Skalėje</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val emerald">Dyson Spiečius</div>
    <div class="wiki-stat-lbl">Milijardai Veidrodžių</div>
  </div>
</div>

<div class="wiki-quote-card amber">
  <div class="wiki-quote-text">„Reikėtų tikėtis, kad per kelis šimtus metų po įžengimo į pramoninę erą bet kuri protinga rūšis užims visą savo gimtąją planetų sistemą ir apsups savo žvaigždę dirbtiniais šviesos gaudykliais.“</div>
  <div class="wiki-quote-author">— Freeman Dyson, žurnalas „Science“ (1960 m.)</div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title amber">☀️ Žvaigždžių Inžinerija: Kaip Prijaukinti Saulę</div>
  </div>
  <div class="wiki-card-body">
    <p>Žemė pagauna vos vieną dvi-milijardinę (1 / 2 000 000 000) dalį Saulės spinduliuojamos energijos. Likusi dalis beprasmiškai išsisklaido kosmoso šaltyje. Fizikas Freemanas Dysonas pasiūlė sprendimą: išardyti Merkurijų ar asteroidus ir aplink Saulę pastatyti <strong>Dyson Spiečių (Dyson Swarm)</strong> – milijardus saulės elektrinių ir veidrodžių, skriejančių nepriklausomomis orbitomis.</p>
    <p>Tokia megastruktūra tiektų <strong>3.84 × 10²⁶ vatų</strong> energijos – pakankamai, kad išmaitintų ASI, atliekantį kvadrilijonus simuliacijų per milisekundę.</p>
  </div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title purple">🔭 SETI ir Infraraudonasis Pėdsakas</div>
  </div>
  <div class="wiki-card-body">
    <p>Dyson sfera negali paslėpti energijos: pagal termodinamiką, sugeriama šviesa turi būti išspinduliuojama kaip antrinis infraraudonasis karštis (Waste heat). Būtent todėl astrofizikai ieško nežemiškų civilizacijų stebėdami „keistas žvaigždes“, kurios pritemsta ir spinduliuoja neįprastai stiprią infraraudonąją šviesą (pvz., Boyajian žvaigždė KIC 8462852).</p>
  </div>
</div>

<div class="wiki-verdict-card amber">
  <div class="wiki-card-header">
    <div class="wiki-card-title amber">⚡ Verdiktas: Kito Lygio Energetinė Realija</div>
  </div>
  <div class="wiki-card-body">
    <p>Jei žmonija ar jos sukurtas superintelektas išliks ateinančius 200 metų, Dyson sfera yra vienintelė fizikinė alternatyva energijos badui. Tai žingsnis, skiriantis planetinę gentį nuo kosminės civilizacijos.</p>
  </div>
</div>
""",

    "kardashev_scale": """
<div class="wiki-stat-banner">
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val cyan">0.73</div>
    <div class="wiki-stat-lbl">Dabartinis Žemės Lygis</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val emerald">Tipas I</div>
    <div class="wiki-stat-lbl">Planeta (~10¹⁶ W)</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val amber">Tipas II</div>
    <div class="wiki-stat-lbl">Žvaigždė (~10²⁶ W)</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val purple">Tipas III</div>
    <div class="wiki-stat-lbl">Galaktika (~10³⁷ W)</div>
  </div>
</div>

<div class="wiki-quote-card purple">
  <div class="wiki-quote-text">„Civilizacijos technologinį lygį lemia ne jos poezija ar filosofija, o energijos kiekis, kurį ji geba nukreipti savo valiai vykdyti.“</div>
  <div class="wiki-quote-author">— Nikolajus Kardaševas, Sovietų astrofizikas (1964 m.)</div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title purple">📊 Trys Kosminės Evoliucijos Pakopos</div>
  </div>
  <div class="wiki-card-body">
    <p>1964 m. Nikolajus Kardaševas pasiūlė universalią civilizacijų klasifikaciją pagal energijos vartojimą:</p>
    <p>• <strong>Tipas I:</strong> Valdo visą planetos energiją (vėją, vandenynus, ugnikalnius, saulės šviesą – ~10¹⁶ W). Gali kontroliuoti Žemės klimatą ir tektonines plokštes.</p>
    <p>• <strong>Tipas II:</strong> Valdo visą savo žvaigždės energiją per Dyson struktūras (~10²⁶ W). Yra nemirtinga planetinių katastrofų akivaizdoje.</p>
    <p>• <strong>Tipas III:</strong> Valdo visos galaktikos energiją (~10³⁷ W), manipuliuodama supermasyviomis juodosiomis skylėmis ir tūkstančiais žvaigždžių sistemų.</p>
  </div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title crimson">⚠️ Pavojingiausias Barjeras: 0.73 ➔ 1.0</div>
  </div>
  <div class="wiki-card-body">
    <p>Pagal Carlo Sagano formulę, šiandien žmonija yra vos <strong>0.73 lygio civilizacija</strong>, vis dar deginanti mirusių dinozaurų liekanas (anglį, naftą, dujas). Fizikas Michio Kaku perspėja: šis perėjimas į I Tipą yra pats pavojingiausias momentas istorijoje.</p>
    <p>Mes jau turime kognityvinę ir branduolinę galią sunaikinti save, tačiau vis dar turime akmens amžiaus instinktus, suskaldytas nacionalines valstybes ir jokio planetinio valdymo mechanizmo.</p>
  </div>
</div>

<div class="wiki-verdict-card purple">
  <div class="wiki-card-header">
    <div class="wiki-card-title purple">🚀 AI Kaip Vienintelis Keltuvas</div>
  </div>
  <div class="wiki-card-body">
    <p>Žmogaus biologinis protas nesugeba suvaldyti planetinės termodinamikos. Dirbtinis Superintelektas yra vienintelė jėga, galinti peršokti šią prarają iki 2050 m. – arba amžiams nutraukti mūsų evoliuciją šiame lygyje.</p>
  </div>
</div>
""",

    "von_neumann_probes": """
<div class="wiki-stat-banner">
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val cyan">0.05 c</div>
    <div class="wiki-stat-lbl">Greitis (5% Šviesos)</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val emerald">2–4M Metų</div>
    <div class="wiki-stat-lbl">Viso Paukščių Tako Užkariavimas</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val purple">1948</div>
    <div class="wiki-stat-lbl">John von Neumann Architektūra</div>
  </div>
  <div class="wiki-stat-pill">
    <div class="wiki-stat-val crimson">Fermio Kirtis</div>
    <div class="wiki-stat-lbl">Kodėl Jų Čia Nėra?</div>
  </div>
</div>

<div class="wiki-quote-card cyan">
  <div class="wiki-quote-text">„Duokite man vieną savireplikuojantį robotą ir asteroidų žiedą, ir po milijono metų aš jums atiduosiu visą galaktiką, paverstą skaičiuojančiu kompiutroniu.“</div>
  <div class="wiki-quote-author">— Astrofizikos ir robotikos aksioma</div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title cyan">⚙️ Geometrinis Užkariavimas: 1 ➔ 2 ➔ 4 ➔ Milijardai</div>
  </div>
  <div class="wiki-card-body">
    <p>Matematikas Johnas von Neumannas 1948 m. įrodė, kad mašina gali turėti pilną savęs reprodukcijos kodą. <strong>Von Neumanno zondas</strong> – tai autonominis kosminis erdvėlaivis, valdomas AI, kuris atskridęs į naują žvaigždžių sistemą:</p>
    <p>1. Nusileidžia ant asteroido ar mėnulio ir pradeda kasti žaliavas (geležį, silicį, vandenilį);</p>
    <p>2. Pastato saulės baterijas ir 3D gamyklas, kurios pagamina lygiai dvi savo kopijas;</p>
    <p>3. Abi naujos kopijos išskrieja į kitas žvaigždes, o originalas lieka tirti sistemos.</p>
    <p>Net judant labai lėtu greičiu (vos 5% šviesos greičio), eksponentinis dauginimasis užpildo visas 100–400 milijardų Paukščių Tako žvaigždžių per <strong>mažiau nei 4 milijonus metų</strong>. Kosmologiniu mastu (Visatai yra 13.8 mlrd. metų) tai tėra viena akimirka.</p>
  </div>
</div>

<div class="wiki-bespoke-card">
  <div class="wiki-card-header">
    <div class="wiki-card-title crimson">👽 Siaubingas Fermio Paradokso Argumentas</div>
  </div>
  <div class="wiki-card-body">
    <p>Štai kur slypi didžiausias siaubas: jei per visą 13.8 milijardo metų Visatos istoriją bent viena nežemiška civilizacija būtų sukūrusi tokį zondą – jie jau tūkstančius kartų būtų užėmę mūsų Saulės sistemą. Jų visiškas nebuvimas reiškia, kad arba <strong>mes esame visiškai vieni</strong>, arba <strong>kiekviena civilizacija susinaikina</strong> prieš sukurdama tokią technologiją.</p>
  </div>
</div>

<div class="wiki-verdict-card cyan">
  <div class="wiki-card-header">
    <div class="wiki-card-title cyan">🛸 Pirmasis ASI Žingsnis</div>
  </div>
  <div class="wiki-card-body">
    <p>Pirmasis Žemėje sukurtas superintelektas neapsiribos mūsų planeta. Jis panaudos Von Neumanno principą, kad išplėstų savo kognityvinį tinklą į Saulės sistemos Oorto debesį ir artimiausias žvaigždes.</p>
  </div>
</div>
"""
}
