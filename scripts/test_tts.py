import requests

API_KEY = 'sk_1a094f76f759cfdff515ef80607038b59073058f48ce69fd'
headers = {
    'xi-api-key': API_KEY,
    'Content-Type': 'application/json'
}

# Bandome su populiariausiu universaliu balsu 'Adam' (ID: pNInz6obpgDQGcFmaJgB)
voice_id = 'pNInz6obpgDQGcFmaJgB'
url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'

payload = {
    "text": "Sveiki atvykę į knygą PO DARBO. Mes pradedame didžiąją kelionę į dirbtinio superintelekto erą.",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75
    }
}

r = requests.post(url, headers=headers, json=payload)
print('STATUS:', r.status_code)
if r.status_code == 200:
    out_file = r'C:\Users\Lenovo\Downloads\AI KNYGA\assets\elevenlabs_sample_adam.mp3'
    with open(out_file, 'wb') as f:
        f.write(r.content)
    print(f'SUCCESS! Audio saved ({len(r.content)} bytes) to {out_file}')
else:
    print('ERROR:', r.text)
