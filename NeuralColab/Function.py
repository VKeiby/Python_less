# This Python file uses the following encoding: utf-8
#


# Задача 4
#
# Напишите функцию, которая рассчитает примерное время выполнения этого домашнего задания.
# На вход она принимает количество минут, потраченное на каждое задание и количество заданий.
# Выведите посчитанное время на экран.
# from datetime import datetime, timedelta
#
#
# def homeTime(num, task):
#     task.pop()
#     theSum = 0
#     for el in task:
#         theSum = theSum + int(el)
#
#     def GetTime(theSum):
#         Min = timedelta(minutes=int(theSum))
#         d = datetime(1, 1, 1) + Min
#         # print("DAYS:HOURS:MIN:SEC")
#         # print("%d:%d:%d:%d" % (d.day - 1, d.hour, d.minute, d.second))
#         return "%d:%d:%d" % (d.day - 1, d.hour, d.minute)
#     print('Вы выполнили',num,'заданий,')
#     print('На домашнее задание потребовалось: ', GetTime(theSum), "DAYS:HOURS:MIN")
#
# task = []
# i = 0
# num = 0
# task.append(input('Сколько времени в минутах вам потребовалось на первую задачу? '))
# print('Если задач не осталось, нажмите n')
# while i != 'n':
#     i = input('А на следующую задачу? ')
#     task.append(i)
#     num += 1
#
#
# homeTime(num,task)

# def reverse(text):
#     return text[::-1]
#
# print(reverse('AbCdEfGhIjKlMnOpQrStUvWxYz'))

# Задача 6
#
# Напишите функцию mult_str(), которая в качестве параметров принимает
# строковую переменную input_str и число n, а возвращает строку, в которой
# повторяется input_str ровно n раз через пробел ' '.
# Найти значение mult_str() для input_str = 'KuKu' и n = 10.

# def repeatF(input_str,n):
#     strInput = ''
#     for i in range (n):
#         strInput = strInput + input_str + ' '
#     return strInput
#
# print(repeatF('KuKu',10))

# Задача 7
#
# Создайте функцию генератор, возвращающую случайное равновероятное значение из множества {0,1}.
# Сгенерируйте с ее помощью 1000 значений. Найдите среднее арифметическое этих значений.

# import random
# def get_rand():
#   return  random.random()
# s=0
# for i in range (0,1000):
#   s=s+get_rand()
# print(s/1000)


# import random
# def gen(n):
#     for i in range(n):
#         yield random.random()
#
# Num = gen(1000)
# print(sum(Num)/1000)
#
