# This Python file uses the following encoding: utf-8
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

columns = ['ФИО', 'Дата рождения', 'Знак зодиака', 'Вост. календарь']
data = [['Иванов Иван Иванович', '7.10.1984 (вскр)', 'Весы', 'Крыса']]
df = pd.DataFrame(data, columns = columns)
dfIndex = 1

# -------------            test
# https://pythonworld.ru/moduli/modul-calendar.html
# calendar.Calendar
# import calendar
# a = calendar.LocaleHTMLCalendar(locale='Russian_Russia')
# with open('calendar.html', 'w') as g:
#     print(a.formatyear(2020, width=4), file=g)

# name = 'Victor'
# surname = 'Lushin'
# parent = 'A'
# age = 43
# birthdayList = '19 05'

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

# -------- !!! WORK WHILE !!! ----------
name = ''
while name != 'выход':
    print('Для окончания цикла наберите "выход"')
# # ----------- input data ------------
    name = input('Введите Имя: ')
    if name == 'выход':
        print(df)
        break
    surname = input('Введите Фамилию: ')
    parent = input('Введите Отчество: ')
    age = int(input('Введите количество полных лет: '))
    birthdayList = input('Введите дату рождения (ДД ММ): ')

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

# --- DF ---
    df_WDay = get_multiplier(WDay)
    fio = surname + ' ' + name + ' ' + parent
    df_BDay = str(dateBDay.day) + '.' + str(dateBDay.month) + '.' + str(dateBDay.year) + df_WDay[:5] + ')'
    df_zodiak = get_zodiac_of_date(birthday[1]+birthday[0])
    dfIndex += 1
    df.loc[dfIndex] = [fio, df_BDay, df_zodiak, eastD]

