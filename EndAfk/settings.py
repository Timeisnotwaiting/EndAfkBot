from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup as IKM, InlineKeyboardButton as IKB, InputMediaPhoto as IMP
from .det import det
from config import OWNER_USERNAME
import time

level = None

SETTINGS1 = [
            [IKB(" 🤵 Owner", url=f"t.me/{OWNER_USERNAME[1:]}"),
             IKB(" 🛠 Settings", data="settings2"),
            ]
            ]

async def get_admin_list(_, m):
    ADMINS = []
    async for member in _.iter_chat_members(m.chat.id, filters="administrators"):
        ADMINS.append(member.user.id)
        return ADMINS
        
 admins = None 

@Client.on_message(filters.command("settings") & filters.group)
async def settings(_, m):
    global admins
    global level
    admins = await get_admin_list(_, m)
    if not m.from_user.id in admins:
        return 
    level = m.from_user.id
    d = await det(_)
    name = (await _.get_users(d[1])).first_name
    await m.reply_photo("https://te.legra.ph/file/7637e88a7367abb6336d5.jpg", caption=f"""Hello! My name is {name}

To know more about me check help section.""", reply_markup=IKM(SETTINGS1))

TEXT_2 = f"""⚙️ AFK Bot Settings

🖇Group: {m.chat.title}
🔖Group ID: {m.chat.id}

💡Choose the function buttons from below which you want to edit or change."""

SETTINGS2_E = [
            [
             IKB("🔁 Clean Mode", data="CM"),
             IKB("✅ Enabled", data="toggle_disbale"),
            ]
            ]

SETTINGS2_D = [
            [
             IKB("🔁 Clean Mode", data="CM"),
             IKB("❌ Disabled", data="toggle_enable"),
            ]
            ]

@Client.on_callback_query()
async def cbq(_, q):
    global level
    global admins
    if q.from_user.id != admins:
        return
    
