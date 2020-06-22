# This Python file uses the following encoding: utf-8
#
import math
import numpy as np #подключим библиотеку numpy
'''
Напишите функцию, которая получает на вход пару матриц и проверяет закон 
коммутативности умножения, то есть свойства  A∗B=B∗A , возвращая 1 в случае 
подтверждения и 0 в противном случае. 
Поставьте 1000 экспериментов для случайных целочисленных матриц 
размера (5,5) элементов, которые принадлежат отрезку [-5,5], и найдите 
количество успешных срабатываний.
'''

def Commutative(matrixA, matrixB):
    MatrixAB = np.dot(matrixA, matrixB)
    MatrixBA = np.dot(matrixB, matrixA)
    if (MatrixAB != MatrixBA).all(): return False
    else: return True

Pos = 0
Neg = 0

for i in range(1000):
    ArM5 = np.random.randint(-5, 5, (5,5))
    BrM5 = np.random.randint(-5, 5, (5,5))
    CheckResult = Commutative(ArM5,BrM5)
    if CheckResult == True: Pos += 1
    else: Neg += 1
print('Матрицы прошли проверку на коммутативность умножения: ',Pos, '\nМатрицы не прошли проверку на коммутативность умножения:',Neg)


