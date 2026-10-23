import os
import sys
import re
import asyncio
import edge_tts

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
AUDIO_DIR = os.path.join(BASE_DIR, "assets", "audio")
AUDIO_LT_DIR = os.path.join(AUDIO_DIR, "lt")
DIST_AUDIO_DIR = os.path.join(BASE_DIR, "dist", "assets", "audio")
DIST_AUDIO_LT_DIR = os.path.join(DIST_AUDIO_DIR, "lt")

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(AUDIO_LT_DIR, exist_ok=True)
os.makedirs(DIST_AUDIO_DIR, exist_ok=True)
os.makedirs(DIST_AUDIO_LT_DIR, exist_ok=True)

VOICE = "lt-LT-LeonasNeural"

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

async def generate_chapter_audio(ch_file):
    ch_name = os.path.splitext(ch_file)[0]
    out_mp3_name = f"{ch_name}.mp3"
    
    dest_path_lt = os.path.join(AUDIO_LT_DIR, out_mp3_name)
    dest_path_main = os.path.join(AUDIO_DIR, out_mp3_name)
    dist_path_lt = os.path.join(DIST_AUDIO_LT_DIR, out_mp3_name)
    dist_path_main = os.path.join(DIST_AUDIO_DIR, out_mp3_name)

    cpath = os.path.join(CHAPTERS_DIR, ch_file)
    with open(cpath, "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned = clean_markdown_for_speech(raw_text)
    print(f" -> Generuojamas LT garsas: {ch_file} ({len(cleaned)} simboliu)...", flush=True)

    comm = edge_tts.Communicate(cleaned, VOICE)
    await comm.save(dest_path_lt)

    # Kopijuojame i pagrindini audio kataloga ir dist
    import shutil
    shutil.copyfile(dest_path_lt, dest_path_main)
    shutil.copyfile(dest_path_lt, dist_path_lt)
    shutil.copyfile(dest_path_lt, dist_path_main)

    size_mb = os.path.getsize(dest_path_lt) / (1024 * 1024)
    print(f"    [SEKME] {out_mp3_name}: {size_mb:.2f} MB sugeneruota ir sinchronizuota!", flush=True)

async def main():
    files = sorted([f for f in os.listdir(CHAPTERS_DIR) if f.endswith(".md")])
    print(f"Rasta skyriu generavimui: {len(files)}")
    for f in files:
        await generate_chapter_audio(f)
    print("\nVISI 17 SKYRIU SEKMINGAI IGARSINTI SU LEONAS (LT)!")

if __name__ == "__main__":
    asyncio.run(main())
