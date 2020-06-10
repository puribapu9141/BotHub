"""Emoji

Available Commands:

.cargdrive"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 13)

    input_str = event.pattern_match.group(1)

    if input_str == "cargdrive":

        await event.edit(input_str)

        animation_chars = [
        
            "__Downloading To Heroku Started...__\n\n░░░░░░░░░░",
            "__Downloading...__\n\n█░░░░░░░░░",
            "__Downloading...__\n\n███░░░░░░░",
            "__Downloading...__\n\n█████░░░░░",
            "__Downloading...__\n\n█████████░",    
            "__Download Completed.__\n\n██████████",
            "__Uploading To G-Drive Started...__\n\n░░░░░░░░░░",
            "__Uploading To G-Drive...__\n\n█░░░░░░░░░",
            "__Uploading To G-Drive...__\n\n█████░░░░░",
            "__Uploading To G-Drive...__\n\n█████████░",
            "__Uploading To G-Drive Completed.__\n\n██████████",
            "__Generating G-Drive link........__",
            "Link Generated: [G-Drive Link](https://drive.google.com/file/d/1BHKB9byAp2S381BNNvhx8_Ep3XKGS0Lx/view?usp=drivesdk)"
 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 13])
