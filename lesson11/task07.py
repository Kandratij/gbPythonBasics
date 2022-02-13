# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNum:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b} j'

    def __mul__(self, other):
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a} j'

    def __str__(self):
        return f'{self.a} + {self.b} j'


x1 = ComplexNum(6, 2)
x2 = ComplexNum(7, 3)
print(x1)
print(x1 + x2)
print(x1 * x2)
