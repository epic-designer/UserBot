import time 
import random 
import asyncio
from config import HANDLER, OWNER_ID, BARATH
from pyrogram import filters, __version__ as pyrover
from Barath import barath, get_readable_time, StartTime
from Barath import bot

s1 = """



╔═══╗─╔╗
║╔══╝─║║
║╚══╦═╝╠╦══╦══╦═╗
║╔══╣╔╗╠╣══╣╔╗║╔╗╗
║╚══╣╚╝║╠══║╚╝║║║║
╚═══╩══╩╩══╩══╩╝╚╝
"""


@barath.on_message(filters.command("alive",prefixes=HANDLER) & filters.user(OWNER_ID))
async def alive(_, message):
    name = (await barath.get_me()).first_name
    await message.edit(s1)
    await asyncio.sleep(3)
    await message.delete()
    alive = await message.reply_animation(BARATH, caption="")
    await message.reply_text(f"{s1}\n\nʜᴇʏ ᴍᴀsᴛᴇʀ,\nɪ ᴀᴍ ᴀʟɪᴠᴇ\n\n» ᴍʏ Dᴇᴠʟᴏᴘᴇʀ: {name}\n» ᴘʏʀᴏɢʀᴀᴍ ᴠɪʀsᴏɴ: {pyrover}\n» ʀᴇᴘᴏ: ɪᴛᴢ ᴘʀɪᴠᴀᴛᴇ ᴍʏ ғʀɪᴇɴᴅ")

@barath.on_message(filters.command("ping",prefixes=HANDLER) & filters.user(OWNER_ID))
async def ping(_, message):
     start_time = time.time()
     end_time = time.time()
     ping_time = round((end_time - start_time) * 1000, 3)
     uptime = get_readable_time((time.time() - StartTime))
     await message.edit(f"\ (•◡•) / **ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ**\n⋙ 🔔 **ᑭｴƝG**: {ping_time}\n⋙ ⬆️ **ⴑⲢⲦⲒⲘⲈ**: {uptime}")

