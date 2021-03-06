#5. Создать список, содержащий цены на товары (10–20 товаров), например:
#[57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

def format_price(price):
    return '{0} руб {1:0>2} коп'.format(int(price // 1), int(price*100 % 100 ))


def get_all_price(list_prices):
    str_prices = ''
    for price in list_prices:
        if len(str_prices) > 0:
            str_prices += ', '
        str_prices += format_price(price)
    return str_prices


list_price = [57.8, 46.51, 97, 23.5, 2.11, 52.01, 43.09, 45.21, 15.44, 75.86, 24.66,
              35.93, 25.83, 22.58, 1.52, 26.9, 8.41, 25.74, 57.5, 97.1]

print('Цены без сортировки: ',get_all_price(list_price))

print('Отсортированные цены: ', get_all_price(sorted(list_price)))

print('Исходный список сохранился: ',get_all_price(list_price))

list_sort_price = sorted(list_price, key=None, reverse=True)
print('Цены 5 самых дорогих товаров:',get_all_price(list_sort_price[0:5:]))