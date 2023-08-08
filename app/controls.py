import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.database.engine import SQLite
from app.misc.env import TG_BOT_TOKEN

logging.basicConfig(
    format=("%(asctime)s | %(levelname)8s | %(name)s | %(filename)s:%(lineno)d | %(message)s"),
    level=logging.INFO,
)


if TG_BOT_TOKEN is None:
    import sys
    sys.exit("TG_BOT_TOKEN is required.")


bot = Bot(token=TG_BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

sqlite = SQLite("sqlite3.db")
