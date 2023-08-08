import logging

from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message

from app.controls import dispatcher as dp
from app.database import coffee

logger = logging.getLogger(__name__)


command_target_status = {
    "coffeeon": coffee.CoffeeStatus.ON,
    "coffeeoff": coffee.CoffeeStatus.OFF
}


# coffeon / coffeeoff
@dp.message_handler(Command(commands=("coffeeon", "coffeeoff")))
async def coffeeon_command(message: Message, command: Command.CommandObj):
    target_status = command_target_status[command.command]
    if coffee.change_status(message.from_user.id, target_status):
        await message.answer(f"Успешно установлен статус {target_status.name}.")
    else:
        await message.answer("Возникли какие-то проблемы. Но мы скоро всё починим.")


#coffeestatus
@dp.message_handler(commands=["coffeestatus"])
async def coffeestatus_command(message: Message):
    status = coffee.get_status(message.from_user.id)
    await message.answer(f"Текущий статус: {status.name}")
