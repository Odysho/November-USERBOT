# اكس او
U = "𓆰 sᴏᴜʀᴄᴇ 𝞝 ɴᴏᴠᴇᴍʙᴇʀ - 𝑪𝑶𝑴𝑴𝑬𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⌔∮ قائـمه اوامر الالعاب :** \n⪼ `.اكس او` \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n𓆩 sᴏᴜʀᴄᴇ 𝞝 ɴᴏᴠᴇᴍʙᴇʀ - [𝐃𝐄𝐕](t.me/oorrr) 𓆪"

@icssbot.on(icss_cmd(pattern="م22"))
async def wspr(kimo):
    await eor(kimo, U)

@icssbot.on(
    icss_cmd(
       pattern="اكس او$"
    )
)

async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()
