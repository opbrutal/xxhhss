from SpamBots import UstaD, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
    
HELP_PIC = "https://telegra.ph/file/31d7fb96cdba287a05515.jpg"

UstaD_Help = "ð¥ ÊÊá´á´Êá´Ês Sá´á´á´ Êá´Êá´ ð¥\n\n"
 
UstaD_Help += f"_á´á´É´á´s á´á´ á´ÉªÊá´ÊÊá´ ÉªÉ´ ÊÊá´á´Êá´Ês__\n\n"

UstaD_Help += f" â§ ððð´ðð±ð¾ð ð²ð¼ð³ð â§\n\n"

UstaD_Help += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n .`restart` - to restart all spam bots \n `.addecho` - to addecho \n `.rmecho` - To remove Echo \n `.addsudo` - To add sudo user using spam bot \n\n"
 
UstaD_Help += f" â§ ð»ð´ð°ðð´ ð²ð¼ð³ â§\n\n"

UstaD_Help += f" `.leave` - to leave public/private channel/groups\n\n"
 
UstaD_Help += f" â§ ðð¿ð°ð¼ ð²ð¼ð³ð â§\n\n"

UstaD_Help += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.uspam` - this cmd use for unlimited Spam until You restart the bots!!\n `.delayspam` - this cmd use for delay spam\n `.pornspam` - this cmd is use for porn spam\n\n"

UstaD_Help += f"Â© @Nishu_bothub\n"


@UstaD.on(events.NewMessage(pattern="/help"))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await UstaD.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=UstaD_Help,
                                  buttons=[
        [
        Button.url("á´ÊÊ á´á´á´s", "https://telegra.ph/%F0%9D%90%92%F0%9D%9F%92%F0%9D%90%92%F0%9D%90%87%F0%9D%90%88%F0%9D%90%95-%F0%9D%90%97%F0%9D%90%83%E0%BD%91-%E2%84%91-%F0%9D%90%80%F0%9D%94%AA-%E1%97%AAye%F0%9D%90%8C%F0%9D%95%A0%E2%84%95-%E0%BD%8C-03-18-2")
        ],
        [
        Button.url("á´ÒÒÉªá´Éªá´Ê É¢Êá´á´á´", "https://t.me/The_Brothers_Group")
        ] 
        ]
        )                                                         
