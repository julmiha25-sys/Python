#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta  # Работа со временем, вых дни
import pandas as pd
from random import randint # Рандомить список компаний по покупке акций
import configparser
import os

config = configparser.ConfigParser()
dirname = os.path.dirname(__file__)
config.read(os.path.join(dirname, 'config.ini'))

COMPANIES=eval(config['Companies']['COMPANIES']) # Компании торгуют на бирже

today=datetime.today()
# today.weekday() - День недели от 0 до 6 (0-Понедельник)
# Скприпт запускается на следующий день после торгов
yesterday=today-timedelta(days=1)
if 1<=today.weekday()<=5:
    d={
        'dt': [yesterday.strftime("%d-%m-%Y")]*len(COMPANIES)*2, # 5 компаний * 2 покупка-продажа
        'company': COMPANIES*2, # Покупка-продажа
        'transaction_type': ['bye']*len(COMPANIES)+['sell']*len(COMPANIES),
        'amount': [randint(0,1000) for _ in range(len(COMPANIES)*2)]
      }
    df=pd.DataFrame(d)
    df.to_csv(os.path.join(dirname,"sales-data.csv"),index=False)
    





