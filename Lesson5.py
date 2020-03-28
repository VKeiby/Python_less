# This Python file uses the following encoding: utf-8
import os, sys

def SimpleNum(p):
    listP = []
    dividers = [1,p]
    countD = 2
    if p > 2:
        while countD < p:
            if p%countD==0:
                dividers.append(countD)
            countD += 1
        if dividers != [1,p]:
            print('Это составное число, имеющее делители ',dividers)
            print('Cамый большой делитель числа: ', dividers[-1])
        else:
            listP.append(p)
            print('This is simple number',listP)
    if p==2 or p==1:
        listP.append(p)
        print('This is simple number', listP)
    return

def MassiveP():
    listP = []
    for num in range (1000):
        countD = 2
        dividers = []
        while countD < num:
            if num % countD == 0:
                dividers.append(countD)
            countD += 1
        if dividers ==[]:
            listP.append(num)
    listP.remove(0)
    listP.remove(1)
    return listP

def CanonicNum(listSimpNum):
    global NUM
    NOD = []
    i=0
    while i < NUM:
        if NUM != 1:
            if NUM % listSimpNum[i] == 0:
                NUM = NUM / listSimpNum[i]
                NOD.append(listSimpNum[i])
            else: i += 1
    print('Разложение на простые множители: ', NOD)
    print('Cамый большой простой делитель числа: ', NOD[-1])



# ________PROC________

listSimpNum = MassiveP() # Формируем массив простых чисел до 1000
NUM=int(input('Input number 1-1000, for exit inter 0: '))
while NUM != 0:
    print('Number entered = ',NUM)
    SimpleNum(NUM)
    CanonicNum(listSimpNum)
    NUM = int(input('One more? For stop inter 0: '))
    print()
print('TNX,Have a nice day!')

