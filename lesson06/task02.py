# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
def my_split(line, split_symbol=' '):
    str_list = ['']
    is_split = True
    idx = 0
    for ch in line:
        if ch == split_symbol and is_split:
            str_list.append('')
            idx = idx + 1
            continue
        elif ch in ['"', '[', ']']:
            is_split = not is_split
            continue
        else:
            str_list[idx] = str_list[idx] + ch
    return str_list


req_dict = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
    for rec in log_file:
        rec_cols = my_split(rec)
        req_dict[rec_cols[0]] = req_dict.get(rec_cols[0], 0) + 1

sort_ip = sorted(req_dict, key=req_dict.get)
print(f'Max requests from IP {sort_ip[-1]} count {req_dict[sort_ip[-1]]}')
