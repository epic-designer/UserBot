from Hoshino import pbot as app
import httpx
from pyrogram import filters, Client
from pyrogram.types import Message


@app.on_message(filters.command("chat"))
async def gpt(_: Client, message: Message):
    txt = await message.reply("**writing....**")
    if len(message.command) < 2:
        return await txt.edit("**give me a message too.**")

    query = message.text.split(maxsplit=1)[1]
    url = "https://api.safone.me/chatgpt"
    payload = {
        "message": query,
        "chat_mode": "assistant",
        "dialog_messages": '[{"bot":"","user":""}]',
    }

    async with httpx.AsyncClient(timeout=20) as client:
        try:
            response = await client.post(
                url, json=payload, headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            results = response.json()
            await txt.edit(results["message"])
        except httpx.HTTPError as e:
            await txt.edit(f"An error occurred: {str(e)}")
        except Exception as e:
            await txt.edit(f"An error occurred: {str(e)}")



__help__ = """
ᴀɴ ᴇꜰꜰᴇᴄᴛɪᴠᴇ ᴄʜᴀᴛ ɢᴘᴛ ᴍᴏᴅᴜʟᴇ ᴡɪᴛʜ ʀᴇᴀʟ ɢᴘᴛ ᴀᴘɪ.ᴜɴʟɪᴍɪᴛᴇᴅ ʀᴇQᴜᴇꜱᴛꜱ.  

 ➢ /chat*:* ɢᴇɴᴇʀᴀᴛᴇꜱ ʀᴇꜱᴘᴏɴꜱᴇ ᴛʜʀᴏᴜɢʜ ᴄʜᴀᴛ ɢᴘᴛ ᴀᴘɪ.
"""

__mod_name__ = "Gᴘᴛ"
