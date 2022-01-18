#3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
# которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
# Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?
import requests
from xml.dom import minidom
from datetime import datetime

def currency_rates(currency_code):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    dom = minidom.parseString(requests.get(url).text)
    valutes = dom.getElementsByTagName("Valute")
    dat = datetime.strptime(dom.getElementsByTagName("ValCurs")[0].getAttribute('Date'), '%d.%m.%Y')
    rate = [[element.getElementsByTagName("Value")[0].firstChild.data.replace(',', '.'),
             element.getElementsByTagName("Nominal")[0].firstChild.data]
            for element in valutes if element.getElementsByTagName('CharCode')[0].firstChild.data == currency_code.upper()]
    if len(rate) == 1:
        return [dat, float(rate[0][0])/float(rate[0][1])]
    else:
        return None


print(currency_rates('USD'))

print(currency_rates('eur')[0].strftime('%d.%m.%Y'), currency_rates('USD')[1])
# Вопрос. В данном случае Python 2 раза выполнит функцию или 1 раз?
