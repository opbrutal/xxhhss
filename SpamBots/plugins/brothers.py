import asyncio
import random
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import UstaD, UstaD2, UstaD3, UstaD4, UstaD5, UstaD6, UstaD7, UstaD8, UstaD9, UstaD10, SUDO_USERS
from SpamBots import GROUP, PORMS





@UstaD.on(events.NewMessage(incoming=True, pattern=r"\%sbrothers(?: |$)(.*)" % hl))
@UstaD2.on(events.NewMessage(incoming=True, pattern=r"\%sbrothers(?: |$)(.*)" % hl))
@UstaD3.on(events.NewMessage(incoming=True, pattern=r"\%sbrothers(?: |$)(.*)" % hl))
@UstaD4.on(events.NewMessage(incoming=True, pattern=r"\%sbrothers(?: |$)(.*)" % hl))
@UstaD5.on(events.NewMessage(incoming=True, pattern=r"\%sbrothers(?: |$)(.*)" % hl))
@UstaD6.on(events.NewMessage(incoming=True, pattern=r"\%sbrothers(?: |$)(.*)" % hl))
@UstaD7.on(events.NewMessage(incoming=True, pattern=r"\%sbrothers(?: |$)(.*)" % hl))
@UstaD8.on(events.NewMessage(incoming=True, pattern=r"\%sbrothers(?: |$)(.*)" % hl))
@UstaD9.on(events.NewMessage(incoming=True, pattern=r"\%sbrothers(?: |$)(.*)" % hl))
@UstaD10.on(events.NewMessage(incoming=True, pattern=r"\%sbrothers(?: |$)(.*)" % hl))
async def pspam(e):
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Brothers = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(Brothers) == 1:
            counter = int(Brothers[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I can't spam here"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                 porrn = random.choice(PORMS)
                 for _ in range(counter):
                     async with e.client.action(e.chat_id, "document"):
                         smex = await e.client.send_file(e.chat_id, porrn)
                         await gifspam(e, smex) 
                     await asyncio.sleep(0.4)
        else:
            usage = f"**MODULE NAME : EVER DANGER** \n\n command: `.brothers <count>`"
            await e.reply(usage, parse_mode=None, link_preview=None )
