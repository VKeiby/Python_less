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
    return listP

listP = SimpleNum(100)
print(listP)