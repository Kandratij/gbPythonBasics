# скрипт чтения сумм из файла bakery.csv
import sys

start_line = 0 if len(sys.argv) == 1 else int(sys.argv[1])-1

with open("bakery.csv", 'r', encoding='utf-8') as bakery_file:
    for lin in bakery_file.readlines()[start_line:]:
        print(lin.strip())

