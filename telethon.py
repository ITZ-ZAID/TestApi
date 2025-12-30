from telethon import TelegramClient, events
from telethon.sessions import StringSession
import re
from datetime import datetime

# ========= CONFIG =========
api_id = 123456              # your api_id
api_hash = "API_HASH"        # your api_hash
STRING_SESSION = "PASTE_STRING_SESSION_HERE"
SERVICE_NUMBER = "42777"
# ==========================

client = TelegramClient(
    StringSession(STRING_SESSION),
    api_id,
    api_hash
)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    sender = await event.get_sender()

    # Some service messages may not have phone
    phone = getattr(sender, "phone", None)
    if phone != SERVICE_NUMBER:
        return

    text = event.text or ""
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n📩 New message received")
    print("⏰ Time:", time_now)
    print("📞 From: +42777")
    print("📄 Message:", text)

    # Extract OTP (4–6 digits)
    otp = re.search(r"\b\d{4,6}\b", text)
    if otp:
        print("🔑 OTP FOUND:", otp.group())
    else:
        print("⚠️ OTP not detected")

    print("-" * 50)

async def main():
    print("✅ Script started successfully.")
    print("📡 Waiting for OTP messages from Telegram service +42777...")
    print("⛔ Press CTRL+C to stop the script.\n")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
