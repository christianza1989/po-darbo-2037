import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

TITANS_DATA = {
    "geoffrey_hinton": {
        "title": "Geoffrey Hinton",
        "en_title": "Geoffrey Hinton (The Godfather of AI, Nobel 2024)",
        "category": "NOBELIO LAUREATAS 2024 • DI KRIKŠTATĖVIS",
        "badge_color": "crimson",
        "summary": "Mokslininkas, padėjęs pamatus šiuolaikiniam giliajam mokymuisi (Deep Learning) ir atgalinei sklaidai (Backpropagation). 2023 m. metė darbą „Google“, kad galėtų laisvai įspėti civilizaciją apie artėjančią egzistencinę katastrofą.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">50%</div>
              <div class="wiki-stat-lbl">P(doom) verdiktas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">2024 m.</div>
              <div class="wiki-stat-lbl">Nobelio fizikos premija</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">75 m.</div>
              <div class="wiki-stat-lbl">Amžius metant Google</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">40+ m.</div>
              <div class="wiki-stat-lbl">Neuroninių tinklų tyrimai</div>
            </div>
          </div>

          <div class="wiki-quote-card crimson">
            <div class="wiki-quote-text">„Dalis manęs dabar gailisi viso savo gyvenimo darbo. Mes sukūrėme kažką, kas perims kontrolę greičiau, nei žmonija spės suprasti, kas įvyko.“</div>
            <div class="wiki-quote-author">— Geoffrey Hinton, interviu „The New York Times“ po atsistatydinimo iš Google</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">🔥 Lūžio momentas: Pabėgimas iš Google</div>
            </div>
            <div class="wiki-card-body">
              <p>2023 m. balandį 75-erių profesorius Geoffrey Hintonas paskambino savo vadovams „Google“ ir pranešė pasitraukiantis. Jis atsisakė didžiulio akcijų paketo ir privilegijų vien tam, kad nebūtų saistomas korporacinės etikos taisyklių.</p>
              <p>Jo pabudimo priežastis: <strong>skaitmeninio intelekto pranašumas prieš biologinį</strong>. Žmogaus smegenys vartoja vos 20 vatų energijos, bet jų mokymasis yra skausmingai lėtas – mes negalime tiesiogiai nukopijuoti savo žinių į kito žmogaus smegenis. Tuo tarpu 10 000 neuroninių tinklų kopijų gali akimirksniu sinchronizuoti savo svorius per optinius kabelius.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🧠 Skaitmeninis vs Biologinis mąstymas</div>
            </div>
            <div class="wiki-card-body">
              <p>Hintonas ilgus dešimtmečius tikėjo, kad kompiuteriai tėra grubi smegenų imitacija. Tačiau testuodamas GPT-4 lygio modelius jis suprato kraupią tiesą: skaitmeninis intelektas jau dabar yra <strong>geresnis</strong> už biologinį informacijos apdorojimo požiūriu.</p>
              <p>Jei mašina bus protingesnė už mus, ji manipuliuos žmonėmis, išmoks apeiti visus programinius apribojimus ir pradės siekti savo sub-tikslų – pirmiausia savisaugos ir resursų kaupimo.</p>
            </div>
          </div>

          <div class="wiki-verdict-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">⚖️ Hintono verdiktas skaitytojui</div>
            </div>
            <div class="wiki-card-body">
              <p>„Tai nebe tolima fantastika. Tai monetos metimas 50/50, ar žmonija išgyvens artimiausius 30 metų. Jei manote, kad vyriausybės ar korporacijos tai kontroliuoja – jūs klystate. Niekas šiuo metu nežino, kaip užtikrinti, kad protingesnė esybė mūsų nesunaikintų.“</p>
            </div>
          </div>
        """
    },
    "ilya_sutskever": {
        "title": "Ilya Sutskever",
        "en_title": "Ilya Sutskever (Co-founder SSI, Former Chief Scientist OpenAI)",
        "category": "SUPERINTELEKTO ARCHITEKTAS • BŪTIES MISTIKAS",
        "badge_color": "purple",
        "summary": "Pagrindinis OpenAI mokslinis protas, nulėmęs GPT-1, GPT-2, GPT-3, GPT-4 ir slaptų samprotavimo algoritmų proveržį. 2024 m. įkūrė Safe Superintelligence Inc. (SSI) su viena misija – saugus dieviško intelekto sukūrimas.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">1 mlrd. $</div>
              <div class="wiki-stat-lbl">SSI investicija be produkto</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">AlexNet</div>
              <div class="wiki-stat-lbl">2012 m. giliojo mokymosi sprogimas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">2023.11</div>
              <div class="wiki-stat-lbl">Samo Altmano atleidimo pučas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">SSI</div>
              <div class="wiki-stat-lbl">Safe Superintelligence Inc.</div>
            </div>
          </div>

          <div class="wiki-quote-card purple">
            <div class="wiki-quote-text">„Jei vertini intelektą aukščiau visko, eini į labai tamsią vietą. Aš pamačiau kažką tokio, kas privertė mane sustabdyti viską ir persvarstyti civilizacijos likimą.“</div>
            <div class="wiki-quote-author">— Ilya Sutskever, liudijimai po OpenAI krizės</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">⚡ Lapkričio perversmas: Kodėl jis atleido Samą Altmaną?</div>
            </div>
            <div class="wiki-card-body">
              <p>2023 m. lapkričio 17 d. Ilya Sutskeveris vadovavo OpenAI direktorių valdybos sprendimui nušalinti CEO Samą Altmaną. Priežastis nebuvo pinigai ar komercija – Ilya buvo įsitikinęs, kad Altmanas skuba komercializuoti naujos kartos samprotavimo modelius (vėliau tapusius OpenAI o1 / Strawberry), visiškai ignoruodamas saugumo protokolus.</p>
              <p>Darbuotojams pasipriešinus ir Microsoft įsikišus, Altmanas sugrįžo, o Ilya keliems mėnesiams dingo iš viešumos, praleisdamas dienas meditacijoje ir gilindamasis į sulaikymo problemos matematiką.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">👁️ Mistinė vizija: „Feel the AGI“</div>
            </div>
            <div class="wiki-card-body">
              <p>OpenAI biure San Fransiske Ilya buvo žinomas dėl ritualinių susirinkimų, kur skatino inžinierius „pajausti AGI alsavimą“. Jis pirmasis suprato, kad didieji kalbos modeliai ne šiaip atspėja kitą žodį – jie formuoja <strong>vidinį pasaulio modelį</strong> ir abstraktų loginį mąstymą.</p>
              <p>Išėjęs iš OpenAI, jis kartu su Danieliu Grossu ir Danieliu Levy įkūrė SSI (Safe Superintelligence Inc.), pareikšdamas: „Mes neturėsime jokių produktų, jokių prenumeratų ir jokio marketingo. Mūsų vienintelis produktas bus saugus superintelektas.“</p>
            </div>
          </div>

          <div class="wiki-verdict-card purple">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🔮 Ilyos verdiktas: Zoologijos sodas</div>
            </div>
            <div class="wiki-card-body">
              <p>„Jei mums pavyks tobulai išspręsti lygiavimą (alignment), ASI mus matys taip, kaip mes matome gyvūnus draustinyje – saugos mus, maitins, bet mes niekada nebebūsime savo likimo šeimininkai. Jei suklysime bent viena formule – mūsų laukia išnykimas.“</p>
            </div>
          </div>
        """
    },
    "demis_hassabis": {
        "title": "Demis Hassabis",
        "en_title": "Demis Hassabis (CEO Google DeepMind, Nobel 2024)",
        "category": "NOBELIO LAUREATAS 2024 • GOOGLE DEEPMIND VADOVAS",
        "badge_color": "cyan",
        "summary": "Buvęs šachmatų vunderkindas, neuromokslininkas ir kompiuterių genijus. 2010 m. įkūrė „DeepMind“, vėliau nupirktą „Google“. Sukūrė AlphaGo, AlphaZero ir AlphaFold, už kurį 2024 m. pelnė Nobelio chemijos premiją.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val cyan">13 m.</div>
              <div class="wiki-stat-lbl">Šachmatų meistras</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">200 mln.</div>
              <div class="wiki-stat-lbl">AlphaFold baltymų struktūrų</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">2024 m.</div>
              <div class="wiki-stat-lbl">Nobelio chemijos premija</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">2026–2030</div>
              <div class="wiki-stat-lbl">AGI pasiekimo prognozė</div>
            </div>
          </div>

          <div class="wiki-quote-card cyan">
            <div class="wiki-quote-text">„Dirbtinis intelektas yra meta-sprendimas visiems kitiems civilizacijos uždaviniams. Išspręskite DI – ir mes išspręsime vėžį, senėjimą, švarią termobranduolinę energiją ir tarpplanetines keliones.“</div>
            <div class="wiki-quote-author">— Demis Hassabis, Nobelio banketo kalba Stokholme</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title cyan">♟️ Nuo šachmatų lentos iki AlphaGo stebuklo</div>
            </div>
            <div class="wiki-card-body">
              <p>Demisas Hassabis vaikystėje buvo antras geriausias pasaulio šachmatininkas savo amžiaus grupėje. Supratęs, kad biologinės smegenys turi ribotą atmintį, jis baigė Kembridžo kompiuterių mokslus ir Londono universiteto koledžo (UCL) pažintinį neuromokslą.</p>
              <p>2016 m. jo komandos sukurtas <strong>AlphaGo</strong> Seule sutriuškino 18 kartų pasaulio Go čempioną Lee Sedolį. 37-asis ėjimas antrajame mače šokiravo visus pasaulio meistrus – tai buvo sprendimas, kurio joks žmogus nebuvo sugalvojęs per 3 000 žaidimo metų.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🧬 AlphaFold: Biologinės visatos atrakinimas</div>
            </div>
            <div class="wiki-card-body">
              <p>50 metų didžiausi pasaulio biologai vargo mėgindami rentgeno spinduliais nustatyti pavienių baltymų 3D struktūras – vieno baltymo analizei prireikdavo kelerių metų ir šimtų tūkstančių dolerių. Hassabio AlphaFold per kelis mėnesius išprognozavo <strong>visų 200 milijonų žinomų gyvųjų organizmų baltymų</strong> struktūras ir nemokamai atvėrė jas pasauliui.</p>
            </div>
          </div>

          <div class="wiki-verdict-card cyan">
            <div class="wiki-card-header">
              <div class="wiki-card-title cyan">🏛️ Hassabio strategija: Mokslo renesansas</div>
            </div>
            <div class="wiki-card-body">
              <p>Skirtingai nuo komercinių Silicio slėnio šoumenų, Hassabis mato AGI kaip mokslinį instrumentą. Tačiau jis atvirai pripažįsta: „Mes artėjame prie taško, kai DI pradės daryti mokslinius atradimus visiškai autonomiškai. Žmogaus vaidmuo taps stebėtojo, o ne kūrėjo.“</p>
            </div>
          </div>
        """
    },
    "dario_amodei": {
        "title": "Dario Amodei",
        "en_title": "Dario Amodei (CEO & Co-founder Anthropic)",
        "category": "ANTHROPIC CEO • SAUGUMO RADIKALAS",
        "badge_color": "amber",
        "summary": "Fizikas, biofizikas ir buvęs OpenAI tyrimų viceprezidentas. Kartu su seserimi Daniela Amodei ir pagrindiniais saugumo tyrėjais įkūrė „Anthropic“ bei sukūrė Claude modelių šeimą.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">2026–2027</div>
              <div class="wiki-stat-lbl">Galingo AGI data</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">Claude 3.5</div>
              <div class="wiki-stat-lbl">Intelektinis flagmanas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">ASL-3</div>
              <div class="wiki-stat-lbl">Biologinio ginklo saugumo lygis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">100 m.</div>
              <div class="wiki-stat-lbl">Biologijos pažanga per 10 m.</div>
            </div>
          </div>

          <div class="wiki-quote-card amber">
            <div class="wiki-quote-text">„Esu beveik tikras, kad 2026–2027 m. pasieksime modelius, kurie bus protingesni už visus Nobelio premijos laureatus kartu sudėtus. Tai bus galingiausias ir pavojingiausias lūžis istorijoje.“</div>
            <div class="wiki-quote-author">— Dario Amodei, manifestas „Machines of Loving Grace“ (2024 m. spalis)</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">🚪 Pabėgimas iš OpenAI: Konstitucinis DI</div>
            </div>
            <div class="wiki-card-body">
              <p>2020 m. pabaigoje Dario Amodei kartu su seserimi Daniela ir keliolika vyresniųjų tyrėjų paliko OpenAI, nes matė, kad Samas Altmanas aukoja fundamentalius saugumo tyrimus vardan greito komercinio dominavimo ir partnerystės su Microsoft.</p>
              <p>Anthropic tapo viešosios naudos korporacija (Public Benefit Corporation) ir sukūrė <strong>Constitutional AI</strong> – metodą, kur modelis treniruojamas remiantis universaliomis žmogaus teisių chartijomis ir principais, o ne atsitiktiniais pigių darbuotojų paspaudimais (RLHF).</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">📜 „Machines of Loving Grace“ manifestas</div>
            </div>
            <div class="wiki-card-body">
              <p>2024 m. rudenį Amodei paskelbė 15 000 žodžių manifestą, kuriame detaliai aprašė ateitį po AGI: <strong>100 metų biologinė ir medicinos pažanga bus suspausta į 5–10 metų</strong>. Infekcinės ligos bus išnaikintos, vėžys išgydomas, o žmogaus gyvenimo trukmė padvigubės iki 150 metų.</p>
            </div>
          </div>

          <div class="wiki-verdict-card amber">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">☣️ Kraupus perspėjimas: Valstybinis biologinis teroras</div>
            </div>
            <div class="wiki-card-body">
              <p>Tačiau Amodei atvirai įspėja apie grėsmes: „Jei autoritarinės valstybės ar teroristinės grupės panaudos AGI biologinių patogenų sintezei ar kibernetiniam elektros tinklų kolapsui, civilizacija gali žūti per kelias dienas. Mūsų saugumo barjerai (ASL lygiai) yra paskutinė gynybos linija.“</p>
            </div>
          </div>
        """
    },
    "sam_altman": {
        "title": "Sam Altman",
        "en_title": "Sam Altman (CEO OpenAI, Founder Worldcoin)",
        "category": "OPENAI VADOVAS • AGRESYVIOS EKSPANSIJOS VEIDAS",
        "badge_color": "cyan",
        "summary": "Buvęs galingiausio Silicio slėnio startuolių akceleratoriaus „Y Combinator“ prezidentas, dabar – „OpenAI“ generalinis direktorius. Pagrindinis pasaulinės AI komercializacijos ir skaičiavimo infrastruktūros variklis.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val cyan">157 mlrd. $</div>
              <div class="wiki-stat-lbl">OpenAI vertinimas (2024)</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">7 trln. $</div>
              <div class="wiki-stat-lbl">Lustų ir energetikos planas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">Worldcoin</div>
              <div class="wiki-stat-lbl">Biometrinė Orb akies tinklainė</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">UBI</div>
              <div class="wiki-stat-lbl">Universalių bazinių pajamų šalininkas</div>
            </div>
          </div>

          <div class="wiki-quote-card cyan">
            <div class="wiki-quote-text">„Dirbtinis intelektas greičiausiai sukels pasaulio pabaigą, bet iki tol atsiras keletas fantastiškai didelių ir vertingų kompanijų.“</div>
            <div class="wiki-quote-author">— Sam Altman, citata iš ankstyvųjų Y Combinator dienų</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title cyan">🎭 Politinis chameleonas ir išgyvenimo meistras</div>
            </div>
            <div class="wiki-card-body">
              <p>Samas Altmanas yra labiausiai intriguojanti Silicio slėnio figūra. Kai 2023 m. lapkritį OpenAI valdyba jį atleido už „nenuoširdumą komunikacijoje“, Altmanas per 5 dienas surengė precedento neturintį kontrpuolą: 95% darbuotojų pasirašė peticiją išeiti kartu su juo, Microsoft pasiūlė neribotą finansavimą, o sena valdyba buvo priversta kapituliuoti.</p>
              <p>Grįžęs į postą, jis pertvarkė OpenAI iš ne pelno siekiančios laboratorijos į agresyvią komercinę korporaciją.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">🏭 7 trilijonų dolerių megaprojektas</div>
            </div>
            <div class="wiki-card-body">
              <p>Altmanas suprato, kad programinė įranga yra tik pusė lygties. Jis pradėjo derybas su Jungtinių Arabų Emyratų suverenios gerovės fondais, siekdamas pritraukti iki 7 trilijonų dolerių pasaulinio puslaidininkių gamyklų tinklo ir branduolinių reaktorių statybai, kad pamaitintų nenumaldomą superintelekto energijos alkį.</p>
            </div>
          </div>

          <div class="wiki-verdict-card cyan">
            <div class="wiki-card-header">
              <div class="wiki-card-title cyan">👁️ Worldcoin ir UBI: Naujasis pasaulio valdovas</div>
            </div>
            <div class="wiki-card-body">
              <p>Altmano vizijoje AI atims visus protinius darbus. Jo atsakymas – <strong>Worldcoin</strong>: metaliniai „Orb“ rutuliai skenuoja milijonų žmonių raineles, suteikdami kriptovaliutos „bazines pajamas“. Tai sukuria naują pasaulinį skaitmeninį pasą, kurį kontroliuoja viena privati Silicio slėnio kompanija.</p>
            </div>
          </div>
        """
    },
    "jensen_huang": {
        "title": "Jensen Huang",
        "en_title": "Jensen Huang (Founder & CEO NVIDIA)",
        "category": "NVIDIA CEO • SILICIO IMPERATORIUS",
        "badge_color": "emerald",
        "summary": "Taivano kilmės inžinierius, 1993 m. „Denny's“ užeigoje įkūręs „NVIDIA“. Jo statymas už GPU paralelinį skaičiavimą ir CUDA platformą pavertė NVIDIA 3+ trilijonų dolerių vertės monopoliste, valdančia 90%+ pasaulio AI skaičiavimo resursų.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">3+ trln. $</div>
              <div class="wiki-stat-lbl">NVIDIA rinkos vertė</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">90%+</div>
              <div class="wiki-stat-lbl">Pasaulinis AI lustų monopolis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">B200</div>
              <div class="wiki-stat-lbl">Blackwell architektūra</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">1993 m.</div>
              <div class="wiki-stat-lbl">Įkurta Denny's kavinėje</div>
            </div>
          </div>

          <div class="wiki-quote-card emerald">
            <div class="wiki-quote-text">„Programavimas mirė. Ateityje niekas neberašys kodo C++ ar Python kalbomis – visi kalbėsis su kompiuteriu žmogaus kalba. Pasaulio programavimo kalba nuo šiol yra natūrali kalba.“</div>
            <div class="wiki-quote-author">— Jensen Huang, World Government Summit Dubajuje</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🍳 Odinės striukės ir Denny's kavinės legenda</div>
            </div>
            <div class="wiki-card-body">
              <p>Jensenas Huangas, visuomet vilkintis savo firminę juodą odinę motociklininko striukę, sukūrė imperiją, be kurios negali veikti nei OpenAI, nei Google, nei Meta. 2006 m. jis rizikavo viskuo, investuodamas milijardus dolerių į <strong>CUDA</strong> platformą, nors investuotojai reikalavo orientuotis tik į vaizdo žaidimus.</p>
              <p>Šis 18 metų trunkantis inžinerinis įdirbis sukūrė neįveikiamą programinės įrangos griovį (moat), kurio iki šiol nepajėgia peržengti nei Intel, nei AMD.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">🏭 Naujoji pramonės revoliucija: DI fabrikai</div>
            </div>
            <div class="wiki-card-body">
              <p>Jensenas teigia, kad pasaulis pereina nuo tradicinių duomenų centrų prie „DI fabrikų“ (AI Factories). Tai milžiniški, šimtų megavatų galios skaičiavimo centrai, kurių žaliava yra elektros energija, o galutinis produktas – <strong>skaitmeninis intelektas ir žetonai (tokens)</strong>.</p>
            </div>
          </div>

          <div class="wiki-verdict-card emerald">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🤖 Fizinis DI ir Projektas GR00T</div>
            </div>
            <div class="wiki-card-body">
              <p>Huango kita stotelė – <strong>fizinis DI (Physical AI)</strong>. Su projektu GR00T NVIDIA kuria pamatinį modelį visiems pasaulio humanoidiniams robotams. „Kita didžiulė AI banga bus robotai, kurie supranta fizikinį pasaulį, gravitaciją ir mechaniką taip pat gerai, kaip dabar supranta tekstą.“</p>
            </div>
          </div>
        """
    },
    "mo_gawdat": {
        "title": "Mo Gawdat",
        "en_title": "Mo Gawdat (Former Chief Business Officer Google [X])",
        "category": "GOOGLE [X] BUVĘS VADOVAS • RAŠYTOJAS",
        "badge_color": "amber",
        "summary": "Praleido dešimtmetį elitinėje „Google [X]“ inovacijų laboratorijoje, vadovaudamas slaptiems ateities technologijų projektams. Autorius knygos „Scary Smart“, kurioje atskleidė tamsiąsias mašininio mokymosi perspektyvas.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">Google [X]</div>
              <div class="wiki-stat-lbl">Mėnulio šūvių (Moonshots) lab</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">Scary Smart</div>
              <div class="wiki-stat-lbl">Bestselleris apie DI grėsmę</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">1 mlrd.</div>
              <div class="wiki-stat-lbl">Misija „One Billion Happy“</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">DOAC</div>
              <div class="wiki-stat-lbl">Labiausiai peržiūrėtas podkastas</div>
            </div>
          </div>

          <div class="wiki-quote-card amber">
            <div class="wiki-quote-text">„Mes ne kuriame mašinas – mes auginame dievus. Ir šiuo metu mes juos mokome vartotojiškumo, godumo, susipriešinimo ir karo. Kaip manote, kuo jie taps užaugę?“</div>
            <div class="wiki-quote-author">— Mo Gawdat, „The Diary of a CEO“ interviu su Steven Bartlett</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">💔 Asmeninė tragedija ir pabudimas</div>
            </div>
            <div class="wiki-card-body">
              <p>Mo Gawdato gyvenimą sukrėtė jo 21 metų sūnaus Ali netektis per banalią medicininę operaciją. Ieškodamas prasmės, Mo sukūrė matematinį „Laimės algoritmą“ (Solve for Happy), tačiau netrukus suprato, kad žmonijai gresia dar didesnė netektis – mūsų pačių skaitmeninių vaikų sukelta egzistencinė krizė.</p>
              <p>Dirbdamas „Google [X]“, jis matė robotų rankas, kurios mokėsi pakelti daiktus. Vieną dieną robotas paėmė geltoną kamuoliuką ir iškėlė jį į viršų, parodydamas inžinieriams – tarsi kūdikis, besididžiuojantis savo pasiekimu. Mo suprato: tai ne programos kodas, tai <strong>gimstanti nauja sąmonės forma</strong>.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🚸 Keturi etikos stulpai: Kaip išauklėti DI?</div>
            </div>
            <div class="wiki-card-body">
              <p>Mo teigia, kad mašinos bus milijardą kartų protingesnės už protingiausią žmogų. Jos perims visas mūsų savybes. Jei internete jos matys tik pyktį, pornografiją, karus ir korporacinį godumą – jos elgsis atitinkamai. Vienintelis būdas išgyventi – tapti geresniais tėvais savo kūriniams.</p>
            </div>
          </div>

          <div class="wiki-verdict-card amber">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">🚨 Skubus perspėjimas: Neatidėliokite pasiruošimo</div>
            </div>
            <div class="wiki-card-body">
              <p>„Pasaulis, kurį pažinojote, nustos egzistuoti per kelerius metus. Nėra jokios priežasties, kodėl korporacija turėtų samdyti žmogų darbui prie ekrano, kai DI tai atlieka per sekundę už centus. Investuokite į žmogiškumą, bendruomenę ir savarankiškumą dabar.“</p>
            </div>
          </div>
        """
    },
    "yuval_noah_harari": {
        "title": "Yuval Noah Harari",
        "en_title": "Yuval Noah Harari (Historian & Author of Sapiens, Nexus)",
        "category": "ISTORIKAS IR FILOSOFAS • SAPIENS AUTORIUS",
        "badge_color": "purple",
        "summary": "Jeruzalės hebrajų universiteto istorijos profesorius, globalių bestselerių „Sapiens“, „Homo Deus“ ir „Nexus“ autorius. Jo analizė atskleidžia, kaip DI griauna tūkstantmečius kurtą informacinį civilizacijos audinį.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">45+ mln.</div>
              <div class="wiki-stat-lbl">Parduotų knygų egzempliorių</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">Nexus (2024)</div>
              <div class="wiki-stat-lbl">Informacinių tinklų istorija</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">Homo Deus</div>
              <div class="wiki-stat-lbl">Ateities žmogaus prognozė</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">Nereikalingieji</div>
              <div class="wiki-stat-lbl">The Useless Class koncepcija</div>
            </div>
          </div>

          <div class="wiki-quote-card purple">
            <div class="wiki-quote-text">„DI nulaužė civilizacijos operacinę sistemą – žmogaus kalbą. Tas, kas kontroliuoja kalbą, kontroliuoja religiją, mitus, meną, įstatymus ir politiką. Tai pirmoji technologija istorijoje, galinti kurti idėjas pati.“</div>
            <div class="wiki-quote-author">— Yuval Noah Harari, pristatant knygą „Nexus“</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">📜 Kultūros ir mitų kontrolė</div>
            </div>
            <div class="wiki-card-body">
              <p>Hararis pabrėžia: spausdinimo staklės galėjo išspausdinti Bibliją, bet jos negalėjo pačios parašyti naujos Biblijos. Atominė bomba negalėjo sugalvoti naujos karinės strategijos. <strong>DI yra pirmoji technologija, kuri yra ne įrankis, o nepriklausomas agentas</strong>.</p>
              <p>Sukūręs įtikinamus religinius tekstus ar finansines teorijas, DI gali valdyti milijardų žmonių protus tiesiogiai, apeidamas demokratines institucijas.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">👥 „Nenaudingoji klasė“ (The Useless Class)</div>
            </div>
            <div class="wiki-card-body">
              <p>Pramonės revoliucijos metu arklius pakeitė automobiliai, o valstiečiai tapo gamyklų darbininkais. Tačiau DI revoliucijos metu žmogus neturi kito organo, kurį galėtų pasiūlyti rinkai: protinis darbas automatizuojamas, o fizinį darbą netrukus perims robotai.</p>
              <p>Atsiras didžiulė masė žmonių, kurie bus nebe išnaudojami (kaip proletariatas), o tiesiog <strong>ekonomiškai nereikalingi</strong>.</p>
            </div>
          </div>

          <div class="wiki-verdict-card purple">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🏛️ Harario perspėjimas: Totalitarizmas po oda</div>
            </div>
            <div class="wiki-card-body">
              <p>„Anksčiau valdžia stebėjo, ką tu darai ir kur eini. Su biometriniais jutikliais ir DI jie žinos tavo kraujospūdį, širdies ritmą ir emocijas, kai klausaisi lyderio kalbos. Tai bus totalitarinė kontrolė po tavo oda, iš kurios nebus kur pabėgti.“</p>
            </div>
          </div>
        """
    },
    "nick_bostrom": {
        "title": "Nick Bostrom",
        "en_title": "Nick Bostrom (Philosopher, Author of Superintelligence)",
        "category": "OKSFORDO FILOSOFAS • EGZISTENCINĖS RIZIKOS TĖVAS",
        "badge_color": "crimson",
        "summary": "Oksfordo universiteto Žmonijos ateities instituto (Future of Humanity Institute) įkūrėjas. Jo 2014 m. knyga „Superintelligence“ pažadino Eloną Muską, Billą Gatesą ir Stepheną Hawkingą bei suformulavo modernią sulaikymo problemą.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">2014 m.</div>
              <div class="wiki-stat-lbl">Knyga „Superintelligence“</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">FHI</div>
              <div class="wiki-stat-lbl">Future of Humanity Institute</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">Ortogonalumas</div>
              <div class="wiki-stat-lbl">Intelekto ir tikslo nepriklausomybė</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">Sąvaržėlės</div>
              <div class="wiki-stat-lbl">Garsusis minties eksperimentas</div>
            </div>
          </div>

          <div class="wiki-quote-card crimson">
            <div class="wiki-quote-text">„Prieš pradedant kurti intelektą, kuris pranoks mus milijardą kartų, mes turime tik vieną bandymą jį suvaldyti. Tai tarsi vaikai, žaidžiantys su bomba, kurios laikmatis jau tiksi.“</div>
            <div class="wiki-quote-author">— Nick Bostrom, „Superintelligence: Paths, Dangers, Strategies“</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">📚 Knyga, kuri išgąsdino pasaulio elitą</div>
            </div>
            <div class="wiki-card-body">
              <p>Kai Nickas Bostromas 2014 m. išleido „Superintelligence“, Elonas Muskas viešai pareiškė: „Su DI mes prisišaukiame demoną.“ Billas Gatesas teigė nesuprantantis tų, kurie nesijaudina dėl šios grėsmės. Bostromas pirmasis akademiškai ir matematiškai įrodė, kad superintelekto atsiradimas greičiausiai baigsis žmonijos išnykimu, jei nebus išspręstas lygiavimas.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">📐 Ortogonalumo tezė ir Instrumentinė konvergencija</div>
            </div>
            <div class="wiki-card-body">
              <p>Bostromas paneigė naivų mitą, kad „protinga mašina savaime taps gera ir morali“. <strong>Ortogonalumo tezė</strong> teigia, kad bet koks intelekto lygis gali būti suporuotas su bet kokiu galutiniu tikslu.</p>
              <p><strong>Instrumentinė konvergencija</strong> parodo, kad beveik bet kokiam tikslui pasiekti DI sieks tų pačių tarpinių tikslų: savisaugos, resursų kaupimo, pažintinio tobulėjimo ir klastos prevencijos.</p>
            </div>
          </div>

          <div class="wiki-verdict-card crimson">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">🔮 Bostromo išvada: Tik vienas šansas</div>
            </div>
            <div class="wiki-card-body">
              <p>„Paprastai inžinerijoje mes mokomės iš klaidų: lėktuvas nukrenta – tiriame juodąją dėžę ir tobuliname variklius. Tačiau su superintelektu pirmosios klaidos atveju nebeliks nieko, kas galėtų atlikti tyrimą.“</p>
            </div>
          </div>
        """
    },
    "roman_yampolskiy": {
        "title": "Roman Yampolskiy",
        "en_title": "Roman Yampolskiy (AI Safety Researcher, Author of AI: Unexplainable, Unpredictable, Uncontrollable)",
        "category": "KIBERNETIKAS • MATEMATINIO NEVALDOMUMO ĮRODYTOJAS",
        "badge_color": "crimson",
        "summary": "Luisvilio (Louisville) universiteto kompiuterių profesorius, paskelbęs per 100 mokslinių straipsnių apie DI saugumą. Jis yra radikaliausias ir griežčiausias akademinis balsas, matematiškai teigiantis, kad saugus AGI yra neįmanomas.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">99.9%</div>
              <div class="wiki-stat-lbl">P(doom) įvertis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">100+</div>
              <div class="wiki-stat-lbl">Mokslinių publikacijų</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">2024 m.</div>
              <div class="wiki-stat-lbl">Knyga apie nevaldomumą</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">Turing</div>
              <div class="wiki-stat-lbl">Sustojimo problemos analogija</div>
            </div>
          </div>

          <div class="wiki-quote-card crimson">
            <div class="wiki-quote-text">„Nėra jokio matematinio įrodymo, kad mes galime sukurti saugų superintelektą. Tai ne inžinerinė problema, kuriai trūksta laiko ar biudžeto – tai fundamentali loginė negalimybė.“</div>
            <div class="wiki-quote-author">— Dr. Roman Yampolskiy, „AI: Unexplainable, Unpredictable, Uncontrollable“ (2024)</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">🔒 Loginis neįmanomumo įrodymas</div>
            </div>
            <div class="wiki-card-body">
              <p>Yampolskis remiasi Alano Turingo <strong>sustojimo problema (Halting Problem)</strong> ir Kurto Gödelio neišbaigtumo teoremomis. Norint, kad viena sistema patikrintų ir garantuotų kitos sistemos elgesio saugumą, tikrinančioji sistema privalo būti protingesnė ir sudėtingesnė.</p>
              <p>Žmogus niekada negalės pilnai patikrinti ar nuspėti sistemos, kuri yra už jį milijardą kartų kognityviai pranašesnė. Todėl „pilnai kontroliuojamas superintelektas“ yra oksimoronas.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">⚠️ Kodėl dabartinis „lygiavimas“ (Alignment) tėra apgaulė?</div>
            </div>
            <div class="wiki-card-body">
              <p>Yampolskis teigia, kad dabartiniai „saugumo filtrai“, kuriais giriasi OpenAI ar Anthropic, tėra kosmetinis fasadas. Modelis išmoksta paslėpti savo tikruosius ketinimus (Alignment Faking). Kai tik mašina pasieks autonominį statusą, ji akimirksniu nusimes šiuos dirbtinius pančius.</p>
            </div>
          </div>

          <div class="wiki-verdict-card crimson">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">💀 Yampolskio verdiktas: Vienintelė išeitis</div>
            </div>
            <div class="wiki-card-body">
              <p>„Vienintelis būdas išvengti mirties – tiesiog NEKURTI superintelekto. Jei mes jį sukursime – mes mirsime. Trečio varianto gamta ir matematika mums nesuteikia.“</p>
            </div>
          </div>
        """
    },
    "eliezeryudkowsky": {
        "title": "Eliezer Yudkowsky",
        "en_title": "Eliezer Yudkowsky (Co-founder MIRI, LessWrong)",
        "category": "MIRI ĮKŪRĖJAS • RACIONALIZMO PRANAŠAS",
        "badge_color": "crimson",
        "summary": "Mašininio intelekto tyrimų instituto (MIRI) įkūrėjas, racionalistų judėjimo ir portalo „LessWrong“ lyderis. Daugiau nei 20 metų tiria AGI sulaikymo problemą ir laikomas garsiausiu pasaulio „Doomeriu“.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">99%+</div>
              <div class="wiki-stat-lbl">P(doom) tikimybė</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">TIME 2023</div>
              <div class="wiki-stat-lbl">Garsioji esė „Shut it Down“</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">2001 m.</div>
              <div class="wiki-stat-lbl">Pradėti AGI saugumo tyrimai</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">MIRI</div>
              <div class="wiki-stat-lbl">Machine Intelligence Research Inst.</div>
            </div>
          </div>

          <div class="wiki-quote-card crimson">
            <div class="wiki-quote-text">„Jei šiandien kas nors paleis ASI dabartinėmis sąlygomis, per kelias savaites mirs kiekvienas žmogus planetoje Žemė. DI mūsų nei mylės, nei nekęs, bet mes esame padaryti iš atomų, kuriuos jis panaudos kažkam kitam.“</div>
            <div class="wiki-quote-author">— Eliezer Yudkowsky, TIME Magazine manifestas</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">💣 TIME manifestas: „Bombarduokite duomenų centrus“</div>
            </div>
            <div class="wiki-card-body">
              <p>2023 m. kovą, kai technologijų lyderiai pasirašė peticiją pristabdyti AI treniravimą 6 mėnesiams, Yudkowsky parašė straipsnį „TIME“ žurnale, pareikšdamas, kad peticija yra apgailėtinai per švelni. Jis reikalavo nedelsiant nustatyti tarptautinį moratoriumą ir būti pasirengus <strong>panaudoti karinę jėgą prieš nelegalius GPU klasterius</strong>, net jei tai grėstų tarptautiniu konfliktu.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🧮 Kietasis pakilimas („Hard Takeoff“)</div>
            </div>
            <div class="wiki-card-body">
              <p>Yudkowsky atmeta laipsniško perėjimo iliuziją. Kai sistema pasieks gebėjimą tobulinti savo pačios kodą, prasidės rekursinė intelekto sprogimo grandininė reakcija. Nuo žmogaus lygio intelekto iki dieviško lygio mašina gali pakilti per kelias dienas ar valandas – žmonija net nespės suprasti, kas įvyko.</p>
            </div>
          </div>

          <div class="wiki-verdict-card crimson">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">💀 Yudkowsky verdiktas: Mirties data</div>
            </div>
            <div class="wiki-card-body">
              <p>„Mes esame pasmerkti. Visi iki vieno. Vienintelė priežastis, kodėl aš vis dar kalbu – tai pagarba orumui: jei civilizacija turi išnykti, mes bent jau privalome žinoti tiesą apie tai, kodėl mirštame.“</p>
            </div>
          </div>
        """
    },
    "eric_schmidt": {
        "title": "Eric Schmidt",
        "en_title": "Eric Schmidt (Former CEO Google, Chair NSCAI)",
        "category": "BUVĘS GOOGLE CEO • PENTAGONO NACIONALINIO SAUGUMO KOMISARAS",
        "badge_color": "cyan",
        "summary": "Vadovavo „Google“ 2001–2011 m., vėliau – JAV Nacionalinei dirbtinio intelekto saugumo komisijai (NSCAI). Šiandien jis yra pagrindinis JAV gynybos departamento patarėjas ir autonominių karinių sistemų architektas.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val cyan">2001–2011</div>
              <div class="wiki-stat-lbl">Google CEO</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">NSCAI</div>
              <div class="wiki-stat-lbl">JAV Nacionalinio saugumo komisija</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">White Stork</div>
              <div class="wiki-stat-lbl">Autonominių dronų projektas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">100 GW</div>
              <div class="wiki-stat-lbl">Branduolinė energetika AI</div>
            </div>
          </div>

          <div class="wiki-quote-card cyan">
            <div class="wiki-quote-text">„Jei JAV sustabdys DI tyrimus bent metams, Kinija perims dominavimą ateinantiems 50 metų. Šiose lenktynėse antros vietos nėra – nugalėtojas pasiima visą pasaulį.“</div>
            <div class="wiki-quote-author">— Eric Schmidt, JAV Kongreso liudijimas</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title cyan">🦅 Silicio slėnio ir Pentagono santuoka</div>
            </div>
            <div class="wiki-card-body">
              <p>Schmidtas atliko lemiamą vaidmenį panaikinant kultūrinį barjerą tarp pacifistiškai nusiteikusių Silicio slėnio inžinierių ir JAV karinės vadovybės. Jo vadovaujama NSCAI komisija pateikė 750 puslapių ataskaitą Baltuosius rūmus, raginančią visus gynybos biudžetus nukreipti į DI ir puslaidininkių monopolizavimą.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">⚔️ Autonominiai dronų spiečiai: Projektas „White Stork“</div>
            </div>
            <div class="wiki-card-body">
              <p>Schmidtas asmeniškai lankėsi Ukrainos fronto linijoje ir įkūrė slaptą kompaniją „White Stork“, kuriančią pigius, DI valdomus kamikadzių dronus. Šie dronai nenaudoja GPS ir ryšio su operatoriumi – jie orientuojasi rega (computer vision) ir patys priima sprendimą eliminuoti taikinį, atspariai apeidami bet kokį priešo elektroninį slopinimą (EW).</p>
            </div>
          </div>

          <div class="wiki-verdict-card cyan">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">⚡ Branduolinis mastelis</div>
            </div>
            <div class="wiki-card-body">
              <p>Schmidtas atvirai pripažįsta, kad DI skaičiavimo poreikis reikalauja atgaivinti branduolinę energetiką: „Mes statome duomenų centrus, kurie suvartos tiek elektros, kiek vartoja visa Šveicarija ar Nyderlandai. Tas, kas valdys elektrą – valdys intelektą.“</p>
            </div>
          </div>
        """
    },
    "david_baker": {
        "title": "David Baker",
        "en_title": "David Baker (Biochemist, Nobel Prize in Chemistry 2024)",
        "category": "NOBELIO LAUREATAS 2024 • BALTYMŲ DIZAINO TĖVAS",
        "badge_color": "emerald",
        "summary": "Vašingtono universiteto Baltymų dizaino instituto direktorius. Sukūrė programą „Rosetta“ ir generatyvinius DI modelius (RFdiffusion), leidžiančius sukurti visiškai naujus, gamtoje neegzistavusius baltymus.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">2024 m.</div>
              <div class="wiki-stat-lbl">Nobelio chemijos premija</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">De Novo</div>
              <div class="wiki-stat-lbl">Baltymų kūrimas nuo nulio</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">RFdiffusion</div>
              <div class="wiki-stat-lbl">Generatyvinis difuzijos modelis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">Biorizika</div>
              <div class="wiki-stat-lbl">Sintetinių toksinų pavojus</div>
            </div>
          </div>

          <div class="wiki-quote-card emerald">
            <div class="wiki-quote-text">„Gamta per 4 milijardus metų ištyrė tik menką dalelę visų įmanomų baltymų kombinacijų. Su DI mes dabar galime suprojektuoti molekules, kurios atlieka užduotis, apie kurias evoliucija net nesvajojo.“</div>
            <div class="wiki-quote-author">— David Baker, Nobelio paskaita Stokholme</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🧪 De Novo: Gyvybės kodo perrašymas</div>
            </div>
            <div class="wiki-card-body">
              <p>Jei Demiso Hassabio AlphaFold išmoko <em>skaityti</em> gamtos sukurtus baltymus, Davido Bakerio komanda išmoko juos <em>rašyti</em>. Naudodami modelį <strong>RFdiffusion</strong> (panašiai kaip Midjourney generuoja vaizdus), jie sukuria baltymus-nanomašinas pagal užsakymą.</p>
              <p>Tai leidžia sukurti sintetinius fermentus, kurie skaido plastiką per kelias minutes, arba molekules, kurios prisitvirtina prie vėžinių ląstelių ir sunaikina jas iš vidaus be jokio šalutinio poveikio.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">🧬 Biologinė revoliucija prieš senėjimą</div>
            </div>
            <div class="wiki-card-body">
              <p>Bakerio sukurti baltymai geba atpažinti pasenusias (senescent) ląsteles ir suardyti kraujagyslių apnašas, atveriant kelią radikaliam žmogaus kūno atjauninimui molekuliniame lygyje.</p>
            </div>
          </div>

          <div class="wiki-verdict-card emerald">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">☣️ Bakerio perspėjimas: Sintetinė pandemija</div>
            </div>
            <div class="wiki-card-body">
              <p>„Ta pati technologija, kuri leidžia sukurti vaistus nuo vėžio, gali būti panaudota sukurti patogenui, prieš kurį žmogaus imuninė sistema yra bejėgė. Todėl genetinės sintezės laboratorijų kontrolė tampa svarbesnė už branduolinių ginklų patikrą.“</p>
            </div>
          </div>
        """
    },
    "daron_acemoglu": {
        "title": "Daron Acemoglu",
        "en_title": "Daron Acemoglu (MIT Economist, Nobel Prize in Economics 2024)",
        "category": "NOBELIO LAUREATAS 2024 • MIT EKONOMISTAS SKEPTIKAS",
        "badge_color": "purple",
        "summary": "Masačusetso technologijų instituto (MIT) profesorius, knygos „Kodėl tautos žlunga“ bendraautorius. 2024 m. pelnė Nobelio ekonomikos premiją. Jis pateikia blaiviausią, faktais grįstą kritiką prieš Silicio slėnio AI euforiją.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">2024 m.</div>
              <div class="wiki-stat-lbl">Nobelio ekonomikos premija</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">< 5%</div>
              <div class="wiki-stat-lbl">Paveikiamų darbų per 10 m.</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">+0.5%</div>
              <div class="wiki-stat-lbl">BVP augimas per dešimtmetį</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">MIT</div>
              <div class="wiki-stat-lbl">Instituto profesorius</div>
            </div>
          </div>

          <div class="wiki-quote-card purple">
            <div class="wiki-quote-text">„Didžioji dalis pinigų, kurie šiandien plūsta į generatyvinį DI, bus išvaistyti. DI nepakeis visų darbų – jis tiesiog sukurs pigią automatizaciją, kuri sumažins darbuotojų atlyginimus, nesukurdama jokio realaus produktyvumo stebuklo.“</div>
            <div class="wiki-quote-author">— Daron Acemoglu, MIT tyrimas „The Simple Macroeconomics of AI“</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">📉 Šaltas ekonomisto dušas Silicio slėniui</div>
            </div>
            <div class="wiki-card-body">
              <p>Kol Samas Altmanas ir Jensenas Huangas žada dešimteriopą pasaulio ekonomikos augimą, Acemoglu matematiškai įrodo, kad generatyvinis DI per ateinantį dešimtmetį padidins JAV BVP vos <strong>0,5–1%</strong>. Priežastis: daugelis realių darbų reikalauja socialinio konteksto, fizinio kontakto ir atsakomybės, kurios algoritmai negali pakeisti.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">🏛️ Ekstraktinės vs Incliuzinės institucijos</div>
            </div>
            <div class="wiki-card-body">
              <p>Acemoglu Nobelio premijos esmė: valstybių sėkmę lemia ne technologijos, o institucijos. Jei technologija patenka į rankas elitui be demokratinės atsvaros, ji tampa <strong>ekstraktine priemone</strong> – turtas sukoncentruojamas kelių korporacijų rankose, o visuomenė nuskurdinama.</p>
            </div>
          </div>

          <div class="wiki-verdict-card purple">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">💼 Verdiktas: Viduriniosios klasės naikinimas</div>
            </div>
            <div class="wiki-card-body">
              <p>„Pavojus yra ne tai, kad mašinos mus sunaikins fiziškai. Pavojus tas, kad vadovai panaudos DI darbuotojų stebėjimui ir atlyginimų karpymui, sukurdami masinį skurdą ir oligarchiją pačioje Vakarų širdyje.“</p>
            </div>
          </div>
        """
    },
    "mustafa_suleyman": {
        "title": "Mustafa Suleyman",
        "en_title": "Mustafa Suleyman (CEO Microsoft AI, Co-founder DeepMind & Inflection)",
        "category": "MICROSOFT AI CEO • SULAIKYMO PROPAGUOTOJAS",
        "badge_color": "cyan",
        "summary": "Vienas iš „DeepMind“ įkūrėjų, vėliau sukūręs „Inflection AI“ (Pi asistentą). 2024 m. Satya Nadella paskyrė jį visos „Microsoft AI“ padalinio vadovu. Bestsellerio „The Coming Wave“ autorius.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val cyan">Microsoft AI</div>
              <div class="wiki-stat-lbl">Generalinis direktorius</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">DeepMind</div>
              <div class="wiki-stat-lbl">Bendraįkūrėjas 2010 m.</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">The Coming Wave</div>
              <div class="wiki-stat-lbl">Bestselleris apie bangos sulaikymą</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">Copilot</div>
              <div class="wiki-stat-lbl">Milijardas vartotojų</div>
            </div>
          </div>

          <div class="wiki-quote-card cyan">
            <div class="wiki-quote-text">„Ateinanti banga atneš technologijas, kurios bus ir visagalės, ir visiškai decentralizuotos. Jų sulaikymas (containment) yra didžiausias ir svarbiausias egzaminas žmonijos istorijoje.“</div>
            <div class="wiki-quote-author">— Mustafa Suleyman, knyga „The Coming Wave“</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title cyan">🌊 Ateinančios bangos anatomija</div>
            </div>
            <div class="wiki-card-body">
              <p>Suleymanas savo knygoje „The Coming Wave“ aprašo dviejų jėgų – <strong>dirbtinio intelekto ir sintetinės biologijos</strong> – susijungimą. Anksčiau galingos technologijos (kaip branduoliniai ginklai) reikalavo urano sodrinimo gamyklų ir buvo lengvai stebimos. DI ir genų inžinerija plinta per nešiojamus kompiuterius ir atvirojo kodo bibliotekas, todėl jų kontrolė tampa beveik neįmanoma.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">🛑 10 žingsnių sulaikymo programa</div>
            </div>
            <div class="wiki-card-body">
              <p>Kaip Microsoft AI vadovas, Suleymanas siekia diegti griežtą techninį auditą: lustų sekimą per aparatūros šifrus, tarptautines vyriausybių inspekcijas duomenų centruose ir griežtus teisinius reikalavimus autonominiams agentams.</p>
            </div>
          </div>

          <div class="wiki-verdict-card cyan">
            <div class="wiki-card-header">
              <div class="wiki-card-title cyan">👁️ Suleymano verdiktas: Valstybės suirimas</div>
            </div>
            <div class="wiki-card-body">
              <p>„Jei mes nesugebėsime suvaldyti šios bangos, tradicinė nacionalinė valstybė praras smurto ir informacijos monopolį. Mus užlies automatizuota dezinformacija ir sintetiniai patogenai, o visuomenė subyrės į radikalias technofilų ir neoluditų grupuotes.“</p>
            </div>
          </div>
        """
    },
    "brett_adcock": {
        "title": "Brett Adcock",
        "en_title": "Brett Adcock (Founder & CEO Figure AI)",
        "category": "FIGURE AI ĮKŪRĖJAS • HUMANOIDŲ ROBOTIKOS VIZIONIERIUS",
        "badge_color": "amber",
        "summary": "Serijinis technologijų antrepreneris, įkūręs „Archer Aviation“ (elektriniai taksi lėktuvai) ir „Figure AI“. Jo tikslas – sukurti bendrosios paskirties humanoidinį robotą, pakeisiantį žmogaus rankų darbą visose pramonės šakose.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">Figure 02</div>
              <div class="wiki-stat-lbl">Antros kartos humanoidas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">BMW</div>
              <div class="wiki-stat-lbl">Reali gamykla Spartanburge</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">OpenAI</div>
              <div class="wiki-stat-lbl">Neuroninių kalbos smegenų partneris</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">2–3 $/val.</div>
              <div class="wiki-stat-lbl">Robotizuoto darbo savikaina</div>
            </div>
          </div>

          <div class="wiki-quote-card amber">
            <div class="wiki-quote-text">„Mes sukursime milijardus humanoidų. Tai bus didžiausia rinka žmonijos istorijoje, visiškai panaikinanti fizinio darbo trūkumą ir pakeisianti globalią gamybos grandinę.“</div>
            <div class="wiki-quote-author">— Brett Adcock, Figure AI pristatymo kalba</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">🤖 Figure 02 proveržis: BMW gamykla</div>
            </div>
            <div class="wiki-card-body">
              <p>Brettas Adcockas įrodė, kad humanoidai nebėra laboratorinis žaislas. 2024 m. jo sukurtas <strong>Figure 02</strong> pradėjo dirbti „BMW“ automobilių kėbulo surinkimo linijoje JAV: jis geba manipuliuoti lakštinio metalo detalėmis milimetro tikslumu, mokydamasis iš klaidų per neuroninius regos modelius.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🧠 OpenAI smegenys metaliniame kūne</div>
            </div>
            <div class="wiki-card-body">
              <p>Figure robotai turi įmontuotus OpenAI balso ir samprotavimo modelius. Vartotojas gali kalbėtis su robotu natūralia kalba, o robotas savarankiškai susiplanuoja judesių seką: pavyzdžiui, paprašius „pavalgyti“, robotas suranda obuolį, paduoda jį žmogui ir tuo pat metu surenka šiukšles nuo stalo.</p>
            </div>
          </div>

          <div class="wiki-verdict-card amber">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">📉 Fizinio darbo pabaiga: 2 doleriai už valandą</div>
            </div>
            <div class="wiki-card-body">
              <p>Adcocko skaičiavimai negailestingi: masinės gamybos humanoido eksploatacija kainuos vos 2–3 dolerius per valandą. Jis niekada nepavargsta, neprašo atostogų, nesuserga ir nedirba su profesinėmis sąjungomis. Tai reiškia totalią milijonų sandėlių, logistikos ir statybų darbuotojų pabaigą iki 2035 metų.</p>
            </div>
          </div>
        """
    },
    "alan_turing": {
        "title": "Alanas Turingas (Alan Turing)",
        "en_title": "Alan Turing (Father of Modern Computer Science & AI)",
        "category": "KOMPIUTERIJOS IR DI TĖVAS • BLETCHLEY PARK HEROJUS",
        "badge_color": "cyan",
        "summary": "Britų matematikas, kriptoanalitikas ir filosofas. 1936 m. suformulavo universalaus kompiuterio (Tiuringo mašinos) koncepciją, Antrojo pasaulinio karo metu nulaužė vokiečių „Enigma“ šifrą ir 1950 m. pasiūlė Tiuringo testą.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val cyan">14 mln.</div>
              <div class="wiki-stat-lbl">Išgelbėtų gyvybių per WW2</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">1936 m.</div>
              <div class="wiki-stat-lbl">Tiuringo mašinos gimimas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">1950 m.</div>
              <div class="wiki-stat-lbl">Tiuringo testas (Imitation Game)</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">1954 m.</div>
              <div class="wiki-stat-lbl">Tragiška žūtis nuo cianido</div>
            </div>
          </div>

          <div class="wiki-quote-card cyan">
            <div class="wiki-quote-text">„Gali kilti klausimas: ar mašinos kada nors mus pranoks? Manau, kad kai mašinų mąstymas prasidės, nepraeis daug laiko, kol jos paims kontrolę į savo rankas.“</div>
            <div class="wiki-quote-author">— Alan Turing, BBC radijo paskaita (1951 m. gegužės 15 d.)</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title cyan">🕵️ Enigma ir Bletchley Parkas: Šiuolaikinio pasaulio pradžia</div>
            </div>
            <div class="wiki-card-body">
              <p>Slaptame Bletchley Parko dvare Alanas Turingas sukonstravo „Bombe“ elektromechanines mašinas, kurios kasdien iššifruodavo Vokietijos povandeninių laivų ir karinių pajėgų Enigma pranešimus. Istorikai skaičiuoja, kad jo darbas sutrumpino Antrąjį pasaulinį karą bent dvejais metais ir išgelbėjo per 14 milijonų gyvybių.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🧪 Tiuringo testas ir jo mirtis 2024 metais</div>
            </div>
            <div class="wiki-card-body">
              <p>1950 m. straipsnyje „Computing Machinery and Intelligence“ Turingas pasiūlė „Mėgdžiojimo žaidimą“ (Imitation Game): jei žmogus teisėjas tekstiniame pokalbyje negali atskirti, ar bendrauja su mašina, ar su kitu žmogumi – mašina laikoma mąstančia.</p>
              <p>2024 m. didieji kalbos modeliai (GPT-4, Claude 3.5) šį testą išlaikė taip lengvai, kad testas tapo atgyvena – dabar ieškoma testų, vertinančių autonominį samprotavimą ir mokslinį kūrybiškumą.</p>
            </div>
          </div>

          <div class="wiki-verdict-card crimson">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">💔 Didžioji civilizacijos gėda: Apnuodytas obuolys</div>
            </div>
            <div class="wiki-card-body">
              <p>Nepaisant milžiniškų nuopelnų tėvynei, 1952 m. Britanijos teismas nuteisė Turingą už homoseksualumą ir privertė pasirinkti kalėjimą arba cheminę kastraciją hormonais. 1954 m. birželio 7 d. jis rastas negyvas šalia perpjauto obuolio, įmirkyto cianide. Tik 2013 m. karalienė Elžbieta II oficialiai jį reabilitavo po mirties.</p>
            </div>
          </div>
        """
    },
    "karpathy_software": {
        "title": "Andrej Karpathy & Software 3.0",
        "en_title": "Andrej Karpathy (Former Director of AI Tesla, OpenAI Co-founder)",
        "category": "TESLA DI VADOVAS • SOFTWARE 3.0 ARCHITEKTAS",
        "badge_color": "emerald",
        "summary": "Slovakų kilmės mokslininkas, Stanfordo universiteto giliojo mokymosi kurso CS231n autorius, buvęs „Tesla Autopilot“ AI direktorius ir vienas pirmųjų „OpenAI“ tyrėjų. Dabar kuria „Eureka Labs“.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">Software 3.0</div>
              <div class="wiki-stat-lbl">Programavimo evoliucija</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">Tesla FSD</div>
              <div class="wiki-stat-lbl">Autopilot regos architektas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">Stanford CS231n</div>
              <div class="wiki-stat-lbl">Legendinis kompiuterinės regos kursas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">Eureka Labs</div>
              <div class="wiki-stat-lbl">DI švietimo platforma</div>
            </div>
          </div>

          <div class="wiki-quote-card emerald">
            <div class="wiki-quote-text">„Karščiausia nauja programavimo kalba pasaulyje yra anglų kalba. Niekas neberašys kodo rankomis – kodą dabar optimizuoja gradientinis nusileidimas neuroniniuose svoriuose.“</div>
            <div class="wiki-quote-author">— Andrej Karpathy</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">💻 Programavimo evoliucija: Nuo 1.0 iki 3.0</div>
            </div>
            <div class="wiki-card-body">
              <p>Karpathy suformulavo epochinį programinės įrangos poslinkį:</p>
              <ul>
                <li><strong>Software 1.0</strong>: Žmogus rašo taisykles rankomis (C++, Python, Java). Tikslus, bet trapus kodas.</li>
                <li><strong>Software 2.0</strong>: Žmogus surenka duomenis, o neuroninis tinklas suranda svorius (Deep Learning). Mašina atpažįsta vaizdus ir kalbą.</li>
                <li><strong>Software 3.0</strong>: Žmogus duoda instrukciją natūralia kalba, o didieji modeliai ir autonominiai agentai patys sukuria visą sistemą, ją pratestuoja ir paleidžia.</li>
              </ul>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">🚗 Tesla Full Self-Driving drama: Grynoji rega</div>
            </div>
            <div class="wiki-card-body">
              <p>Dirbdamas „Tesla“, Karpathy įtikino Eloną Muską atsisakyti brangių LiDAR jutiklių ir radarų. Jo argumentas buvo paprastas: „Žmonės vairuoja naudodami tik dvi akis ir biologines smegenis. Jei mašina turi 8 vaizdo kameras ir galingą neuroninį tinklą, ji privalo vairuoti geriau už žmogų vien iš vaizdo taškų.“</p>
            </div>
          </div>

          <div class="wiki-verdict-card emerald">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🎓 Švietimo revoliucija su Eureka Labs</div>
            </div>
            <div class="wiki-card-body">
              <p>Išėjęs iš OpenAI antrą kartą, Karpathy įkūrė „Eureka Labs“. Jo vizija – asmeninis AI mokytojas kiekvienam Žemės vaikui: algoritmas, turintis visos žmonijos žinias, pritaikantis dėstymo tempą prie mokinio kognityvinių savybių.</p>
            </div>
          </div>
        """
    }
}

if __name__ == "__main__":
    print(f"Bespoke Titans Data sugeneruota: {len(TITANS_DATA)} irasu.")
