import os 
import time
import logging
from pyrogram import Client
from pymongo import MongoClient 

FORMAT = "[Barath]: %(message)s"

logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], format=FORMAT)


StartTime = time.time()

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
                  
#set in hosting app vars
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
SESSION = os.getenv("SESSION") 
TOKEN = os.getenv("TOKEN")

#for userbot
barath = Client(name="Barath", session_string=SESSION, api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, plugins=dict(root="Barath"),)

#for bot 
bot = Client(name="Bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN, plugins=dict(root="Barath"))


DB_URL = "mongodb+srv://personaluse:ImCrAzYbOy@personaluse.ounsjuz.mongodb.net/?retryWrites=true&w=majority"
DB = MongoClient(DB_URL)
DATABASE = DB.MAIN
