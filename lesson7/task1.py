# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(('\t'.join([str(el) for el in row]) for row in self.matrix))

    def __add__(self, other):
        try:
            matrix_res = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in
                          range(len(self.matrix))]
            return Matrix(matrix_res)
        except IndexError:
            return "Error: Out of range"


matrix_1 = Matrix([[1, 2, -2], [3, 4, 4], [5, 6, 3]])
matrix_2 = Matrix([[7, 8, 0], [9, 10, 4], [11, 12, 10]])
print(matrix_1)
print()
print(matrix_2)
print()
print(matrix_1 + matrix_2)
