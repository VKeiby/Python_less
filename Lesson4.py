# This Python file uses the following encoding: utf-8
import os, sys
import random

def f(names,intX):
    integer_list = []
    for i in range(intX):
        rnd = random.randint(0,(len(names)-1))
        integer_list.append(names[rnd])
    return integer_list

def topWord(integer_list):
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
    return topWords

def lessLetter(integet_list):

    return






dbase = ['Yana','Marina','Vasiliy','Alex','Egor','Yaroslav','Dariya','Nina','Katerine','Fodor','Anton','Victoria',
         'Vera','Boris','Yasha','Grisha','Tolik','Timofey','Sandra','Nastya','Kseniya','Kristina','Polina','Tanya']


print(f(dbase,5))

topWord(f(dbase,100))

print()

# -------------..2..-----------

# -------------..3..-----------

# ------------..PRO..----------