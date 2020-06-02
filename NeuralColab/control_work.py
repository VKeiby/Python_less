# This Python file uses the following encoding: utf-8
'''
a,b=map(int,input('Введите два целых числа через пробел (второе должно быть больше первого): ').split())
if (a < b) and (a != b):
    arr = list(range(a, b+1))
    even = []
    odd = []
    for el in arr:
        if el % 2 == 0:
            even.append(el)
        else:
            odd.append(el)
    print('количество элементов в сформированном массиве: ',len(arr))
    print('четныe элементы массива:', even)
    print('нечетныe элементы массива:', odd)
else: print("К сожалению, ничего не получится")
'''
'''
Создайте словарь со следующей структурой: ключ - название страны значение - список, содержащий цвета государственного флага
Пример: {'Россия' : ['красный', 'синий', 'белый']}
Словарь должен содержать не менее 10 стран.
Создайте цикл с условием, с помощью которого выведите фразу: "Введите цвет для поиска или введите "выход" для завершения работы".
Обработайте введенные пользователем данные и выведите на экран все страны, флаги которых содержат введенный цвет.
Работа с пользователем должна продолжаться до тех пор, пока он не введёт слово "выход".
'''
'''
d1 = {"Россия":("белый",'красный','синий'),
      'США':("белый",'красный','синий'),
      'Китай': ('красный', 'желтый'),
      'Англия':('красный','белый'),
      'Абхазия':('зеленый','красный','белый'),
      'Албания':('черный','красный'),
      'Ангола':('черный','красный','желтый'),
      'Багамские о-ва':('черный','голубой','желтый'),
      'Армения':('красный','синий','оранжевый'),
      'Афганистан':('черный','красный','зеленый','белый'),
      'Бельгия':('черный','красный','желтый'),
      'Болгария':('зеленый','красный','белый'),
      'Румыния':('синий','красный','желтый')}


usrData = ''
while usrData != 'выход':
    usrData = input('Введите цвет для поиска или введите "выход" для завершения работы: ')
    for key in d1:
        if usrData in d1[key]:
            print(key, d1[key])
'''
import numpy as np
array = np.random.sample((8, 8))

# print(array[0])
# for el in range(len(array[0])):
#     array[0,el] = el+1
# print(array[0])

# for el in range(len(array[1])):
#     if el % 2 == 0: array[1,el] = 1
#     else: array[1,el] = 0
# print(array[1])

# i = 100
# for el in range(len(array[2])):
#     array[2,el] = i
#     i -= 3
# print(array[2])

# for el in range(len(array[3])):
#     array[3,el] = el**2
# print(array[3])

# for el in range(0,len(array[7])):
#     array[7,el] = (el+1)**2
# print(array[7])

''' Попросите пользователя ввести его имя, фамилию и отчество, количество полных лет, день и месяц рождения.
Обработайте введенные данные и выведите на экран следующую информацию о пользователе:
ФИО: Иванов Иван Иванович
Дата рождения: 7 октября 1984 (воскресенье)
Знак зодиака: Весы
Год по восточному календарю: Крыса
Создайте пустой DataFrame и каждый раз после обработки пользовательских данных добавляйте полученную информацию в DataFrame и выводите обновленные данные. В результате у Вас должен получиться DataFrame приблизительно следующего содержания.
P. S. Код должен быть уникальным и работать через произвольный период времени. '''
# name, surname, parent=map(str,input('Введите Имя Фамилию и Отчество: ').split())

import datetime
import numpy as np
import pandas as pd


def weekday(year: int, month: int, day: int) -> int:
    if month < 3:
        year -= 1
        month += 10
    else: month -= 2
    return (day + 31 * month // 12 + year + year // 4 - year // 100 + year // 400) % 7

def get_multiplier(WDay):
    if WDay == 1:
        return '(Понедельник)'
    if WDay == 2:
        return '(Вторник)'
    if WDay == 3:
        return '(Среда)'
    if WDay == 4:
        return '(Четверг)'
    if WDay == 5:
        return '(Пятница)'
    if WDay == 6:
        return '(Суббота)'
    if WDay == 0:
        return '(Воскресенье)'

def get_zodiac_of_date(date):
    date_number = int(date)
    for z in zodiacs:
        if date_number <= z[0]:
            return z[1]

def get_monthName(Month):
    if Month == 1:
        return 'Января'
    if Month == 2:
        return 'Февраля'
    if Month == 3:
        return 'Марта'
    if Month == 4:
        return 'Апреля'
    if Month == 5:
        return 'Мая'
    if Month == 6:
        return 'Июня'
    if Month == 7:
        return 'Июля'
    if Month == 8:
        return 'Августа'
    if Month == 9:
        return 'Сентября'
    if Month == 10:
        return 'Октября'
    if Month == 11:
        return 'Ноября'
    if Month == 12:
        return 'Декабря'

# -------------            test
# https://pythonworld.ru/moduli/modul-calendar.html
# calendar.Calendar
# import calendar
# a = calendar.LocaleHTMLCalendar(locale='Russian_Russia')
# with open('calendar.html', 'w') as g:
#     print(a.formatyear(2020, width=4), file=g)

name = 'Victor'
surname = 'Lushin'
parent = 'A'
age = 43
birthdayList = '19 05'

# # ----------- input data ------------
eastYear = {
    0: 'Крыса',
    1: 'Бык',
    2: 'Тигр',
    3: 'Кролик',
    4: 'Дракон',
    5: 'Змея',
    6: 'Лошадь',
    7: 'Коза',
    8: 'Обезьяна',
    9: 'Петух',
    10: 'Собака',
    11: 'Свинья',}
zodiacs = [(120, 'Козерог'), (218, 'Водолей'), (320, 'Рыбы'), (420, 'Овен'), (521, 'Телец'),
              (621, 'Близнецы'), (722, 'Рак'), (823, 'Лев'), (923, 'Дева'), (1023, 'Весы'),
              (1122, 'Скорпион'), (1222, 'Стрелец'), (1231, 'Козерог')]
# name = input('Введите Имя: ')
# surname = input('Введите Фамилию: ')
# parent = input('Введите Отчество: ')
# age = int(input('Введите количество полных лет: '))
# birthdayList = input('Введите дату рождения (ДД ММ): ')

# ------------- calc -------------
dateNow = datetime.datetime.now()
birthday = birthdayList.split()
dayU = int(birthday[0])
monthU = int(birthday[1])
yearU = dateNow.year - age
dateBDay = datetime.datetime(yearU,monthU,dayU)
if dateNow.month < dateBDay.month:
    yearU -= 1
elif dateNow.month == dateBDay.month and dateNow.day < dateBDay.day:
    yearU -= 1
eastD = eastYear[(yearU - 2008) % 12]
WDay = (weekday(yearU,monthU,dayU))

# ------------ print --------------
print('ФИО: ',surname, name, parent)
print('Date of birsday:',dayU,get_monthName(monthU),yearU,'года',(get_multiplier(WDay)))
print('Знак зодиака: ',get_zodiac_of_date(birthday[1]+birthday[0]))
print('Год по восточному календарю: ',eastD)
