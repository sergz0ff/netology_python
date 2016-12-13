import json
import re
from collections import Counter
import codecs

with open('newsafr.json') as newsafr:
    newsafr = json.load(newsafr)

with codecs.open('newscy.json', 'r', encoding="cp1251") as newscy:
    with codecs.open('newscy.json', 'r', encoding="koi8-r") as newscy:
        newscy = json.load(newscy)

with codecs.open('newsfr.json', 'r', encoding="cp1252") as newsfr:
    with codecs.open('newsfr.json', 'r', encoding="iso8859_5") as newsfr:
        newsfr = json.load(newsfr)


with codecs.open('newsit.json', 'r', encoding="cp1252") as newsit:
    with codecs.open('newsit.json', 'r', encoding="cp1251") as newsit:
        newsit = json.load(newsit)

running_program = True

def count_words(country_name, jname):
    temp = ''

    for i in range(len(jname['rss']['channel']['item'])):
        temp += jname['rss']['channel']['item'][i]['description']['__cdata']

    p = re.compile(r'<.*?>')

    temp = p.sub('', temp)

    temp = re.sub("^\s+|\n|\r|\s+$", '', temp)

    temp = temp.replace("'", ' ').replace('/', ' ').replace('.', ' ').replace(',', ' ').replace('"', ' ')

    temp = temp.split(' ')

    long_words = []

    for i in range(len(temp)):
        if len(temp[i]) >= 6:
            long_words.append(temp[i])

    long_words = Counter(long_words)

    long_words = sorted(long_words.items(), key=lambda item: item[1])

    result = long_words[-10:]

    print(country_name + '. Топ 10 слов в новостях:')

    for i in reversed(result):
        print(i)

def count_words_1(country_name, jname):
        temp = ''

        for i in range(len(jname['rss']['channel']['item'])):
            temp += jname['rss']['channel']['item'][i]['description']

        p = re.compile(r'<.*?>')

        temp = p.sub('', temp)

        temp = re.sub("^\s+|\n|\r|\s+$", '', temp)

        temp = temp.replace("'", ' ').replace('/', ' ').replace('.', ' ').replace(',', ' ').replace('"', ' ')

        temp = temp.split(' ')

        long_words = []

        for i in range(len(temp)):
            if len(temp[i]) >= 6:
                long_words.append(temp[i])

        long_words = Counter(long_words)

        long_words = sorted(long_words.items(), key=lambda item: item[1])

        result = long_words[-10:]

        print(country_name + '. Топ 10 слов в новостях:')

        for i in reversed(result):
            print(i)


while running_program:
    country_id = input('Введите номер страны из списка: \r\n 1 - Африка\r\n 2 - Кипр\r\n 3 - Кипр\r\n 4 - Италия\r\n 0 - Выход\r\n')
    if country_id == '1':
        count_words('Африка', newsafr)
    if country_id == '2':
        count_words('Кипр', newscy)
    if country_id == '3':
        count_words('Кипр', newsfr)
    if country_id == '4':
        count_words_1('Италия', newsit)
    if country_id == '0':
        print('Программа завершена.\r\n До скорых встреч. ')
        running_program = False
    else:
        continue
