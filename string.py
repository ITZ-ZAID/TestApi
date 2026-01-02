from pyrogram import Client, filters, idle

api_id = 6435225
api_hash = "4e984ea35f854762dcde906dce426c2d"
string_session = "BQBiMZkAEcdO4hgTmcRJqfAl6QboO8n2Jx0H8CxghODBF_fV_RTAWy0YsablDh8K3c8I849TImrFodCsnfw_pSU2oj1T82BiIspbimdUpjfr46QhtD7_qmNd-d2MPfQyQBV4bDYbqo3EEu8UQ1d1ZkBgjjoaMHDD6LWgyJItDwSd9KqM0Dh8o0sgETbo9uTB6hs3Ec9LP-Tai61gYh62zPwRbrj38HvA2CbQ8IR-yKrmZbDUpJJapC3qxoAdMsJszT93wmCIKnVGzIcfyBznQhbnSmZoB_k0ZcBM-Q6PnjbZadTVQtNln2q-j6x9Cwk7zeMIaMr02_sIxhfzvCsqBd6pmPlDggAAAAHWcYcqAA"

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
