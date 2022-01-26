# 5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать путь к
# обоим исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая,
# когда все файлы находятся в разных папках.
import sys

users_list = [line.strip().replace(',', ' ')  for line in open(sys.argv[1], 'r')]
hobby_list = [line.strip() for line in open(sys.argv[2], 'r')]

if len(users_list) < len(hobby_list):
    sys.exit(1)

users_hobby_dict = {user: hobby_list[idx] if len(hobby_list) > idx else None for idx, user in enumerate(users_list)}

print(users_hobby_dict)
