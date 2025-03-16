import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "7682036592:AAE-CgfXgoBjN6JM_FPSRbkUA4UTPE3h0Rg")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1001906981230))

OWNER_ID = int(getenv("OWNER_ID", 8115484618))

OWNER = int(getenv("OWNER", 8115484618))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HK543fklqxgt66hvxf")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/URANIUM11011/ALEXAYTZ",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TheMenXD")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+gTnkINaHa98wZTI1")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = "BQGV228AqLDxqYhJoOreMLchcvCv_EA5Dw5X4YKZyrwmUgkG8NYgcN15U-Xq8WGEnLwLryxIPq6LapiIo7MJd5ms7VoNQrun721FTReFZTkzIAVbv8W3HbUjFHeoOF_Cu19dTGGIJFJcC_scyw3Ii9-1fhsLtV7jn6cQWATihDUuDgHQVsSDSW8n2Fr3gDdTBCcvNFirNd91lSfXzckoA6Bv2B3PKY9MR5bFG8qPW4fWY9x3M-wJc0SsdaVVJj859UoHodHf8LX44upyfb3nMQmIot7yzOwy5ErLXDg7n-7rAYwue9DCiFJq2Bihkp5qvBFXfIGJrH4O8e_WhrQqD5S-3zdV-QAAAAErXXWAAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/nwxoo8.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/nwxoo8.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://files.catbox.moe/nwxoo8.jpg")
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/nwxoo8.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/nwxoo8.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/nwxoo8.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/nwxoo8.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/nwxoo8.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/nwxoo8.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/nwxoo8.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/nwxoo8.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
