# my modules
from commands import *
# external libraries
from aiogram.utils import executor


# set commands
async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)


# run bot
if __name__ == '__main__':
    executor.start_polling(dp)