
import json
import os


def get_user_list(config, key):
    with open("{}/Yone/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]

class Config(object):
    LOGGER = True

    API_ID = "12227067"
    API_HASH = "b463bedd791aa733ae2297e6520302fe"
    TOKEN = "2006479947:AAGnohED8M1p9HXMxoLAG_kne-m8OZ9I0a0"
    OWNER_ID = "2105971379"
    OWNER_USERNAME = "sultan11100"
    SUPPORT_CHAT = "AM_YTSUPPORT"
    JOIN_LOGGER = "-1001841879487"
    EVENT_LOGS = "-1001908711819"
    DEEP_API = "c8e3d7fc-1f7e-455b-8019-5c1b7f21047a"
    OPENAI_KEY = ""
    BOT_USERNAME = "MissPoppy_bot"
    BOT_NAME = "Miss Poppy"
    # 
    # DATABASE_URL = "postgres://ixweewbx:9OoB_feF6d6wK1W4YycgwHzRHQXezsNA@arjuna.db.elephantsql.com/ixweewbx"  # sql
    DATABASE_URL = "postgres://ixweewbx:9OoB_feF6d6wK1W4YycgwHzRHQXezsNA@arjuna.db.elephantsql.com/ixweewbx"  # sql
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    REDIS_URL = "redis://default:725m47dhlmisA0QecURSMkcHNGXkM1uP@redis-15808.c275.us-east-1-4.ec2.cloud.redislabs.com:15808"

    INSPECTOR = get_user_list("elevated_users.json", "ins")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    REQUESTER = get_user_list("elevated_users.json", "req")

    CERT_PATH = None
    STRICT_GBAN = True
    PORT = "8080"
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 20
    ALLOW_EXCL = True
    ALLOW_CHATS = True
    PHOTO = "https://graph.org/file/308d29f27bb21103dc01b.jpg" # Miss Poppy Music Pic
    INFOPIC = True


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
