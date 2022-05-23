

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/NekoRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 7761098
    API_HASH = "6b19682d1aeeda50a4aa8b6eb61f3a4e"

    BOT_ID = ""
    TOKEN = ""  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1938491135  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Husbandoo"
    DRAGONS = ""
    DEMONS = ""
    DEV_USERS = "5358835742 5132611794 1802324609"
    SUPPORT_CHAT = "NexusXSupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001551314374
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001551314374
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = ""  # needed for any database module
    DATABASE_URL = ""
    DB_URL = ""

    REDIS_URI = ""


    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    INFOPIC = True
    URL = None
    HEROKU_API_KEY = ""
    HEROKU_APP_NAME = ""
    BOT_USERNAME = "MishaXRobot"
    SPAMWATCH_API = 'ixd7Qui~aQOTeaLynGRKeVqczYaZQFopZpfYagMx2ZrdUcSzMW~h2N1gJoGRZzmP'  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    ARQ_API_KEY = "1234"
    ARQ_API_URL = "https://thearq.tech/"
    TEMP_DOWNLOAD_DIRECTORY = "./"
    OPENWEATHERMAP_ID = ""
    VIRUS_API_KEY = ""
    REDIS_URL = ""
    LASTFM_API_KEY = ""
    

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    ALLOW_CHATS = ""
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    WHITELIST_USERS = get_user_list("elevated_users.json", "whitelists")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "xyz"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "xyz"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "xyz"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = ""  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None
    REM_BG_API_KEY = ""
    GENIUS_API_TOKEN = ""
    MONGO_DB_URI = ""
    STRING_SESSION = ""
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
