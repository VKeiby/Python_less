# This Python file uses the following encoding: utf-8
#

#Загружаем биллиотеки
import numpy as np #Numpy массивы
import matplotlib.pyplot as plt #Для отрисовки графиков
# from math import sin
#Подключаем библиотеки для отображения 2d поверхностей
import pylab
from mpl_toolkits.mplot3d import Axes3D

def f2_0():
  x = np.arange(-1000,1000,.5)
  y = y = x*x*np.sin(x/100) + 300*x
  cross = []
  plt.plot(x,y)
  for i in range(len(y)-1):
    if (y[i-1]<0 and y[i+1]>0) or (y[i-1]>0 and y[i+1]<0):
      cross.append(i)
  plt.plot([x[i] for i in cross],[y[i] for i in cross],'ro')
  plt.show()


f2_0()