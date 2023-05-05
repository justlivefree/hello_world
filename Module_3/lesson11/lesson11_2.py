import csv
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from dotenv import load_dotenv
import os

load_dotenv('.env')

API_TOKEN = os.getenv('TOKEN')
storage = MemoryStorage()
bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)

REG = []
DIS = []

with open('regions.csv', encoding='utf-8-sig') as f:
    REG = list(csv.DictReader(f))

with open('districts.csv', encoding='utf-8-sig') as f:
    DIS = list(csv.DictReader(f))


class Form(StatesGroup):
    name = State()
    age = State()
    reg = State()
    dis = State()


@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await Form.name.set()
    await message.answer('Name: ')


@dp.message_handler(state=Form.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await Form.next()
    await message.answer('Age: ')


@dp.message_handler(state=Form.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await Form.next()
    mas = [i['name'] for i in REG]
    ids = [i['id'] for i in REG]
    ikm = InlineKeyboardMarkup(row_width=4)
    for i in range(len(mas)):
        ikm.add(InlineKeyboardButton(mas[i], callback_data=ids[i]))
    await message.answer('Regions: ', reply_markup=ikm)


@dp.callback_query_handler(state=Form.reg)
async def get_group(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(reg=callback.data)
    await Form.next()
    mas = [i['name'] for i in DIS if i['region'] == callback.data]
    ids = [i['id'] for i in DIS if i['region'] == callback.data]
    ikm = InlineKeyboardMarkup()
    for i in range(len(mas)):
        ikm.add(*[InlineKeyboardButton(mas[i], callback_data=ids[i])])
    await bot.edit_message_text('Chose district: ', callback.message.chat.id, callback.message.message_id, reply_markup=ikm)
    await callback.answer('')


@dp.callback_query_handler(state=Form.dis)
async def get_group(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(dis=callback.data)
    async with state.proxy() as data:
        data['email'] = callback.data
        name = data['name']
        age = data['age']
        r = [i['name'] for i in REG if i['id'] == data['reg']][0]
        d = [i['name'] for i in DIS if i['id'] == data['dis']][0]
        text = f'{name}, {age}, {r}, {d}'
        await bot.edit_message_text(text, callback.message.chat.id, callback.message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
