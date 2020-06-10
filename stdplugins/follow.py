""" Userbot module for getting information about the social media. """

from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from sample_config import Config
from uniborg.util import admin_cmd
import uniborg


# ================= CONSTANT =================
DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================


@borg.on(admin_cmd(pattern="follow ?(.*)"))
async def follow(follow):
        """ For .follow command, check if the bot is running.  """
    await follow.edit(
                     f"`FOLLOW {DEFAULTUSER} ON` \n\n"
                     f"[Instagram](https://www.instagram.com/pm_the_angry) \n\n"
                     f"[Telegram](https://www.instagram.com/PM_The_Angry) \n\n"
                     f"[Messenger](https://m.me/pratikgoswami9141) \n\n"
                     f"[GitHub](https://github.com/puribapu9141) \n\n"
                     f"[Facebook](https://www.facebook.com/pratikgoswami9141) \n\n"
                     f"[Twitter](https://twitter.com/PM_The_Angry) \n\n"
                     f"[LinkedIn](https://www.linkedin.com/in/pratik-goswami-pm-94122415b) \n\n"
                     )   

