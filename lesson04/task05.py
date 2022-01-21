#5. * (вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
#> python task_4_5.py USD
#  75.18, 2020-09-05
## можно вызывать с несколькими параметрами
# например: python3 task05.py usd EUR amd
# USD: 76.0404, 2022-01-18
# EUR: 86.8609, 2022-01-18
# AMD: 0.15776, 2022-01-18
import sys
import utils

for arg in sys.argv[1:]:
    rate = utils.currency_rates(arg)
    print(f'{arg.upper()}: {rate[1]}, {rate[0].date()}')
