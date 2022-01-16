#5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
#nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
#adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
#adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#        Например:
#>>> get_jokes(2)
#["лес завтра зеленый", "город вчера веселый"]
#Документировать код функции.
#Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
#Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное ДЗ.
import random as rnd


def get_jokes(joke_count, only_one=False):
    if only_one and joke_count > 5:
        print('Ошибка. Без повторений может быть не более 5 шуток')
        return
    jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for j in range(joke_count):
        nouns_idx = rnd.randint(0, len(nouns)-1)
        adverbs_idx = rnd.randint(0, len(adverbs)-1)
        adjectives_idx = rnd.randint(0, len(adjectives)-1)
        jokes.append('{} {} {}'.format(nouns[nouns_idx], adverbs[adverbs_idx], adjectives[adjectives_idx]))
        if only_one:
            nouns.pop(nouns_idx)
            adverbs.pop(adverbs_idx)
            adjectives.pop(adjectives_idx)
    print(jokes)


get_jokes(5, only_one=True)
