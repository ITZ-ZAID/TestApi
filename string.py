from pyrogram import Client, filters, idle

api_id = 6435225
api_hash = "4e984ea35f854762dcde906dce426c2d"
string_session = "STRING_SESSION_HERE"

app = Client(
    "string_session_client",
    api_id=api_id,
    api_hash=api_hash,
    session_string=string_session
)

@app.on_message(filters.incoming & filters.chat(42777))
async def handler(client, message):
    print("💬 Message from 42777:", message.text or message.caption)

async def main():
    await app.start()

    me = await app.get_me()
    print("✅ Login Successful")
    print("📱 My Number:", me.phone_number)
    print("🆔 My ID:", me.id)

    await idle()

app.run(main())
