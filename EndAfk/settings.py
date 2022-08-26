from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery as q, InlineKeyboardMarkup as IKM, InlineKeyboardButton as IKB, InputMediaPhoto as IMP
from .det import det
from config import OWNER_USERNAME
from .AlphaDB.cleanmode import *

level = None
botid = None
chid = None
chill = None

SETTINGS1 = [
            [IKB(" 🤵 Owner", url=f"t.me/{OWNER_USERNAME[1:]}"),
             IKB(" 🛠 Settings", callback_data="settings2"),
            ]
            ]

async def check_admin(_, m):
    mem = await _.get_chat_member(m.chat.id, m.from_user.id)
    if mem.can_delete_messages():
        return True
    return False

async def check_cbq_admin(_, q):
    mem = await _.get_chat_member(q.message.chat.id, q.from_user.id)
    if mem.can_delete_messages():
        return True
    return False
        
admins = None 

@Client.on_message(filters.command("settings") & filters.group)
async def settings(_, m):
    global chid
    global chill
    global botid
    global level
    level = m.from_user.id
    chid = m.chat.id
    chill = m.chat.title
    d = await det(_)
    botid = d[1]
    name = (await _.get_users(d[1])).first_name
    try:
        await m.reply_photo("https://te.legra.ph/file/7637e88a7367abb6336d5.jpg", caption=f"""Hello! My name is {name}

To know more about me check help section.""", reply_markup=IKM(SETTINGS1))
    except Exception as e:
        await m.reply(e)

TEXT_2 = """⚙️ AFK Bot Settings

🖇Group: {}
🔖Group ID: {}

💡Choose the function buttons from below which you want to edit or change."""

SETTINGS2_E = [
            [
             IKB("🔁 Clean Mode", callback_data="CM"),
             IKB("✅ Enabled", callback_data="toggle_disbale"),
            ]
            ]

SETTINGS2_D = [
            [
             IKB("🔁 Clean Mode", callback_data="CM"),
             IKB("❌ Disabled", callback_data="toggle_enable"),
            ]
            ]

@Client.on_callback_query()
async def cbq(_, q):
    global level
    global admins
    global chid
    global chill
    if q.data == "settings2":
        if not check_cbq_admin(_, q):
            return await q.answer("You must be admin of this group..!", show_alert=True)
        if await cme(chid):
            coded = f"<code>{chid}</code>"
            med = IMP(SP, caption=TEXT_2.format(chill, coded))
            await _.edit_message_media(chat_id=q.message.chat.id, message_id=q.message.message_id, media = med, reply_markup=IKM(SETTINGS2_E))
        else:
            coded = f"<code>{chid}</code>"
            med = IMP(SP, caption=TEXT_2.format(chill, coded))
            await _.edit_message_media(chat_id=q.message.chat.id, message_id=q.message.message_id, media = med, reply_markup=IKM(SETTINGS2_D))
    elif q.data == "toggle_disable":
        if not check_cbq_admin(_, q):
            return await q.answer("You must be admin of this group..!", show_alert=True)
        await scd(chid)
        coded = f"<code>{chid}</code>"
        med = IMP(SP, caption=TEXT_2.format(chill, coded))
        await _.edit_message_media(chat_id=q.message.chat.id, message_id=q.message.message_id, media = med, reply_markup=IKM(SETTINGS2_D))
    elif q.data == "toggle_enable":
        if not check_cbq_admin(_, q):
            return await q.answer("You must be admin of this group..!", show_alert=True)
        await sce(chid)
        coded = f"<code>{chid}</code>"
        med = IMP(SP, caption=TEXT_2.format(chill, coded))
        await _.edit_message_media(chat_id=q.message.chat.id, message_id=q.message.message_id, media = med, reply_markup=IKM(SETTINGS2_E))
    elif q.data == "CM":
        return await q.answer("Delete messages sent by bot after 5min, to keep the chat clean...", show_alert=True)
    

@Client.on_message(group=6)
async def alone(_, m):
    global botid
    if m.from_user.id == botid:
        time.sleep(10)
        await m.delete()
