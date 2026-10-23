import requests

API_KEY = 'sk_1a094f76f759cfdff515ef80607038b59073058f48ce69fd'
headers = {
    'xi-api-key': API_KEY,
    'Content-Type': 'application/json'
}

test_text = "Civilizacija stovi prieš didžiausią lūžį žmonijos istorijoje. Tai nėra trijų metų mada. Tai septyniasdešimt metų trukęs tylus silicio prabudimas, kuris dabar pasiekė devyniasdešimt laipsnių statumo kreivę."

voices_to_test = {
    "Brian": "nPczCjzI2devNBz1zQrb",
    "George": "JBFqnCBsd6RMkjVDRZzb"
}

for name, vid in voices_to_test.items():
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{vid}'
    payload = {
        "text": test_text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.55,
            "similarity_boost": 0.8,
            "style": 0.15
        }
    }
    r = requests.post(url, headers=headers, json=payload)
    if r.status_code == 200:
        out = f"C:\\Users\\Lenovo\\Downloads\\AI KNYGA\\assets\\sample_{name.lower()}.mp3"
        with open(out, 'wb') as f:
            f.write(r.content)
        print(f"Generated {name}: {len(r.content)} bytes -> {out}")
    else:
        print(f"Failed {name}: {r.status_code} {r.text}")
