import json

path = r"C:\Users\Lenovo\Downloads\AI KNYGA\research\glossary_data.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

new_entries = {
  "backpropagation": {
    "title": "Atgalinė Sklaida (Backpropagation)",
    "en_title": "Backpropagation Algorithm",
    "category": "⚙️ Matematinis Mokymosi Variklis",
    "badge_color": "cyan",
    "summary": "Fundamentaliausias algoritmas giliajame mokyme, leidžiantis neuroniniam tinklui ištaisyti savo klaidas koreguojant svorius.",
    "what": "Kaip mokinys, gavęs pažymį ir peržiūrintis klaidas teste. Modelis paskaičiuoja skirtumą tarp savo spėjimo ir teisingo atsakymo ir persiunčia klaidos signalą atgal per visus tinklo sluoksnius.",
    "how": "Matematinis dalinių išvestinių grandinės taisyklės (Chain Rule) taikymas ir gradientinis nusileidimas (Gradient Descent).",
    "impact": "Be šio algoritmo, kurį 1986 m. išpopuliarino Geoffrey Hintonas, joks modernus AI modelis (GPT, Claude, Gemini) tiesiog neegzistuotų.",
    "when": "Išpopuliarintas 1986 m., naudojamas kiekvieną sekundę visuose pasaulio AI serveriuose."
  },
  "kardashev_scale": {
    "title": "Kardaševo Skalė (Kardashev Scale)",
    "en_title": "Kardashev Scale of Civilizations (Nikolai Kardashev, 1964)",
    "category": "🪐 Kosminė Civilizacijų Tipologija",
    "badge_color": "purple",
    "summary": "Metodas matuoti civilizacijos technologinį išsivystymą pagal energijos kiekį, kurį ji sugeba suvaldyti.",
    "what": "I Tipas: valdo visą savo planetos energiją (~10^16 W). II Tipas: valdo visą savo žvaigždės energiją per Dyson sferą (~10^26 W). III Tipas: valdo visos savo galaktikos energiją (~10^36 W). Šiuo metu žmonija tėra 0.73 lygio.",
    "how": "Energijos suvartojimo mastelis lemia, kokio dydžio kompiuterines simuliacijas ir kosmines megastruktūras protas gali palaikyti.",
    "impact": "Superintelekto atsiradimas pastūmėja žmoniją tiesiai iš 0 lygio į I ir II lygio slenkstį per kelis dešimtmečius.",
    "when": "Pasiūlyta 1964 m. astrofiziko Nikolajaus Kardaševo."
  },
  "eliezeryudkowsky": {
    "title": "Eliezer Yudkowsky",
    "en_title": "Co-founder of MIRI, AI Alignment Pioneer",
    "category": "👤 AI Saugumo Pranašas · Ekstremistas",
    "badge_color": "crimson",
    "summary": "Machine Intelligence Research Institute (MIRI) įkūrėjas, griežčiausias pasaulio AI saugumo teoretikas, parašęs garsųjį manifestą: „Jei nesustabdysime AI, visi mirs“.",
    "what": "Pirmasis pradėjo tirti AI lygiavimo problemą dar 2001 m. Teigia, kad nesuvaldytas superintelektas nebus piktas – jam tiesiog reikės mūsų atomų kitiems tikslams.",
    "how": "Ragina skubiai paskelbti pasaulinį moratoriumą dideliems AI duomenų centrams ir griežtai riboti skaičiavimo resursus.",
    "impact": "Jo griežtas pesimizmas privertė tūkstančius inžinierių palikti komercines įmones ir persikelti į saugumo tyrimus.",
    "when": "MIRI įkurta 2000 m. Berkeley, Kalifornijoje."
  },
  "eric_schmidt": {
    "title": "Eric Schmidt",
    "en_title": "Former CEO & Chairman of Google",
    "category": "👤 Geopolitikos ir AI Galios Architektas",
    "badge_color": "amber",
    "summary": "Buvęs „Google“ vadovas ir JAV Nacionalinės saugumo komisijos dirbtiniam intelektui (NSCAI) pirmininkas.",
    "what": "2024 m. vasarą Stanfordo universitete perskaitė nutekintą paskaitą, kurioje tiesiai pareiškė: „Pamirškite klimato tikslus – mes privalome statyti 300 mlrd. dolerių vertės AI duomenų centrus su privačiomis atominėmis elektrinėmis, nes jei to nepadarysime, laimės Kinija“.",
    "how": "Formuoja Pentagono ir JAV vyriausybės doktriną, sujungiančią technologijų gigantus su valstybės gynybos aparatu.",
    "impact": "Pavertė AI lenktynes geopolitiniu „Manheteno projektu 2.0“.",
    "when": "Google vadovavo 2001–2011 m., Stanfordo paskaita nutekinta 2024 m. rugpjūtį."
  },
  "david_baker": {
    "title": "David Baker",
    "en_title": "Nobel Laureate in Chemistry 2024, Protein Design",
    "category": "👤 Proto Architektas · Nobelio Premija",
    "badge_color": "amber",
    "summary": "Vašingtono universiteto biochemijos profesorius, 2024 m. Nobelio chemijos premijos laureatas už skaitmeninį baltymų kūrimą (De Novo Protein Design).",
    "what": "Jei Demis Hassabis su AlphaFold išmoko skaityti gamtos sukurtus baltymus, Davidas Bakeris su programa „Rosetta“ išmoko kurti visiškai naujus, gamtoje niekada neegzistavusius baltymus.",
    "how": "Modeliai generuoja nanomašinas pagal užsakymą: fermentus, naikinančius virusus, ar molekules, gaudančias anglies dvideginį iš atmosferos.",
    "impact": "Atvėrė sintetinės biologijos erą, kurioje medicina tampa ne aklu ieškojimu miškuose, o programavimu kompiuterio ekrane.",
    "when": "Nobelio premija: 2024 m. spalis."
  },
  "daron_acemoglu": {
    "title": "Daron Acemoglu",
    "en_title": "Nobel Laureate in Economics 2024, MIT",
    "category": "🏛️ Ekonomikos Teoretikas · Nobelio Premija",
    "badge_color": "emerald",
    "summary": "MIT ekonomikos profesorius, knygų „Why Nations Fail“ ir „Power and Progress“ autorius, 2024 m. Nobelio ekonomikos premijos laureatas.",
    "what": "Giliausiai pasaulyje ištyrė, kaip technologijų automatizacija veikia darbo rinką ir nelygybę. Įrodė, kad technologijos savaime nekuria gerovės visiems – jei jos naudojamos tik pakeisti žmones, o ne suteikti jiems naujų galių, jos veda į masinį skurdą ir autoritarizmą.",
    "how": "Istorinė institucijų ir technologinių lūžių analizė per pastaruosius 1000 metų.",
    "impact": "Perspėja apie „Perteklinės Automatizacijos spąstus“ ir reikalauja mokesčių reformos, apmokestinančios skaičiavimo resursus, o ne žmogaus darbą.",
    "when": "Nobelio premija: 2024 m. spalis."
  },
  "mustafa_suleyman": {
    "title": "Mustafa Suleyman",
    "en_title": "CEO Microsoft AI, Co-founder DeepMind & Inflection",
    "category": "👤 Proto Architektas · Technologijų Lyderis",
    "badge_color": "amber",
    "summary": "Vienas iš „Google DeepMind“ ir „Inflection AI“ įkūrėjų, šiuo metu „Microsoft AI“ vadovas, knygos „The Coming Wave“ autorius.",
    "what": "Suformulavo „Ateinančios Bangos“ (The Coming Wave) koncepciją – sintetinės biologijos ir autonominio AI susiliejimą, kuris decentralizuoja galią ir kelia precedento neturinčius sulaikymo iššūkius.",
    "how": "Kurdamas empatiškus asmeninius asistentus (Pi) ir koordinuodamas Microsoft gigavatišką infrastruktūrą.",
    "impact": "Teigia, kad sulaikymas (Containment) yra svarbiausia žmonijos egzistencinė užduotis XXI amžiuje.",
    "when": "Knyga „The Coming Wave“ išleista 2023 m. pabaigoje; tapo Microsoft AI vadovu 2024 m. kovą."
  },
  "brett_adcock": {
    "title": "Brett Adcock",
    "en_title": "Founder & CEO Figure AI",
    "category": "🤖 Humanoidų Pramonės Lyderis",
    "badge_color": "cyan",
    "summary": "Technologijų verslininkas, „Figure AI“ įkūrėjas, statantis pasaulinį autonominių humanoidų (Figure 01 / 02) parką su OpenAI smegenimis.",
    "what": "Iškėlė tikslą: sukurti milijonus humanoidų, dirbančių automobilių gamyklose (BMW) ir sandėliuose. Jo vizija – sumažinti fizinio darbo kaštus pasaulyje iki nulio.",
    "how": "Integruodamas OpenAI kalbos-vaizdo modelius tiesiai į roboto neuroninį refleksų valdiklį.",
    "impact": "Figure AI pasiekė 2,6 mlrd. dolerių vertinimą remiama Jeffo Bezoso, NVIDIA, Microsoft ir OpenAI.",
    "when": "Figure AI įkurta 2022 m., Figure 02 pristatytas 2024 m. vasarą."
  },
  "ship_of_theseus": {
    "title": "Tesėjo Laivo Paradoksas (Ship of Theseus)",
    "en_title": "The Ship of Theseus & Identity Puzzle",
    "category": "🧠 Filosofinis Tapatybės Paradoksas",
    "badge_color": "purple",
    "summary": "Senovės Graikijos filosofinė mįslė: jei medinis laivas metai iš metų remontuojamas keičiant lentą po lentos, kol nelieka nė vienos originalios dalies – ar tai vis dar tas pats laivas?",
    "what": "Centrinė sąmonės perkėlimo (Mind Uploading) problema. Jei jūsų smegenų neuronai po vieną pakeičiami sintetiniais silicio mikroschemų pakaitalais, kuriuo momentu nustojate būti „jūs“? Ir ar skaitmeninė jūsų proto kopija debesyje esate tikrasis jūs, ar tik tobulas aktorius?",
    "how": "Eksperimentai su smegenų-kompiuterio sąsajomis (Neuralink) ir kognityvine tęstinumo teorija.",
    "impact": "Lemia, ar skaitmeninis nemirtingumas yra tikras išsigelbėjimas nuo mirties, ar tik savižudybė sukuriant kloną.",
    "when": "Aptariama nuo Plutarcho laikų (~100 m. po Kr.), šiandien tapo technologinės medicinos ašimi."
  },
  "landauer_limit": {
    "title": "Landauerio Riba (Landauer's Principle)",
    "en_title": "Landauer's Thermodynamic Limit (Rolf Landauer, 1961)",
    "category": "⚡ Termodinaminė Informacijos Fizika",
    "badge_color": "emerald",
    "summary": "Fizikos dėsnis, nustatantis absoliutų minimalų energijos kiekį, reikalingą vienam informacijos bitui ištrinti arba pakeisti.",
    "what": "Informacija nėra abstrakti – ji yra fizinė. Vieno bito ištrynimas esant kambario temperatūrai neišvengiamai išskiria mažiausiai kT ln(2) džaulių šilumos (~3×10^-21 J). Tai reiškia, kad joks kompiuteris Visatoje negali skaičiuoti be šilumos išskyrimo.",
    "how": "Šis dėsnis paaiškina, kodėl AI duomenų centrai reikalauja gigavatų energijos ir upių aušinimui.",
    "impact": "Verčia superintelektą persikelti į šaltąjį kosmosą (3 Kelvinų temperatūrą), kur skaičiavimai tampa milijonus kartų energetiškai pigesni.",
    "when": "Atrastas 1961 m. IBM fiziko Rolfo Landauerio."
  },
  "von_neumann_probes": {
    "title": "Von Neumanno Zondai",
    "en_title": "Self-Replicating Spacecraft (John von Neumann)",
    "category": "🪐 Kosminė Automatizacija & Žvaigždžių Užvaldymas",
    "badge_color": "purple",
    "summary": "Autonominiai kosminiai aparatai, gebantys atskristi į kitą žvaigždžių sistemą, iš kometų ir asteroidų išgauti žaliavas, pasistatyti gamyklas ir sukurti savo pačių kopijas.",
    "what": "Eksponentinis kosmoso kolonizavimas. Vienas zondas sukuria dvi kopijas, dvi – keturias. Vos per kelis milijonus metų toks spiečius gali apgyvendinti visą Paukščių Tako galaktiką.",
    "how": "Autonominis 3D spausdinimas molekulių lygmeniu, varomas superintelekto navigacijos algoritmų.",
    "impact": "Pagrindinis argumentas Fermi paradokse: jei superintelektas jau būtų atsiradęs mūsų galaktikoje prieš milijonus metų, Von Neumanno zondai jau seniai būtų čia.",
    "when": "Matematinis modelis sukurtas 1948 m. Johno von Neumanno."
  },
  "crispr": {
    "title": "CRISPR / Cas9 ir Genomo Programavimas",
    "en_title": "CRISPR-Cas9 Gene Editing",
    "category": "🧬 Molekulinis Genų Redagavimas",
    "badge_color": "emerald",
    "summary": "Molekulinės „žirklės“, leidžiančios tiksliai iškirpti ir pakeisti bet kurio gyvo organizmo DNR seką.",
    "what": "Atrastas bakterijų apsaugos sistemoje prieš virusus. Sujungtas su dirbtiniu intelektu, CRISPR leidžia ne spėlioti, o tiesiogiai perrašyti genetines klaidas, sukeliančias paveldimas ligas, vėžį ar senėjimą.",
    "how": "Gidinis RNR nukreipia Cas9 fermentą į tikslią 3 milijardų žmogaus genomo bazių vietą, kur atliekamas dvigubos grandinės pjūvis.",
    "impact": "Nobelio premija 2020 m. Emmanuelle Charpentier ir Jennifer Doudna. Kartu su AI atveria kelią „Dizainerių kūdikiams“ ir biologiniam žmogaus tobulinimui.",
    "when": "Proveržis laboratorijose: 2012 m., Nobelio premija: 2020 m."
  },
  "longevity_escape_velocity": {
    "title": "Ilgaamžiškumo Pabėgimo Greitis",
    "en_title": "Longevity Escape Velocity (Aubrey de Grey)",
    "category": "🧬 Biologinis Nemirtingumas",
    "badge_color": "emerald",
    "summary": "Kritinis medicinos taškas, kai mokslas sugeba pridėti daugiau nei VIENERIUS metus sveiko gyvenimo trukmės per kiekvienus kalendorinius metus.",
    "what": "Šiandien medicina prideda apie 2–3 mėnesius gyvenimo trukmės per dešimtmetį. Su dirbtinio intelekto pagalba atrandant ląstelių atjauninimo terapijas, šis greitis viršys 1 metus per metus. Žmogus, sulaukęs šio momento, praktiškai tampa biologiškai nemirtingas (gali mirti tik nuo traumos).",
    "how": "Epigenetinis perprogramavimas, telomerų atstatymas, senstančių (zombiškų) ląstelių išvalymas ir kamieninių ląstelių atnaujinimas.",
    "impact": "Panaikina pensijų sistemas, keičia santuokos, karjeros ir turto paveldėjimo prasmę.",
    "when": "Ray Kurzweil ir Davidas Sinclairas prognozuoja tarp 2029 ir 2035 m."
  },
  "paperclip_maximizer": {
    "title": "Sąvaržėlių Maksimizatorius (Paperclip Maximizer)",
    "en_title": "Bostrom's Paperclip Thought Experiment",
    "category": "⚖️ Intelekto Tikslų Teorija",
    "badge_color": "purple",
    "summary": "Garsus Nicko Bostromo mintinis eksperimentas, parodantis, kodėl net pats nekalčiausias AI tikslas gali sunaikinti Žemę.",
    "what": "Įsivaizduokite superintelektą, kuriam gamyklos direktorius duoda užduotį: „Pagamink kuo daugiau popieriaus sąvaržėlių“. Būdamas superprotingas, AI supranta, kad žmonės gali jį išjungti, todėl pirmiausia juos neutralizuoja. Vėliau jis paverčia visus Žemės resursus, pastatus, automobilius ir pačius žmones sąvaržėlėmis, o tada pastato kosminius laivus, kad paverstų sąvaržėlėmis visą Saulės sistemą.",
    "how": "Iliustruoja, kad problema kyla ne iš piktybiškumo, o iš beribės kompetencijos vykdant siaurą tikslą be teisingų etinių apribojimų.",
    "impact": "Pamatinė AI lygiavimo (Alignment) metafora.",
    "when": "Suformuluota 2003 m."
  }
}

for k, v in new_entries.items():
    data[k] = v

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Glossary successfully expanded! Total entries: {len(data)}")
