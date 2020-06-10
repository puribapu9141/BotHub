""".gangestar Plugin"""

from telethon import events
import random, re
from uniborg.util import admin_cmd
import asyncio 



@borg.on(admin_cmd("gangestar ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("EvErYbOdY")
        await asyncio.sleep(0.3)
        await event.edit("wAs")
        await asyncio.sleep(0.2)
        await event.edit("GaNgEsTaR")
        await asyncio.sleep(0.5)
        await event.edit("uNtIL ")
        await asyncio.sleep(0.2)
        await event.edit("i")
        await asyncio.sleep(0.3)
        await event.edit("ArRiVeD")
        await asyncio.sleep(0.3)
        await event.edit("🔥🔥")
        await asyncio.sleep(0.3)
        await event.edit("EvErYbOdY wAs GaNgEsTaR uNtIL i ArRiVeD 🔥🔥")
