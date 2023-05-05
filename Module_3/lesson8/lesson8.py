from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from data import DATA
import os

load_dotenv('.env')

API_TOKEN = os.getenv('TOKEN')

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def message(message: types.Message):
    cur_page = 1
    ikm = InlineKeyboardMarkup()
    ikm.add(InlineKeyboardButton('<-', callback_data=f'b_1'),
            InlineKeyboardButton(f'{cur_page}/{len(DATA)}', callback_data='len_1'),
            InlineKeyboardButton('->', callback_data=f'th_2'))
    await message.answer(DATA[cur_page - 1], reply_markup=ikm)


@dp.callback_query_handler()
async def message(callback: types.CallbackQuery):
    d = callback.data
    cur_page = 1
    if d.startswith('b_'):
        cur_page = int(d.split('b_')[-1])
    if d.startswith('th_'):
        cur_page = int(d.split('th_')[-1])
    if d.startswith('len_'):
        cur_page = int(d.split('len_')[-1])
    ikm = InlineKeyboardMarkup()
    ikm.add(InlineKeyboardButton('<-', callback_data=f'b_{len(DATA) if cur_page == 1 else cur_page - 1}'),
            InlineKeyboardButton(f'{cur_page}/{len(DATA)}', callback_data=f'len_{cur_page}'),
            InlineKeyboardButton('->', callback_data=f'th_{1 if cur_page == len(DATA) else cur_page + 1}'))
    await bot.edit_message_text(DATA[cur_page - 1], callback.from_user.id, callback.message.message_id,
                                reply_markup=ikm)
    await callback.answer(str(cur_page))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
