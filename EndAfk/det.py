from pyrogram import Client

async def det(Client):
    id = (await Client.get_users(BOT_USERNAME)).id
    BOT_DET = []
    BOT_DET.append(BOT_USERNAME)
    BOT_DET.append(id)
    return BOT_DET
