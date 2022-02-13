# 5 Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод
# должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ''
    def drow(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'ручка'
    def drow(self):
        Stationery.drow(self)
        print(f'  пишем текст ({self.title})')


class Pensil(Stationery):
    title = 'карандаш'
    def drow(self):
        Stationery.drow(self)
        print(f'  рисуем эскиз ({self.title})')


class Handle(Stationery):
    title = 'маркер'
    def drow(self):
        Stationery.drow(self)
        print(f'  выделяем текст ({self.title}) ')

pen = Pen()
pensil = Pensil()
handle = Handle()

pen.drow()
pensil.drow()
handle.drow()
