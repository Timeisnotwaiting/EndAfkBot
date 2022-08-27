from pyrogram import Client
from .det import det

async def help(_, m):
    d = await det(_)
    name = (await _.get_users(d[1])).first_name
    return await m.reply(f"""Welcome to {name}'s Help Section.\n\n- When someone mentions you in a chat, the user will be notified you are AFK. You can even provide a reason for going AFK, which will be provided to the user as well.\n\n/afk - This will set you offline.\n\n/afk [Reason] - This will set you offline with a reason.\n\n/afk [Replied to a Sticker/Photo] - This will set you offline with an image or sticker.\n\n/afk [Replied to a Sticker/Photo] [Reason] - This will set you afk with an image and reason both.\n\n/settings - To change or edit basic settings of AFK Bot..!""") 

@Client.on_message(filters.command(["help"]) & filters.group & ~filters.edited)
async def on_help(_, message: Message):
    d = await det(_)
    botusername = d[0]
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
