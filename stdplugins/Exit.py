# For @UniBorg

"""use cmd `.fexit` to create a fake exit"""



from telethon import events

from datetime import datetime

from uniborg.util import admin_cmd

import importlib.util

import asyncio

import random

import importlib.util




@borg.on(events.NewMessage(outgoing=True, pattern='^\.(f?f)exit'))

async def timer_blankx(e):

 txt=e.text[7:] + '\n\n`Processing....` '

 j=1

 k=j

 for j in range(j):

  await e.edit(txt + str(k))

  k=k-1

  await asyncio.sleep(1)

 if e.pattern_match.group(1) == 'f':

  await e.edit("`Legend is Leaving This Chat.....!` @admin `Goodbye Aren't Forever. It Was a Pleasant Time With You Guys..` ")

