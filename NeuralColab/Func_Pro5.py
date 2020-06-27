# This Python file uses the following encoding: utf-8
#
# Задача 5
# Напишите функцию, которая находит точку, где функция растёт быстрее всего
# и медленнее всего и отображает на графике функции эти точки
# зелёным и красным кругом

#Загружаем биллиотеки
import numpy as np #Numpy массивы
import matplotlib.pyplot as plt #Для отрисовки графиков
# from math import sin
#Подключаем библиотеки для отображения 2d поверхностей
import pylab
from mpl_toolkits.mplot3d import Axes3D


# Функция, которая выводит график y
# y - вектор
# a - точка начала
# b - точка завершения
def plot_vect(y, a, b):
    # Формируем координаты точек по x
    x = np.array([i for i in range(a, b)])
    # Отображаем график
    plt.plot(x, y)
    plt.show()


# Функция, которая выводит график функции f
# y - вектор
# a - точка начала
# b - точка завершения
def plot_func(f, a, b):
    # Формируем координаты точек по x
    x = np.array([i for i in range(a, b)])
    # Вычисляем функцию в этих точках
    y = [f(i) for i in x]

    # Отображаем график
    plot_vect(y, a, b)

    # Возвращаем y
    return np.array(y)

def f4_1(x):
  y = y = x*x*np.sin(x/100) + 300*x
  return y

#Функция вычисления производной функции
def get_deriviate(f, a, b):
  #Вычисляем точки по x
  x = np.array([i for i in range(a,b)])
  len_x = x.shape[0]

  #Рассчитываем производную
  dy = np.array([f(x[i+1]) - f(x[i]) for i in range(len_x-1)])

  #Возвращаем производную
  return dy


#Функция расчёта второй производной
def get_second_deriviate(f, a, b):
  x = np.array([i for i in range(a,b)])
  len_x = x.shape[0]
  #Вычисляем вторую производную
  ddy = np.array([f(x[i+2]) - 2*f(x[i+1]) + f(x[i]) for i in range(len_x-2)])
  return ddy

# yDin = plot_func(f4_1, -1000, 1000)
#Вычисляем вторую производную и выводим график
ddy = get_second_deriviate(f4_1, -1000, 1000)
dy = get_deriviate(f4_1, -1000, 1000)
plot_vect(dy, -999, 999)

