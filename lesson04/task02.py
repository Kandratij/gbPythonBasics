#2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре
# был передан аргумент? В качестве примера выведите курсы доллара и евро.
import requests
from xml.dom import minidom


def currency_rates(currency_code):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    dom = minidom.parseString(requests.get(url).text)
    valutes = dom.getElementsByTagName("Valute")
    rate = [[element.getElementsByTagName("Value")[0].firstChild.data.replace(',', '.'),
             element.getElementsByTagName("Nominal")[0].firstChild.data]
            for element in valutes if element.getElementsByTagName('CharCode')[0].firstChild.data == currency_code.upper()]
    if len(rate) == 1:
        return float(rate[0][0])/float(rate[0][1])
    else:
        return None


print(currency_rates('USD'))

print(currency_rates('eur'))
