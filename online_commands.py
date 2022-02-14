import datetime
import pandas as pd
import requests
import xml.etree.ElementTree as ET
from lxml import html
import re

def transform_gold(x):
    if len(x) == 10:
        x = str(x).replace(',', '').replace(' ', '')
        return float(x[:4] + '.' + x[4:])
    else:
        return float(x)

# OnlineCommands
class OnlineCommands:
    def __init__(self, message):
        self.message = message

    @staticmethod
    def currency_today():
        today_date = datetime.datetime.now().strftime('%d.%m.%Y')
        currency_xml = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={today_date}').text
        root = ET.fromstring(currency_xml)
        for child in root:
            if child.attrib['ID'] == 'R01035':
                gbp_text = child.find('CharCode').text
                gbp_value = child.find('Value').text
            if child.attrib['ID'] == 'R01235':
                usd_text = child.find('CharCode').text
                usd_value = child.find('Value').text
            if child.attrib['ID'] == 'R01239':
                eur_text = child.find('CharCode').text
                eur_value = child.find('Value').text
        currency_today_message =f"""Курс валют на сегодня ({today_date}):
    - Доллар стоит {usd_value} руб.
    - Евро стоит {eur_value} руб.
    - Фунт стерлинга стоит {gbp_value} руб.
    """
        return currency_today_message

    @staticmethod
    def metals_today():
        dragmetals_online = pd.read_html(
        'https://www.cbr.ru/hd_base/metall/metall_base_new/', decimal=',', thousands='d')
        dragmetals_online = dragmetals_online[0]
        dragmetals_online.columns = ['Дата', 'Золото', 'Серебро', 'Платина', 'Палладий']
        today_date = datetime.datetime.now().strftime('%d.%m.%Y')

        dragmetals_online['Золото'] = dragmetals_online['Золото'].apply(transform_gold)
        dragmetals_online['Платина'] = dragmetals_online['Платина'].apply(transform_gold)
        dragmetals_online['Палладий'] = dragmetals_online['Палладий'].apply(transform_gold)
        drag_message = f"""Стоимость драг. металлов на сегодня ({today_date})\n"""
        drag_actual = dragmetals_online.head(1).to_dict()
        for k, v in drag_actual.items():
            if k != 'Дата':
                drag_message = drag_message + k + ' стоит ' + str(v[0]) + ' руб.\n'
        return drag_message
    
    @staticmethod
    def key_indices_today():
        today_date = datetime.datetime.now().strftime('%d.%m.%Y')
        key_indices = requests.get('https://www.cbr.ru/key-indicators/')
        tree = html.fromstring(key_indices.content)
        target_inflation = tree.xpath('/html/body/main/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]') # inflation target
        target_inflation = target_inflation[0].text.split('\r')[0]
        fact_inflation = tree.xpath('/html/body/main/div/div/div/div[1]/div[1]/div[2]/div[2]/div[2]')
        fact_inflation = fact_inflation[0].text.split('\r')[0]
        fact_inflation_month = tree.xpath('/html/body/main/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]')
        fact_inflation_month = fact_inflation_month[0].text.split('\r')[0]
        key_rate = tree.xpath('/html/body/main/div/div/div/div[1]/div[2]/div[2]/div/div[2]')
        key_rate = key_rate[0].text.split('\r')[0]
        key_rate_date = tree.xpath('/html/body/main/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div[1]')
        key_rate_date = key_rate_date[0].text.split('\xa0')[-1]
        key_indices_message = f"""Ключевые показатели ЦБ на {today_date}
    Цель по инфляции {target_inflation}
    Фактическая инфляция {fact_inflation} на {fact_inflation_month.lower()}
    Ключевая ставка с {key_rate_date} равна {key_rate}
    """
        return key_indices_message
