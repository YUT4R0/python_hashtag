# access site with  https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui as auto
import pandas as pd
import time

auto.PAUSE = 1

# variables
url = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'jeffersoncamisinhas@gmail.com'
password = 'jucimar42forever'
delay = 1.75

# open navigator
auto.press('win')
auto.write('chrome')
auto.press('enter')
time.sleep(delay)


# # acess the link
auto.write(url)
auto.press('enter')
time.sleep(delay)

# login and password
auto.press('tab')
auto.write(email)
auto.press('tab')
auto.write(password)
auto.press('enter')
time.sleep(1)
auto.press('tab')

# import db from products.csv
table = pd.read_csv('./produtos.csv')

# get a value from table, register this value on the field and repeat registration for products in products.csv

for i in table.index:
    auto.write(str(table.loc[i, 'codigo']))
    auto.press('tab')
    auto.write(str(table.loc[i, 'marca']))
    auto.press('tab')
    auto.write(str(table.loc[i, 'tipo']))
    auto.press('tab')
    auto.write(str(table.loc[i, 'categoria']))
    auto.press('tab')
    auto.write(str(table.loc[i, 'preco_unitario']))
    auto.press('tab')
    auto.write(str(table.loc[i, 'custo']))
    auto.press('tab')
    if not pd.isna(table.loc[i, 'obs']):
        auto.write(str(table.loc[i, 'obs']))
    auto.press('enter')
    auto.hotkey('ctrl', 'l')
    auto.press('tab', presses=4)

auto.hotkey('ctrl', 'w')
print(f'All of {table.size} items was registered!')
