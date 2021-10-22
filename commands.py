from os import fsdecode
import re
from aiogram import types
from aiogram import filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message
from aiogram.types import File, InputFile
from aiogram.types.input_media import MediaGroup

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
/keyrate_at - Узнать ключевую ставку на определенную дату
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


##### inflation_graph
inflation_markup = InlineKeyboardMarkup(
    one_time_keyboard=True # to hide buttons after pressing the button
    )

inflation_buttons = [
    InlineKeyboardButton(text='1992', callback_data='inflation_1992'),
    InlineKeyboardButton(text='1993', callback_data='inflation_1993'),
    InlineKeyboardButton(text='1994', callback_data='inflation_1994'),
    InlineKeyboardButton(text='1995', callback_data='inflation_1995'),
    InlineKeyboardButton(text='1996', callback_data='inflation_1996'),
    InlineKeyboardButton(text='1997', callback_data='inflation_1997'),
    InlineKeyboardButton(text='1998', callback_data='inflation_1998'),
    InlineKeyboardButton(text='1999', callback_data='inflation_1999'),
    InlineKeyboardButton(text='2000', callback_data='inflation_2000'),
    InlineKeyboardButton(text='2001', callback_data='inflation_2001'),
    InlineKeyboardButton(text='2002', callback_data='inflation_2002'),
    InlineKeyboardButton(text='2003', callback_data='inflation_2003'),
    InlineKeyboardButton(text='2004', callback_data='inflation_2004'),
    InlineKeyboardButton(text='2005', callback_data='inflation_2005'),
    InlineKeyboardButton(text='2006', callback_data='inflation_2006'),
    InlineKeyboardButton(text='2007', callback_data='inflation_2007'),
    InlineKeyboardButton(text='2008', callback_data='inflation_2008'),
    InlineKeyboardButton(text='2009', callback_data='inflation_2009'),
    InlineKeyboardButton(text='2010', callback_data='inflation_2010'),
    InlineKeyboardButton(text='2011', callback_data='inflation_2011'),
    InlineKeyboardButton(text='2012', callback_data='inflation_2012'),
    InlineKeyboardButton(text='2013', callback_data='inflation_2013'),
    InlineKeyboardButton(text='2014', callback_data='inflation_2014'),
    InlineKeyboardButton(text='2015', callback_data='inflation_2015'),
    InlineKeyboardButton(text='2016', callback_data='inflation_2016'),
    InlineKeyboardButton(text='2017', callback_data='inflation_2017'),
    InlineKeyboardButton(text='2018', callback_data='inflation_2018'),
    InlineKeyboardButton(text='2019', callback_data='inflation_2019'),
    InlineKeyboardButton(text='2020', callback_data='inflation_2020'),
    InlineKeyboardButton(text='2021', callback_data='inflation_2021'),    
]
inflation_markup.add(*inflation_buttons)


@dp.message_handler(commands=['inflation_graph'])
async def inflation_at(message : types.Message):
    await message.reply("Выбери год, на который хочешь посмотреть график:", 
    reply_markup=inflation_markup)



years_inflation = ['inflation_1992', 'inflation_1993', 'inflation_1994', 'inflation_1995',
 'inflation_1996', 'inflation_1997', 'inflation_1998', 'inflation_1999', 'inflation_2000',
  'inflation_2001', 'inflation_2002', 'inflation_2003', 'inflation_2004', 'inflation_2005', 
  'inflation_2006', 'inflation_2007', 'inflation_2008', 'inflation_2009', 'inflation_2010',
   'inflation_2011', 'inflation_2012', 'inflation_2013', 'inflation_2014', 'inflation_2015',
    'inflation_2016', 'inflation_2017', 'inflation_2018', 'inflation_2019', 'inflation_2020',
     'inflation_2021']

@dp.message_handler(filters.CommandStart())
@dp.callback_query_handler(text=years_inflation)
async def send_inflation_graph(call: types.CallbackQuery):
    if call.data == 'inflation_1992':
        photo = InputFile("graphs/inflation_1992.png")
        await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_1993':
        photo = InputFile("graphs/inflation_1993.png")
        await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_1994':
            photo = InputFile("graphs/inflation_1994.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_1995':
            photo = InputFile("graphs/inflation_1995.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_1996':
            photo = InputFile("graphs/inflation_1996.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_1997':
            photo = InputFile("graphs/inflation_1997.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_1998':
            photo = InputFile("graphs/inflation_1998.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_1999':
            photo = InputFile("graphs/inflation_1999.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2000':
            photo = InputFile("graphs/inflation_2000.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2001':
            photo = InputFile("graphs/inflation_2001.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2002':
            photo = InputFile("graphs/inflation_2002.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2003':
            photo = InputFile("graphs/inflation_2003.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2004':
            photo = InputFile("graphs/inflation_2004.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2005':
            photo = InputFile("graphs/inflation_2005.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2006':
            photo = InputFile("graphs/inflation_2006.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2007':
            photo = InputFile("graphs/inflation_2007.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2008':
            photo = InputFile("graphs/inflation_2008.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2009':
            photo = InputFile("graphs/inflation_2009.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2010':
            photo = InputFile("graphs/inflation_2010.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2011':
            photo = InputFile("graphs/inflation_2011.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2012':
            photo = InputFile("graphs/inflation_2012.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2013':
            photo = InputFile("graphs/inflation_2013.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2014':
            photo = InputFile("graphs/inflation_2014.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2015':
            photo = InputFile("graphs/inflation_2015.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2016':
            photo = InputFile("graphs/inflation_2016.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2017':
            photo = InputFile("graphs/inflation_2017.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2018':
            photo = InputFile("graphs/inflation_2018.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2019':
            photo = InputFile("graphs/inflation_2019.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2020':
            photo = InputFile("graphs/inflation_2020.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    if call.data == 'inflation_2021':
            photo = InputFile("graphs/inflation_2021.png")
            await bot.send_photo(call.from_user.id, photo=photo)
    

  



#####