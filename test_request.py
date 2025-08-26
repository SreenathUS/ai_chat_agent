import requests

API_URL = "http://127.0.0.1:8000/chat"

data = {"user_id": "user123", "message": "Hello AI, how are you?"}
response = requests.post(API_URL, json=data)
print("Response:", response.json())
