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
        if dividers != [1,p]: print('Это составное число, имеющее делители ',dividers)
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
    return listP


# ________PROC________

MassiveP() # Формируем массив простых чисел до 1000

NUM=int(input('Input number 1-1000, for exit inter 0: '))
while NUM != 0:
    print('Number entered= ',NUM)
    SimpleNum(NUM)
    # MaxDivNum()
    # CanonicNum()
    NUM = int(input('One more? For stop inter 0: '))
print('TNX,Have a nice day!')

