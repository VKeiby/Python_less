# # input (приведение типов:) )
# age = input('input age')
# print(age, type(age))
# # print(age, type(int(age)))
# print(int(age), type(int(age)))
# age = input('Number')
# age = int(age)
# print(age, type(age))

# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# for i in range (5):print (i, '000000000000000000000000000000000000')

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# sum = 0
# fives = 0
# for i in range (10):
#     fives = input("Input number: ")
#     if int(fives)==5: sum+=1
# print (sum)


'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# sum = 1
# for i in range(1,11):
#     sum*=i
# print(sum)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
# sum = 0
# last = 0
# number = 24
# integer_number = number
# while integer_number>0:
#     last = integer_number%10
#     sum+=last
#     integer_number = integer_number//10
# print ("Сумма цифр числа {} равна {}".format(number, sum))


'''
Задача 7
Найти произведение цифр числа.
'''
# definition = 1
# last = 1
# number = 5434
# integer_number = number
# while integer_number>0:
#     last = integer_number%10
#     definition*=last
#     integer_number = integer_number//10
# print ("Произведение цифр числа {} равна {}".format(number, definition))

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# max_num = 0
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 > max_num:
#         max_num = integer_number%10
#     integer_number = integer_number//10
# print('Максимальная цифра - ',max_num)

'''
Задача 10
Найти количество цифр 5 в числе
'''

# sum = 0
# integer_number = 2134551355
# while integer_number>0:
#     if integer_number%10 == 5:
#         sum+=1
#     integer_number = integer_number//10
# print('количество цифр пять в этом числе - ',sum)