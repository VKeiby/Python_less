# This Python file uses the following encoding: utf-8
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Подгрузите данные datatraining.txt при помощи соответствующей функции библиотеки Pandas.
# Преобразуйте индекс в datetime index, удалите столбец с датой.

# db1 = pd.read_csv('datatraining.txt', index_col = 0)
# db1_backup = db1.copy()
#
# db1.index = pd.to_datetime(db1.date)
# db1.drop('date', axis=1, inplace=True)
# print(db1.head())
# y = db1.Occupancy
# print(y)
# Постройте график всех парных взаимосвязей с разметкой цвета в соответствии с метками классов
# (столбец Occupancy)
#
# P.S. используйте функцию sns.pairplot c параметром hue

# sns.set_style('darkgrid')
# sns.lmplot(data=db1, x=db1.columns[0], y=db1.columns[1], hue='Occupancy')    # db1.columns[0] - это значения столбика Temperature
#                                                             # db1.columns[1] - это значения столбика Humidity
# plt.show()

# **********************************

# plt.figure(figsize=(4,6))

# график boxplot показывает средний, нижний и верхний квартили,
# минимальное и максимальное значение выборки и выбросы
# sns.boxplot(data=db1, palette=sns.color_palette('Greens'), orient='h')

# sns.pairplot(db1, hue='Occupancy', palette='Set1')
# plt.show()


# Gistogram
# Используя библиотеку Matplotlib, постройте гистограмму для первого признака
# в датасете выше следующим образом:
#
# на одном графике должно быть три гистаграммы, по одной на каждый класс
# для этого используйте методологии подвыборки массива с условием
# количество бинов должно определяться автоматически (режим "auto")
# гистограмма должна быть читаемой, т.е. добавьте подписи, лейблы, названия и т.д.
#
# matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None,
#                        cumulative=False, bottom=None, histtype='bar', align='mid',
#                        orientation='vertical', rwidth=None, log=False, color=None,
#                        label=None, stacked=False, \*, data=None, \*\*kwargs)

x = np.arange(1, 8)
y1 = np.random.randint(1, 10, size = 7)
y2 = np.random.randint(1, 10, size = 7)

fig, ax = plt.subplots()

color_rectangle = np.random.rand(7, 3)    # RGB
ax.bar(x, y1, color = color_rectangle, width = 0.5)

color_rectangle = np.random.rand(7, 4)    # RGBA
color_rectangle[:,3] = 0.5
ax.bar(x, y2, color = color_rectangle)

fig.set_figwidth(12)    #  ширина и
fig.set_figheight(6)    #  высота "Figure"
fig.set_facecolor('floralwhite')
ax.set_facecolor('seashell')

plt.show()


# from sklearn import datasets
# data = datasets.load_iris(return_X_y=False)
# X = data.data
# y = data.target
# target_names = data.target_names
# namesx = data.feature_names
#
# f,axes = plt.subplots(2,2, sharex=False, sharey=False, figsize=(10,7))
# for i,axs in enumerate(axes.flatten()):
#     for target in np.unique(data.target):
#         mask = (y == target)
#         ax.hist(x=np.arange(len(y[mask])), bins='auto', linewidth = 4, color=colors[target])
#     axs.set_title(namesx[i])
#     axs.legend(target_names)