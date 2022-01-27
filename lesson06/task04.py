# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей
# и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
# Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные,
# полученные в результате парсинга.
import sys

user_hobby_list = []
user_hobby_dict = {}
with open("users.csv", 'r') as users_file:
    with open("hobby.csv", 'r') as hobby_file:
        for user in users_file:
            fio = user.strip().split(',')
            user_hobby_dict['first_name'] = fio[0]
            user_hobby_dict['second_name'] = fio[1]
            user_hobby_dict['middle_name'] = fio[2]
            hobby = hobby_file.readline().strip()
            user_hobby_dict['hobbies'] = hobby.split(',') if len(hobby) > 0 else None
            user_hobby_list.append(user_hobby_dict)
        # если после чтения всех строк users.csv остались строки в hobby.csv exit c кодом 1
        hobby = hobby_file.readline().strip()
        if len(hobby) > 0:
            sys.exit(1)
print(user_hobby_list)
