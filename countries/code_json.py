import json

# Наш денежный баланс
money_amount = 10000

# Открываем файл
with open('countries.json') as countries_file:
    countries = json.load(countries_file)

def print_countries_list():
    print('Страны в файле:')
    for country_name, properties in countries.items():
        print('-', country_name, '-')
        for prop in properties:
            print(prop, ':', properties.get(prop))
    print('-' * 50)

print_countries_list()
# Объявление множеств стран шенгена и стран с морем
schengen_countries = set()
sea_countries = set()

# Входящие данные раскидывем по множествам
for country_name, properties in countries.items():
    if properties['schengen'] == 'True':
        schengen_countries.add(country_name)
    if properties['sea'] == 'True':
        sea_countries.add(country_name)

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
for country_name, properties in countries.items():
    print('-', country_name, '-')
    currency_amount = money_amount / properties['currency_rate']
    print('У нас будет %.2f денег в местной валюте' % currency_amount)


# # Вывод содержания пересечения множеств
# for country_name in sea_schengen_countries:
#     print(country_name, countries[country_name])
