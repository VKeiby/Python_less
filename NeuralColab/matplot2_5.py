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

line = np.linspace(0,150,200)
# Задаем пространство для подграфиков plt.scatter(x, y, color)
f, axes = plt.subplots(2, 2, sharex=False, sharey=False, figsize=(12,8)) # параметры shareх и sharey - если False, то у каждого графика
                                                                         # будет отображена своя ось х и y, если True, то оси х и у будут
                                                                         # общими для всего пространства графиков

# График с координатами положения (0,0) по отношению к оси
axes[0,0].scatter(data=df, x=df.columns[0], y=df.columns[4], label=df.columns[0], c =y)
axes[0,0].legend()

# График с координатами положения (0,1) по отношению к оси
axes[0,1].scatter(data=df, x=df.columns[1], y=df.columns[4], label=df.columns[1], c =y)
axes[0,1].legend()

# График с координатами положения (1,0) по отношению к оси
axes[1,0].scatter(data=df, x=df.columns[2], y=df.columns[4], label=df.columns[2], c =y)
axes[1,0].legend()

# График с координатами положения (1,1) по отношению к оси
axes[1,1].scatter(data=df, x=df.columns[3], y=df.columns[4], label=df.columns[3], c =y)
axes[1,1].legend()
plt.show())