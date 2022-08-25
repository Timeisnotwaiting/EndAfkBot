from pyrogram import Client
from .det import det

async def help(_, m):
    d = await det(_)
    name = (await _.get_users(d[1]).first_name
    await m.reply(f"""Welcome to {name}'s Help Section.

- When someone mentions you in a chat, the user will be notified you are AFK. You can even provide a reason for going AFK, which will be provided to the user as well.


/afk - This will set you offline.

/afk [Reason] - This will set you offline with a reason.

/afk [Replied to a Sticker/Photo] - This will set you offline with an image or sticker.

/afk [Replied to a Sticker/Photo] [Reason] - This will set you afk with an image and reason both.


/settings - To change or edit basic settings of AFK Bot."""
