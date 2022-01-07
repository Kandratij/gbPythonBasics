#3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

list_info_weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

pos = 0
while pos < len(list_info_weather):
    word = list_info_weather[pos]
    if word.isdigit() or (word[0] in ('+', '-') and word[1:].isdigit()):
        list_info_weather.insert(pos,'"')
        pos += 1
        if word[0] in ('+', '-'):
            list_info_weather[pos] = word[0]+word[1:].rjust(2, '0')
        else:
            list_info_weather[pos] = word.rjust(2, '0')
        pos += 1
        list_info_weather.insert(pos,'"')
    pos += 1

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