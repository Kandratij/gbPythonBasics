# Есть два списка:
# tutors = [
#    'Иван', 'Анастасия', 'Петр', 'Сергей',
#    'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
# чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.
def join(tutors_list, klasses_list):
    for i, tutor in enumerate(tutors_list):
        yield tuple([tutor, klasses_list[i] if i < len(klasses_list) else None])


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
 ]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]

gen = join(tutors, klasses)

print('type(gen) =>', type(gen))
print('-----------------------')
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# следующий шаг вызовет Exception StopIteration
print(next(gen))
