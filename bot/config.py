import os
import dotenv
import sqlite3


from vkbottle import API, BuiltinStateDispenser, PhotoMessageUploader
from vkbottle.bot import BotLabeler

dotenv.load_dotenv("..\\.env")

api = API(os.getenv('token'))
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()
photo_upd = PhotoMessageUploader(api)
db_conn = sqlite3.connect(os.getenv('DB_NAME'))


class BOT:
    pass

