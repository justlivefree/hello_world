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


class Form(StatesGroup):
    name = State()
    surname = State()
    num = State()
    group = State()
    vaqt = State()


@dp.message_handler(commands='start')
async def starter(message: types.Message):
    await Form.name.set()
    await message.answer('Welcome to our study center!')
    await message.answer('Name: ')


@dp.message_handler(state=Form.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await Form.next()
    await message.answer('Surname: ')


@dp.message_handler(state=Form.surname)
async def get_surename(message: Message, state=FSMContext):
    await state.update_data(surname=message.text)
    await Form.next()
    await message.answer('Phone number: ')


@dp.message_handler(lambda val: not (len(val.text) == 9 and val.text.isdigit()), state=Form.num)
async def get_num(message: Message):
    await message.answer('Phone number incorrect')


@dp.message_handler(lambda val: len(val.text) == 9 and val.text.isdigit(), state=Form.num)
async def get_num(message: Message, state=FSMContext):
    await state.update_data(num=message.text)
    await Form.next()
    mas = [['Beginner', 'Elementary'], ['Pre-inter', 'Inter'], ['Up-inter', 'IELTS']]
    ikm = InlineKeyboardMarkup()
    for i in mas:
        ikm.add(*[InlineKeyboardButton(j, callback_data=j) for j in i])
    await message.answer('Chose group: ', reply_markup=ikm)


@dp.callback_query_handler(state=Form.group)
async def get_group(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(group=callback.data)
    await Form.next()
    ikm = InlineKeyboardMarkup()
    ikm.add(InlineKeyboardButton('09:00', callback_data='morning'),
            InlineKeyboardButton('18:00', callback_data='evening'))
    await bot.send_message(callback.message.chat.id, 'Chose time: ', reply_markup=ikm)


@dp.callback_query_handler(state=Form.vaqt)
async def get_group(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(vaqt=callback.data)
    async with state.proxy() as data:
        data['email'] = callback.data
        name = data['name']
        surname = data['surname']
        gr = data['group']
        tm = data['vaqt']
        num = data['num']
        text = f'Sizning malumotlaringiz\n' \
               f'name - {name}\n' \
               f'surename - {surname}\n' \
               f'phone num - {num}'
        text += f'\ngroup - {gr}\n time - {tm}'
        await bot.send_message(callback.message.chat.id, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
