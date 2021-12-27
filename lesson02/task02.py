#2. Дан список:
#['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
#Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
# и дополнить нулём до двух целочисленных разрядов:
#['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
#
#Сформировать из обработанного списка строку:
#в "05" часов "17" минут температура воздуха была "+05" градусов

#Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
#Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. Главное: дополнить числа до двух разрядов нулём!

list_info_weather_src = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_info_weather = []

for word in list_info_weather_src:
    if word.isdigit() or (word[0] in ('+', '-') and word[1:].isdigit()):
        list_info_weather.append('"')
        if word[0] in ('+', '-'):
            list_info_weather.append(word[0]+word[1:].rjust(2, '0'))
        else:
            list_info_weather.append(word.rjust(2, '0'))
        list_info_weather.append('"')
    else:
        list_info_weather.append(word)

str_info_weather = ''
open_quotes = False
for word in list_info_weather:
    str_info_weather += word
    if open_quotes and word == '"':
        open_quotes = False
    elif word == '"':
        open_quotes = True
    if not open_quotes:
        str_info_weather += ' '

print(str_info_weather)



