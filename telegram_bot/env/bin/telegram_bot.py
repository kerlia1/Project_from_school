from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from __init__ import TgBot_logic


PARAMS = {}
URL = "https://anilibria.life/serials/"
FILE_PATH = "anilibria.html"
PARSED_FILE_PATH = "anilibria_data.json"

API_TOKEN = '6022301328:AAGu_RBNmdPIcQx6zD48SUID7-TlI4cT9wQ' 
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) # Явно указываем в декораторе, на какую команду реагируем. 
async def send_welcome(message: types.Message):
    key_buttons = [
                [types.KeyboardButton(text = "Стата по аниме с anilibria.life")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard = key_buttons)
    await message.reply("Салат молекул вам в хату, юзеры", reply_markup=keyboard)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text == "Стата по аниме с anilibria.life" :
        anime_analysis = TgBot_logic()
        await message.reply(anime_analysis.procees(URL, FILE_PATH, PARSED_FILE_PATH))
    else :
        await bot.send_message(message.from_user.id, message.text)
        print(message.text)

    



# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)