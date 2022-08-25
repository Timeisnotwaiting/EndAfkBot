import config
import logging
from pyromod import listen
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
import asyncio

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


app = Client(
    ":EndAfkBot:",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="EndAfk"),
)

app.start()
BOT_DET = []
UN = app.get_me().username
ID = app.get_me().id
BOT_DET.append(UN)
BOT_DET.append(ID)
idle()
print(f"@{UN} started successfully...")

