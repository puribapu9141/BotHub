"""Available Commands: `.ding`"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 10)

    input_str = event.pattern_match.group(1)

    if input_str == "ding":

        await event.edit(input_str)

        animation_chars = [
        
            "ðŸ”´â¬›â¬›â¬œâ¬œ\nâ¬œâ¬œâ¬œâ¬œâ¬œ\nâ¬œâ¬œâ¬œâ¬œâ¬œ",
            "â¬œâ¬œâ¬›â¬œâ¬œ\nâ¬œâ¬›â¬œâ¬œâ¬œ\nðŸ”´â¬œâ¬œâ¬œâ¬œ",
            "â¬œâ¬œâ¬›â¬œâ¬œ\nâ¬œâ¬œâ¬›â¬œâ¬œ\nâ¬œâ¬œðŸ”´â¬œâ¬œ",
            "â¬œâ¬œâ¬›â¬œâ¬œ\nâ¬œâ¬œâ¬œâ¬›â¬œ\nâ¬œâ¬œâ¬œâ¬œðŸ”´",
            "â¬œâ¬œâ¬›â¬›ðŸ”´\nâ¬œâ¬œâ¬œâ¬œâ¬œ\nâ¬œâ¬œâ¬œâ¬œâ¬œ",    
            "â¬œâ¬œâ¬›â¬œâ¬œ\nâ¬œâ¬œâ¬œâ¬›â¬œ\nâ¬œâ¬œâ¬œâ¬œðŸ”´",
            "â¬œâ¬œâ¬›â¬œâ¬œ\nâ¬œâ¬œâ¬›â¬œâ¬œ\nâ¬œâ¬œðŸ”´â¬œâ¬œ",
            "â¬œâ¬œâ¬›â¬œâ¬œ\nâ¬œâ¬›â¬œâ¬œâ¬œ\nðŸ”´â¬œâ¬œâ¬œâ¬œ",
            "ðŸ”´â¬›â¬›â¬œâ¬œ\nâ¬œâ¬œâ¬œâ¬œâ¬œ\nâ¬œâ¬œâ¬œâ¬œâ¬œ",
            "â¬œâ¬œâ¬œâ¬œâ¬œ\nâ¬œ [BotHub](https://github.com/puribapu9141/BotHub/) â¬œ\nâ¬œâ¬œâ¬œâ¬œâ¬œ"

 ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
