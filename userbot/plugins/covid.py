from covid import Covid

from . import covidindia

Memian = "**كمامتك سلامتك!**"
@bot.on(admin_cmd(pattern="كورونا(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="كورونا(?: |$)(.*)", allow_sudo=True))
async def corona(event):
    if event.pattern_match.group(1):
        country = (event.pattern_match.group(1)).title()
    else:
        country = "World"
    catevent = await edit_or_reply(event, "**⌔∮ يتم جمع المعلومات من الصحة العالمية 🏥**")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data["confirmed"] + country_data["new_cases"]
        hmm2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\n⌔∮ الاصابات المؤكدة 🦠 : <code>{hmm1}</code>"
        data += f"\n⌔∮ الاصابات المشبوهة 🤧 : <code>{country_data['active']}</code>"
        data += f"\n⌔∮ مجموع الوفيات ⚰️ : <code>{hmm2}</code>"
        data += f"\n⌔∮ الحالات الحرجة 🏨 : <code>{country_data['critical']}</code>"
        data += f"\n⌔∮ حالات الشفاء 🔋 : <code>{country_data['recovered']}</code>"
        data += f"\n⌔∮ اجمالي الاختبارات : <code>{country_data['total_tests']}</code>"
        data += f"\n⌔∮ الاصابات الجديدة 🤒 : <code>{country_data['new_cases']}</code>"
        data += f"\n⌔∮ الوفيات الجديدة ☠️ : <code>{country_data['new_deaths']}</code>"
        data += f"\n\n\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n{Memian}"
        await catevent.edit(
            "<b>⌔∮ معلومات فايروس كورونا في الـ - {} :\n{}</b>".format(
                country, data
            ),
            parse_mode="html",
        )
    else:
        data = await covidindia(country)
        if data:
            cat1 = int(data["new_positive"]) - int(data["positive"])
            cat2 = int(data["new_death"]) - int(data["death"])
            cat3 = int(data["new_cured"]) - int(data["cured"])
            result = f"<b>⌔∮ معلونات فايروس كورونا في الـ - {data['state_name']} :\
                \n⌔∮ الاصابات المؤكدة 🦠 : <code>{data['new_positive']}</code>\
                \n⌔∮ الاصابات المشبوهة 🤧 : <code>{data['new_active']}</code>\
                \n⌔∮ مجموع الوفيات ⚰️ : <code>{data['new_death']}</code>\
                \n⌔∮ حالات الشفاء 🔋 : <code>{data['new_cured']}</code>\
                \n⌔∮ اجمالي الاختبارات  : <code>{cat1}</code>\
                \n⌔∮ الحالات الجديدة 🤒 : <code>{cat2}</code>\
                \n⌔∮ الوفيات الجديدة ☠️ : <code>{cat3}</code> </b>\n\n\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            await catevent.edit(result, parse_mode="html")
        else:
            await edit_delete(
                catevent,
                "**⌔∮ معلومات فايروس كورونا في - {} غير متوفره !**".format(country),
                5,
            )


CMD_HELP.update(
    {
        "covid": "**Plugin : **`covid`\
        \n\n  •  **Syntax : **`.covid <country name>`\
        \n  •  **Function :** __Get an information about covid-19 data in the given country.__\
        \n\n  •  **Syntax : **`.covid <state name>`\
        \n  •  **Function :** __Get an information about covid-19 data in the given state of India only.__\
        "
    }
)
