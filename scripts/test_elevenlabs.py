import requests
import json

API_KEY = 'sk_1a094f76f759cfdff515ef80607038b59073058f48ce69fd'
headers = {'xi-api-key': API_KEY}

try:
    r = requests.get('https://api.elevenlabs.io/v1/user/subscription', headers=headers)
    if r.status_code == 200:
        sub = r.json()
        print('TIER:', sub.get('tier'))
        print('USED_CHARS:', sub.get('character_count'))
        print('LIMIT_CHARS:', sub.get('character_limit'))
        print('REMAINING:', sub.get('character_limit', 0) - sub.get('character_count', 0))
    else:
        print('Subscription error:', r.status_code, r.text)

    r_voices = requests.get('https://api.elevenlabs.io/v1/voices', headers=headers)
    if r_voices.status_code == 200:
        data = r_voices.json()
        voices = data.get('voices', [])
        print(f'VOICES_TOTAL: {len(voices)}')
        for v in voices:
            print(f"VOICE: {v['name']} | ID: {v['voice_id']} | CATEGORY: {v.get('category')} | LABELS: {v.get('labels')}")
    else:
        print('Voices error:', r_voices.status_code, r_voices.text)
except Exception as e:
    print('Exception:', e)
