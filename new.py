import time
import random
import requests
from urllib.parse import urlparse, parse_qs, urlencode

def ytd(url):
    headers = {"Referer": "https://id.ytmp3.mobi/"}
    video_id = None

    # Parse YouTube URL
    parsed = urlparse(url)
    if parsed.hostname == "youtu.be":
        video_id = parsed.path.lstrip("/")
    elif parsed.hostname and "youtube.com" in parsed.hostname:
        video_id = parse_qs(parsed.query).get("v", [None])[0]

    if not video_id:
        raise ValueError("Couldn't extract video ID")

    url_params = {
        "v": video_id,
        "f": "mp4",
        "_": random.random()
    }

    # Step 1: Init
    init_url = f"https://d.ymcdn.org/api/v1/init?p=y&23=1llum1n471&_={random.random()}"
    init_data = requests.get(init_url, headers=headers).json()

    # Step 2: Convert
    full_convert_url = f"{init_data['convertURL']}&{urlencode(url_params)}"
    convert_data = requests.get(full_convert_url, headers=headers).json()

    # Step 3: Poll progress
    while True:
        prog = requests.get(convert_data["progressURL"], headers=headers).json()
        if "error" in prog and prog["error"]:
            raise Exception(f"Convert failed: {prog['error']}")
        if prog.get("progress") == 3:
            return {
                "title": prog.get("title"),
                "url": convert_data.get("downloadURL")
            }
        time.sleep(1)

# Example usage

try:
    geturl = ytd("https://youtu.be/bq96s64K2YM")
    print(geturl)
except Exception as e:
    print("Error:", e)
