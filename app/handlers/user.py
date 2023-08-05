import logging

from aiogram.types import Message

from app.controls import dispatcher as dp
from app.database import coffee

logger = logging.getLogger(__name__)


# coffeon
@dp.message_handler(commands=["coffeeon"])
async def coffeeon_command(message: Message):
    if coffee.change_status(message.from_user.id, coffee.CoffeeStatus.ON):
        await message.answer("Успешно установлен статус on.")
    else:
        await message.answer("Возникли какие-то проблемы. Но мы скоро всё починим.")


# coffeeoff
@dp.message_handler(commands=["coffeeoff"])
async def coffeeoff_command(message: Message):
    if coffee.change_status(message.from_user.id, coffee.CoffeeStatus.OFF):
        await message.answer("Успешно установлен статус off.")
    else:
        await message.answer("Возникли какие-то проблемы. Но мы скоро всё починим.")


#coffeestatus
@dp.message_handler(commands=["coffeestatus"])
async def coffeestatus_command(message: Message):
    if coffee.get_status(message.from_user.id) == coffee.CoffeeStatus.ON:
        await message.answer("Текущий статус on")
    else:
        await message.answer("Текущий статус off")
