# скрипт записи сумм в файл bakery.csv
import sys

with open("bakery.csv", 'a', encoding='utf-8') as bakery_file:
    for ind in range(1, len(sys.argv)):
        bakery_file.write(sys.argv[ind]+'\n')

