# For @UniBorg
# Courtesy @r4v4n4
"""
.leave to kick yourself from any group
"""

from telethon.tl.functions.channels import LeaveChannelRequest
from uniborg.util import admin_cmd
import time


@borg.on(admin_cmd("leave", outgoing=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`Underworld Mafia is leaving this chat.....!` @admin `Goodbye Aren't Forever.. `")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`Sir This is Not A Chat`')
