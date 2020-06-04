# This Python file uses the following encoding: utf-8
#
import numpy as np
import matplotlib.pyplot as plt

# Создаем игрушечные данные:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Задаем пространство для подграфиков
f, axes = plt.subplots(2, 2, sharex=False, sharey=False, figsize=(12,8)) # параметры shareх и sharey - если False, то у каждого графика
                                                                         # будет отображена своя ось х и y, если True, то оси х и у будут
                                                                         # общими для всего пространства графиков

# График с координатами положения (0,0) по отношению к оси
axes[0,0].scatter(x,y,label='sin(x^2)', c='r')
axes[0,0].legend()

# График с координатами положения (0,1) по отношению к оси
axes[0,1].plot(x, np.abs(y), label='np.abs(y)')
axes[0,1].legend()

# График с координатами положения (1,0) по отношению к оси
axes[1,0].plot(x,y**3)

# График с координатами положения (1,1) по отношению к оси
axes[1,1].plot(x,np.arccos(y))
plt.show()