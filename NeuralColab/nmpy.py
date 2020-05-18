# This Python file uses the following encoding: utf-8
#
print('Домашка 2 - Numpy')
import numpy as np

def mean_arr(np_arr):
    sum = 0
    for i in range(np_arr.shape[0]):
        for j in range(np_arr.shape[1]):
            sum = sum + np_arr[i, j]
    print('Среднее значение всех элементов массива: ',sum / np_arr.size)


# lst = [i for i in range(36)]
#
# np_lst = np.array(lst)
# np_lst = np_lst.reshape((6,6))
# print(np_lst)
#
# mean_arr(np_lst)

# Всякости
# print(np_lst > 69)
# print(np_lst[(np_lst > 12) & (np_lst < 46)])
# print(np_lst[4,9])
# print(len(np_lst[0]))
# print(len(np_lst[0:]))
# print(np_lst.size)

my_array = np.loadtxt('iris.csv', delimiter=',', skiprows=1)
my_generated_array = np.random.rand(my_array.shape[0], my_array.shape[1])

# v1_generated_array = np.random.uniform(my_array.shape[0], my_array.shape[1])
# my_generated_array = np.random.rand(0, 19, (150,5))
# print(my_array.shape[0])
# print(my_array.shape[1])
# print(my_generated_array.shape,my_generated_array.dtype)
# print(v1_generated_array)
#
# mean_arr(my_array)
#
# my_list = my_array.tolist()
# print(my_list)
#
# sumCol = my_array.sum(axis=0)
# print(sumCol)

# Используя библиотеку numpy, создайте массив 3x3, значения которого находятся в диапазоне от 11 до 40.
# Не используя цикл for, выведите на экран список элементов, которые меньше 20.
# Просуммируйте все элементы (не используя цикл for)

# rr = np.random.randint(11, 40, (3,3))
# print(rr)
#
# print('Cписок элементов, массива меньше 20 - ',rr[rr<20])
# print('Сумма всех элементов - ',rr.sum())

# Создайте массив, который будет содержать списки с именем студента(str),
# его возрастом(int) и средней оценкой(float).
# Отсортируйте такой массив
# Замените значение, отвечающее за возраст, у всех студентов на одно и то же, например, 10.
# Отсортируйте такой массив теперь.
# numpy.sort(a, axis=-1, kind='quicksort', order=None)
# type_arr =[('name','U16'), ('age',int), ('eval', float)]
# tmpList = [('Колаев',30,4.9), ('Романов',27,4.7), ('Тобольский',28,4.4),('Аббаев',23,4.4), ('Бажов',25,4.3),('Баранов',21,4.5), ('Васечкин',21,4.7), ('Петров',20,4.8)]
#
# st_array = np.array(tmpList, dtype=type_arr)
#
# print(st_array.dtype)
# print(1)
# print(st_array)
# st_array.sort()
# print(2)
# print(st_array)
# st_array.sort(order='eval')
# print('Сортировка по оценке')
# print(st_array)
# print()
# st_array.sort(order='name')
# print('Сортировка по имени')
# print(st_array)
# print()
# st_array.sort(order='age')
# print('Сортировка по возрасту')
# print(st_array)
# print()
#
# st_array['age']=10
# st_array.sort()
# print(3)
# print(st_array)
# print()

# >>> a = np.array([[1, 2], [3, 4]])
# >>> b = np.array([[5, 6], [7, 8]])
# >>> np.vstack((a, b))
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
# >>> np.hstack((a, b))
# array([[1, 2, 5, 6],
#        [3, 4, 7, 8]])

# multyArr = np.hstack((my_array, my_generated_array))
# print(multyArr)
# print(multyArr.shape, multyArr.dtype)
# arrSplit = np.hsplit(multyArr, 5)
# print(len(arrSplit))
# print(arrSplit[4])
# print(arrSplit[4].dtype)

# Создайте трехмерный массив размера 2 на 3 на 4, состоящий из случайных вещественных чисел от 15 до 37.
# Используйте встроенные методы библиотеки np.random...

# arr3d = np.random.uniform(15, 37, (2, 3, 4))

# list_tmp = arr3d.tolist()
# rand234 = np.array(list_tmp, dtype='object')
#
# for row in rand234:
#   for column in row:
#     for i in range(len(column)):
#       if column[i]<20:
#         column[i]='small'
#       elif column[i]<=30 and column[i]>=20:
#         column[i]='medium'
#       elif column[i]>30:
#         column[i]='large'
# print(rand234)

# Создайте одномерный массив из случайных 10 значений.
#
# Не используя цикл for, сумму значений с 3 по 7 элемент.
# Найдите сумму квадратов последних двух элементов.

generatArray = np.random.randint(0, 100, 10)
print(generatArray)
sumV37 = generatArray[3:7]
print(sumV37.sum())