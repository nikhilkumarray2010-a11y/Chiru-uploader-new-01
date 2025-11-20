import os

API_ID = os.environ.get("API_ID", "26468828")

API_HASH = os.environ.get("API_HASH", "4693513c08d1ac6af15f95b116c29478")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7445620075))

LOG = -1002702049353,

UPDATE_GRP = , # bot sat group

auth_chats = []

try:
    ADMINS=[7445620075]
    for x in (os.environ.get("ADMINS", "7445620075").split()):
        ADMINS.append(int(x))
except ValueError:
        #raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
