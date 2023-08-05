from aiogram.utils import executor

from app import handlers
from app.controls import dispatcher as dp
from app.database.deploy import create_tables

if __name__ == "__main__":
    create_tables()
    executor.start_polling(dp, skip_updates=True)
