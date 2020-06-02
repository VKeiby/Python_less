# This Python file uses the following encoding: utf-8
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Подгрузите данные datatraining.txt при помощи соответствующей функции библиотеки Pandas.
# Преобразуйте индекс в datetime index, удалите столбец с датой.

db1 = pd.read_csv('datatraining.txt', index_col = 0)
db1_backup = db1.copy()

db1.index = pd.to_datetime(db1.date)
db1.drop('date', axis=1, inplace=True)
print(db1.head())
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

plt.figure(figsize=(12,6))

# график boxplot показывает средний, нижний и верхний квартили,
# минимальное и максимальное значение выборки и выбросы
sns.boxplot(data=db1, palette=sns.color_palette('Greens'), orient='h')
plt.show()