from aiogram.types import Message

from app.controls import dispatcher as dp
from app.database.engine import execute, fetchall, fetchone


# coffeon
@dp.message_handler(commands=["coffeeon"])
async def coffeeon_command(message: Message):
    arguments = message.get_args()
    print("DEBUG args=", arguments)
    print("DEBUG types.Message", Message)
    await message.reply("Hi!\nThis is coffeon command!")
    user_id=int(str(message.chat.id).replace(" ", ""))
    print("DEBUG user id=",user_id)
    find_user = fetchall(f"SELECT cur_status FROM users WHERE id = {message.chat.id}")
    if find_user:
        if len(find_user) == 0:
            execute(f"INSERT INTO users VALUES ('{message.chat.id}', '0')")
            await message.answer("Пользователь не найден в бд. Меняем на on.")
        else:
            execute(f"UPDATE users set cur_status=0 where id={message.chat.id}")
            await message.answer("Пользователь найден в бд. Меняем на on.")


# coffeeoff
@dp.message_handler(commands=["coffeeoff"])
async def coffeeoff_command(message: Message):
    await message.reply("Hi!\nThis is coffeoff command!")
    print("DEBUG user id=",message.chat.id)
    find_user = fetchall(f"SELECT cur_status FROM users WHERE id = {message.chat.id}")
    if find_user and len(find_user) > 0:
        execute(f"UPDATE users set cur_status=1 where id={message.chat.id}")
        await message.answer("Пользователь найден в бд. Меняем на off.")
    else:
        execute(f"INSERT INTO users VALUES ('{message.chat.id}', '1')")
        await message.answer("Пользователь не найден в бд. Меняем на off.")


#coffeestatus
@dp.message_handler(commands=["coffeestatus"])
async def coffeestatus_command(message: Message):
    await message.reply("Hi!\nThis is coffeestatus command!")
    print("DEBUG user id=",message.chat.id)
    find_user = fetchone(f"SELECT cur_status FROM users WHERE id = {message.chat.id}")
    if find_user:
        if len(find_user) != 0:
            print("DEBUG find_user=",find_user)
            if find_user[0]==0:
                await message.answer("Текущий статус on")
            else:
                await message.answer("Текущий статус off")
