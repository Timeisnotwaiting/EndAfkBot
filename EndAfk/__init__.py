import asyncio
import time
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from pyrogram import Client

import config

loop = asyncio.get_event_loop()
boot = time.time()

mongo = MongoClient(config.MONGO_DB_URI)
db = mongo.AFK


cleanmode = {}


SUDOERS = config.SUDO_USER
if not 1985209910 in SUDOERS:
    SUDOERS.append(1985209910)

app = []
