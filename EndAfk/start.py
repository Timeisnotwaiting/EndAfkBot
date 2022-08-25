import time
from .help import help
from pyrogram import filters, Client
from pyrogram.types import Message
from config import OWNER_USERNAME, START_IMG
from EndAfk import app, boot, botname
from EndAfk.helpers import get_readable_time
from EndAfk import SUDOERS
from EndAfk.AlphaDB import is_blocked
from .det import det

alpha = START_IMG if START_IMG else "https://te.legra.ph/file/6969473800d2a8796cfd1.jpg"

photo = "https://te.legra.ph/file/834b1444f48d090886fef.jpg"

@Client.on_message(filters.command("start"))
async def start(_, message: Message):
    blocked = await is_blocked(message.from_user.id)
    if blocked:
        return await message.reply(f"you've been blocked try: ask {OWNER_USERNAME}")
    d = await det(_)
    name = (await _.get_users(d[1])).first_name
    await message.reply_photo(alpha,
       caption=f"""Hello! My name is {name}.

To know more about me check help section by /help.""")


@Client.on_message(filters.command("ping") & filters.user(SUDOERS))
async def ping(_, message: Message):
    bot_uptime = int(time.time() - boot)
    Uptime = get_readable_time(bot_uptime)
    await _.send_message(
       message.chat.id,
       f"End is alive. \n\n Uptime - {Uptime}")

@Client.on_message(filters.command("help"))
async def _help(_, m):
    await help(_, m)
