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

async def generate_ru_chapter(ch_file):
    ch_name = os.path.splitext(ch_file)[0]
    out_mp3_name = f"{ch_name}.mp3"
    
    dest_path_ru = os.path.join(AUDIO_RU_DIR, out_mp3_name)
    dist_path_ru = os.path.join(DIST_AUDIO_RU_DIR, out_mp3_name)

    if os.path.exists(dest_path_ru) and os.path.getsize(dest_path_ru) > 500000:
        print(f" -> [Worker] RU garsas jau yra: {out_mp3_name} ({os.path.getsize(dest_path_ru)//1024} KB), praleidziama.", flush=True)
        return

    cpath = os.path.join(CHAPTERS_RU_DIR, ch_file)
    with open(cpath, "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned = clean_markdown_for_speech(raw_text)
    print(f" -> [Worker] Generuojamas RU garsas (Dmitry): {ch_file} ({len(cleaned)} simboliu)...", flush=True)

    for attempt in range(3):
        try:
            comm = edge_tts.Communicate(cleaned, VOICE)
            await comm.save(dest_path_ru)
            shutil.copyfile(dest_path_ru, dist_path_ru)
            size_mb = os.path.getsize(dest_path_ru) / (1024 * 1024)
            print(f"    [SEKME RU] {out_mp3_name}: {size_mb:.2f} MB sugeneruota ir sinchronizuota!", flush=True)
            break
        except Exception as e:
            print(f"    [Ispejimas] Klaida generuojant {out_mp3_name}: {e}. Bandymas {attempt+1}/3...", flush=True)
            await asyncio.sleep(3)

async def main():
    if len(sys.argv) < 3:
        print("Usage: narrate_ru_range.py <start_idx> <end_idx>")
        sys.exit(1)
        
    start_idx = int(sys.argv[1])
    end_idx = int(sys.argv[2])
    
    all_files = sorted([f for f in os.listdir(CHAPTERS_RU_DIR) if f.endswith(".md")])
    target_files = all_files[start_idx:end_idx+1]
    
    print(f"[Worker] Paleistas ruozui [{start_idx}:{end_idx}] ({len(target_files)} failu): {[os.path.basename(f) for f in target_files]}", flush=True)
    
    for f in target_files:
        await generate_ru_chapter(f)
        
    print(f"[Worker] Ruozas [{start_idx}:{end_idx}] SEKMINGAI BAIGTAS!", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
