import csv
import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv

reg = [*csv.DictReader(open('../../../Module4Project/regions.csv', encoding='utf-8'))]
dist = [*csv.DictReader(open('../../../Module4Project/districts.csv'))]
load_dotenv('.env')

API_TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for row in reg:
        rkm.add(row['name'])
    await message.answer('Viloyatlar', reply_markup=rkm)


@dp.message_handler(lambda msg: msg.text in (i['name'] for i in reg))
async def echo(message: types.Message):
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    _id = [i['\ufeffid'] for i in reg if i['name'] == message.text]
    print(_id[0])
    _dist = [i['name'] for i in dist if i['region'] == _id[0]]
    for i in _dist:
        rkm.add(i)


@dp.message_handler(content_types=types.ContentTypes.USER_SHARED)
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
