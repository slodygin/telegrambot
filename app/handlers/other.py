from aiogram.types import Message

from app.controls import dispatcher as dp


@dp.message_handler()
async def echo(msg: Message):
    # todo: remove echo example:3
    await msg.answer(msg.text)
