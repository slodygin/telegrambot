from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.misc.env import TG_BOT_TOKEN

if TG_BOT_TOKEN is None:
    import sys
    sys.exit("TG_BOT_TOKEN is required.")


bot = Bot(token=TG_BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)
