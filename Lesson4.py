# This Python file uses the following encoding: utf-8
import os, sys
import random

def f(names,intX):
    integer_list = []
    for i in range(intX):
        rnd = random.randint(0,(len(names)-1))
        integer_list.append(names[rnd])
    return integer_list

def countNsort(integer_list):
    DictOut = {}
    for key in integer_list:
        if not key in DictOut:
            DictOut[key] = 1
        else:
            DictOut[key] += 1
   # -------------Freq Words
    Dict = list(DictOut.items())
    Dict.sort(key=lambda i: i[1], reverse=True)
    return Dict

def topWord(sortedDict):
    print('Самое популярное слово = ', sortedDict[0])
def lessLetter(sortedDict):
    letter_tmp=str(sortedDict[-1])
    print('Самая редкая буква имени = ', letter_tmp[2])

dbase = ['Yana','Marina','Vasiliy','Alex','Egor','Yaroslav','Dariya','Nina','Katerine','Fedor','Anton','Victoria',
         'Vera','Boris','Yasha','Grisha','Tolik','Timofey','Sandra','Nastya','Kseniya','Kristina','Polina','Tanya']


outList=(f(dbase,200))
sortedDict=countNsort(outList)
# print(f(dbase,5))
topWord(sortedDict)
lessLetter(sortedDict)

# ------------..PRO..----------
