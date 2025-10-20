# youtube_service.py
import requests
import urllib.parse

def fetch_youtube_data(youtube_url: str):
    try:
        encoded_url = urllib.parse.quote(youtube_url, safe='')

        # Build request
        full_url = f"https://api.vidfly.ai/api/media/youtube/download?url={encoded_url}"

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json",
        }

        # Send request
        response = requests.get(full_url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        video_url = (
            data.get("data", {})
            .get("items", [{}])[0]
            .get("url")
        )
        if not video_url:
            raise ValueError("Video URL not found")

        return video_url

    except requests.RequestException as e:
        raise RuntimeError(f"YouTube downloader request failed: {e}")

video_url = "https://youtu.be/HBj4OSE3F6g"
try:
    result = fetch_youtube_data(video_url)
    print(result)
except Exception as e:
    print("Error:", e)
