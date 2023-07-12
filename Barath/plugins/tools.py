import glob
import io
import os
import re
import urllib
import urllib.request

import requests
from bing_image_downloader import downloader
from bs4 import BeautifulSoup
from PIL import Image
from search_engine_parser import GoogleSearch

from pyrogram import filters
from pyrogram.types import *


from Barath import  barath
from config import HANDLER, OWNER_ID


@barath.on_message(filters.command("video",prefixes=HANDLER) & filters.user(OWNER_ID))
async def _(event):
    if event.fwd_from:
        return

    webevent = await event.reply("searching........")
    match = event.pattern_match.group(1)
    page = re.findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"❍[{title}]({link})\n**{desc}**\n\n"
        except IndexError:
            break
    await webevent.edit(
        "**Search Query:**\n`" + match + "`\n\n**Results:**\n" + msg, link_preview=False
    )
