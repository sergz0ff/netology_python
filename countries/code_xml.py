import xml.etree.ElementTree as ET
from pprint import pprint

# Наш денежный баланс
money_amount = 10000

# Открываем файл
tree = ET.parse('countries.xml')
root = tree.getroot()



def print_countries_list():
    print('Страны в файле:')
    for country in root:
        for prop in range(len(country)):
            if country[prop].tag == 'name':
                print('-', country[prop].text, '-')
            else:
                print(country[prop].tag, ':', country[prop].text)
    print('-' * 50)

print_countries_list()

# Объявление множеств стран шенгена и стран с морем
schengen_countries = set()
sea_countries = set()
# Входящие данные раскидывем по множествам
for country in root.findall('country'):
    if country.findtext('schengen') == 'True':
        schengen_countries.add(country.findtext('name'))
    if country.findtext('sea') == 'True':
        sea_countries.add(country.findtext('name'))

# Вывод множеств
print('Страны с морем:')
for c in sea_countries:
    print('-', c, '-')
print('-' * 50)
print('Страны в Шенгене:')
for c in schengen_countries:
    print('-', c, '-')
print('-' * 50)
# Переменная на пересечении множеств
sea_schengen_countries = schengen_countries & sea_countries
# Вывод пересечения множеств
print('Страны в Шенгене и с морем:')
for c in sea_schengen_countries:
    print('-', c, '-')
print('-' * 50)
# Считаем и выводим денежный баланс в нужно валюте
print('Конвертер валюты:')
for country in root:
    print('-', country.findtext('name'), '-')
    currency_amount = money_amount / float(country.findtext('currency_rate'))
    print('У нас будет %.2f денег в местной валюте' % currency_amount)
