from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inflation_markup = InlineKeyboardMarkup(
    one_time_keyboard=True # to hide buttons after pressing the button
    )

inflation_buttons = [
    InlineKeyboardButton(text=str(year), callback_data=f'inflation_{str(year)}') for year in range(1992, 2022)
]

inflation_markup.add(*inflation_buttons)

years_inflation = [f'inflation_{str(year)}' for year in range(1992, 2022)]

######
currency_markup = InlineKeyboardMarkup(
    one_time_keyboard=True # to hide buttons after pressing the button
    )


currency_buttons = [
    InlineKeyboardButton(text=str(year), callback_data=f'currency_{str(year)}') for year in range(1999, 2022)
]

currency_markup.add(*currency_buttons)

years_currency = [f'currency_{str(year)}' for year in range(1999, 2022)]


###
######
metals_markup = InlineKeyboardMarkup(
    one_time_keyboard=True # to hide buttons after pressing the button
    )


metals_buttons = [
    InlineKeyboardButton(text=str(year), callback_data=f'metals_{str(year)}') for year in range(2008, 2022)
]


metals_markup.add(*metals_buttons)

years_metals = [f'metals_{str(year)}' for year in range(2008, 2022)]
