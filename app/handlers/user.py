import logging

from aiogram.types import Message

from app.controls import dispatcher as dp
from app.controls import sqlite

logger = logging.getLogger(__name__)


# coffeon
@dp.message_handler(commands=["coffeeon"])
async def coffeeon_command(message: Message):
    arguments = message.get_args()
    logger.debug("args=", arguments)
    logger.debug("types.Message", Message)
    await message.reply("Hi!\nThis is coffeon command!")
    user_id=int(str(message.chat.id).replace(" ", ""))
    logger.debug("user id=",user_id)
    find_user = sqlite.fetchall(
        "SELECT cur_status FROM users WHERE id = ?", (message.from_user.id,)
    )
    if find_user:
        if len(find_user) == 0:
            sqlite.execute("INSERT INTO users VALUES (?, 0)", (message.from_user.id,))
            await message.answer("Пользователь не найден в бд. Меняем на on.")
        else:
            sqlite.execute("UPDATE users set cur_status = 0 where id = ?", (message.from_user.id,))
            await message.answer("Пользователь найден в бд. Меняем на on.")


# coffeeoff
@dp.message_handler(commands=["coffeeoff"])
async def coffeeoff_command(message: Message):
    await message.reply("Hi!\nThis is coffeoff command!")
    logger.debug("user id=",message.chat.id)
    find_user = sqlite.fetchall(
        "SELECT cur_status FROM users WHERE id = ?", (message.from_user.id,)
    )
    if find_user and len(find_user) > 0:
        sqlite.execute("UPDATE users set cur_status = 1 where id = ?", (message.from_user.id,))
        await message.answer("Пользователь найден в бд. Меняем на off.")
    else:
        sqlite.execute("INSERT INTO users VALUES (?, 1)", (message.from_user.id,))
        await message.answer("Пользователь не найден в бд. Меняем на off.")


#coffeestatus
@dp.message_handler(commands=["coffeestatus"])
async def coffeestatus_command(message: Message):
    await message.reply("Hi!\nThis is coffeestatus command!")
    logger.debug("user id=",message.chat.id)
    find_user = sqlite.fetchone(
        "SELECT cur_status FROM users WHERE id = ?", (message.from_user.id,)
    )
    if find_user:
        if len(find_user) != 0:
            logger.debug("find_user=",find_user)
            if find_user[0]==0:
                await message.answer("Текущий статус on")
            else:
                await message.answer("Текущий статус off")
