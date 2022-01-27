#1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
#(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список
# кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
# Например:
#[
#...
#('141.138.90.60', 'GET', '/downloads/product_2'),
#('141.138.90.60', 'GET', '/downloads/product_2'),
#('173.255.199.22', 'GET', '/downloads/product_2'),
#...
#]
#Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
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


req_list = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
    for rec in log_file:
        rec_cols = my_split(rec)
        req = rec_cols[4].split()
        req_list.append((rec_cols[0], req[0], req[1]))

print(req_list)
