from aiogram import Dispatcher, types


def register_admin_handlers(dp: Dispatcher):
    # todo: register all admin handlers
    @dp.message_handler(commands=['dr'])
    async def send_welcome(message: types.Message):
      await message.reply("Hi!\nThis command will send congratulations messages to people!")
