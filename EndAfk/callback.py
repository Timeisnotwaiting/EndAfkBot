from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from EndAfk.AlphaDB.cleanmode import *
from pyrogram.errors import *
from .helpers import settings_markup

@Client.on_callback_query(filters.regex("close"))
async def on_close_button(client, CallbackQuery):
    await CallbackQuery.answer()
    await CallbackQuery.message.delete()

@Client.on_callback_query(filters.regex("cleanmode_answer"))
async def on_cleanmode_button(client, CallbackQuery):
    await CallbackQuery.answer("⁉️ What is This?\n\nWhen activated, Bot will delete its message after 5 Mins to make your chat clean and clear.", show_alert=True)

@Client.on_callback_query(filters.regex("settings_callback"))
async def on_settings_button(client, CallbackQuery):
    await CallbackQuery.answer()
    status = await is_cleanmode_on(CallbackQuery.message.chat.id)
    buttons = settings_markup(status)
    return await CallbackQuery.edit_message_text(f"⚙️ **AFK Bot Settings**\n\n🖇**Group:** {CallbackQuery.message.chat.title}\n🔖**Group ID:** `{CallbackQuery.message.chat.id}`\n\n💡**Choose the function buttons from below which you want to edit or change.**", reply_markup=InlineKeyboardMarkup(buttons),)

@Client.on_callback_query(filters.regex("CLEANMODE"))
async def on_cleanmode_change(client, CallbackQuery):
    admin = await app.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if admin.status in ["creator", "administrator"]:
        pass
    else:
        return await CallbackQuery.answer("Only Admins can perform this action.", show_alert=True)
    await CallbackQuery.answer()
    status = None
    if await is_cleanmode_on(CallbackQuery.message.chat.id):
        await cleanmode_off(CallbackQuery.message.chat.id)
    else:
        await cleanmode_on(CallbackQuery.message.chat.id)
        status = True
    buttons = settings_markup(status)
    try:
        return await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
    except MessageNotModified:
        return
