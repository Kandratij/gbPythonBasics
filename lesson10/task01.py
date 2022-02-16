# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    val = []

    def __init__(self, matrix):
        self.val = matrix

    def __str__(self):
        ret_str = ''
        for line in self.val:
            for element in line:
                ret_str = ret_str + str(element) + ' '
            ret_str = ret_str + '\n'
        return ret_str

    def __add__(self, other):
        sum_matrix = []
        for i in range(len(self.val)):
            new_column = []
            for j in range(len(self.val[0])):
                new_column.append(self.val[i][j] + other.val[i][j])
            sum_matrix.append(new_column)
        return Matrix(sum_matrix)


mtrx1 = Matrix([[23, 17, 34], [27, 54, 71], [44, 10, 7]])
mtrx2 = Matrix([[12, 7, 13], [8, 5, 31], [22, 10, 73]])
print(mtrx1+mtrx2)
