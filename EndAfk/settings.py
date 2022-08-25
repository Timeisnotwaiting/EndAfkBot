from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup as IKM, InlineKeyboardButton as IKB
from .det import det

SETTINGS1 = [
            [IKB(" 🤵 Owner", url=f"t.me/{OWNER_USERNAME[1:]}"),
             IKB(" 🛠 Settings", data="settings2"),
            ]
            ]

@Client.on_message(filters.command("settings") & filters.group)
async def settings(_, m):
    d = await det(_)
    name = (await _.get_users(d[1])).first_name
    await m.reply_photo("https://te.legra.ph/file/7637e88a7367abb6336d5.jpg", caption=f"""Hello! My name is {name}

To know more about me check help section.""", reply_markup=IKM(SETTINGS1))
