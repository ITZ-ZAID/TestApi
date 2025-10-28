import asyncio, aiohttp, os, random
from urllib.parse import urlparse, parse_qs, urlencode

async def ytd(url, folder="downloads"):
    parsed = urlparse(url)
    vid = parsed.path.lstrip("/") if "youtu.be" in url else parse_qs(parsed.query).get("v", [None])[0]
    if not vid:
        raise ValueError("Invalid YouTube URL")

    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{vid}.mp3")
    if os.path.exists(path):
        print(f"⚡ File already exists: {path}")
        return path

    headers = {"Referer": "https://id.ytmp3.mobi/"}
    async with aiohttp.ClientSession(headers=headers) as s:
        init = await (await s.get(f"https://d.ymcdn.org/api/v1/init?p=y&_={random.random()}")).json()
        conv = await (await s.get(f"{init['convertURL']}&{urlencode({'v': vid, 'f': 'mp3', '_': random.random()})}")).json()

        while True:
            prog = await (await s.get(conv["progressURL"])).json()
            if prog.get("progress") == 3:
                async with s.get(conv["downloadURL"]) as r:
                    with open(path, "wb") as f:
                        while chunk := await r.content.read(1024):
                            f.write(chunk)
                print(f"✅ Downloaded: {path}")
                return path
            await asyncio.sleep(1)

# 🔹 One simple call
asyncio.run(ytd("https://youtu.be/bq96s64K2YM", folder="MyMP3s"))
                
