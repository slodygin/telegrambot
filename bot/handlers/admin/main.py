from aiogram import Dispatcher, types
from bot.ai import generate_text, generate_image
from bot import *

def register_admin_handlers(dp: Dispatcher):
    # todo: register all admin handlers
    @dp.message_handler(commands=['drtext'])
    async def send_welcome(message: types.Message):
      arguments = message.get_args()
      await message.reply("Hi!\nThis command will send congratulations messages to people!")
      await message.answer(arguments)
      ret=generate_text(arguments)
      await message.answer(ret)
    @dp.message_handler(commands=['drimage'])
    async def send_welcome(message: types.Message):
      #bot = get_bot()
      arguments = message.get_args()
      await message.reply("Hi!\nThis command will send congratulations messages to people!")
      await message.answer(arguments)
      url1 = generate_image(arguments)
      await message.answer(url1)
      await bot.send_photo(chat_id=message.chat.id, photo=url1)
