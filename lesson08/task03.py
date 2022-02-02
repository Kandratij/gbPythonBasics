# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#    ...
#@type_logger
#def calc_cube(x):
#   return x ** 3

import datetime


def type_logger(func):
    def wrapper(*args):
        result = func(*args)
        with open('calc_cube.log', 'a', encoding='utf-8') as log:
            log.write(f'{datetime.datetime.now()} call {func.__name__}({args}) => {result} \n')
        return result
    return wrapper


def calc_cube(x):
    return x ** 3


calc_cube = type_logger(calc_cube)
print(calc_cube(7))
print(calc_cube(9))

