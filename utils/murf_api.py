import requests

MURF_API_KEY = "ap2_c95ac967-e663-41cd-8f30-aa3078a025ae"

def murf_stt(audio_file):
    url = "https://api.murf.ai/v1/speech-to-text"

    headers = {
        "Authorization": f"Bearer {MURF_API_KEY}"
    }

    files = {"file": audio_file}

    response = requests.post(url, headers=headers, files=files)
    return response.json().get("text", "")