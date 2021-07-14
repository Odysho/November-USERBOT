import asyncio
import os
import random
from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from . import ALIVE_NAME, deEmojify

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "icss"

CARBONLANG = "auto"
LANG = "en"


@icssbot.on(admin_cmd(outgoing=True, pattern="كاربون(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="كاربون(?: |$)(.*)", allow_sudo=True))
async def carbon_api(e):
    """ A Wrapper for carbon.now.sh """
    await e.edit("**⌔∮ جاري المعالجه.. **")
    CARBON = "https://carbon.now.sh/?l={lang}&code={code}"
    textx = await e.get_reply_message()
    pcode = e.text
    if pcode[8:]:
        pcode = str(pcode[8:])
    elif textx:
        pcode = str(textx.message)  # Importing message to module
    pcode = deEmojify(pcode)
    code = quote_plus(pcode)  # Converting to urlencoded
    cat = await edit_or_reply(e, "**⌔∮ جاري انشاء الكاربون** \n25%")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = Config.CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        executable_path=Config.CHROME_DRIVER, options=chrome_options
    )
    driver.get(url)
    await cat.edit("**⌔∮ انتظر قليلا** \n50%")
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    # driver.find_element_by_xpath("//button[contains(text(),'4x')]").click()
    # driver.find_element_by_xpath("//button[contains(text(),'PNG')]").click()
    await cat.edit("⌔**∮ جاري المعالجه**\n75%")
    # Waiting for downloading
    await asyncio.sleep(2)
    await cat.edit("**⌔∮ تم انشاء الكاربون**\n100%")
    file = "./carbon.png"
    await cat.edit("**⌔∮ جاري التنزيل**")
    await e.client.send_file(
        e.chat_id,
        file,
        caption="**⌔∮ هذا هو الكاربون الخاص بك,** \n **تم انشاء هذا الكاربون بواسطه نوفمبر. **",
        force_document=True,
        reply_to=e.message.reply_to_msg_id,
    )
    os.remove("./carbon.png")
    driver.quit()
    # Removing carbon.png after uploading
    await cat.delete()




CMD_HELP.update(
    {
        "carbon": "**Plugin : **`carbon`\
    \n\n**Commands are :** \
    \n  •  `.carbon <reply to code>`\
    \n  •  `.krb <reply to code>`\
    \n  •  `.kar1 <reply to code>`\
    \n  •  `.kar2 <reply to code>`\
    \n  •  `.kar3 <reply to code>`\
    \n  •  `.kar4 <reply to code>`\
    \n  •  `.rgbk2 <reply to code>`\
    \n  •  `.kargb <reply to code>`\
    \n\n**Function : **\
    \n__Carbon generators, each command has one style of carbon (krb ,kargb shows random carbons, remaining all are fixed)__\
    "
    }
)
