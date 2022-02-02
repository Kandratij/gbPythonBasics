# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#    ...
#@val_checker(lambda x: x > 0)
#def calc_cube(x):
#   return x ** 3
#
#
#>>> a = calc_cube(5)
#125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
# ...
# raise ValueError(msg)
# ValueError: wrong val -5


def val_checker(chk_func):
    def _checker(func):
        def wrapper(*args):
            if chk_func(*args):
                result = func(*args)
            else:
                msg = f'wrong val {args[0]}'
                raise ValueError(msg)
            return result
        return wrapper
    return _checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(7))
print(calc_cube(-9))
