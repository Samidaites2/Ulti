from time import sleep
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, edit_or_reply


@ayiin_cmd(pattern="teemo(?: |$)(.*)")
async def _(teemo):
    yins = await edit_or_reply(teemo, "`   `")
    sleep(2)
    await yins.edit("`   `")
    sleep(1)
    await yins.edit("`   , -    `")


@ayiin_cmd(pattern="give(?: |$)(.*)")
async def _(giveaway):
    ayiin = await edit_or_reply(giveaway, "`  `")
    sleep(2)
    await ayiin.edit("`  10 `")
    sleep(1)
    await ayiin.edit("` ,    `")


@ayiin_cmd(pattern="uno(?: |$)(.*)")
async def _(uno):
    xd = await edit_or_reply(uno, "` `")
    sleep(2)
    await xd.edit("`   `")
    sleep(1)
    await xd.edit("`    `")


CMD_HELP.update(
    {
        "gabut2": f"**Plugin : **`gabut2`\
        \n\n  »  **Perintah :** `{cmd}teemo`\
        \n  »  **Kegunaan : **Coba Sendiri Tod.\
        \n\n  »  **Perintah :** `{cmd}give`\
        \n  »  **Kegunaan : **Coba Sendiri Tod.\
        \n\n  »  **Perintah :** `{cmd}uno`\
        \n  »  **Kegunaan : **Coba Sendiri Tod.\
    "
    }
)