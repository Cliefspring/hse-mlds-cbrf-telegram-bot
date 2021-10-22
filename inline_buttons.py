from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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

years_inflation = ['inflation_1992', 'inflation_1993', 'inflation_1994', 'inflation_1995',
 'inflation_1996', 'inflation_1997', 'inflation_1998', 'inflation_1999', 'inflation_2000',
  'inflation_2001', 'inflation_2002', 'inflation_2003', 'inflation_2004', 'inflation_2005', 
  'inflation_2006', 'inflation_2007', 'inflation_2008', 'inflation_2009', 'inflation_2010',
   'inflation_2011', 'inflation_2012', 'inflation_2013', 'inflation_2014', 'inflation_2015',
    'inflation_2016', 'inflation_2017', 'inflation_2018', 'inflation_2019', 'inflation_2020',
     'inflation_2021']


######
currency_markup = InlineKeyboardMarkup(
    one_time_keyboard=True # to hide buttons after pressing the button
    )


currency_buttons = [
    InlineKeyboardButton(text='1999', callback_data='currency_1999'),
    InlineKeyboardButton(text='2000', callback_data='currency_2000'),
    InlineKeyboardButton(text='2001', callback_data='currency_2001'),
    InlineKeyboardButton(text='2002', callback_data='currency_2002'),
    InlineKeyboardButton(text='2003', callback_data='currency_2003'),
    InlineKeyboardButton(text='2004', callback_data='currency_2004'),
    InlineKeyboardButton(text='2005', callback_data='currency_2005'),
    InlineKeyboardButton(text='2006', callback_data='currency_2006'),
    InlineKeyboardButton(text='2007', callback_data='currency_2007'),
    InlineKeyboardButton(text='2008', callback_data='currency_2008'),
    InlineKeyboardButton(text='2009', callback_data='currency_2009'),
    InlineKeyboardButton(text='2010', callback_data='currency_2010'),
    InlineKeyboardButton(text='2011', callback_data='currency_2011'),
    InlineKeyboardButton(text='2012', callback_data='currency_2012'),
    InlineKeyboardButton(text='2013', callback_data='currency_2013'),
    InlineKeyboardButton(text='2014', callback_data='currency_2014'),
    InlineKeyboardButton(text='2015', callback_data='currency_2015'),
    InlineKeyboardButton(text='2016', callback_data='currency_2016'),
    InlineKeyboardButton(text='2017', callback_data='currency_2017'),
    InlineKeyboardButton(text='2018', callback_data='currency_2018'),
    InlineKeyboardButton(text='2019', callback_data='currency_2019'),
    InlineKeyboardButton(text='2020', callback_data='currency_2020'),
    InlineKeyboardButton(text='2021', callback_data='currency_2021')
]

currency_markup.add(*currency_buttons)

years_currency = ['currency_1999', 'currency_2000', 'currency_2001', 'currency_2002', 'currency_2003',
 'currency_2004', 'currency_2005', 'currency_2006', 'currency_2007', 'currency_2008', 'currency_2009',
  'currency_2010', 'currency_2011', 'currency_2012', 'currency_2013', 'currency_2014', 'currency_2015',
   'currency_2016', 'currency_2017', 'currency_2018', 'currency_2019', 'currency_2020', 'currency_2021']


###
######
metals_markup = InlineKeyboardMarkup(
    one_time_keyboard=True # to hide buttons after pressing the button
    )


metals_buttons = [
    InlineKeyboardButton(text='2008', callback_data='metals_2008'),
InlineKeyboardButton(text='2009', callback_data='metals_2009'),
InlineKeyboardButton(text='2010', callback_data='metals_2010'),
InlineKeyboardButton(text='2011', callback_data='metals_2011'),
InlineKeyboardButton(text='2012', callback_data='metals_2012'),
InlineKeyboardButton(text='2013', callback_data='metals_2013'),
InlineKeyboardButton(text='2014', callback_data='metals_2014'),
InlineKeyboardButton(text='2015', callback_data='metals_2015'),
InlineKeyboardButton(text='2016', callback_data='metals_2016'),
InlineKeyboardButton(text='2017', callback_data='metals_2017'),
InlineKeyboardButton(text='2018', callback_data='metals_2018'),
InlineKeyboardButton(text='2019', callback_data='metals_2019'),
InlineKeyboardButton(text='2020', callback_data='metals_2020'),
InlineKeyboardButton(text='2021', callback_data='metals_2021')
]

metals_markup.add(*metals_buttons)

years_metals = ['metals_2008', 'metals_2009', 'metals_2010', 'metals_2011', 'metals_2012',
 'metals_2013', 'metals_2014', 'metals_2015', 'metals_2016', 'metals_2017', 'metals_2018',
  'metals_2019', 'metals_2020', 'metals_2021']
