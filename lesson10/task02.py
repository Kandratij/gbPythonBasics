# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма(2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
from abc import ABC, abstractmethod


class Outerwear(ABC):
    @abstractmethod
    def cloth_amount(self):
        pass


class Costume(Outerwear):
    H = 0

    @property
    def cloth_amount(self):
        return round(2*self.H + 0.3, 2)


class Coat(Outerwear):
    V = 0

    @property
    def cloth_amount(self):
        return round(self.V/6.5 + 0.5, 2)


costume = Costume()
costume.H = 3
print(costume.cloth_amount)

coat = Coat()
coat.V = 1.5
print(coat.cloth_amount)