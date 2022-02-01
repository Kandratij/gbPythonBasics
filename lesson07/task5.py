# Написать скрипт, который выводит статистику для заданной папки в виде
# словаря, в котором ключи те же, а значения — кортежи
# вида( < files_quantity >, [ < files_extensions_list >]), например:
# {
#    100: (15, ['txt']),
#    1000: (3, ['py', 'txt']),
#    10000: (7, ['html', 'css']),
#    100000: (2, ['png', 'jpg'])
#}
import os

DIR = '/home/geek/gbPythonBasics/venv/bin/'

stat_dict = {100: (0, []), 1000: (0, []), 10000: (0, []), 100000: (0, [])}
for file in os.listdir(DIR):
    file_name, file_ext = os.path.splitext(file)
    file_size = os.path.getsize(DIR + file)
    for size in (100000, 10000, 1000, 100):
        if file_size > size:
            elem = list(stat_dict[size])
            elem[0] += 1
            if file_ext not in elem[1]:
                elem[1].append(file_ext)
            stat_dict[size] = tuple(elem)
            break

print(stat_dict)
