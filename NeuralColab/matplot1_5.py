# This Python file uses the following encoding: utf-8
#

import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(5000)
y1 = np.random.gamma(1, size = 5000)
y2 = np.random.gamma(2, size = 5000)
y3 = np.random.gamma(4, size = 5000)
y4 = np.random.gamma(8, size = 5000)

fig, ax = plt.subplots()

# ключ цвета из {'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}:
ax.scatter(x, y1,
           c = 'r',
           s = 1)
# RGB:
ax.scatter(x + 1, y2,
           c = [[0.1, 0.63, 0.55]],
           s = 1)
# hex RGB:
ax.scatter(x + 2, y3,
           c = '#ad09a3',
           s = 1)
# уровень серого в интервале [0, 1]:
ax.scatter(x + 3, y4,
           c = ['0.9'],
           s = 1)


ax.set_facecolor('black')
ax.set_title('Один цвет')

#  Увеличим размер графика:
fig.set_figwidth(14)
fig.set_figheight(14)

plt.show()