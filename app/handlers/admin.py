from aiogram.types import Message

from app.controls import dispatcher as dp
from app.misc import ai


@dp.message_handler(commands=["drtext"])
async def drtext_command(message: Message):
    arguments = message.get_args()
    await message.reply("Hi!\nThis command will send congratulations messages to people!")
    await message.answer(arguments)
    ret = ai.generate_text(arguments)
    await message.answer(ret)


@dp.message_handler(commands=["drimage"])
async def drimage_command(message: Message):
    #bot = get_bot()
    arguments = message.get_args()
    await message.reply("Hi!\nThis command will send congratulations messages to people!")
    await message.answer(arguments)
    url1 = ai.generate_image(arguments)
    await message.answer(url1)
    await message.answer_photo(photo=url1)
