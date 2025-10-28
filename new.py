import asyncio, aiohttp, os, random
from urllib.parse import urlparse, parse_qs, urlencode

async def ytd(url, folder="downloads"):
    vid = (urlparse(url).path.lstrip("/") if "youtu.be" in url 
           else parse_qs(urlparse(url).query).get("v", [None])[0])
    if not vid: raise ValueError("Invalid YouTube URL")

    os.makedirs(folder, exist_ok=True)
    headers = {"Referer": "https://id.ytmp3.mobi/"}
    async with aiohttp.ClientSession(headers=headers) as s:
        init = await (await s.get(f"https://d.ymcdn.org/api/v1/init?p=y&_={random.random()}")).json()
        conv = await (await s.get(f"{init['convertURL']}&{urlencode({'v': vid, 'f': 'mp3', '_': random.random()})}")).json()

        while True:
            prog = await (await s.get(conv["progressURL"])).json()
            if prog.get("progress") == 3:
                title = "".join(c for c in prog.get("title", vid) if c.isalnum() or c in " _-")
                path = os.path.join(folder, f"{title}.mp3")
                async with s.get(conv["downloadURL"]) as resp:
                    with open(path, "wb") as f:
                        while chunk := await resp.content.read(1024):
                            f.write(chunk)
                print(f"✅ {title}.mp3 saved in '{folder}'")
                break
            await asyncio.sleep(1)

# 🔹 Single async call
asyncio.run(ytd("https://youtu.be/bq96s64K2YM", folder="MyMP3s"))
            
