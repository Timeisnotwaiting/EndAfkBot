from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup as IKM, InlineKeyboardButton as IKB, InputMediaPhoto as IMP
from .det import det
from config import OWNER_USERNAME
from .AlphaDB.cleanmode import *

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

TEXT_2 = """⚙️ AFK Bot Settings

🖇Group: {}
🔖Group ID: {}

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
async def cbq(_, q, m: Message):
    global level
    global admins
    if q.data == "settings2":
        if q.from_user.id != admins:
            return await q.answer()
        if await cme(m.chat.id):
            coded = f"<code>{m.chat.id}</code>"
            med = IMP(SP, caption=TEXT_2.format(m.chat.title, coded))
            await q.edit_message_media(media = med, reply_markup=IKM(SETTINGS2_E))
        else:
            coded = f"<code>{m.chat.id}</code>"
            med = IMP(SP, caption=TEXT_2.format(m.chat.title, coded))
            await q.edit_message_media(media = med, reply_markup=IKM(SETTINGS2_D))
    elif q.data == "toggle_disable":
        if q.from_user.id != admins:
            return await q.answer()
        await scd(m.chat.id)
        coded = f"<code>{m.chat.id}</code>"
        med = IMP(SP, caption=TEXT_2.format(m.chat.title, coded))
        await q.edit_message_media(media = med, reply_markup=IKM(SETTINGS2_D))
    elif q.data == "toggle_enable":
        if q.from_user.id != admins:
            return await q.answer()
        await sce(m.chat.id)
        coded = f"<code>{m.chat.id}</code>"
        med = IMP(SP, caption=TEXT_2.format(m.chat.title, coded))
        await q.edit_message_media(media = med, reply_markup=IKM(SETTINGS2_E))
    elif q.data == "CM":
        return await q.answer("Deleted messages sent by bot after 5min, to keep the chat clean...", show_alert=True)
    

@Client.on_message(group=6)
async def alone(_, m):
    d = await det(_)
    if m.from_user.id == d[1]:
        time.sleep(10)
        await m.delete()
