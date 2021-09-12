"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "\n".join("".join(f'{value:5}' for value in rows) for rows in self.data)

    def __add__(self, other):
        if len(other.data) != len(self.data):
            raise Exception('Матрицы не совпадают по размеру')
        result = Matrix([])
        for i in range(len(other.data)):
            if len(other.data[i]) != len(self.data[i]):
                raise Exception('Матрицы не совпадают по размеру')
            result.data.insert(i, [])
            for j in range(len(other.data[i])):
                result.data[i].insert(j, other.data[i][j]+self.data[i][j])
        return result


A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = Matrix([[4, 5, 6], [1, 2, 3], [7, 8, 9]])
print(A)
print()
print(B)
print()
print(A + B)
