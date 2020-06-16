"""COMMAND : .helpme, .dc, .exec ls stdplugins, .stdplugins, .syntax"""

import sys
from telethon import events, functions, __version__
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="helpme ?(.*)", allow_sudo=False))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    splugin_name = event.pattern_match.group(1)
    if splugin_name in borg._plugins:
        s_helpme_string = borg._plugins[splugin_name].__doc__
    else:
        s_helpme_string = "****:"
    helpme_string = """@PM_The_Angry ( **Custom Built By** @PM_The_Angry_Bot ) \n**Verified Account**: ✅\n**Official \n**NOTICE**: **COMMANDS** are CASE **sensitive**\n**DESCRIPTION**: https://telegra.ph/command-list-for-BotHub-Userbot-11-08\n
 """.format(
        sys.version,
        __version__
    )
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER  # pylint:disable=E0602
    if tgbotusername is not None:
        results = await borg.inline_query(  # pylint:disable=E0602
            tgbotusername,
            helpme_string + "\n\n" + s_helpme_string
        )
        await results[0].click(
            event.chat_id,
            reply_to=event.reply_to_msg_id,
            hide_via=True
        )
        await event.delete()
    else:
        await event.reply(helpme_string + "\n\n" + s_helpme_string)
        await event.delete()


@borg.on(admin_cmd(pattern="dc"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await event.edit(f"**Country** : `{result.country}`\n"
                     f"**Nearest DC** : `{result.nearest_dc}`\n"
                     f"**This DC** : `{result.this_dc}`")


@borg.on(admin_cmd(pattern="config"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await borg(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""Telethon UserBot powered by @PM_The_Angry""")


@borg.on(admin_cmd(pattern="syntax ?(.*)" ))
async def _(event):
    if event.fwd_from:
        return
    plugin_name = event.pattern_match.group(1)
    if plugin_name in borg._plugins:
        helpme_string = borg._plugins[plugin_name].__doc__
        unload_string = f"Use `.unload {plugin_name}` to remove this plugin.\n           © @PM_The_Angry_Bot"
        if helpme_string:
            plugin_syntax = f"Syntax for plugin **{plugin_name}**:\n\n{helpme_string}\n{unload_string}"
        else:
            plugin_syntax = f"No DOCSTRING has been setup for {plugin_name} plugin."
    else:
        plugin_syntax = "Enter valid **Plugin** name.\nDo `.exec ls stdplugins` or `.helpme` or `.stdplugins` to get list of valid plugin names."
    await event.edit(plugin_syntax)
