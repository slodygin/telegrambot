import logging

from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message

from app.controls import dispatcher as dp
from app.database import coffee

from aiogram import Dispatcher,types
import jsonpickle
#пишет aiogram.filters не найден
#from aiogram.filters import Text

logger = logging.getLogger(__name__)


command_target_status = {
    "coffeeon": coffee.CoffeeStatus.ON,
    "coffeeoff": coffee.CoffeeStatus.OFF
}

# coffeon / coffeeoff
@dp.message_handler(Command(commands=("coffeeon", "coffeeoff")))
async def coffeeon_command(message: Message, command: Command.CommandObj):
    target_status = command_target_status[command.command]
    print('DEBUG args=', command.args)
    if coffee.change_status(message.from_user.id, target_status):
        await message.answer(f"Успешно установлен статус {target_status.name}.")
    else:
        await message.answer("Возникли какие-то проблемы. Но мы скоро всё починим.")


#coffeestatus
@dp.message_handler(commands=["coffeestatus"])
async def coffeestatus_command(message: Message):
    status = coffee.get_status(message.from_user.id)
    await message.answer(f"Текущий статус: {status.name}")

user_data = {}

def get_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(text="yes", callback_data="vote_yes"),
            types.InlineKeyboardButton(text="no", callback_data="vote_no")
        ],
        [types.InlineKeyboardButton(text="Подтвердить", callback_data="vote_finish")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


async def update_num_text(message: types.Message, new_value: int):
    await message.edit_text(
        f"Hey! Нажмите да, если участвуете в кофечате (число yes: {new_value})",
        reply_markup=get_keyboard()
    )


@dp.message_handler(Command("coffeevote"))
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer("Hey! Нажмите да, если участвуете в кофечате!", reply_markup=get_keyboard())

#1
@dp.callback_query_handler(text="vote_yes")
#TODO можно было бы одним колбэком обойтись если бы работал Text
#@dp.callback_query(Text(startswith="vote_"))
async def callbacks_num(callback: types.CallbackQuery):
    print('callback.message:', jsonpickle.encode(callback.message))
    user_value = user_data.get(callback.from_user.id, 0)
    action = callback.data.split("_")[1]

    if action == "yes":
        user_data[callback.from_user.id] = user_value+1
        await update_num_text(callback.message, user_value+1)
    elif action == "no":
        user_data[callback.from_user.id] = user_value-1
        await update_num_text(callback.message, user_value-1)
    elif action == "finish":
        await callback.message.edit_text(f"Итого: {user_value}")

    await callback.answer()
#2
@dp.callback_query_handler(text="vote_no")
#TODO можно было бы одним колбэком обойтись если бы работал Text
#@dp.callback_query(Text(startswith="vote_"))
async def callbacks_num(callback: types.CallbackQuery):
    print('callback.message:', jsonpickle.encode(callback.message))
    user_value = user_data.get(callback.from_user.id, 0)
    action = callback.data.split("_")[1]

    if action == "yes":
        user_data[callback.from_user.id] = user_value+1
        await update_num_text(callback.message, user_value+1)
    elif action == "no":
        user_data[callback.from_user.id] = user_value-1
        await update_num_text(callback.message, user_value-1)
    elif action == "finish":
        await callback.message.edit_text(f"Итого: {user_value}")

    await callback.answer()

#3
@dp.callback_query_handler(text="vote_finish")
async def callbacks_num(callback: types.CallbackQuery):
    print('callback.message:', jsonpickle.encode(callback.message))
    user_value = user_data.get(callback.from_user.id, 0)
    action = callback.data.split("_")[1]

    if action == "yes":
        user_data[callback.from_user.id] = user_value+1
        await update_num_text(callback.message, user_value+1)
    elif action == "no":
        user_data[callback.from_user.id] = user_value-1
        await update_num_text(callback.message, user_value-1)
    elif action == "finish":
        await callback.message.edit_text(f"Итого: {user_value}")

    await callback.answer()
