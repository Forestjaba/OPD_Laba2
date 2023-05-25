from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6066949542:AAE9oGxAT_zBCNbHC-P4MJ-FjngC6hfS9Ko"

bot = Bot(TOKEN)
dp = Dispatcher(bot)

SCRIPT = """
/help - список команд
/timetable - ссылка на расписание
/map - расположение 8 корпуса
/omgtu - официальный сайт ОмГТУ
/fitiks - сообщество ФИТиКС
"""
@dp.message_handler(commands = ['start'])
async def echo(message: types.Message):
    await message.answer(text = SCRIPT)

@dp.message_handler(commands = ['help'])
async def echo(message: types.Message):
    await message.answer(text = SCRIPT)

@dp.message_handler(commands = ['timetable'])
async def echo(message: types.Message):
    await message.answer(text = 'https://rasp.omgtu.ru/')

@dp.message_handler(commands = ['map'])
async def echo(message: types.Message):
    await message.answer(text = 'https://yandex.ru/maps/66/omsk/house/prospekt_mira_11k8/Y0oYdA5iTkIGQFtvfXxzdH1mYw==/?display-text=%D0%9E%D0%BC%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9%20%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82&indoorLevel=1&ll=73.294415%2C55.025276&mode=search&sctx=ZAAAAAgBEAAaKAoSCap%2FEMmQV1JAEZVHN8KifktAEhIJyEJ0CBwJ4j8RLA5nfjUH4z8iBgABAgMEBSgAOABA7cwGSAFiNnJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vU3VidGl0bGVzL1VzZUxvbmdQaW5TdWJ0aXRsZXM9MWI1cmVhcnI9c2NoZW1lX0xvY2FsL0dlby9TdWJ0aXRsZXMvUmFuZG9tUGluU3VidGl0bGVzPTFqAnJ1nQHNzEw9oAEAqAEAvQHveIzUwgE%2Bj73ZuATAw9rGBuDw0dkE88W3owS%2F%2BZn5A%2FLeoZ8Gpsev9APO6qTFhgf00%2FnJBu2v3NWjBdOdw6AGkfmIkQTqAQDyAQD4AQCCAhRjaGFpbl9pZDooODA1NTc0MjE4KYoCAJICAJoCDGRlc2t0b3AtbWFwcw%3D%3D&sll=73.294415%2C55.025276&sspn=0.004647%2C0.001623&text=chain_id%3A%28805574218%29&z=18.68')

@dp.message_handler(commands = ['omgtu'])
async def echo(message: types.Message):
    await message.answer(text = 'https://www.omgtu.ru/news/')

@dp.message_handler(commands = ['fitiks'])
async def echo(message: types.Message):
    await message.answer(text = 'https://vk.com/fitiks_omgtu')

if __name__ == '__main__':
    executor.start_polling(dp)