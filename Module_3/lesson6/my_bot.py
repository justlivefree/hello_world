import os

import aiogram
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv('../lesson7/.env')
API_TOKEN = os.getenv('TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Online')


"""  USER PANEL  """


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Hello')
    except aiogram.utils.exceptions.BotBlocked:
        await message.reply('After click start to bot! @p11newbot')


@dp.message_handler(commands=['type_jobs'])
async def command_type(message: types.Message):
    await bot.send_message(message.from_user.id, 'mon->fr 9pm-22pm')


@dp.message_handler(commands=['location'])
async def command_location(message: types.Message):
    await bot.send_message(message.chat.id, 'Tashkent')


"""  ADMIN PANEL  """


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    # await message.answer('You wrote message: ' + message.text)
    # await message.reply('I reply you: ' + message.text)
    # await bot.send_message(message.from_user.id, message.text+str(message.from_user.id))


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
