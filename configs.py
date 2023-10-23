# (c) @Kuntejss

import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = 23358396
    API_HASH = "06a8a838fbba7e1a432b48110a7ef598"
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = "BAFka7wArZaUtpKzNh_usSOHrRmVGMqqkip9BM2bjZT0JGWzxDoy9jGuGN8HWZ9xL3wVTa7pB_MflrIFfbWdu_svsZUTWTreJQ6ovv6DEqisqqHB9V6uzncRzBqv-SIuf5Tt0INha5Sxzp7vS4c_QPYThq3tS0kuPV6B42vr-02W6cwRjPBoBY-BLOWQCpOdGngKPkMd1A9sC8zlpzmiZQPI5Wm3J4Jg0WCiBJMs0NSn_GIK2cidU1_YZjC-ai54KMAQ1bNMrZZ_wp43zmA_zLLt-WIxBN12BV8ZJBXQn16Hssyf2gS-ASgIEJCwPRBnEl2D2ueC7m3fi9QXWEE6lJzkj0-ONwAAAAGCa0iRAA"
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
