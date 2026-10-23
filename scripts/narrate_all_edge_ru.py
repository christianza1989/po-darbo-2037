import os
import sys
import re
import asyncio
import edge_tts
import shutil

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHAPTERS_RU_DIR = os.path.join(BASE_DIR, "chapters_ru")
AUDIO_DIR = os.path.join(BASE_DIR, "assets", "audio")
AUDIO_RU_DIR = os.path.join(AUDIO_DIR, "ru")
DIST_AUDIO_DIR = os.path.join(BASE_DIR, "dist", "assets", "audio")
DIST_AUDIO_RU_DIR = os.path.join(DIST_AUDIO_DIR, "ru")

os.makedirs(AUDIO_RU_DIR, exist_ok=True)
os.makedirs(DIST_AUDIO_RU_DIR, exist_ok=True)

VOICE = "ru-RU-DmitryNeural"

def clean_markdown_for_speech(raw_text):
    text = re.sub(r'<[^>]+>', ' ', raw_text)
    text = re.sub(r'!\[.*?\]\(.*?\)', ' ', text)
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    text = re.sub(r'\|', ' ', text)
    text = re.sub(r'-{3,}', ' ', text)
    text = re.sub(r'```.*?```', ' ', text, flags=re.DOTALL)
    text = re.sub(r'`.*?`', ' ', text)
    text = re.sub(r'#+\s*', '', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

async def generate_ru_chapter_audio(ch_file):
    ch_name = os.path.splitext(ch_file)[0]
    out_mp3_name = f"{ch_name}.mp3"
    
    dest_path_ru = os.path.join(AUDIO_RU_DIR, out_mp3_name)
    dist_path_ru = os.path.join(DIST_AUDIO_RU_DIR, out_mp3_name)

    # Jei failas jau egzistuoja ir dydis > 100KB, praleidziame
    if os.path.exists(dest_path_ru) and os.path.getsize(dest_path_ru) > 100000:
        print(f" -> RU garsas jau yra: {out_mp3_name} ({os.path.getsize(dest_path_ru)//1024} KB), praleidziama.")
        return

    cpath = os.path.join(CHAPTERS_RU_DIR, ch_file)
    with open(cpath, "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned = clean_markdown_for_speech(raw_text)
    print(f" -> Generuojamas RU garsas (Dmitry): {ch_file} ({len(cleaned)} simboliu)...", flush=True)

    comm = edge_tts.Communicate(cleaned, VOICE)
    await comm.save(dest_path_ru)

    shutil.copyfile(dest_path_ru, dist_path_ru)
    size_mb = os.path.getsize(dest_path_ru) / (1024 * 1024)
    print(f"    [SEKME RU] {out_mp3_name}: {size_mb:.2f} MB sugeneruota ir sinchronizuota!", flush=True)

async def main():
    files = sorted([f for f in os.listdir(CHAPTERS_RU_DIR) if f.endswith(".md")])
    print(f"Rasta RU skyriu generavimui: {len(files)}")
    for f in files:
        await generate_ru_chapter_audio(f)
    print("\nVISI RASTI RU SKYRIAI SEKMINGAI IGARSINTI SU DMITRY (RU)!")

if __name__ == "__main__":
    asyncio.run(main())
