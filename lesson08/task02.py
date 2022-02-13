# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера
# из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)
import re

lineformat = r"""
(?P<remote_addr>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - 
\[(?P<request_datetime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] 
("(?P<request_type>(GET|POST)) 
(?P<requested_resource>.+?(?=\ http\/1.1")) http\/1.1") 
(?P<response_code>\d{3}) 
(?P<response_size>\d+)
"""
lineformat = lineformat.replace('\n','')

re_format = re.compile(lineformat, re.IGNORECASE)

with open('nginx_logs.txt', 'r', encoding='utf-8') as log_file:
    for line in log_file:
        req_line = []
        data = re.search(re_format, line)
        if data:
            datadict = data.groupdict()
            req_line = (datadict["remote_addr"], datadict["request_datetime"], datadict["request_type"],
                             datadict["requested_resource"], datadict["response_code"], datadict["response_size"])
            print(req_line)






