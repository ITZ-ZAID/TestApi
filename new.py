import asyncio
import random
import aiohttp
from urllib.parse import urlparse, parse_qs, urlencode

async def ytd(url):
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
        "f": "mp3",
        "_": random.random()
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        # Step 1: Init
        init_url = f"https://d.ymcdn.org/api/v1/init?p=y&23=1llum1n471&_={random.random()}"
        async with session.get(init_url) as resp:
            init_data = await resp.json()

        # Step 2: Convert
        full_convert_url = f"{init_data['convertURL']}&{urlencode(url_params)}"
        async with session.get(full_convert_url) as resp:
            convert_data = await resp.json()

        # Step 3: Poll progress
        while True:
            async with session.get(convert_data["progressURL"]) as resp:
                prog = await resp.json()
            if "error" in prog and prog["error"]:
                raise Exception(f"Convert failed: {prog['error']}")
            if prog.get("progress") == 3:
                return {
                    "title": prog.get("title"),
                    "url": convert_data.get("downloadURL")
                }
            await asyncio.sleep(1)

# Example usage
async def main():
    try:
        geturl = await ytd("https://youtu.be/bq96s64K2YM")
        print(geturl)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    asyncio.run(main())
