# (c) @Kuntejs

import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = 9583161
    API_HASH = "aecf9e2b7c655c4f916564ab6d598a73"
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = "BACSOjkAZ1yKm-8zPpvq6m-s0hVvpSGh-0O-U8KX8I-jvnMdpeHq9R8jQ0Bl2fCiKFRVynz05UgDtcz9Zluw4lK4zGDVsBbjmBVkZcqy2w3Y1gZahS38-5xVPMqAbNVUuCa-0sIq0UV2cwJo3lsUacH2LG-B-NN6eA29D39uQ6Fyle0f5zx_k5L4dymZSswlsuL8kgtKuJ1fuNFQLcMKgyz8WK_5JTFmJjEaehPe6WA4kdFrdFl8nCqiu1FQc2jyAwmJItYMi2HZjqp2wXW6uUJ8cyb4CP80xRLl3GMp7PW72GglPYGvl55gA-ChBS_PTL4lVO9OIQ8CbdcQn4QDFL43Q_G4xAAAAAFf0rn8AA"
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = "-1001925654676"
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = "-1001975641001"
    # Filters for Forwards
    DEFAULT_FILTERS = "document forwarded"
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
