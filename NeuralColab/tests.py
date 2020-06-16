# This Python file uses the following encoding: utf-8
#


# a = 15
# sum = 0
# while a < 23:
#   sum += a
#   a += 1
# print (sum)

# my_list = [56, 23, 67, 45, 67, 2, 47, 158, 31, 34, 78, 23, 78, 23, 89, 23, 36]
# # for el in my_list:
# #     sum += el
# #     print (el,sum)

# sweets = {'Наташа': '2',
#           'Алина': '3',
#           'Марат': '15',
#           'Лев': '1',
#           'Валера': '0'
#           }
# print(sweets)

# j = 1
# for i in range(4):
#     for x in range(j):
#         print(j, end=' ')
#     print()
#     print()
#     j+=1
#
# for i in range(5,10):
#     for x in range(j,0,-1):
#         print(i, end=' ')
#     print()
#     print()
#     j-=1
#
# for i in range(7,8):
#     for j in range(2,10):
#         print(i,'*',j,'=',i*j)

# factor=1
# while factor < 10:
#     print('7 *',factor,'=',7*factor)
#     factor+=1

# d1 = int(input())
# d2 = int(input())
# sum= d1+d2
# if (0 < d1 <= 6 and 0 < d2 <= 6):
#     if sum == 7 or  sum == 11: print('Я победил!!!')
#     elif sum == 2 or sum == 3 or sum == 12: print('Я проиграл :(')
#     else: print ('Сумма значений',sum)
# elif d1 > 6 or d1 < 1:
#     print('Ошибка! Значение на первом кубике не входит в интервал [1, 6]')
# else: print('Ошибка! Значение на втором кубике не входит в интервал [1, 6]')

# for i in range(3000,3005):
#     if (i % 11 == 0) & (i % 5 != 0):
#         print('Found:',i)
#     print(i)

# sample_list = ["мандаринки", "киви", "лимон"]
# list=[]
# for i in range (1,5):
#     for el in sample_list:
#         el_i = el + '_' + str(i)
#         list.append(el_i)
# print(list)
#
# list_for_pro_task_2 = [35, 0.24, 3 + 4j, "котики", 0.45, (8, 9), "слоники", {"Мадрид": 3, 'Лондон':5}, 23498]
# print(list_for_pro_task_2)
# count = 0
# for el in list_for_pro_task_2:
#     if type(el) != dict:
#         count += 1
#         # print(type(el))
#     else: print('Словарь', count, '-й  элемент в листе')
# print('The EOL')

# Заполнение словаря
# DictOut = {}
# for key in range(1,21):
#     DictOut[key] = key * key
# print(DictOut)

# text = 'Я полагаю что все в общих чертах знают о существовании такого замечательного математического инструмента как преобразование Фурье. Однако в ВУЗах его почему-то преподают настолько плохо, что понимают как это преобразование работает и как им правильно следует пользоваться сравнительно немного людей. Между тем математика данного преобразования на удивление красива, проста и изящна. Я предлагаю всем желающим узнать немного больше о преобразовании Фурье и близкой ему теме того как аналоговые сигналы удается эффективно превращать для вычислительной обработки в цифровые.'
#
# print(len(text))
# count_dict = {}
# for i in range(len(text)):
#     count_dict[text[i]] = 0
# for i in range(len(text)):
#     count_dict[text[i]] += 1
#
# print(count_dict)
# sym = None
# while (sym != ''):
#     sym = input()
#     print(sym, count_dict[sym])

# words = text.split()
# print(len(words))
# print(words)
# len_words = [len(w) for w in words]
# max_len_words = max(len_words)
# # print(max_len_words)
# # for w in words:
# #     if (len(w) == max_len_words):
# #         print(w)
# max_len_words_index = len_words.index(max_len_words)
# print(max_len_words_index)
# print(len_words[max_len_words_index])
# print(words[max_len_words_index])

# import numpy as np
#
# lst = [i for i in range(100)]
# print(lst)
# np_lst = np.array(lst)
# np_lst = np_lst.reshape((20,5))
# print(np_lst)

# for i in range(5,150):
#     s = 0
#     for j in range(1,i):
#         if i%j == 0:
#             s += j
#     if s == i:
#         print(i)

def Palindrom(string):
    marks = [' ']
    # Перебираем текст для анализа на знаки и создаем новый текст
    new_list = []
    for el in string:
        if el != ' ':
            new_list.append(el)
    new_list = list((map(lambda x: x.lower(), new_list)))
    string = str(''.join(new_list))
    l = len(new_list)
    for i in range(l//2):
        if new_list[i] != new_list[-1-i]:
            print("It's not palindrome")
            quit()
    print("It's palindrome")

palindrom = 'А муза рада музе без ума да разума'
Palindrom(palindrom)
Palindrom('А роза упала на лапу Азора')
Palindrom('BanaNa')