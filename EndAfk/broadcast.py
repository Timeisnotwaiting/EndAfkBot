import asyncio

from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from EndAfk import SUDOERS, app
from EndAfk.AlphaDB import get_afk_users, get_served_chats


@Client.on_message(filters.command("afkusers") & filters.user(SUDOERS))
async def total_users(_, message: Message):
    afk_users = []
    try:
        chats = await get_afk_users()
        for chat in chats:
            afk_users.append(int(chat["user_id"]))
    except Exception as e:
        return await message.reply_text(f"**Error:-** {e}")

    afk_users_msg = f"Afk users :- {len(afk_users)}"
    await message.reply_text(afk_users_msg)


@Client.on_message(filters.command("broadcast") & filters.user(SUDOERS))
async def broadcast(_, message):
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    pinned = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            if message.reply_to_message:
                ok = await _.forward_messages(i, y, x)
                sent += 1
                try:
                    await _.pin_chat_message(i, ok.message_id)
                    pinned += 1
                except:
                    continue 
            else:
                ok = await _.send_message(i, query)
                sent += 1
                try:
                    await _.pin_chat_message(i, ok.message_id)
                    pinned += 1
                except:
                    continue
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await message.reply_text(
            f"**Broadcasted Message In {sent} Chats and pinned in {str(pinned)} Chats**"
        )
    except:
        pass

@Client.on_message(filters.command("schats") & filters.user(SUDOERS) & ~filters.edited & ~filters.forwarded)
async def schats(_, m: Message):
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
        if str(chat) == "-1001680465920":
            chats.remove((chat))
    msg = ""
    for i in chats:
        i = str(i)
        msg += f"\n<code>{i}</code>"
    await m.reply(f"**Served chats** :-\n{msg}\n\n**Count** :- {len(chats)}")
