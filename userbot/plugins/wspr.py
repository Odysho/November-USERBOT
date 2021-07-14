from . import reply_id as rd
from userbot.tosh import *


WPIC = "https://telegra.ph/file/dfd7fc05a81748a87761c.jpg"
T = "**⌔∮ قائـمه اوامر الهمسه :** \n\n\n⪼ `.الهمسة`للإرسال من بوتك\n⪼ `.همسة` للإرسال عن طريق بوت الهمسة  \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\nՏøuƦcε πøνεʍβεƦ 🌦⪼ [𝐃𝐄𝐕](http://t.me/oorrr)"

@icssbot.on(icss_cmd(pattern="م21"))
async def wspr(kimo):
    await eor(kimo, T)


@icssbot.on(icss_cmd(outgoing=True, pattern="الهمسة$"))
async def kimo(lon):
    if lon.fwd_from:
        return
    ld = await rd(lon)
    if WPIC:
        ics_c = f"اذا تريد ترسل همسه من خلال البوت الخاص بك يجب كتابه اولا #معرف_البوت ثم #secret ثم تكتب #معرف_الي_تريد_تهمسله ثم #الرساله وستضهر ايقونه وتضغط عليها وبس 🖤✨.\n"
        ics_c += f"**- قم بنسخ :**\n `{TBOT} secret @OORRR الرساله`"
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=ld)
        await lon.delete()   

@icssbot.on(
    icss_cmd(pattern="همسة ?(.*)")
)
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    bu = "@nnbbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(bu, wwwspr) 
    await tap[0].click(event.chat_id)
    await event.delete()
