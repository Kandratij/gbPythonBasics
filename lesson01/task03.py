#3.Склонение слова
#Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
#1 процент
#2 процента
#3 процента
#4 процента
#5 процентов
#6 процентов
#...
#100 процентов

def declensions_persent(p):
    r = p % 10
    if p == 0 or r == 0 or r >= 5 or p in range(10, 19):
        st = 'процентов'
    elif r == 1:
        st = 'процент'
    else:
        st = 'процента'
    return st


for i in range(0, 100):
 print (f'{i} {declensions_persent(i)}')