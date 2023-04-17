from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6066949542:AAE9oGxAT_zBCNbHC-P4MJ-FjngC6hfS9Ko"

bot = Bot(TOKEN)
dp = Dispatcher(bot)

HELP = """
/start - Вступительное сообщение
/help - список команд
/timetable - ссылка на расписание
"""
@dp.message_handler(commands = ['start'])
async def echo(message: types.Message):
    await message.answer(text = 'Добро пожаловать')

@dp.message_handler(commands = ['help'])
async def echo(message: types.Message):
    await message.answer(text = HELP)

@dp.message_handler(commands = ['timetable'])
async def echo(message: types.Message):
    await message.answer(text = 'https://rasp.omgtu.ru/')

if __name__ == '__main__':
    executor.start_polling(dp)