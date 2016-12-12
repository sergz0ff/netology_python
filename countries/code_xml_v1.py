import xml.etree.ElementTree as ET
from pprint import pprint

# Наш денежный баланс
money_amount = 10000

# Открываем файл
tree = ET.parse('countries.xml')
root = tree.getroot()

countries = {}
#Заполняем словарь из xml
for child in root:
    print(child[0].text)
    countries[child[0].text] = dict((i, {child[i].tag: child[i].text}) for i in child)
    # for i in range(len(child)):
    #     print(child[i].tag, ':', child[i].text)
    #     countries[child[0].text] = dict(i, (child[i].tag, child[i].text) for iin range(len(child))

pprint(countries)
