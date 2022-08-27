import time
import random

from pyrogram import filters, Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import MessageNotModified
from config import START_IMG
from EndAfk.AlphaDB.blocked import is_blocked
from EndAfk.AlphaDB.cleanmode import cleanmode_off, cleanmode_on, is_cleanmode_on
from .helpers import get_readable_time, put_cleanmode, settings_markup, RANDOM, HELP_TEXT


@Client.on_message(filters.command(["start", "settings"]) & filters.group & ~filters.edited)
async def on_start(_, message: Message):
    huh = await is_blocked(message.from_user.id)
    if huh:
        return 
    smex = await det(_)
    botname = smex[2]
    botid = smex[1]
    botusername = smex[0]
    bot_uptime = int(time.time() - boot)
    Uptime = get_readable_time(bot_uptime)
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="📜 Help Section",
                    url=f"https://t.me/{botusername}?start=help",
                ),
                InlineKeyboardButton(
                    text="🔧 Settings",
                    callback_data="settings_callback",
                ),
            ]
        ]
    )
    image = random.choice(RANDOM)
    send = await message.reply_photo(image, caption=f"Hello! My name is {botname}.\n\nTo know more about me check help section. Active since {Uptime}", reply_markup=upl)
    await put_cleanmode(message.chat.id, send.message_id)
    

@Client.on_message(filters.command(["help"]) & filters.group & ~filters.edited)
async def on_help(_, message: Message):
    huh = await is_blocked(message.from_user.id)
    if huh:
        return 
    smex = await det(_)
    botname = smex[2]
    botid = smex[1]
    botusername = smex[0]
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="📜 Help Section",
                    url=f"https://t.me/{botusername}?start=help",
                ),
            ]
        ]
    )
    send = await message.reply_text("Contact me in PM for help.", reply_markup=upl)
    await put_cleanmode(message.chat.id, send.message_id)

@Client.on_message(filters.command(["start"]) & filters.private & ~filters.edited)
async def on_private_start(_, message: Message):
    huh = await is_blocked(message.from_user.id)
    if huh:
        return await m.reply(f"You're blocked to use this bot \n\n Contact ~ {OWNER_USERNAME}")
    smex = await det(_)
    botname = smex[2]
    botid = smex[1]
    botusername = smex[0]
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            return await message.reply_text(HELP_TEXT)
    else:
        bot_uptime = int(time.time() - boot)
        Uptime = get_readable_time(bot_uptime)
        upl = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="➕ Add me to a Group",
                        url=f"https://t.me/{botusername}?startgroup=true",
                    ),
                ]
            ]
        )
        image = START_IMG if START_IMG else random.choice(RANDOM)
        await message.reply_photo(image, caption=f"Hello! My name is {botname}.\n\nTo know more about me check help section by /help. Active since {Uptime}", reply_markup=upl)

@Client.on_message(filters.command(["help"]) & filters.private & ~filters.edited)
async def on_private_help(_, message: Message):
    smex = await det(_)
    botname = smex[2]
    botid = smex[1]
    botusername = smex[0]
    return await message.reply_text(HELP_TEXT.format(botname))
