import requests
import urllib.parse
import asyncio

async def fetch_youtube_data(youtube_url: str) -> str | None:
    """
    Query vidfly.ai for a direct media URL for the given YouTube link.
    Returns the media URL on success, or None on failure.
    """
    try:
        encoded_url = urllib.parse.quote(youtube_url, safe="")

        full_url = f"https://api.vidfly.ai/api/media/youtube/download?url={encoded_url}"

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json",
        }

        loop = asyncio.get_running_loop()
        resp = await loop.run_in_executor(
            None, lambda: requests.get(full_url, headers=headers, timeout=30)
        )
        resp.raise_for_status()
        data = resp.json()
        video_url = (
            data.get("data", {}).get("items", [{}])[11].get("url")
        )
        if not video_url:
            return None

        return print(video_url)

    except Exception:
        return None


asyncio.run(fetch_youtube_data("https://youtu.be/Fk50lCFkl1g"))
