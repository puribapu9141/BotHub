"""Available Commands:  .owner"""

from telethon import events

import asyncio




@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "owner":

        await event.edit(input_str)

        animation_chars = [
        
            "P\nR\nA\nT\nI\nK",
            "G\nO\nS\nW\nA\nM\nI",
            "P\nM",
            "I\nS",
            "O\nW\nN\nE\nR",
            "[👑\nPRATIK GOSWAMI PM IS OWNER 👑](t.me/PM_The_Angry)"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])
