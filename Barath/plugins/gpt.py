from Barath import barath
import httpx
from pyrogram import filters, Client
from pyrogram.types import Message
from config import HANDLER, OWNER_ID

@barath.on_message(filters.command("chat",prefixes=HANDLER) & filters.user(OWNER_ID))
async def gpt(_, message):
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


