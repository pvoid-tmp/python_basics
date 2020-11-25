# Lesson 7 task 1

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    # валидность матрицы: матрица непустая, и все строки имеют одинаковое количество элементов
    def is_valid(self):
        if not self.matrix:
            return False
        check = len(self.matrix[0])
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != check:
                return False
        return True

    # размерность валидной матрицы
    def dim(self):
        return [len(self.matrix[0]), len(self.matrix)]

    def __str__(self):
        return '\n'.join([str('\t'.join([str(j) for j in i])) for i in self.matrix])

    def __add__(self, other):
        if not self.is_valid() or not other.is_valid() or self.dim() != other.dim():
            return Matrix([])
        return Matrix([[self.matrix[i][j] + other.matrix[i][j]
                        for j in range(self.dim()[0])] for i in range(self.dim()[1])])


# main
a = Matrix([[3, 2, 1, 1], [2, 0, 3, 1], [1, 1, 2, 1]])
b = Matrix([[2, 2, 1, 1], [2, -1, 3, 1], [1, 1, 1, 1]])
c = Matrix([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
print(a + b + c)
