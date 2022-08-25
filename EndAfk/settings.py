from pyrogram import Client, filters
from pyrogram.types import Message
from .det import det

@Client.on_message(filters.command("settings") & filters.group)
async def settings(_, m):
    d = await det(_)
    name = (await _.get_users(d[1])).first_name
    await m.reply(f"""Hello! My name is {name}

To know more about me check help section.""")
