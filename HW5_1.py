import random


class Matrix:
    """Class for operations with."""

    def __init__(self, num, *others):
        """Constructor. Receive matrix elements or numbers of rows and columns to generate random int matrix with
        elements from 0 to 100.

        :param num: list of elements or number of rows
        :type num: list or int
        :param others: used to set int number of columns.
        """

        self.matrix = []
        if type(num) is int and len(others) == 1:
            row = []
            column = []
            for i in range(num):
                row.append(random.randint(0, 100))
            for j in range(others[0]):
                column.append(random.randint(0, 100))
            self.matrix.append(row)
            self.matrix.append(column)
            print(self.matrix)
        else:
            try:
                for i in num:
                    self.matrix.append([int(j) for j in i])
            except(TypeError, ValueError):
                print("List must contain integers only")

    def is_squared(self):
        """Checks if matrix is squared.

         :return: Matrix object.
         """

        if len(self.matrix) == len(self.matrix[0]):
            return True
        else:
            return False

    def transpose(self):
        """Transposes a matrix.

        :return: Matrix object.
        """

        result = [[0] * len(self.matrix) for k in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[j][i] = self.matrix[i][j]
        return Matrix(result)

    def same_size(self, other):
        """Checks if two matrices have the same number of rows and columns.

        :return: bool.
        """

        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            return True
        else:
            return False

    def is_symmetric(self):
        """Checks if matrix is symmetric.

        :return: bool.
        """

        lab = True
        if Matrix.is_squared(self):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if self.matrix[i][j] == self.matrix[j][i]:
                        continue
                    else:
                        lab = False
        return lab

    def __str__(self):
        """Prints Matrix object."""

        self.output = '\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix])
        return self.output

    def __add__(self, other):
        """Adds one matrix to another.

        :return: Matrix object.
        """

        result = []
        numbers = []
        if Matrix.same_size(self, other):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    summa = other.matrix[i][j] + self.matrix[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.matrix):
                        result.append(numbers)
                        numbers = []
        else:
            raise ValueError("Only matrices of the same size can be added.")
        return Matrix(result)

    def __sub__(self, other):
        """Вычитание двух матриц"""

        if Matrix.same_size(self, other):
            result = self + other * (-1)
            return result
        else:
            raise ValueError("Only matrices of the same size can be substructed.")

    def __mul__(self, other):
        """Умножение двух матриц или матрицы и числа.

        :param self: Matrix object only
        :param other: Matrix object or integer.
        :return: Matrix object.
        """

        if isinstance(self, Matrix) and isinstance(other, Matrix):
            res = [[0] * len(other.matrix[0]) for k in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for k in range(len(self.matrix[0])):
                        res[i][j] += self.matrix[i][k] * other.matrix[k][j]
        elif type(other) is int:
            res = [[0] * len(self.matrix[0]) for k in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    res[i][j] = self.matrix[i][j] * other
        else:
            raise TypeError("Wrong data type. Please input 2 matrices or matrix and integer")
        return Matrix(res)

    def __eq__(self, other):
        """Checks if matrices are equivalent.
        :param self: Matrix object
        :param another: Matrix object
        :return: bool.
        """

        if isinstance(self, Matrix) and isinstance(other, Matrix):
            if Matrix.same_size(self, other):
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        if self.matrix[i][j] == other.matrix[i][j]:
                            return True
            else:
                return False
        else:
            raise TypeError("Only 2 matrices can be evaluated here.")


if __name__ == '__main__':
    m1 = Matrix([[1, 9], [4, 1]])
    m2 = Matrix([[2, 1, -2], [1, 0, 3], [-2, 3, -4]])
    m3 = Matrix([[1, 7], [4, 1]])
    a = Matrix(['fgh', [4, 0]])
    print(m1 + m3)
    # print(m1.is_squared())
    # print(m1 + m2)

    print("********")

    # print(m1 * m2)
    # print("********")
    # print(m1)
    # print(m1.transpose())
    print("********")
    print(m1-m3)
    print("********")
    # print(m2.is_symmetric())
    m = Matrix(2, 2)
    