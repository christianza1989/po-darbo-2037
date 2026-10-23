#!/usr/bin/env python3
"""
PILNAS VISU KNYGOS SKYRIU IGARSINIMO VARIKLIS (ElevenLabs - Adam)
Nuosekliai apdoroja visus skyrius, isvalo markdown zymas, suskaido i sakinius,
sugeneruoja MP3 per ElevenLabs ir sinchronizuoja i /assets/audio/ ir /dist/assets/audio/.
"""

import os
import sys
import re
import shutil
import time
import requests

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

API_KEY = "sk_1a094f76f759cfdff515ef80607038b59073058f48ce69fd"
VOICE_ID = "pNInz6obpgDQGcFmaJgB"  # Adam
MODEL_ID = "eleven_multilingual_v2"

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
AUDIO_DIR = os.path.join(BASE_DIR, "assets", "audio")
DIST_AUDIO_DIR = os.path.join(BASE_DIR, "dist", "assets", "audio")

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(DIST_AUDIO_DIR, exist_ok=True)

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

def split_into_chunks(text, max_chars=3400):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = []
    current_len = 0

    for s in sentences:
        s = s.strip()
        if not s:
            continue
        if current_len + len(s) + 1 > max_chars and current_chunk:
            chunks.append(' '.join(current_chunk))
            current_chunk = [s]
            current_len = len(s)
        else:
            current_chunk.append(s)
            current_len += len(s) + 1

    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks

def synthesize_chunk(chunk_text, chunk_idx, total_chunks, retries=3):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": chunk_text,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.50,
            "similarity_boost": 0.80,
            "style": 0.10,
            "use_speaker_boost": True
        }
    }

    for attempt in range(retries):
        print(f"    [Blokas {chunk_idx + 1}/{total_chunks}] Siunciama {len(chunk_text)} simboliu... (bandymas {attempt + 1})", flush=True)
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=90)
            if r.status_code == 200:
                return r.content
            elif r.status_code in (401, 402):
                print(f"    [ELEVENLABS LIMITAS] Statusas {r.status_code}: {r.text}", flush=True)
                return "QUOTA_EXCEEDED"
            elif r.status_code == 429:
                print("    [429 Rate Limit] Laukiama 10s...", flush=True)
                time.sleep(10)
            else:
                print(f"    [Klaida {r.status_code}] {r.text}", flush=True)
                time.sleep(3)
        except Exception as e:
            print(f"    [Tinklo klaida]: {e}", flush=True)
            time.sleep(4)

    return None

def process_all_chapters():
    files = sorted([f for f in os.listdir(CHAPTERS_DIR) if f.endswith(".md")])
    total_chapters = len(files)

    print("=============================================================", flush=True)
    print(f"PRADEDAMAS PILNAS KNYGOS IGARSINIMAS ({total_chapters} SKYRIAI)", flush=True)
    print(f"Balsas: ADAM (ElevenLabs) | Modelis: {MODEL_ID}", flush=True)
    print("=============================================================", flush=True)

    for ch_idx, fname in enumerate(files):
        out_mp3_name = fname.replace(".md", ".mp3")
        target_path = os.path.join(AUDIO_DIR, out_mp3_name)
        dist_path = os.path.join(DIST_AUDIO_DIR, out_mp3_name)

        # Jei failas jau sugeneruotas ir didesnis nei 100 KB - praleidziame
        if os.path.exists(target_path) and os.path.getsize(target_path) > 100000:
            print(f"\n[{ch_idx + 1}/{total_chapters}] {fname} -> JAU YRA ({os.path.getsize(target_path) // 1024} KB). Praleidziama.", flush=True)
            if not os.path.exists(dist_path) or os.path.getsize(dist_path) != os.path.getsize(target_path):
                shutil.copy2(target_path, dist_path)
            continue

        filepath = os.path.join(CHAPTERS_DIR, fname)
        with open(filepath, "r", encoding="utf-8") as f:
            raw = f.read()

        clean_text = clean_markdown_for_speech(raw)
        chunks = split_into_chunks(clean_text)

        print(f"\n-------------------------------------------------------------", flush=True)
        print(f"[{ch_idx + 1}/{total_chapters}] GARSINAMAS: {fname}", flush=True)
        print(f"Viso teksto simboliu: {len(clean_text)} | Bloku: {len(chunks)}", flush=True)
        print(f"-------------------------------------------------------------", flush=True)

        audio_chunks = []
        quota_hit = False

        for c_idx, chunk in enumerate(chunks):
            audio_data = synthesize_chunk(chunk, c_idx, len(chunks))
            if audio_data == "QUOTA_EXCEEDED":
                quota_hit = True
                break
            elif audio_data:
                audio_chunks.append(audio_data)
                time.sleep(0.6)  # Mandagi pauze tarp uzklausu
            else:
                print(f"    [ISPEJIMAS] Nepavyko sugeneruoti bloko {c_idx + 1}", flush=True)

        if quota_hit:
            print("\n[STOP] Pasiektas ElevenLabs tokenu limitas. Sustojama ties dabartine vieta.", flush=True)
            print("Galite papildyti ElevenLabs tokenus ir paleisti is naujo – sistema tes nuo ten, kur baige!", flush=True)
            break

        if audio_chunks:
            with open(target_path, "wb") as f:
                for b in audio_chunks:
                    f.write(b)
            shutil.copy2(target_path, dist_path)
            size_kb = os.path.getsize(target_path) // 1024
            print(f" -> [SEKME] Skyrius {fname} baigtas: {size_kb} KB!", flush=True)

    print("\n=============================================================", flush=True)
    print("KNYGOS IGARSINIMO PROCESAS BAIGTAS ARBA PAUZUOTAS!", flush=True)
    print("=============================================================", flush=True)

if __name__ == "__main__":
    process_all_chapters()
