import os,sys
sys.path.append("../Python_less/")
import Lesson4
import pytest

print('this is master branch pyTEST')
print ('This branch is testing assignment from lesson 6')

from Lesson4 import f,countNsort,topWord,lessLetter


def test_f():
    # Генерация массива определенной длины из вводимого массива
    nameList = ['Vasya','Fedor','Sasha']
    assert len(f(nameList,20)) == 20


def test_countNsort():
    # Вычисление повторяющихся элементов
    integer_list = [34,54,34,54,34,54,34,54,34]
    assert countNsort(integer_list) == [(34, 5), (54, 4)]

def test_lessLetter():
    # Выводит первую букву последнего элемента массива
    sortedDict = [('Vasya',44),('Fedor',33),('Sasha',11)]
    lessLetter(sortedDict)
    assert lessLetter(sortedDict) == 'S'