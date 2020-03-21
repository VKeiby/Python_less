# This Python file uses the following encoding: utf-8
import os, sys
import random

def f(names,intX):
    integer_list = []
    for i in range(intX):
        rnd = random.randint(0,(len(names)-1))
        integer_list.append(names[rnd])
    print(integer_list)

    # DEF 2
    DictOut = {}
    for key in integer_list:
        if not key in DictOut:
            DictOut[key] = 1
        else:
            DictOut[key] += 1
    # -------------Freq Words
    SortDict = list(DictOut.items())
    SortDict.sort(key=lambda i: i[1], reverse=True)
    topWords = SortDict[0]

    print('Самое популярное слово = ', topWords)

    # DEF 3



    return

dbase = ['Yana','Marina','Vasiliy','Alex','Egor','Yaroslav','Dariya','Nina','Katerine','Fodor','Anton','Victoria',
         'Vera','Boris','Yasha','Grisha','Tolik','Timofey','Sandra','Nastya','Kseniya','Kristina','Polina','Tanya']
f(dbase,50)
print()

# -------------..2..-----------

# -------------..3..-----------

# ------------..PRO..----------