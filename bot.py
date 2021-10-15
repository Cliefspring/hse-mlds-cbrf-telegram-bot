# token
from TOKEN import *
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# bot instance
bot = Bot(token=TOKEN)

# For example use simple MemoryStorage for Dispatcher. uses local memory. not the best idea :)
storage = MemoryStorage()

# dispatcher instance
dp = Dispatcher(bot, storage=storage)