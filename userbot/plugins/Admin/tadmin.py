from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from ...utils import errors_handler
from .. import BOTLOG, BOTLOG_CHATID, extract_time, get_user_from_event

NO_ADMIN = "**↫ عذرًا انا لست مشرفًا هنا ⁂**"
NO_PERM = "**⏎ عذرًا ليست لدي صلاحيات لتنفيذ الامر ✘**"


@icssbot.on(admin_cmd(pattern=r"كتمه(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern=r"كتمه(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def tmuter(kimo):
    chat = await kimo.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # If not admin and not creator, return
    if not admin and not creator:
        await edit_or_reply(kimo, NO_ADMIN)
        return
    icse = await edit_or_reply(kimo, "**⏎سيتم الكتم انتظر من فضلك ... √**")
    user, reason = await get_user_from_event(kimo, icse)
    if not user:
        return
    if reason:
        reason = reason.split(" ", 1)
        hmm = len(reason)
        icst = reason[0]
        reason = reason[1] if hmm == 2 else None
    else:
        await icse.edit("**⏎ لم تذكر الوقت!\n لمعرفة كيفية كتابة الامر :**`.info tadmin`")
        return
    self_user = await kimo.client.get_me()
    itime = await extract_time(kimo, icst)
    if not itime:
        await icse.edit(
            f"Invalid time type specified. Expected m , h , d or w not as {icst}"
        )
        return
    if user.id == self_user.id:
        await icse.edit(f"Sorry, I can't mute myself")
        return
    try:
        await icse.client(
            EditBannedRequest(
                kimo.chat_id,
                user.id,
                ChatBannedRights(until_date=itime, send_messages=True),
            )
        )
        # Announce that the function is done
        if reason:
            await icse.edit(
                f"{_format.mentionuser(user.first_name ,user.id)} was muted in {kimo.chat.title}\n"
                f"**Muted for : **{icst}\n"
                f"**Reason : **__{reason}__"
            )
            if BOTLOG:
                await kimo.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{kimo.chat.title}(`{kimo.chat_id}`)\n"
                    f"**Muted for : **`{icst}`\n"
                    f"**Reason : **`{reason}``",
                )
        else:
            await icse.edit(
                f"{_format.mentionuser(user.first_name ,user.id)} was muted in {kimo.chat.title}\n"
                f"Muted for {icst}\n"
            )
            if BOTLOG:
                await kimo.client.send_message(
                    BOTLOG_CHATID,
                    "#TMUTE\n"
                    f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                    f"**Chat : **{kimo.chat.title}(`{kimo.chat_id}`)\n"
                    f"**Muted for : **`{icst}`",
                )
        # Announce to logging group
    except UserIdInvalidError:
        return await icse.edit("`Uh oh my mute logic broke!`")
    except UserAdminInvalidError:
        return await icse.edit(
            "`Either you're not an admin or you tried to mute an admin that you didn't promote`"
        )
    except Exception as e:
        return await icsw.edit(f"`{str(e)}`")


@icssbot.on(admin_cmd(pattern="tban(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="tban(?: |$)(.*)", allow_sudo=True))
@errors_handler
async def ban(kimo):
    chat = await kimo.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    # If not admin and not creator, return
    if not admin and not creator:
        await edit_or_reply(kimo, NO_ADMIN)
        return
    icse = await edit_or_reply(kimo, "`banning....`")
    user, reason = await get_user_from_event(kimo, icse)
    if not user:
        return
    if reason:
        reason = reason.split(" ", 1)
        tosh = len(reason)
        icst = reason[0]
        reason = reason[1] if tosh == 2 else None
    else:
        await icse.edit("**⏎ لم تذكر الوقت!\n لمعرفة كيفية كتابة الامر :**`.info tadmin`")
        return
    self_user = await kimo.client.get_me()
    itime = await extract_time(kimo, icst)
    if not itime:
        await icse.edit(
            f"Invalid time type specified. Expected m , h , d or w not as {icst}"
        )
        return
    if user.id == self_user.id:
        await icse.edit(f"Sorry, I can't ban myself")
        return
    await icse.edit("`Whacking the pest!`")
    try:
        await kimo.client(
            EditBannedRequest(
                kimo.chat_id,
                user.id,
                ChatBannedRights(until_date=itime, view_messages=True),
            )
        )
    except UserAdminInvalidError:
        return await icse.edit(
            "`Either you're not an admin or you tried to ban an admin that you didn't promote`"
        )
    except BadRequestError:
        await icse.edit(NO_PERM)
        return
    try:
        reply = await kimo.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await icse.edit("`I dont have message nuking rights! But still he was banned!`")
        return
    if reason:
        await icse.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} was banned in {kimo.chat.title}\n"
            f"banned for {icst}\n"
            f"Reason:`{reason}`"
        )
        if BOTLOG:
            await kimo.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{kimo.chat.title}(`{kimo.chat_id}`)\n"
                f"**Banned untill : **`{icst}`\n"
                f"**Reason : **__{reason}__",
            )
    else:
        await icse.edit(
            f"{_format.mentionuser(user.first_name ,user.id)} was banned in {kimo.chat.title}\n"
            f"banned for {icst}\n"
        )
        if BOTLOG:
            await kimo.client.send_message(
                BOTLOG_CHATID,
                "#TBAN\n"
                f"**User : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**Chat : **{kimo.chat.title}(`{kimo.chat_id}`)\n"
                f"**Banned untill : **`{icst}`",
            )


CMD_HELP.update(
    {
        "tadmin": "**Plugin :** `tadmin`\
      \n\n•  **Syntax : **`.tmute <reply/username/userid> <time> <reason>`\
      \n•  **Function : **__Temporary mutes the user for given time.__\
      \n\n•  **Syntax : **`.tban <reply/username/userid> <time> <reason>`\
      \n•  **Function : **__Temporary bans the user for given time.__\
      \n\n•  **Time units : ** __(2m = 2 minutes) ,(3h = 3hours)  ,(4d = 4 days) ,(5w = 5 weeks)\
      These times are example u can use anything with those units __"
    }
)
