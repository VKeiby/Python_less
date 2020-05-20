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

#задаем маску
priceMask = data1['SalePrice'] > 300000
YrMask = data1['YrSold'] == 2007
PoolMask = data1['PoolArea'] == True

print(data1.loc[1170:1200, ['SalePrice','YrSold','PoolArea']])

# print(priceMask.head(20))
# print(YrMask.head(20))
# print(PoolMask.head(20))




# fig, ax = plt.subplots(figsize=(20,12))
# sns_heatmap = sns.heatmap(data1.isnull(), yticklabels=False, cbar=False, cmap='viridis')
# plt.show()

