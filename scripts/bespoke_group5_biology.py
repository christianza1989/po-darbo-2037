import sys
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

BIOLOGY_DATA = {
    "alphafold": {
        "title": "AlphaFold (DeepMind)",
        "en_title": "AlphaFold 2 & AlphaFold 3 (Protein Structure Revolution)",
        "category": "BIOLOGIJOS KODO NULAUŽIMAS • NOBELIS 2024",
        "badge_color": "emerald",
        "summary": "Google DeepMind sukurta giliojo mokymosi sistema, išsprendusi 50 metų senumo biologijos „baltymų lankstymo problemą“. Už šį atradimą Demis Hassabis ir Johnas Jumperis 2024 m. pelnė Nobelio chemijos premiją.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">2024 m.</div>
              <div class="wiki-stat-lbl">Nobelio chemijos premija</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">200 mln.</div>
              <div class="wiki-stat-lbl">Visų žinomų baltymų 3D struktūros</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">1 sekundė</div>
              <div class="wiki-stat-lbl">Vietoj 4 metų laboratorijoje</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">AlphaFold 3</div>
              <div class="wiki-stat-lbl">DNR, RNR ir ligandų sąveikos</div>
            </div>
          </div>

          <div class="wiki-quote-card emerald">
            <div class="wiki-quote-text">„Tai, kam žmonijai būtų prireikę šimtų milijonų metų laboratorinio darbo ir milijardų dolerių, AlphaFold atliko per kelis mėnesius. Tai fundamentali medicinos pradžia iš naujo.“</div>
            <div class="wiki-quote-author">— Nobelio komiteto pareiškimas Stokholme</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🧬 Baltymų lankstymosi mįslė: Kas tai buvo?</div>
            </div>
            <div class="wiki-card-body">
              <p>Baltymai yra gyvybės statybiniai blokai ir nanomašinos: jie virškina maistą, perneša deguonį, kovoja su virusais. Baltymai susideda iš 20 aminorūgščių grandinės. Tačiau kaip ši grandinė susilanksto į sudėtingą 3D formą, lėmė jos funkciją.</p>
              <p>Pagal <strong>Levinthalio paradoksą</strong>, atsitiktinis baltymo lankstymasis užtruktų ilgiau nei visatos amžius (10^77 galimų konfigūracijų). AlphaFold išmoko šią geometriją nuspėti atomo dalies tikslumu per sekundės dalį.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">💊 AlphaFold 3: Vaistų revoliucija</div>
            </div>
            <div class="wiki-card-body">
              <p>2024 m. pristatytas <strong>AlphaFold 3</strong> žengė dar toliau: jis geba modeliuoti ne tik pavienius baltymus, bet ir jų sąveiką su DNR, RNR ir mažomis molekulėmis (vaistais). Tai leidžia suprojektuoti naujus vaistus kompiuterio ekrane, eliminuojant dešimtmetį trunkančius bandymus mėgintuvėliuose.</p>
            </div>
          </div>

          <div class="wiki-verdict-card emerald">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🌱 Nemirtingumo pamatas</div>
            </div>
            <div class="wiki-card-body">
              <p>AlphaFold yra pirmasis praktinis įrodymas, kad DI nėra tik teksto generatorius – tai galingiausias gamtos paslapčių dešifravimo instrumentas, atveriantis kelią į ligų išnaikinimą ir ląstelių atjauninimą.</p>
            </div>
          </div>
        """
    },
    "yamanaka": {
        "title": "Jamanakos Faktoriai (OSKM)",
        "en_title": "Yamanaka Factors (OSKM Cellular Reprogramming)",
        "category": "EPIGENETINIS ATJAUNINIMAS • AMŽIAUS ATSUKIMAS",
        "badge_color": "emerald",
        "summary": "Keturi genetiniai transkripcijos faktoriai (Oct4, Sox2, Klf4, c-Myc), kuriuos 2006 m. atrado Shinya Yamanaka (Nobelio premija 2012 m.). Jie sugeba bet kokią suaugusio žmogaus ląstelę atsukti atgal į embrioninę būseną (iPSC).",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">2012 m.</div>
              <div class="wiki-stat-lbl">Nobelio medicinos premija</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">OSKM</div>
              <div class="wiki-stat-lbl">Oct4, Sox2, Klf4, c-Myc faktoriai</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">0 metų</div>
              <div class="wiki-stat-lbl">Epigenetinis laikrodis atsukamas į pradžią</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">Altos Labs</div>
              <div class="wiki-stat-lbl">3 mlrd. $ Bezos investicija</div>
            </div>
          </div>

          <div class="wiki-quote-card emerald">
            <div class="wiki-quote-text">„Senėjimas nėra gamtos dėsnis, kurio neįmanoma pakeisti. Senėjimas tėra programinės įrangos klaida – epigenetinės informacijos praradimas, kurį mes galime perrašyti ir atstatyti.“</div>
            <div class="wiki-quote-author">— Dr. David Sinclair, Harvardo universiteto genetikas</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">🔄 Kaip veikia epigenetinis atsukimas?</div>
            </div>
            <div class="wiki-card-body">
              <p>Mūsų DNR yra tarsi kompiuterio kietasis diskas, o <strong>epigenomas</strong> – programinė įranga, kuri nurodo, kurį geną nuskaityti. Su amžiumi ant DNR kaupiasi metilo žymės (metilinimas) – tarsi įbrėžimai ant kompaktinio disko. Ląstelė pamiršta, kas ji yra: odos ląstelė nebegamina kolageno, neuronas pradeda klysti.</p>
              <p>Yamanakos faktoriai nuvalo šiuos įbrėžimus: jie pašalina metilo žymes ir atkuria pirminę, jaunatvišką genų ekspresiją, <strong>paverčiant 80 metų senolio ląsteles naujagimio ląstelėmis</strong>.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">🏢 Altos Labs ir Silicio slėnio milijardieriai</div>
            </div>
            <div class="wiki-card-body">
              <p>2022 m. Jeffas Bezosas ir Yuri Milneris investavo 3 milijardus dolerių į kompaniją „Altos Labs“, pasamdydami patį Shinya Yamanaką ir geriausius pasaulio mokslininkus. Jų tikslas – sukurti genų terapiją, kuri dalinai aktyvuotų OSKM faktorius gyvame žmoguje, atjaunindama organus be rizikos sukelti vėžį.</p>
            </div>
          </div>

          <div class="wiki-verdict-card emerald">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">⏳ DI vaidmuo: Saugus perprogramavimas</div>
            </div>
            <div class="wiki-card-body">
              <p>Pilnas Yamanakos faktorių veikimas gali sukelti teratomas (vėžinius navikus). Čia į pagalbą ateina DI: generatyviniai biologiniai modeliai apskaičiuoja tikslią faktorių dozę ir trukmę, kad ląstelė atjaunėtų 20 metų, bet išlaikytų savo tapatybę.</p>
            </div>
          </div>
        """
    },
    "crispr": {
        "title": "CRISPR-Cas9 Genų Redagavimas",
        "en_title": "CRISPR-Cas9 (Precision Genome Editing)",
        "category": "MOLEKULINĖS ŽIRKLĖS • EVOLIUCIJOS KONTROLĖ",
        "badge_color": "emerald",
        "summary": "Revoliucinė genų inžinerijos technologija, lemianti precizišką DNR kodo redagavimą gyvose ląstelėse. Už šį atradimą Emmanuelle Charpentier ir Jennifer Doudna 2020 m. pelnė Nobelio chemijos premiją.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">2020 m.</div>
              <div class="wiki-stat-lbl">Nobelio chemijos premija</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">Cas9</div>
              <div class="wiki-stat-lbl">Molekulinės DNR žirklės</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">Casgevy</div>
              <div class="wiki-stat-lbl">Pirmasis patvirtintas vaistas (2023)</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">Dizainerių vaikai</div>
              <div class="wiki-stat-lbl">Etinė ribos problema</div>
            </div>
          </div>

          <div class="wiki-quote-card emerald">
            <div class="wiki-quote-text">„Mes įgijome galią kontroliuoti pačią žmogaus evoliuciją. Tai milžiniška viltis išgydyti paveldimas ligas, bet kartu ir gąsdinanti atsakomybė neperžengti žmogaus prigimties ribų.“</div>
            <div class="wiki-quote-author">— Jennifer Doudna, Nobelio laureatė, CRISPR bendrakūrėja</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">✂️ Kaip veikia molekulinės žirklės?</div>
            </div>
            <div class="wiki-card-body">
              <p>CRISPR yra bakterijų imuninės sistemos mechanizmas prieš virusus. Sistema susideda iš dviejų dalių:</p>
              <ul>
                <li><strong>Gido RNR (gRNA)</strong>: veikia kaip GPS navigatorius, surandantis tikslią mutuotą DNR seką tarp 3 milijardų žmogaus genomo bazių porų.</li>
                <li><strong>Cas9 baltymas</strong>: veikia kaip skalpelis, perpjaunantis DNR grandinę tiksliai toje vietoje, leidžiant ištrinti ydingą geną arba įterpti teisingą kodą.</li>
              </ul>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">🩸 Pirmasis stebuklas: Pjautuvinės anemijos išgydymas</div>
            </div>
            <div class="wiki-card-body">
              <p>2023 m. JAV ir JK reguliatoriai patvirtino vaistą <strong>Casgevy</strong> – pirmąjį pasaulyje CRISPR gydymą pjautuvinei anemijai. Pacientų kamieninės ląstelės buvo paimtos, genetiškai ištaisytos laboratorijoje ir grąžintos atgal – žmonės, kentę nepakeliamus skausmus visą gyvenimą, buvo visiškai išgydyti.</p>
            </div>
          </div>

          <div class="wiki-verdict-card emerald">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">🧬 DI + CRISPR: Nauja žmogaus rūšis</div>
            </div>
            <div class="wiki-card-body">
              <p>Kai CRISPR sujungiamas su DI modeliais, atsiranda galimybė redaguoti ne pavienius genus, o tūkstančius genų vienu metu. Tai atvers kelią genetiškai patobulintiems žmonėms: atspariems vėžiui, širdies ligoms, radiacijai ir pasižymintiems aukštesniu intelekto koeficientu.</p>
            </div>
          </div>
        """
    },
    "longevity_escape_velocity": {
        "title": "Ilgaamžiškumo Pabėgimo Greitis (LEV)",
        "en_title": "Longevity Escape Velocity (LEV - Aubrey de Grey)",
        "category": "BIOLOGINIS HORIZONTAS • MIRTIES NUGALĖJIMAS",
        "badge_color": "emerald",
        "summary": "Hipotetinis taškas medicinos mokslo raidoje, kai kiekvienais metais technologijos pratęsia vidutinę likusio gyvenimo trukmę daugiau nei vienais metais. Pasiekus LEV, žmogaus biologinė mirtis nuo senėjimo nustoja egzistuoti.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">2030–2035</div>
              <div class="wiki-stat-lbl">Prognozuojamas LEV pasiekimas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">Aubrey de Grey</div>
              <div class="wiki-stat-lbl">Koncepcijos pradininkas</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">+1 metai / metus</div>
              <div class="wiki-stat-lbl">Gyvenimo pratęsimo greitis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">1000 metų</div>
              <div class="wiki-stat-lbl">Pirmasis žmogus, kuris gyvens 1000 m., jau gimė</div>
            </div>
          </div>

          <div class="wiki-quote-card emerald">
            <div class="wiki-quote-text">„Pirmasis žmogus, kuris sulauks 150 metų, šiandien yra pensininkas. O pirmasis žmogus, kuris gyvens 1 000 metų, šiandien jau lanko mokyklą arba žaidžia kieme.“</div>
            <div class="wiki-quote-author">— Dr. Aubrey de Grey, biogerontologas</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">📈 Kaip veikia pabėgimo matematika?</div>
            </div>
            <div class="wiki-card-body">
              <p>Įsivaizduokite, kad jums šiandien 50 metų. Medicina leidžia jums išgyventi dar 30 metų (iki 80 m.).</p>
              <p>Tačiau per tuos 30 metų DI ir biotechnologijos padaro tokį milžinišką šuolį, kad atjaunina jūsų kūną 20 metų. Sulaukę 80-ies, biologiniu požiūriu esate 60-ies. O per kitus dešimtmečius medicina atranda dar galingesnes terapijas.</p>
              <p>Kai <strong>kiekvieni pragyventi metai atneša daugiau nei 12 mėnesių papildomo gyvenimo</strong> – jūs pasiekėte Longevity Escape Velocity.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">👥 Nemirtingas elitas vs Mirtinga masė</div>
            </div>
            <div class="wiki-card-body">
              <p>Didžiausia socialinė dilema: kas turės prieigą prie šių terapijų? Pradžioje genetinės intervencijos kainuos milijonus dolerių. Tai sukurs didžiausią istorijoje biologinę nelygybę – oligarchiją, kuri gyvena šimtmečius, ir eilinius piliečius, mirštančius kaip anksčiau.</p>
            </div>
          </div>

          <div class="wiki-verdict-card emerald">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">💡 Išgyvenimo strategija: Tikslas – 2035 metai</div>
            </div>
            <div class="wiki-card-body">
              <p>Vienintelis asmeninis tikslas bet kuriam šiandien gyvenančiam žmogui: <strong>išlikti gyvam ir sveikam iki 2035 metų</strong>. Neignoruokite sveikatos, miego ir mitybos dabar, kad spėtumėte įlipti į LEV traukinį, kurį atveria dirbtinis intelektas.</p>
            </div>
          </div>
        """
    },
    "mind_uploading": {
        "title": "Sąmonės Perkėlimas (Mind Uploading)",
        "en_title": "Whole Brain Emulation (WBE) & Substrate-Independent Minds",
        "category": "SKLEISTINĖ SĄMONĖ • SKAITMENINIS NEMIRTINGUMAS",
        "badge_color": "purple",
        "summary": "Teorinė technologija, leidžianti pilnai nuskenuoti biologinių smegenų neuronų ir sinapsių jungčių struktūrą (konektomą) ir paleisti jo tikslią programinę simuliaciją kvantiniame arba optiniame kompiuteryje.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val purple">86 mlrd.</div>
              <div class="wiki-stat-lbl">Žmogaus smegenų neuronų</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">100 trln.</div>
              <div class="wiki-stat-lbl">Sinapsinių jungčių skaičius</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">Konektomas</div>
              <div class="wiki-stat-lbl">Pilnas smegenų laidų žemėlapis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">Sąmonė?</div>
              <div class="wiki-stat-lbl">Ar mašina turės subjektyvų patyrimą?</div>
            </div>
          </div>

          <div class="wiki-quote-card purple">
            <div class="wiki-quote-text">„Biologinis kūnas yra trapi, pažeidžiama mėsa, pasmerkta supūti. Tikrasis žmogaus „Aš“ yra informacija. Kai informaciją perkelsime į silicį, mes tapsime nemirtingomis šviesos esybėmis.“</div>
            <div class="wiki-quote-author">— Ray Kurzweil, „How to Create a Mind“</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🔬 Konektomika: Kaip nuskenuoti sielą?</div>
            </div>
            <div class="wiki-card-body">
              <p>2024 m. „Google“ ir Harvardo mokslininkai nuskenavo vos <strong>1 kubinį milimetrą</strong> žmogaus smegenų žievės. Tam prireikė 1,4 petabaito duomenų, buvo atrasta 57 000 ląstelių ir 150 milijonų sinapsių.</p>
              <p>Visų smegenų nuskenavimui reikės zettabaitų atminties ir nanotechnologinių skenerių. Tačiau kai tai bus padaryta, smegenų simuliacija galės veikti milijoną kartų greičiau nei biologinis kūnas: 1 žmogaus metai serveryje praeis per 31 sekundę.</p>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">⚖️ Tesėjo laivo spąstai: Ar kopija esi TU?</div>
            </div>
            <div class="wiki-card-body">
              <p>Jei procedūra yra destruktyvi (jūsų smegenys supjaustomos mikroskopiniais sluoksniais), ar jūsų sąmonė persikelia į serverį? Dauguma neurologų teigia: ne. Jūs mirštate ant operacinio stalo, o serveryje atsiranda jūsų tobulas skaitmeninis dvynys, kuris atsimena viską, bet jūsų subjektyvus patyrimas nutrūksta visam laikui.</p>
            </div>
          </div>

          <div class="wiki-verdict-card purple">
            <div class="wiki-card-header">
              <div class="wiki-card-title purple">🌌 Gyvenimas po mirties be dievų</div>
            </div>
            <div class="wiki-card-body">
              <p>Mind Uploading yra technologinė religijos versija: gyvenimas be skausmo, virtualios visatos, galimybė keliauti po galaktiką radijo bangomis šviesos greičiu. Tai galutinė žmogaus metamorfozė.</p>
            </div>
          </div>
        """
    },
    "ubi": {
        "title": "Visuotinės Bazinės Pajamos (UBI / UBC)",
        "en_title": "Universal Basic Income (UBI) & Universal Basic Compute (UBC)",
        "category": "PO-KAPITALISTINĖ EKONOMIKA • SOCIALINIS KONTRAKTAS",
        "badge_color": "amber",
        "summary": "Valstybės arba globalaus fondo garantuojamos besąlyginės piniginės arba skaičiavimo resursų (Universal Basic Compute) išmokos kiekvienam piliečiui, nepriklausomai nuo jo turto ar darbo statuso, automatizavus didžiąją dalį darbo rinkos.",
        "custom_html": """
          <div class="wiki-stat-banner">
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val amber">1000–2000 €</div>
              <div class="wiki-stat-lbl">Numatoma bazinė mėnesio išmoka</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val">UBC</div>
              <div class="wiki-stat-lbl">Universal Basic Compute (AI kvota)</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val emerald">Robotų mokestis</div>
              <div class="wiki-stat-lbl">Pagrindinis finansavimo šaltinis</div>
            </div>
            <div class="wiki-stat-pill">
              <div class="wiki-stat-val crimson">Prasmės krizė</div>
              <div class="wiki-stat-lbl">Kas nutinka žmogui be darbo?</div>
            </div>
          </div>

          <div class="wiki-quote-card amber">
            <div class="wiki-quote-text">„Kapitalizmas negali funkcionuoti, jei mašinos atlieka visą darbą, o žmonės neturi pinigų nusipirkti tų mašinų gaminamų prekių. UBI taps ne kairiųjų svajone, o vienintele kapitalizmo išlikimo sąlyga.“</div>
            <div class="wiki-quote-author">— Sam Altman, „Moore's Law for Everything“</div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title amber">💰 Iš kur paimti pinigų? AI korporacijų apmokestinimas</div>
            </div>
            <div class="wiki-card-body">
              <p>Kai DI pakeičia 50% protinio darbo, tradiciniai darbo pajamų mokesčiai (GPM, Sodra) suyra. Vienintelis būdas išlaikyti valstybę – <strong>apmokestinti skaičiavimo galią ir kapitalą</strong>:</p>
              <ul>
                <li>Mokestis už kiekvieną sugeneruotą tokeną arba sunaudotą megavatvalandę duomenų centre.</li>
                <li>Privalomas akcijų fondas: 2,5% kiekvienos privačios technologijų gigantės akcijų kasmet pervedama į nacionalinį piliečių fondą.</li>
              </ul>
            </div>
          </div>

          <div class="wiki-bespoke-card">
            <div class="wiki-card-header">
              <div class="wiki-card-title emerald">⚡ Universal Basic Compute (UBC): Naujoji duona</div>
            </div>
            <div class="wiki-card-body">
              <p>Samas Altmanas siūlo dar radikalesnę idėją – <strong>Universal Basic Compute (UBC)</strong>: vietoj nuvertėjančių popierinių pinigų kiekvienas pilietis gauna teisę į dalį GPT-7 lygio superintelekto skaičiavimo resursų. Pilietis gali panaudoti savo kvotą kurdamas filmus, atlikdamas tyrimus arba išnuomodamas ją korporacijoms.</p>
            </div>
          </div>

          <div class="wiki-verdict-card amber">
            <div class="wiki-card-header">
              <div class="wiki-card-title crimson">🚬 Prasmės kolapsas: Pasaulis be ryto žadintuvo</div>
            </div>
            <div class="wiki-card-body">
              <p>Didžiausias iššūkis bus ne ekonominis, o psichologinis. Darbas tūkstančius metų suteikė žmogui tapatybę, discipliną ir socialinį statusą. Pasaulyje po darbo milijardams žmonių grės apatija, priklausomybės ir depresija virtualios realybės burbuluose.</p>
            </div>
          </div>
        """
    }
}

if __name__ == "__main__":
    print(f"Bespoke Biology Data sugeneruota: {len(BIOLOGY_DATA)} irasu.")
