# youtube_service.py
import requests

def fetch_youtube_data(url: str):
    try:
        response = requests.get(
            "https://api.vidfly.ai/api/media/youtube/download",
            params={"url": url},
            headers={
                "accept": "*/*",
                "content-type": "application/json",
                "x-app-name": "vidfly-web",
                "x-app-version": "1.0.0",
                "Referer": "https://vidfly.ai/",
            },
            timeout=30,
        )

        response.raise_for_status()
        data = response.json().get("data", {})

        # Validate response structure
        if not data or "items" not in data or "title" not in data:
            raise ValueError("Invalid or empty response from YouTube downloader API")

        return {
            "title": data["title"],
            "thumbnail": data.get("cover"),
            "duration": data.get("duration"),
            "formats": [
                {
                    "type": item.get("type"),
                    "quality": item.get("label", "unknown"),
                    "extension": item.get("ext") or item.get("extension", "unknown"),
                    "url": item.get("url"),
                }
                for item in data.get("items", [])
            ],
        }

    except requests.RequestException as e:
        raise RuntimeError(f"YouTube downloader request failed: {e}")

video_url = "https://youtu.be/HBj4OSE3F6g"
try:
    result = fetch_youtube_data(video_url)
    print(result)
except Exception as e:
    print("Error:", e)
