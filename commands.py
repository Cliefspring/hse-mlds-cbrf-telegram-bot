from os import fsdecode
import re
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot import *
from data import *



async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            # command name and description
            types.BotCommand("start", "Запустить бота"), 
            types.BotCommand('currency_today', 'Курс валют на сегодня'),
            types.BotCommand('metals_today', 'Курс драг. металлов на сегодня'),
            types.BotCommand('key_indices_today', 'Инфляция план/факт и ключевая ставка')
        ]
    )


@dp.message_handler(state='*', commands=['cancel'])
@dp.message_handler(lambda message: message.text.lower() == 'cancel', state='*')
async def cancel(message: types.Message, state: FSMContext):
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Запрос отменен')


@dp.message_handler(commands=['start'])
async def welcome_user(message):
    welcome_message = f"""
    Привет, {message.from_user.first_name + ' ' + message.from_user.last_name}!\n
Хочешь посмотреть курс основных валют на сегодня? Жми - /currency_today
Интересуют драг. металлы? - /metals_today
Озабочен ставками по кредитам/депозитам? - Посмотри на ключевую ставку ЦБ и инфляцию - /key_indices_today
Посмотреть все мои комманды /show_commands"""
    await message.reply(welcome_message)


@dp.message_handler(commands=['show_commands'])
async def show_commands(message):
    show_commands_message = """Посмотри, что я умею:\n
/currency_today - Курс основных валют на сегодня
/metals_today - Курс драгоценных металлов на сегодня
/key_indices_today - Цель по инфляции, актуальная инфляция, ключевая ставка ЦБ
/get_license_by_ogrn - Узнать статус банка по ОГРН, а также номер и дату выдачи лицензии
/get_license_by_name - Узнать статус банка по его имени, а также ОГРН, номер и дату выдачи лицензии
/metals_at - Узнать курс драгоценных металлов на определенную дату
/inflation_at - Узнать инфляцию на определенную дату
    """
    await message.answer(show_commands_message)


### ONLINE DATA
@dp.message_handler(commands=['currency_today'])
async def currency_today(message : types.Message):
    #print(message)
    await message.reply(OnlineData.currency_today())

@dp.message_handler(commands=['metals_today'])
async def metals_today(message):
    await message.reply(OnlineData.metals_today())


@dp.message_handler(commands=['key_indices_today'])
async def key_indices_today(message):
    await message.reply(OnlineData.key_indices_today())



## OFFLINE DATA

##### get_license_by_ogrn START 
# in case I will need many states to store
class WaitForOGRN(StatesGroup):
    waiting_for_ogrn = State()


async def get_user_ogrn(message):
    await message.reply("Введите ОГРН")
    await WaitForOGRN.waiting_for_ogrn.set()

async def get_license_by_ogrn(message : types.Message, state: FSMContext):
    if len(message.text) == 13 and re.match(r'\d{13}', message.text):
        await message.reply(OfflineData(message.text).get_license_by_ogrn())
        await state.finish()
    else:
        await message.reply(f"ОГРН {message.text} некорректный. ОГРН состоит из 13 цифр, стоящих друг за другом подряд.\
            Например, 1234566543219")
        

dp.register_message_handler(get_user_ogrn, commands="get_license_by_ogrn")
dp.register_message_handler(get_license_by_ogrn, state = WaitForOGRN.waiting_for_ogrn)



    

##### get_license_by_ogrn END


##### get_license_by_ogrn START 
# in case I will need many states to store
class WaitForNAME(StatesGroup):
    waiting_for_name = State()


async def get_user_org_name(message):
    await message.reply("Введите имя финансовой организации (банка)")
    await WaitForNAME.waiting_for_name.set()

async def get_license_by_name(message : types.Message, state: FSMContext):
    await message.reply(OfflineData(message.text).get_license_by_name())
    await state.finish()

dp.register_message_handler(get_user_org_name, commands="get_license_by_name")
dp.register_message_handler(get_license_by_name, state = WaitForNAME.waiting_for_name)
##### get_license_by_ogrn END


##### metals_at START 
# in case I will need many states to store
class WaitForDate(StatesGroup):
    waiting_for_date = State()


async def get_date_for_metals(message):
    await message.reply("Введите дату в формате: 02.10.2021")
    await WaitForDate.waiting_for_date.set()

async def metals_at(message : types.Message, state: FSMContext):
    await message.reply(OfflineData(message.text).metals_at())
    await state.finish()

dp.register_message_handler(get_date_for_metals, commands="metals_at")
dp.register_message_handler(metals_at, state = WaitForDate.waiting_for_date)
##### metals_at END

##### inflation_at START 
# in case I will need many states to store
class WaitForDate2(StatesGroup):
    waiting_for_date = State()


async def get_date_for_inflation(message):
    await message.reply("Введите дату в формате: 02.10.2021")
    await WaitForDate2.waiting_for_date.set()

async def inflation_at(message : types.Message, state: FSMContext):
    await message.reply(OfflineData(message.text).inflation_at())
    await state.finish()

dp.register_message_handler(get_date_for_inflation, commands="inflation_at")
dp.register_message_handler(inflation_at, state = WaitForDate2.waiting_for_date)
##### inflation_at END



##### keyrate_at START 
# in case I will need many states to store
class WaitForDate3(StatesGroup):
    waiting_for_date = State()


async def get_date_for_keyrate(message):
    await message.reply("Введите дату в формате: 02.10.2021")
    await WaitForDate3.waiting_for_date.set()

async def keyrate_at(message : types.Message, state: FSMContext):
    await message.reply(OfflineData(message.text).keyrate_at())
    await state.finish()

dp.register_message_handler(get_date_for_keyrate, commands="keyrate_at")
dp.register_message_handler(keyrate_at, state = WaitForDate3.waiting_for_date)
##### keyrate_at END
