from pyrogram import Client as Alpha, filters
from pyrogram.types import Message
from EndAfk import SUDOERS
from .det import det


@Alpha.on_message(filters.command(f"leave") & filters.user(SUDOERS))
async def leave(_, m):
    if len(m.command) == 2:
        ch_id = int(m.text.split()[1])
    else:
        ch_id = m.chat.id
    try:
        ok = await m.reply("<code>Leaving chat...</code>")
        await _.leave_chat(ch_id)
    except Exception as e:
        await ok.edit(e)


        
