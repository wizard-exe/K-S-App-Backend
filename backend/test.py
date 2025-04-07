import requests

url = 'https://k-s-app-backend.onrender.com/korrigiere'

payload = {
    "text": "Das ist so ein Ding, das man einfach so machen kann."
}

try:
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        print("Original:", data['original'])
        print("Technisch:", data['technisch'])
    else:
        print("Fehler:", response.status_code, response.text)

except requests.exceptions.RequestException as e:
    print("Verbindungsfehler:", e)
