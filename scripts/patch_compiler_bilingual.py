import os
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

compile_script_path = os.path.join(os.path.dirname(__file__), "compile_book.py")

with open(compile_script_path, "r", encoding="utf-8") as f:
    code = f.read()

# Surandame kur prasideda chapterAudioMap ir baigiasi updateAudioTrackForCurrentChapter
idx_start = code.find("// Skyrių audio takelių žemėlapis")
if idx_start == -1:
    idx_start = code.find("const chapterAudioMap = {{")

idx_end = code.find("function toggleAudioReadAlong()")

if idx_start != -1 and idx_end != -1:
    new_audio_block = """// 6. DINAMINIS AUDIO ŽEMĖLAPIS PAGAL KALBAS IR BALSUS
    let currentVoice = "lt";

    function changeVoice(voice) {{
      currentVoice = voice;
      updateAudioTrackForCurrentChapter();
      if (isPlayingAudio) {{
        const audio = document.getElementById("bookAudioPlayer");
        if (audio) audio.play().catch(e => console.log(e));
      }}
    }}

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

    function updateAudioTrackForCurrentChapter() {{
      const audio = document.getElementById("bookAudioPlayer");
      if (!audio) return;
      const chId = getActiveChapterId();
      let track = "";
      if (currentVoice === "ru") {{
        track = chapterAudioMapRu[chId] || "assets/audio/ru/00_prologas.mp3";
      }} else if (currentVoice === "adam") {{
        track = "assets/audio/adam/" + chId + ".mp3";
      }} else {{
        track = chapterAudioMapLt[chId] || "assets/audio/lt/00_prologas.mp3";
      }}

      if (!audio.src.endsWith(track)) {{
        const wasPlaying = isPlayingAudio;
        audio.src = track;
        if (wasPlaying) {{
          audio.play().catch(e => console.log(e));
        }}
      }}
    }}

    """
    code = code[:idx_start] + new_audio_block + code[idx_end:]
    with open(compile_script_path, "w", encoding="utf-8") as f:
        f.write(code)
    print("Sekmingai atnaujintas audio valdymo blokas compile_book.py faile!")
else:
    print("Klaida: nerastas audio blokas")
