from pyrogram import Client
from config import BOT_USERNAME

async def det(_):
    Le = await _.get_me()
    UN = Le["username"]
    id = Le["id"]
    FN = Le["first_name"]
    BOT_DET = []
    BOT_DET.append(UN)
    BOT_DET.append(id)
    BOT_DET.append(FN)
    return BOT_DET
    
