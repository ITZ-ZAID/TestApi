import requests

url = "https://api.cookie-api.com/api/youtube/download"
headers = {
    "Authorization": "Sj4732eGMe7RjnbahgL2pjUCsDZlFw04ZqwK1td6LLAfV6fQ9LvKdC1iBam9oD8P",
    "Content-Type": "application/json"
}
payload = {
    "url": "https://youtu.be/ZLRCUFRFY-k",
    "mode": "video"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
