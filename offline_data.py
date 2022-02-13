import datetime
import pandas as pd
import requests
import xml.etree.ElementTree as ET
from lxml import html
import re


# OfflineCommands

def license_value(x):
    if x == 'ОТЗ':
        return "отозвана"
    elif x == 'АНН':
        return "аннулирована"
    else:
        return "действительна"


class OfflineCommands:
    
    def __init__(self, message):
        self.message = message
    
    def get_license_by_ogrn(self):
        user_ogrn = self.message
        orglist = pd.read_excel('./data/CREDIT_ORGANIZATIONS_LIST.xlsx', dtype=str)
        orglist['lic'] = orglist['lic'].fillna(1)
        ogrn_data = orglist[orglist['ogrn'] == user_ogrn]
        
        get_license_by_ogrn_message = f"""Под ОГРН {user_ogrn} зарегистрирован {ogrn_data['csname'].iloc[0]}, который \
получил лицензию {ogrn_data['cdreg'].iloc[0]} с номером {ogrn_data['cregnum'].iloc[0]}.
В настоящий момент лицензия {license_value(ogrn_data['lic'].iloc[0])}.
"""
        return get_license_by_ogrn_message

    def get_license_by_name(self):
        user_org_name = self.message
        orglist = pd.read_excel('./data/CREDIT_ORGANIZATIONS_LIST.xlsx', dtype=str)
        orglist['lic'] = orglist['lic'].fillna(1)
        name_data = orglist[orglist['csname'].str.lower().str.find(user_org_name.lower()) != -1]
        if name_data.shape[0] > 0:
            whole_message = f"""По имени {user_org_name} найдены следующие организации в количестве {name_data.shape[0]}:\n"""
            for i, row in enumerate(range(name_data.shape[0])):
                whole_message += f"""{name_data['csname'].iloc[i]} c ОГРН {name_data['ogrn'].iloc[i]}, который
 получил лицензию {name_data['cdreg'].iloc[i]} с номером {name_data['cregnum'].iloc[i]}.
 В настоящий момент лицензия {license_value(name_data['lic'].iloc[i])}\n\n"""
        else:
            whole_message = f"""По имени {user_org_name} ничего не найдено в базе.\
        Попробуйте другое имя или проверьте корректность написания"""
        return whole_message

    def metals_at(self):
        metals = pd.read_csv('./data/PRECIOUS_METALS_01_07_2008_07_10_2021.csv', sep=';')
        if re.fullmatch(r'\d{2}.\d{2}.\d{4}', self.message):
            metals_at_data = metals[metals['date'] == self.message]
            if metals_at_data.shape[0] == 0:
                return f'Нет данных на дату {self.message}'
            else:
                out_str_metals = metals_at_data.to_string(index=False)
                out_str_metals = out_str_metals.replace('date', 'Дата').replace('gold','Золото').\
                    replace('silver','Серебро').replace('platinum','Платинум').replace('palladuim', 'Палладий')
                return out_str_metals
        else:
            return f'Дата {self.message} некорректного формата. Попробуйте, например, такую: 02.10.2021'

    def inflation_at(self):
        inflation = pd.read_csv('./data/INFLATION_RATE_years_prcnt.csv', sep=',')
        if re.fullmatch(r'\d{2}.\d{2}.\d{4}', self.message):
            inflation_at_date = inflation[inflation['Год'] == int(self.message.split('.')[2])]
            if inflation_at_date.shape[0] == 0:
                return f'Нет данных на дату {self.message}'
            else:
                inflation_at_date = inflation_at_date.iloc[:, int(self.message.split('.')[1])]
                if pd.isna(inflation_at_date).any():
                    return f'Нет данных на дату {self.message}'
                else:
                    return f'Инфляция была равна {inflation_at_date.to_string(index=False)}%'
        else:
            return f'Дата {self.message} некорректного формата. Попробуйте, например, такую: 02.10.2021'

    def keyrate_at(self):
        keyrate = pd.read_csv('./data/KEY_RATE.csv', sep=';')
        if re.fullmatch(r'\d{2}.\d{2}.\d{4}', self.message):
            keyrate_at_date = keyrate[keyrate['date'] == self.message]
            if keyrate_at_date.shape[0] == 0:
                return f'Нет данных на дату {self.message}'
            else:
                return f'Ключевая ставка была равна {keyrate_at_date.iloc[0, 1]}%'
        else:
            return f'Дата {self.message} некорректного формата. Попробуйте, например, такую: 02.10.2021'




