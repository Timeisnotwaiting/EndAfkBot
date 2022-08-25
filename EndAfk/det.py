from pyrogram import Client
from config import BOT_USERNAME

async def det(Client):
    Le = await Client.get_me()
    UN = Le["username"]
    id = Le["id"]
    BOT_DET = []
    BOT_DET.append(UN)
    BOT_DET.append(id)
    return BOT_DET
    
