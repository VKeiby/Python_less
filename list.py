# # Тип данных СПИСОК (list)------------------------
# #------------------------------------------
#      # Инициализация (генераторы)
list_temp = [] # пустой список
# print(type(list_temp))
list_temp = [1.2, 123, 'Volvo', [1,2,3]]

# for el in list_temp:
#     print(el, type(el))

# # --------------------------list
list_str = list('Volvo')
# print(list_str)

     # Обращения к элементам списка, подсписки
# for i in range(len(list_temp)):
#     print(i, ':', list_temp[i])
# for i in range(len(list_temp)):
#     print(i, ':', list_temp[i:])
# for i in range(len(list_temp)):
#     print(i, ':', list_temp[:i])
#      # Функции со списками
# print(len(list_temp))
#
#      # Операции со списками
#
print(list_temp + list_str)
# print(list_temp*2)
#
#      # Методы
# # -------------------------------append
# integer_list = []
# for i in range(5):
#     integer_list.append(i)
# print(integer_list)
# integer_list.append(0)
# print(integer_list)
# # -------------------------------remove
# integer_list.remove(0)
# print(integer_list)
# del integer_list[4]
# print(integer_list)
# # -------------------------------reverse
# integer_list.reverse()
# print(integer_list)
# # -------------------------------sort
# integer_list = [9,3,6,2,4]
# integer_list.sort()
# print(integer_list)
# # -------------------------------insert
# integer_list.insert(2, 100)
# print(integer_list)
#
#      # Обработка списков (map, filter, reduce)
#
# # ---------------------------------map
# integer_list = [9,3,6,2,4]

#map(function, list) ----> map -----> list(map)

# new_integer_list = list(map(str, integer_list))
#new_integer_list = list(map(lambda x: x**2, integer_list))
# print(new_integer_list)
#
# # --------------------------------filter
# integer_list = [9,3,6,2,4]
#
# new_integer_list = list(filter(lambda x: x<5, integer_list))
#
# print(new_integer_list)
#
# reduce
# from functools import reduce
#
# integer_list = [1,2,3,4]
#
# sum = reduce(lambda x,y: x+y, integer_list)
# product = reduce(lambda x,y: x*y, integer_list)
# print(sum, product)
# print(integer_list)
#
# #                                        !! string !!
# tmpStr = "Something to wrote "
# # ----------------------------Посимвольный вывод
# for i in range(len(tmpStr)):
#     print(tmpStr[i])
#
# # ----------------------------Срезы
# print(tmpStr[13:-1])
#
# # ----------------------------strFunction
# print(tmpStr, len(tmpStr))
#
# # ----------------------------strFormat
# a = 'Smb'
# b = 33
# who = '{} is {} years old'.format(a,b)
# print (who)
# '''
# for Python less 3
# who = f'{Smith} is {44} years old'
# print(who)
# '''
# -----------------------------Methods
# names = 'Vitya,Vika,Vera,Viorica'
# print(names.split())
# print(names.split(','))
# #
# # -----------------------------Formatting
# print(names.upper())
# print(names.title())
# print(names.lower())
#
# # -----------------------------replace str
# print()
# email_addr='vop@list.ru'
# str_addr='EMail: _mail_'
# print(str_addr.replace('_mail_',email_addr))