# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
from datetime import datetime


class Storage:
    def __init__(self):
        self._dict = {}

    def add_tech(self, tech):
        self._dict.setdefault(tech.type_of, []).append(tech)

    def get_tech(self, type_of):
        if self._dict[type_of]:
            return self._dict.setdefault(type_of).pop(0)

    def __str__(self):
        ret_line = ''
        for k in self._dict.keys():
            ret_line = ret_line + k + '\n'
            for tech in self._dict[k]:
                ret_line = ret_line + tech.__str__() + '\n'
        return ret_line


class Technic:
    def __init__(self, model, year, ser_num):
        self.model = model
        if year > datetime.now().year:
            raise ValueError('год выпуска не может быть больше текущего')
        self.year = year
        self.ser_num = ser_num
        self.type_of = self.__class__.__name__

    def type_of(self):
        return f'{self.type_of}'

    def __str__(self):
        return f'№{self.ser_num} Model:"{self.model}" year:{self.year}'


class Printer(Technic):
    def __init__(self, model, year, ser_num, print_method):
        super().__init__(model, year, ser_num)
        self.print_method = print_method

    def __repr__(self):
        return f'{self.name} {self.series} {self.make} {self.year} {self.print_method}'

    def action(self):
        return 'Printing'


class Scanner(Technic):
    def __init__(self, model, year, ser_num, paper_format, dpi):
        super().__init__(model, year, ser_num)
        self.dpi = dpi
        self.paper_format = paper_format

    def action(self):
        return 'Scanning'


class Xerox(Technic):
    def __init__(self, model, year, ser_num, paper_format, is_color=False):
        super().__init__(model, year, ser_num)
        self.paper_format = paper_format
        self.is_color = is_color

    def action(self):
        return 'Coping'


stor1 = Storage()
stor2 = Storage()
# создаем объект и добавляем
stor1.add_tech(Scanner('HP ScanJet Enterprise Flow 7000 s3', 2021, 10001, 'A4', 1200))
stor1.add_tech(Scanner('HP ScanJet Pro 2000 s2', 2022, 'A4', 10002, 1200))
stor1.add_tech(Printer('HP LaserJet 1908', 2022, 10004, 'laser'))
stor1.add_tech(Printer('Brother HL-1112R', 2019, 10006, 'laser'))
stor1.add_tech(Xerox('Xerox B210', 2022, 10008, 'A4', True))

# выводим склад 1
print('склад 1')
print(stor1)

stor2.add_tech(stor1.get_tech('Scanner'))

# выводим склад 2
print('Склад 2')
print(stor2)


stor1.add_tech(Xerox('Xerox B210', 2024, 10008, 'A4', True))