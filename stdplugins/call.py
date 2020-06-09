"""COMMAND : ./calling"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "/calling":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: YaY This is Me` Pratik Goswami PM,`Please Connect Me to Pavel Durov Shukla`",
            "`User Authorised.`",
            "`Calling Pavel Durov Shukla (@durov) At +911111111111`",
            "`Private Call Connected...`",
            "`Me: Hello Sir, Please Ban This @PM_Alt2 Telegram Account.`",    
            "`Durov: May I Know Who is This?`",
            "`Me: Yeah Bruh, I Am` Pratik Goswami PM",
            "`Durov: OMG!!! I Am Big FAN of You Sir...\nI'll Make Sure That Guy Account Will Get Blocked or Deleted Within 24Hrs.`",
            "`Me: Thanks, See You Later Bruh.`",
            "`Durov: Please Don't Say Me Thanks Sir, You Are Pro Sir. Just Give A Call When You Will Get Time.`",
            "`Me: Is There Any Issue/Emergency Bruh???`",
            "`Durov: Yes Sir, There is A Bug In Telegram v6.2.0.\nI Am Not Able to Fix It. If Possible, Please Help for Fix That Bug.`",
            "`Me: Send Me The App On My Main Account, I Will Fix The Bug & Send You.`",
            "`Durov: Sure Sir \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 22])
