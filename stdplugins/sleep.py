""" use cmd .sleep <time in seconds> to make your bot sleep """

from telethon import events
import asyncio
import os
import sys
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="sleep( [0-9]+)?$", outgoing=True))
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    message = time.text
    if " " not in time.pattern_match.group(1):
        await time.reply("Syntax: `.sleep [seconds]`")
    else:
        counter = int(time.pattern_match.group(1))
        await time.edit("`Thanks Mastor for letting me snooze....`")
        await asyncio.sleep(2)
        if Config.PRIVATE_GROUP_BOT_API_ID is not None:
            await time.client.send_message(
                Config.PRIVATE_GROUP_BOT_API_ID,
                "You Put The Bot to Sleep for " + str(counter) + " seconds",
            )
        await asyncio.sleep(counter)
        await time.edit("`OK, My Mastor, I'm Awake Now.`")
