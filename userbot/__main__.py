# Thanks To paperplane 
#
""" Userbot start point """

from importlib import import_module
import os
import sys

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError

from userbot import LOGS, bot
from userbot.modules import ALL_MODULES

INVALID_PH = (
    "\nERROR: The phone no. entered is incorrect!"
    "\n  Tip: Use country code (eg +44) along with num."
    "\n       Recheck your phone number"
)

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    "Omeg  is running! Test it by typing .alive on any chat."
    " Should you need assistance, head to https://t.me/ItS_PraNav_xD."
)

SEM_TEST = os.environ.get("SEMAPHORE", None)
if SEM_TEST:
    bot.disconnect()
else:
    bot.run_until_disconnected()
