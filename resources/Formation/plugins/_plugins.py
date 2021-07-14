import math
import os
import re
import time
import heroku3
import lottie
import requests

import spamwatch as spam_watch
from validators.url import url

from platform import python_version
from telethon import version

from userbot import *
from userbot.Config import Config
from userbot.helpers import *
from userbot.helpers import _format, _icsstools, _icssutils


USERID = bot.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
AUTONAME = Config.AUTONAME
DEFAULT_BIO = Config.DEFAULT_BIO
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Icss Userbot"
BOT_USERNAME = Config.TG_BOT_USERNAME
ICSBOT = Config.TG_BOT_USERNAME
ICSB = Config.TG_BOT_USERNAME


# mention user
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{DEFAULTUSER}</a>"

TOSHA_NAME = bot.me.first_name
TOSHA_ID = bot.me.id

# Dev tag
tosh = ( 
    "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧˢᵃᑫᵗⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    "↬[- M𝙴𝙼𝙸𝙰𝙽 ODY 𐇰.](t.me/OORRR)༗\n"
    "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧˢᵃᑫᵗⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
)

# Repo 
R = (
    "⌔∮ 𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐒𝐀𝐐𝐓 - 𝙍𝙀𝙋𝙊 𓆪 \n"
    "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    "- 𝐃𝐄𝐕 𝐒𝐎𝐔𝐑𝐂𝐄 ⪼ [- M𝙴𝙼𝙸𝙰𝙽 ODY 𐇰.](t.me/OORRR) ⩫ \n"
    "- 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ⪼ [┊ɴᴏᴠᴇᴍʙᴇʀ 💞' •](T.ME/NNEEE) ⩫"
)
K = "https://github.com/ANL0KE/SAQT-USERBOT"

# Alive Bot 
TOSH = (
       f"**⌔∮ بوت  تليثون نوفمبر ɴᴏᴠᴇᴍʙᴇʀ يعمل بنجاح 🖤❕**\n"
       f"**   - اصدار التليثون :** `{version.__version__}\n`"
       f"**   - اصدار ɴᴏᴠᴇᴍʙᴇʀ :** `{icsv}`\n"
       f"**   - البوت المستخدم :** `{ICSB}`\n"
       f"**   - اصدار البايثون :** `{python_version()}\n`"
       f"**   - المستخدم :** {mention}\n"
)

# send 
Send = "**⌔∮ اسم الاضافه : {}**\n**⌔∮ الوقت المستغرق : {}ثانيه**\n**⌔∮ للمستخدم :** {}"

# mybot
Mb = "**⌔∮ البوت المستخدم - {}**"

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY

thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")

PM_START = []
PMMESSAGE_CACHE = {}
PMMENU = "pmpermit_menu" not in Config.NO_LOAD

if Config.PRIVATE_GROUP_BOT_API_ID == 0:
    BOTLOG = False
    BOTLOG_CHATID = "me"
else:
    BOTLOG = True
    BOTLOG_CHATID = Config.PRIVATE_GROUP_BOT_API_ID

# Gdrive
G_DRIVE_CLIENT_ID = Config.G_DRIVE_CLIENT_ID
G_DRIVE_CLIENT_SECRET = Config.G_DRIVE_CLIENT_SECRET
G_DRIVE_DATA = Config.G_DRIVE_DATA
G_DRIVE_FOLDER_ID = Config.G_DRIVE_FOLDER_ID
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

# spamwatch support
if Config.SPAMWATCH_API:
    token = Config.SPAMWATCH_API
    spamwatch = spam_watch.Client(token)
else:
    spamwatch = None

ics_users = [bot.uid]
if Config.SUDO_USERS:
    for user in Config.SUDO_USERS:
        ics_users.append(user)


# ================================================

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


# thumb image
if Config.THUMB_IMAGE is not None:
    check = url(Config.THUMB_IMAGE)
    if check:
        try:
            with open(thumb_image_path, "wb") as f:
                f.write(requests.get(Config.THUMB_IMAGE).content)
        except Exception as e:
            LOGS.info(str(e))


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif isinstance(dictionary[key], list):
        if value in dictionary[key]:
            return
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]


def check_data_base_heal_th():
    is_database_working = False
    output = "لا توجد اي قاعدة بيانات"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "قاعده البيانات تعمل بنجاح"
        is_database_working = True
    return is_database_working, output


async def icsa():
    _, check_sgnirts = check_data_base_heal_th()
    sudo = "Enabled" if Config.SUDO_USERS else "Disabled"
    uptime = await get_readable_time((time.time() - StartTime))
    try:
        useragent = (
            "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/80.0.3987.149 Mobile Safari/537.36"
        )
        user_id = Heroku.account().id
        headers = {
            "User-Agent": useragent,
            "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
            "Accept": "application/vnd.heroku+json; version=3.account-quotas",
        }
        path = "/accounts/" + user_id + "/actions/get-quota"
        r = requests.get(heroku_api + path, headers=headers)
        result = r.json()
        quota = result["account_quota"]
        quota_used = result["quota_used"]

        # Used
        remaining_quota = quota - quota_used
        math.floor(remaining_quota / quota * 100)
        minutes_remaining = remaining_quota / 60
        hours = math.floor(minutes_remaining / 60)
        minutes = math.floor(minutes_remaining % 60)
        # Current
        App = result["apps"]
        try:
            App[0]["quota_used"]
        except IndexError:
            AppQuotaUsed = 0
        else:
            AppQuotaUsed = App[0]["quota_used"] / 60
            math.floor(App[0]["quota_used"] * 100 / quota)
        AppHours = math.floor(AppQuotaUsed / 60)
        AppMinutes = math.floor(AppQuotaUsed % 60)
        dyno = f"{AppHours}h {AppMinutes}m/{hours}h {minutes}m"
    except Exception as e:
        dyno = e
    return f"**⌔∮ معلومات البوت***\
                 \n - قاعده البيانات : {check_sgnirts}\
                  \n - سودو : {sudo}\
                  \n - مدة التشغيل : {uptime}\
                  \n - مده الاستخدام : {dyno}\
                  "


async def make_gif(event, reply, quality=None, fps=None):
    fps = fps or 1
    quality = quality or 256
    result_p = os.path.join("temp", "animation.gif")
    animation = lottie.parsers.tgs.parse_tgs(reply)
    with open(result_p, "wb") as result:
        await _icssutils.run_sync(
            lottie.exporters.gif.export_gif, animation, result, quality, fps
        )
    return result_p
