# This Python file uses the following encoding: utf-8
#
import math
import numpy as np #подключим библиотеку numpy


# создадим функцию, которая на вход принимает вектор или матрицу и выводит на экран в табличном виде
def print_vector(v):
    if str(type(v)) == "<class 'numpy.ndarray'>":  # проверяем что тип данных на входе, numpy массив
        shape = v.shape  # получим размерность массива
        len_shape = len(
            shape)  # получим количество значений размерности, если 0 пустой , 1- горизонтальный вектор, 2- матрица
    else:  # Если тип отличен от numpy то количество эементов 0
        len_shape = 0

    if (
            len_shape == 0):  # если размер 0 то это либо скаляр, либо пустой массив, либо значение другого типа, например, строка
        print(v)  # выведем входное значение на печать

    if (len_shape == 1):  # Если 1- то это горизонтальный вектор и выведем все значения в строку
        s = ''
        for i in v:
            s += str(i) + '  '
        print(s)

    if (len_shape == 2):  # Если 2-это матрица ,либо вертикальный вектор (размерность вертикального вектора (n, 1))
        for i in range(shape[0]):  # выведем строки по очереди
            s = ''
            for j in range(shape[1]):
                s += str(v[i][j]) + '  '
            print(s)


# функция матричного умножения, принимающая на вход 3 матрицы
def prod_matrix3(matrix1, matrix2, matrix3):

    def procProd(matrix1, matrix2):
        shape1 = matrix1.shape  # определим размерность 1-ой матрицы
        shape2 = matrix2.shape  # определим размерность 2-ой матрицы

        if (shape1[1] != shape2[0]):  # если количество столбцов 1-ой матрицы не равно количеству строк 2-ой матрицы
            return np.array([])  # возвращаем пустой массив

        out_matrix = np.zeros((shape1[0], shape2[1]))
        for i in range(shape1[0]):  # пройдемся по индексам строк 1-ой матрицы
            for j in range(shape2[1]):  # пройдемся по индексам столбцов 2-ой матрицы
                curr_cell = 0
                for t in range(shape1[1]):  # пройдемся по индексам стобцов 1-ой матрицы
                    curr_cell += matrix1[i, t] * matrix2[t, j]
                    out_matrix[i, j] = curr_cell

        return out_matrix  # вернем полученную матрицу

    intermediateMatrix = procProd(matrix1, matrix2) # умножаем 1ю и 2ю матрицы

    resultM = procProd(intermediateMatrix, matrix3) # умножаем промежуточную и 3ю матрицы

    return resultM



matrix1 = np.array([[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]])
matrix2 = np.array([[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]])
matrix3 = np.array([[0, 1, 2.2, 3], [1, 2, 3, 4.2], [2, 13, 4, 5], [3.1, 4, 5, 6]])

matrixRes = prod_matrix3(matrix1, matrix2, matrix3)
# print(matrixRes)

# #Создаём массив от 0 до 999
# x = np.array([i for i in range(1000)])
#
# #Вычисляем функцию y
# y = x*x/1000 + x + 12
#
# #Выводим y на экран
# print(y)

# def extreMatrix(matrix):
#     maX = matrix[0, 0]
#     miN = matrix[0, 0]
#     for x in np.nditer(matrix):
#         if x < miN: miN = x
#         if x > maX: maX = x
#
#     return maX - miN
#
# print(extreMatrix(matrixRes),508-72)

def oneMatrixT(matrix):
  MatrixT = np.transpose(matrix)          # transpone matrix
  prodMatrixT = np.dot(matrix,MatrixT)    # produce matx * Tmatx

  return np.linalg.inv(prodMatrixT)       # return inverve

inverseM = oneMatrixT(matrixRes)

MatTransp = np.transpose(matrixRes)
print(MatTransp)


