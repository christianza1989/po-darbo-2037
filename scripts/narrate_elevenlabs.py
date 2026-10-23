#!/usr/bin/env python3
"""
ELEVENLABS AUDIOBOOK NARRATOR (Adam - Flagship Voice)
Isvalo markdown zymas, suskaido i prasmingus sakiniu blokus ir
sugeneruoja profesionalu MP3 igarsinima naudodamas ElevenLabs eleven_multilingual_v2.
"""

import os
import sys
import re
import requests
import time

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

API_KEY = "sk_1a094f76f759cfdff515ef80607038b59073058f48ce69fd"
VOICE_ID = "pNInz6obpgDQGcFmaJgB"  # Adam (Pats populiariausias ElevenLabs balsas pasaulyje)
MODEL_ID = "eleven_multilingual_v2"

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
AUDIO_OUT_DIR = os.path.join(BASE_DIR, "assets", "audio")
os.makedirs(AUDIO_OUT_DIR, exist_ok=True)

def clean_markdown_for_speech(raw_text):
    # Saliname HTML zymas
    text = re.sub(r'<[^>]+>', ' ', raw_text)
    # Saliname paveikslelius ![alt](url)
    text = re.sub(r'!\[.*?\]\(.*?\)', ' ', text)
    # Saliname nuorodas [tekstas](url) -> tekstas
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)
    # Saliname lenteliu skyriklius ir stulpelius
    text = re.sub(r'\|', ' ', text)
    text = re.sub(r'-{3,}', ' ', text)
    # Saliname kodu blokus
    text = re.sub(r'```.*?```', ' ', text, flags=re.DOTALL)
    text = re.sub(r'`.*?`', ' ', text)
    # Saliname antrastes (#, ##, ###)
    text = re.sub(r'#+\s*', '', text)
    # Saliname paryskinimus (**tekstas**, *tekstas*)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    # Saliname pasikartojancius tarpus ir tuscias eilutes
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def split_into_chunks(text, max_chars=3500):
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

def synthesize_text(text_chunk, chunk_idx):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text_chunk,
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.50,
            "similarity_boost": 0.80,
            "style": 0.10,
            "use_speaker_boost": True
        }
    }
    
    print(f" -> Siunciamas blokas #{chunk_idx + 1} ({len(text_chunk)} simboliu)...")
    r = requests.post(url, headers=headers, json=payload, timeout=60)
    if r.status_code == 200:
        return r.content
    else:
        print(f" [KLAIDA] Blokas #{chunk_idx + 1} grazino koda {r.status_code}: {r.text}")
        return None

def narrate_chapter(chapter_filename, max_chunks=None):
    filepath = os.path.join(CHAPTERS_DIR, chapter_filename)
    if not os.path.exists(filepath):
        print(f"Failas nerastas: {filepath}")
        return None

    with open(filepath, "r", encoding="utf-8") as f:
        raw_text = f.read()

    clean_text = clean_markdown_for_speech(raw_text)
    chunks = split_into_chunks(clean_text)
    if max_chunks:
        chunks = chunks[:max_chunks]

    print(f"\n=======================================================")
    print(f"IGARSINAMAS SKYRIUS: {chapter_filename}")
    print(f"Balsas: ADAM (ElevenLabs Flagship)")
    print(f"Bloku skaicius: {len(chunks)} | Viso simboliu: {sum(len(c) for c in chunks)}")
    print(f"=======================================================")

    audio_bytes = []
    for idx, chunk in enumerate(chunks):
        audio_data = synthesize_text(chunk, idx)
        if audio_data:
            audio_bytes.append(audio_data)
        else:
            print(f"Nepavyko sugeneruoti bloko #{idx + 1}")
            break
        time.sleep(0.5)

    if audio_bytes:
        out_name = chapter_filename.replace(".md", ".mp3")
        out_path = os.path.join(AUDIO_OUT_DIR, out_name)
        with open(out_path, "wb") as f:
            for b in audio_bytes:
                f.write(b)
        print(f"\n[SEKME] Skyrius sekmingai igarsintas i: {out_path} ({os.path.getsize(out_path)} baitu)")
        return out_path
    return None

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "00_prologas.md"
    max_c = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    narrate_chapter(target, max_chunks=max_c)
