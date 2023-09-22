# (c) @Kuntejss

import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = 9583161
    API_HASH = "aecf9e2b7c655c4f916564ab6d598a73"
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = "BACSOjkAwD-nZgyYQVjXbMgHdCw3cWBD27jKPSNV8mvEWhjn4PFrBEmqqEIiineQWcO-AR7RGWUtZcyQ6YY_ynv-ypbHMJM2GTLZWqXKgYRoQEYhZLjQCt7QZ7l9ga2P2neqMyb8B9aLAQhJVL-F744HsfEkLKAVRv_V2TSXMyMdcw9hgSFHwyeesxx0M1fruVtqqwT_D7pBpgXbjsV2ebyG-FOC_inGRAU1FrfWIeTONm6FK2V_CGxMD7W3XHGNxIU2wMgt9QRYYGsylhen9plXjcYFfHml1FLe1Bi38y9Nbbr45umvWJYLOJ0ib4WoFTqPRksLJdrITGtSP6LmlQsdok7ptAAAAAFf0rn8AA"
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = [-1001795573811]
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = [-1001300585373]
    # Filters for Forwards
    DEFAULT_FILTERS = "document photo forwarded"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = True
    # Sleep Time while Kang
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 10))
    # Heroku Management
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] if HEROKU_API_KEY and HEROKU_APP_NAME else None
    # Message Texts
    HELP_TEXT = """
This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.

👨🏻‍💻 **Commands:**
• `!start` - Check UserBot Alive or Not.
• `!help` - Get this Message.
• `!kang` - Start All Messages Kanger.
• `!restart` - Restart Heroku App Dyno Workers.
• `!stop` - Stop Kanger & Restart Service.

©️ **Developer:** @Kuntejs
👥 **Support:** [【★ʟя★】](https://t.me/Kuntejs)"""
