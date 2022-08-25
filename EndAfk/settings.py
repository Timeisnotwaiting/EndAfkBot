from pyrogram import Client, filters
from pyrogram.types import Message
from .det import det

@Client.on_message(filters.command("settings") & filters.group)
async def settings(_, m):
    d = await det(_)
    
