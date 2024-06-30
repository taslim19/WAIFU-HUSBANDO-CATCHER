class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7129472575"
    sudo_users = "7129472575", "7058357442"
    GROUP_ID = -1002209474671
    TOKEN = "7157872153:AAEnEAsyGJj2yqEyrK_ELYnI1jucg-73lvM"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = ""
    UPDATE_CHAT = ""
    BOT_USERNAME = "waifusxsoulbot"
    CHARA_CHANNEL_ID = "-1002209474671"
    api_id = 26021206
    api_hash = "cd9a575457394f081ac8ca5a82673a16"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
