from aiogram.utils import executor

from app import handlers
from app.controls import dispatcher as dp

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
