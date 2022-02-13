# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class MyData:
    data_string = ''

    def __init__(self, data_str):
        self.data_string = data_str

    @classmethod
    def get_ymn(cls, data_string):
        data_list = list(map(int, data_string.split('-')))
        return data_list

    @staticmethod
    def chk_string(data_string):
        data_list = list(map(int, data_string.split('-')))
        if len(data_list) != 3 or not (0 < data_list[2] < 32) or not (0 < data_list[1] < 13):
            return False
        else:
            return True


# Вызов через класс
print(MyData.get_ymn('2022-01-01'))
print(MyData.chk_string('2022-01-01'))
print(MyData.chk_string('2022-21-01'))
# Вызов через объект
md = MyData('1988-01-07')
print(md.get_ymn('1999-12-07'))
