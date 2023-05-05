from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv('.env')

API_TOKEN = os.getenv('TOKEN')

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


def make_board():
    data = [
        ['1', '2', '3', '+'],
        ['4', '5', '6', '-'],
        ['7', '8', '9', '*'],
        ['0', '=', '<-', '/']
    ]
    ikm = InlineKeyboardMarkup(row_width=4)
    for i in data:
        ikm.add(*[InlineKeyboardButton(j, callback_data=j) for j in i])
    return ikm


@dp.message_handler(commands='start')
async def starter(message: types.Message):
    board = make_board()
    await message.answer('Result: 0', reply_markup=board)

@dp.callback_query_handler()
async def calculator(callback: types.CallbackQuery):
    board = make_board()
    click = callback.data
    result = callback.message.text
    result = result.split(': ')[-1]
    if result == '0':
        result = ''
    if click.isdigit():
        result += click
    if click in ('+', '-', '*', '/'):
        if result[-1].isdigit():
            result += click
        else:
            result = result[:-1] + click
    if click == '=':
        result = str(eval(result))

    if click == '<-':
        result = result[:-1]
        if result == '':
            result = '0'
    if result != '0':
        await bot.edit_message_text(f'Result: {result}', callback.from_user.id, callback.message.message_id, reply_markup=board)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
