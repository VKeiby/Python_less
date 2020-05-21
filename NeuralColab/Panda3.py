import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

data = pd.read_csv('train_test.csv', index_col = 0)
data_backup = data.copy()

data1 = data_backup.copy()
lCol = data_backup.columns.tolist()

for el in lCol:
  name = data1[el].isna().sum()
  if name > 200:
    data1 = data1.drop(columns=[el])

data1.dropna(axis = 0, how ='any', inplace=True)

# Задача 5
# Данные, с которыми мы работаем в этом домашнем задании, содержат информацию о проданных домах.
# В табличке из прошлой задачи найдите все дома,
# проданные в 2007 году, у которых цена продажи выше 300000 и есть бассейн.
# Для подвыборки с указанными условиями сначала создайте маску.
#
# цена продажи SalePrice
# год продажи YrSold
# наличие бассейна можно определить по столбцу PoolArea

df = data1.loc[:,['SalePrice','YrSold','PoolArea']]
df.head(10)

#задаем маску
# priceMask = data1['SalePrice'] > 300000
# YrMask = data1['YrSold'] == 2007
# PoolMask = data1['PoolArea'] == True

winner = (df["YrSold"] == 2007) & (df["SalePrice"] > 300000) & (df["PoolArea"] > 1)
print(df[winner])

# Задача 6
# Добавьте к табличке data_1 новый столбец с названием 'Flag'.
# Присвойте ему значения 0 или 1 в случайном порядке. Для этого:
#
# создайте одномерный массив из случайных целых чисел 0 или 1
# размер массива должен соответствовать кол-ву наблюдений в основной табличке
# создайте новый столбец и присвойте ему значения одномерного массива


# fig, ax = plt.subplots(figsize=(20,12))
# sns_heatmap = sns.heatmap(data1.isnull(), yticklabels=False, cbar=False, cmap='viridis')
# plt.show()

