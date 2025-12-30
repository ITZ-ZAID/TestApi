from pyrogram import Client, filters
import re
from datetime import datetime

# ========= CONFIG =========
api_id = 123456              # your api_id
api_hash = "API_HASH"        # your api_hash
STRING_SESSION = "PASTE_STRING_SESSION_HERE"
SERVICE_NUMBER = "42777"
# ==========================

app = Client(
    name="otp_listener",
    api_id=api_id,
    api_hash=api_hash,
    session_string=STRING_SESSION
)

@app.on_message(filters.private)
def read_otp(client, message):
    sender = message.from_user
    if not sender or sender.phone_number != SERVICE_NUMBER:
        return

    text = message.text or ""
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

if __name__ == "__main__":
    print("✅ Script started successfully.")
    print("📡 Waiting for OTP messages from Telegram service +42777...")
    print("⛔ Press CTRL+C to stop the script.\n")
    app.run()
