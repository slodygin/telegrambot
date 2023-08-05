import logging

from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message

from app.controls import dispatcher as dp
from app.misc import ai

logger = logging.getLogger(__name__)


@dp.message_handler(Command("drtext"))
async def drtext_command(message: Message, command: Command.CommandObj):
    logger.debug(command.args)
    ret = ai.generate_text(command.args)
    if ret is not None:
        await message.answer(ret)
    else:
        await message.answer("Возникли какие-то проблемы. Но мы скоро всё починим.")


@dp.message_handler(Command("drimage"))
async def drimage_command(message: Message, command: Command.CommandObj):
    logger.debug(command.args)
    url1 = ai.generate_image(command.args)
    if url1 is not None:
        await message.answer(url1)
        await message.answer_photo(photo=url1)
    else:
        await message.answer("Возникли какие-то проблемы. Но мы скоро всё починим.")
