from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

SUDO_USER = list(
    map(int, getenv("SUDO_USER", "").split())
) 

OWNER_USERNAME = getenv("OWNER_USERNAME", "@Timeisnotwaiting")

if not OWNER_USERNAME[0] == "@":
    OWNER_USERNAME = "@" + OWNER_USERNAME

START_IMG = getenv("START_IMG")

NEW_CHAT_IMG = getenv("NEW_CHAT_IMG", "https://te.legra.ph/file/bb228a198c41e90761d96.jpg")

BOT_USERNAME = getenv("BOT_USERNAME", "@EndAfkBot")
