### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
#      до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

intervals = [[24*60*60, 'дн'], [60*60, 'час'], [60, 'мин'], [1, 'сек']]
duration = int(input('Введените интервал в секундах:'))
msg = ''

for i in intervals:
    r = duration // i[0]
    if r > 0:
        msg = msg + ' ' + str(r) + ' ' + i[1]
        duration = duration % i[0]

print(msg)