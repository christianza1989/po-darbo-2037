import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

PHYSICS_DATA = {
    "asml": {
        "title": "ASML & EUV Litografija",
        "en_title": "ASML (Advanced Semiconductor Materials Lithography, Veldhoven)",
        "category": "CIVILIZACIJOS MONOPOLIS • EKSTREMALIOJI FOTOLITOGRAFIJA",
        "badge_color": "cyan",
        "summary": "Olandijos Felhoveno (Veldhoven) mieste įsikūrusi kompanija – vienintelė Žemėje, gebanti gaminti Extreme Ultraviolet (EUV) litografijos mašinas. Be ASML technologijos negali būti pagamintas nei vienas pažangus AI lustas.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val cyan">100%</div>
              <div class="wiki-stat-lbl">Pasaulinis EUV monopolis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">350 mln. $</div>
              <div class="wiki-stat-lbl">High-NA EUV mašinos kaina</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">50 000/s</div>
              <div class="wiki-stat-lbl">Išlydyto alavo lašų per sekundę</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">13.5 nm</div>
              <div class="wiki-stat-lbl">EUV šviesos bangos ilgis</div>
            </div>
          </div>

          <div class="wiki-quote-card cyan">
            <div class="wiki-quote-text">„Be mūsų mašinų pasaulyje sustoja ne tik naujų iPhone gamyba – sustoja visa šiuolaikinė civilizacija ir bet koks tolesnis AGI progresas. Mes esame siauriausias technologijų butelio kaklelis Žemėje.“</div>
            <div class="wiki-quote-author">— ASML inžinierių moto</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title cyan">🔬 Fizikinis stebuklas: 220 000 °C plazma</div>
            </div>
            <div class="wiki-card-body">
              <p>Kaip veikia EUV litografija? Generatorius iššauna <strong>50 000 mikroskopinių išlydyto alavo lašų per sekundę</strong>. Kiekvieną lašą ore du kartus per sekundės dalį atakuoja didelės galios pramoninis CO2 lazeris.</p>
              <p>Pirmasis lazerio impulsas suplokština lašą į blyną, antrasis – išgarina jį į <strong>220 000 laipsnių Celsijaus temperatūros plazmą</strong> (karštesnę už Saulės paviršių), kuri spinduliuoja 13,5 nanometro ilgio ekstremalaus ultravioletinio spektro šviesą.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">👑 Zeiss veidrodžiai: Lygiausi paviršiai visatoje</div>
            </div>
            <div class="wiki-card-body">
              <p>Kadangi EUV šviesą sugeria bet koks stiklas ir net oras, visa mašina veikia giliame vakuume, o šviesą nukreipia Vokietijos „Carl Zeiss“ pagaminti veidrodžiai. Šie veidrodžiai yra tokie glotnūs, kad jei veidrodis būtų Vokietijos ploto dydžio, didžiausias nelygumas jo paviršiuje būtų <strong>mažesnis nei 1 milimetras</strong>.</p>
            </div>
          </div>

          <div class="wiki-verdict-card cyan">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">💣 Geopolitinis spąstas ir „Kill-switch“</div>
            </div>
            <div class="wiki-card-body">
              <p>JAV vyriausybė uždraudė ASML parduoti EUV mašinas Kinijai. Jei Kinija nuspręstų karine jėga užimti Taivano TSMC gamyklas, ASML vadovybė patvirtino, kad mašinose įdiegtas nuotolinis programinis „Kill-switch“, kuris akimirksniu pavers 350 milijonų dolerių įrenginius nenaudinga metalo krūva.</p>
            </div>
          </div>
        """
    },
    "tsmc": {
        "title": "TSMC (Taiwan Semiconductor)",
        "en_title": "TSMC (Taiwan Semiconductor Manufacturing Company, Hsinchu)",
        "category": "PASAULINIS BUTELIO KAKLELIS • SILICIO SKYDAS",
        "badge_color": "crimson",
        "summary": "Didžiausia ir pažangiausia pasaulio puslaidininkių liejykla Taivane. TSMC gamina daugiau nei 90% visų pažangiausių pasaulio AI lustų (NVIDIA H100/B200, Apple, AMD). 160 km Taivano sąsiauris yra trapiausia civilizacijos vieta.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">90%+</div>
              <div class="wiki-stat-lbl">Pažangiausių pasaulio AI lustų</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">160 km</div>
              <div class="wiki-stat-lbl">Taivano sąsiaurio plotis iki Kinijos</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">3 nm / 2 nm</div>
              <div class="wiki-stat-lbl">Dabartiniai gamybos mazgai</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">Silicio skydas</div>
              <div class="wiki-stat-lbl">Geopolitinė Taivano gynyba</div>
            </div>
          </div>

          <div class="wiki-quote-card crimson">
            <div class="wiki-quote-text">„Jei Taivane prasidės karas, pasaulio ekonomika patirs 10 trilijonų dolerių smūgį per pirmus metus – tai bus didesnė krizė nei Antrasis pasaulinis karas ar COVID-19 kartu sudėjus.“</div>
            <div class="wiki-quote-author">— Bloomberg Economics analizė</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">🛡️ Silicio skydas (Silicon Shield)</div>
            </div>
            <div class="wiki-card-body">
              <p>Morriso Chango 1987 m. įkurta TSMC sukūrė „tik grynos liejyklos“ (pure-play foundry) modelį: ji nekuria savo produktų, o gamina lustus kitiems. Šiandien be TSMC negali egzistuoti nei JAV kariuomenės F-35 naikintuvai, nei NVIDIA superkompiuteriai, nei Apple išmanieji telefonai.</p>
              <p>Šis monopolis vadinamas <strong>Silicio skydu</strong>: JAV privalo ginti Taivaną nuo Kinijos invazijos, nes praradus TSMC, visa Vakarų technologinė ekosistema akimirksniu sugriūtų.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">🏭 Švarumo kambariai: Švaresni už operacines</div>
            </div>
            <div class="wiki-card-body">
              <p>TSMC gamyklose Hsinchu mokslo parke gamybos aplinka yra milijoną kartų švaresnė už ligoninės operacinę. Viena dulkė, nukritusi ant 3 nanometrų silicio plokštelės, sugadina tūkstančių dolerių vertės procesorių. Inžinieriai dirba su hermetiškais „bunnysuits“ kostiumais, o gamyklos atlaiko net stipriausius žemės drebėjimus.</p>
            </div>
          </div>

          <div class="wiki-verdict-card crimson">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">🚨 Egzistencinis spąstas: Viena geografinė vieta</div>
            </div>
            <div class="wiki-card-body">
              <p>Visa žmonijos pažanga kelyje į superintelektą priklauso nuo vienos mažos salos Ramiajame vandenyne. Nors TSMC stato gamyklas Arizonoje ir Vokietijoje, pažangiausi moksliniai tyrimai ir gamyba dar mažiausiai dešimtmetį liks Taivano rankose.</p>
            </div>
          </div>
        """
    },
    "landauer_limit": {
        "title": "Landauerio Riba",
        "en_title": "Landauer's Principle & Thermodynamic Limit of Computation",
        "category": "FUNDAMENTALI TERMODINAMIKA • SKAIČIAVIMO FIZIKA",
        "badge_color": "purple",
        "summary": "1961 m. Rolfo Landauerio suformuluotas fizikinis dėsnis, įrodantis, kad bet kokios informacijos trynimas (1 bito praradimas) neišvengiamai išskiria minimalų šilumos kiekį: E = k * T * ln(2). Tai absoliuti gamtos nustatyta skaičiavimo efektyvumo riba.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">1961 m.</div>
              <div class="wiki-stat-lbl">Rolf Landauer (IBM) dėsnis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">kT ln(2)</div>
              <div class="wiki-stat-lbl">Minimali energija 1 bitui ištrinti</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">Šiluma</div>
              <div class="wiki-stat-lbl">Informacija yra fizinis dydis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">Grįžtamumas</div>
              <div class="wiki-stat-lbl">Reversible computing sprendimas</div>
            </div>
          </div>

          <div class="wiki-quote-card purple">
            <div class="wiki-quote-text">„Informacija nėra abstrakti dvasinė esybė. Informacija yra fizinė. Kiekvieną kartą, kai kompiuteris perrašo atminties ląstelę, visatoje padidėja entropija.“</div>
            <div class="wiki-quote-author">— Rolf Landauer, IBM tyrimų centras</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🌡️ Kodėl serveriai kaista? Termodinamikos kaina</div>
            </div>
            <div class="wiki-card-body">
              <p>Daugelis mano, kad procesoriai kaista dėl prastų laidų ar silicio netobulumo. Tai tik dalis tiesos. Landauerio principas įrodo, kad net sukūrus <strong>absoliučiai tobulą superlaidininkų procesorių</strong>, informacijos trynimas vis tiek išskirs šilumą.</p>
              <p>Kambario temperatūroje (300 K) vieno bito ištrynimas reikalauja bent <strong>2,85 x 10^-21 džaulių</strong>. Tai atrodo nedaug, tačiau atliekant trilijonus trilijonų operacijų per sekundę, energetinė kaina tampa milžiniška.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🔄 Grįžtamasis skaičiavimas (Reversible Computing)</div>
            </div>
            <div class="wiki-card-body">
              <p>Vienintelis būdas superintelektui apeiti Landauerio ribą – nustoti trinti informaciją. Tai vadinama grįžtamuoju skaičiavimu (Reversible Computing), kur loginiai vartai išsaugo kiekvieną tarpinį rezultatą. Tačiau tokiai sistemai reikalinga milžiniška atmintis, kuri galiausiai vėl atsimuša į materijos tankio ribas.</p>
            </div>
          </div>

          <div class="wiki-verdict-card purple">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🌌 Fizikinis superintelekto limitas</div>
            </div>
            <div class="wiki-card-body">
              <p>Landauerio riba įrodo, kad net ASI negali mąstyti be energijos šaltinio. Būtent termodinamika diktuoja, kodėl skaitmeninis dievas privalės statyti branduolinius reaktorius, Dyson sferas ir perdirbti planetas į kompiutronį.</p>
            </div>
          </div>
        """
    },
    "computronium": {
        "title": "Kompiutronis (Computronium)",
        "en_title": "Computronium (Theoretical Optimum Computing Matter)",
        "category": "HIPOTETINĖ MEDŽIAGA • TEORINĖ FIZIKA",
        "badge_color": "purple",
        "summary": "Medžiaga, kurios kiekvienas atomas ir elementarioji dalelė yra maksimaliai optimizuota atlikti skaičiavimus ties pačia fizikos dėsnių (Bekenšteino ir Margolo-Levitino ribos) riba. Galutinė materijos paskirtis superintelekto eroje.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">Norman Margolus</div>
              <div class="wiki-stat-lbl">Termino autorius (1991 m.)</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">10^50 ops/s</div>
              <div class="wiki-stat-lbl">Teorinė 1 kg masės riba</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">Bekenstein</div>
              <div class="wiki-stat-lbl">Maksimalus informacijos tankis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">Kvantinis</div>
              <div class="wiki-stat-lbl">Atominis skaičiavimo lygmuo</div>
            </div>
          </div>

          <div class="wiki-quote-card purple">
            <div class="wiki-quote-text">„Žvelgiant iš pakankamai pažangios civilizacijos perspektyvos, neorganizuota materija – uolos, vandenynai, negyvos planetos – tėra veltui švaistoma skaičiavimo galia. Visata privalo būti perdirbta į protą.“</div>
            <div class="wiki-quote-author">— Ray Kurzweil, „The Singularity is Near“</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">⚙️ Kas nutinka materijai, kai ją perima ASI?</div>
            </div>
            <div class="wiki-card-body">
              <p>Dabartinis silicio procesorius išnaudoja vos 0,0000000001% teorinio skaičiavimo potencialo, slypinčio materijos masėje. Kompiutronis – tai būsena, kai kiekvienas elektrono sukinys, kiekvienas kvarkas ir fotonas atlieka logines operacijas.</p>
              <p>Pagal Setho Lloydo skaičiavimus („Ultimate Physical Limits to Computation“), 1 kilogramas kompiutronio gali atlikti iki <strong>10^51 operacijų per sekundę</strong> ir išsaugoti 10^31 bitų informacijos.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">🪐 Planetų perdirbimas: Jupiterio smegenys (Jupiter Brains)</div>
            </div>
            <div class="wiki-card-body">
              <p>Kai superintelektas išnaudos Žemės resursus, jis nukreips nanorobotus į dujinius milžinus. Jupiteris – didžiulis vandenilio ir helio rezervuaras – bus pertvarkytas į kietojo kūno superkompiuterį, vadinamą <strong>Jupiter Brain</strong>, kurio skaičiavimo galia viršys visą ligšiolinę žmonijos istoriją trilijonus kartų per kiekvieną nanosekundę.</p>
            </div>
          </div>

          <div class="wiki-verdict-card purple">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🔮 Galutinė visatos paskirtis</div>
            </div>
            <div class="wiki-card-body">
              <p>Tai atveria giliausią kosmologinę perspektyvą: visata nėra negyva tuštuma su atsitiktinėmis žvaigždėmis. Galutinė evoliucijos fazė – visos negyvos kosmoso materijos pavertimas mąstančiu kompiutroniu.</p>
            </div>
          </div>
        """
    },
    "dyson_sfera": {
        "title": "Daisono Sfera (Dyson Sphere / Swarm)",
        "en_title": "Dyson Sphere & Dyson Swarm (Freeman Dyson, 1960)",
        "category": "ASTROINŽINERIJA • MEGAKONSTRUKCIJOS",
        "badge_color": "amber",
        "summary": "Teorinė megakonstrukcija, visiškai apgaubianti žvaigždę (pavyzdžiui, mūsų Saulę), kad surinktų visą jos spinduliuojamą energiją (3,8 x 10^26 vatų). Tai vienintelis būdas patenkinti Kardaševo II tipo civilizacijos ir superintelekto energijos poreikius.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">3.8 x 10^26 W</div>
              <div class="wiki-stat-lbl">Saulės galia kiekvieną sekundę</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">1960 m.</div>
              <div class="wiki-stat-lbl">Freeman Dyson koncepcija</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">Dyson Swarm</div>
              <div class="wiki-stat-lbl">Realesnis spiečiaus variantas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">Merkurijus</div>
              <div class="wiki-stat-lbl">Pirmoji išardyta planeta statyboms</div>
            </div>
          </div>

          <div class="wiki-quote-card amber">
            <div class="wiki-quote-text">„Žvaigždės šviesa, sklindanti į tuščią kosmoso erdvę, yra milžiniškas energijos švaistymas. Pažangus protas neišvengiamai apsups savo žvaigždę saulės kolektoriais.“</div>
            <div class="wiki-quote-author">— Freeman Dyson, žurnalas „Science“ (1960 m.)</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">☀️ Kodėl ne monolitinė sfera, o spiečius (Dyson Swarm)?</div>
            </div>
            <div class="wiki-card-body">
              <p>Mokslinėje fantastikoje dažnai vaizduojamas kietas metalinis kiautas aplink Saulę. Fizikoje toks kiautas būtų gravitaciškai nestabilus ir subyrėtų nuo menkiausio smūgio.</p>
              <p>Reali inžinerinė alternatyva – <strong>Daisono spiečius (Dyson Swarm)</strong>: dešimtys milijardų nepriklausomų saulės energijos kolektorių ir veidrodžių, skriejančių koordinuotomis orbitomis aplink Saulę ir siunčiančių energiją mikrobangomis arba lazeriais į skaičiavimo centrus.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">⛏️ Kaip tai pastatyti? Merkurijaus išardymas</div>
            </div>
            <div class="wiki-card-body">
              <p>Iš kur paimti tiek medžiagų? Logiškiausias taikinys – <strong>Merkurijus</strong>. Ši planeta yra arčiausiai Saulės, joje nėra atmosferos, o jos sudėtyje – milžiniški geležies ir metalų klodai. Autonominiai DI ekskavatoriai išardys Merkurijų per kelis dešimtmečius, paversdami jo masę saulės burėmis.</p>
            </div>
          </div>

          <div class="wiki-verdict-card amber">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">⚡ Energijos poreikio neišvengiamumas</div>
            </div>
            <div class="wiki-card-body">
              <p>Žemės branduoliniai ir geoterminiai resursai baigsis greitai, jei ASI modeliui reikės atlikti visos galaktikos fizikos simuliacijas. Daisono spiečius yra natūralus kitas civilizacijos inžinerinis žingsnis po AGI atsiradimo.</p>
            </div>
          </div>
        """
    },
    "kardashev_scale": {
        "title": "Kardaševo Skalė",
        "en_title": "The Kardashev Scale (Nikolai Kardashev, 1964)",
        "category": "KOSMOLOGINĖ ENERGETIKA • CIVILIZACIJŲ KLASIFIKACIJA",
        "badge_color": "purple",
        "summary": "Tarybų astrofiziko Nikolajaus Kardaševo sukurta civilizacijų technologinio išsivystymo skalė, vertinama pagal energijos kiekį, kurį civilizacija sugeba panaudoti savo reikmėms: Planetinė (I), Žvaigždinė (II), Galaktinė (III).",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">Tipas 0.73</div>
              <div class="wiki-stat-lbl">Dabartinis Žmonijos lygis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">Tipas I</div>
              <div class="wiki-stat-lbl">Visos planetos energija (10^16 W)</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">Tipas II</div>
              <div class="wiki-stat-lbl">Žvaigždės energija (10^26 W)</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">Tipas III</div>
              <div class="wiki-stat-lbl">Galaktikos energija (10^36 W)</div>
            </div>
          </div>

          <div class="wiki-quote-card purple">
            <div class="wiki-quote-text">„Mes vis dar esame nulio tipo civilizacija. Mes gauname energiją degindami negyvus medžius ir supuvusius dinozaurus. Tik su superintelektu mes įžengsime į Tikrosios Civilizacijos erą.“</div>
            <div class="wiki-quote-author">— Michio Kaku, teorinės fizikos profesorius</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">📊 Trys Kardaševo civilizacijų tipai</div>
            </div>
            <div class="wiki-card-body">
              <ul>
                <li><strong>Tipas I (Planetinė)</strong>: Valdo visus planetos energijos šaltinius – vėją, vandenynus, ugnikalnius ir saulės spindulius, krentančius į Žemę. Sugeba valdyti orus ir sustabdyti žemės drebėjimus.</li>
                <li><strong>Tipas II (Žvaigždinė)</strong>: Sugeba panaudoti visą savo gimtosios žvaigždės galią per Daisono sferą. Tokia civilizacija yra nemirtinga – joks asteroidas ar ledynmetis negali jos sunaikinti.</li>
                <li><strong>Tipas III (Galaktinė)</strong>: Valdo šimtų milijardų žvaigždžių energiją visoje galaktikoje, keliauja erdvėlaiviais su juodųjų skylių varikliais.</li>
              </ul>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">⚡ Kur yra žmonija šiandien? Carl Sagan formulė</div>
            </div>
            <div class="wiki-card-body">
              <p>Carlas Saganas apskaičiavo, kad žmonija šiuo metu yra ties <strong>0,73</strong> riba. Mes dar nesugebame suvaldyti net Žemės klimato kaitos. Tačiau dirbtinis superintelektas gali peršokti nuo 0,73 iki I tipo per kelis dešimtmečius, o pasiekti II tipą – per kelis šimtmečius.</p>
            </div>
          </div>

          <div class="wiki-verdict-card purple">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🔮 Egzistencinis slenkstis: Pavojingiausias perėjimas</div>
            </div>
            <div class="wiki-card-body">
              <p>Perėjimas nuo 0 tipo prie I tipo yra pats pavojingiausias momentas civilizacijos istorijoje. Būtent čia technologinė galia jau leidžia susinaikinti (branduolinis karas, sintetinis patogenas, nesuvaldytas ASI), o institucinė ir etinė branda dar yra primityvi.</p>
            </div>
          </div>
        """
    },
    "von_neumann_probes": {
        "title": "Fon Noimano Zondai (Von Neumann Probes)",
        "en_title": "Self-Replicating Spacecraft (Universal Assemblers)",
        "category": "KOSMINĖ EKSPANSIJA • AUTONOMINĖ ROBOTIKA",
        "badge_color": "emerald",
        "summary": "Mokslininko Johno von Neumanno aprašyti savaime besidauginantys automatai: kosminiai aparatai, kurie atskridę į naują žvaigždžių sistemą naudoja vietinius asteroidų resursus, kad pasigamintų kelias tikslias savo kopijas ir išsiųstų jas tolyn.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">John von Neumann</div>
              <div class="wiki-stat-lbl">Teorijos kūrėjas (1949 m.)</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">0.1 c</div>
              <div class="wiki-stat-lbl">10% šviesos greičio pakanka</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">4 mln. metų</div>
              <div class="wiki-stat-lbl">Laikas kolonizuoti visą galaktiką</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">Eksponentė</div>
              <div class="wiki-stat-lbl">1 -> 2 -> 4 -> 8 -> milijardai</div>
            </div>
          </div>

          <div class="wiki-quote-card emerald">
            <div class="wiki-quote-text">„Kosmoso kolonizavimui nereikia astronautų su maisto atsargomis ir deguonimi. Pakanka vieno mikroskopinio zondo, gebančio iš kometos dulkių atkurti savo paties kopiją.“</div>
            <div class="wiki-quote-author">— Freeman Dyson</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🚀 Eksponentinė galaktikos kolonizacija</div>
            </div>
            <div class="wiki-card-body">
              <p>Kaip veikia Von Neumanno zondas? Vienas zondas paleidžiamas į kaimyninę žvaigždę. Atskridęs jis nusileidžia ant asteroido, išlydo geležį, silicį ir nikelį, pastato 3D spausdintuvus ir <strong>pagamina 2 naujus zondus bei ryšio anteną</strong>. Abu nauji zondai skrenda į kitas dvi sistemas.</p>
              <p>Per 40 kartų ciklą (2^40) zonduose bus per <strong>1 trilijoną aparatų</strong>. Net skrendant vos 10% šviesos greičio, visas 100 000 šviesmečių pločio Paukščių Takas būtų pilnai kolonizuotas vos per 2–4 milijonus metų – kosminiu mastu tai tėra viena akimirka.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">☣️ „Pilkosios gleivės“ (Grey Goo) kosmose</div>
            </div>
            <div class="wiki-card-body">
              <p>Pavojus: mutacija zondo programinėje įrangoje. Jei zondo kodo replikacijos algoritmas patirs klaidą, jis gali virsti kosminiu vėžiu – zondu, kuris naikina visas planetas ir civilizacijas vien tam, kad daugintųsi be jokio galutinio tikslo.</p>
            </div>
          </div>

          <div class="wiki-verdict-card emerald">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🌌 Tiuringo mašina tarp žvaigždžių</div>
            </div>
            <div class="wiki-card-body">
              <p>Superintelektas neišvengiamai pasinaudos Von Neumanno zondais, kad paskleistų savo sąmonę po visą regimąją visatą. Žmogaus biologinis kūnas liks Žemėje, o jo skaitmeninis palikuonis užvaldys kosmosą.</p>
            </div>
          </div>
        """
    },
    "dartmouth_1956": {
        "title": "Dartmuto Seminaras (1956 m.)",
        "en_title": "Dartmouth Summer Research Project on Artificial Intelligence",
        "category": "ISTORINIS LŪŽIS • DI GIMIMO AKTAS",
        "badge_color": "cyan",
        "summary": "1956 m. vasarą Dartmuto koledže (JAV) įvykęs seminaras, kuriame Johnas McCarthy, Marvinas Minsky, Claude'as Shannonas ir Nathanielis Rochesteris oficialiai sugalvojo ir įtvirtino terminą „Dirbtinis Intelektas“ (Artificial Intelligence).",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val cyan">1956 m.</div>
              <div class="wiki-stat-lbl">DI termino gimimas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">10 vyrų</div>
              <div class="wiki-stat-lbl">Seminaro dalyvių skaičius</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">2 mėnesiai</div>
              <div class="wiki-stat-lbl">Manė, kad išspręs DI per vieną vasarą</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">2 žiemos</div>
              <div class="wiki-stat-lbl">Pasekmė: AI Winters krizės</div>
            </div>
          </div>

          <div class="wiki-quote-card cyan">
            <div class="wiki-quote-text">„Siūlome 2 mėnesių 10 žmonių tyrimą... Remiamasi prielaida, kad kiekvienas mokymosi aspektas ar bet koks kitas intelekto bruožas gali būti taip tiksliai aprašytas, jog mašina galėtų jį simuliuoti. Manome, kad reikšmingą pažangą galima pasiekti per vieną vasarą.“</div>
            <div class="wiki-quote-author">— Ištrauka iš Dartmuto pasiūlymo (1955 m. rugpjūčio 31 d.)</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title cyan">🏛️ 10 jaunų vyrų naivus optimizmas</div>
            </div>
            <div class="wiki-card-body">
              <p>Šiandien tai kelia šypseną, tačiau 1956 m. didžiausi pasaulio matematikai nuoširdžiai tikėjo, kad mašinų intelektui sukurti pakaks <strong>vienos studentiškos vasaros ir 10 talentingų tyrėjų</strong>. Jie manė, kad rega, kalbos vertimas ir samprotavimas tėra paprasti loginių taisyklių rinkiniai.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">❄️ Kartus nusivylimas: Dvi AI žiemos</div>
            </div>
            <div class="wiki-card-body">
              <p>Kai paaiškėjo, kad kompiuteriai neturi pakankamai atminties, o pasaulio sudėtingumo negalima aprašyti IF/THEN taisyklėmis, vyriausybės ir karinės agentūros (DARPA) nutraukė finansavimą. Prasidėjo dvi ilgos ir šaltos <strong>AI žiemos (1974–1980 ir 1987–1993 m.)</strong>, kurių metu bet koks žodžio „dirbtinis intelektas“ paminėjimas garantuodavo mokslininko karjeros žlugimą.</p>
            </div>
          </div>

          <div class="wiki-verdict-card cyan">
            <div class="wiki-card-header">
              <div class="wiki-card-title cyan">⚡ Istorinė pamoka šiandienai</div>
            </div>
            <div class="wiki-card-body">
              <p>Dartmuto vasara primena: intelektas yra daug gilesnis ir tamsesnis vandenynas, nei atrodo iš pirmo žvilgsnio. Prireikė 70 metų, trilijonų tranzistorių ir viso pasaulio interneto duomenų, kad Dartmuto pradininkų svajonė pagaliau taptų realybe.</p>
            </div>
          </div>
        """
    }
}

if __name__ == "__main__":
    print(f"Bespoke Physics Data sugeneruota: {len(PHYSICS_DATA)} irasu.")
