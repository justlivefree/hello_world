from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv('.env')

API_TOKEN = os.getenv('TOKEN')

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
