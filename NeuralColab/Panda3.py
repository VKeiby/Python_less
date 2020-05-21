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

# print(data1.loc[1170:1200, ['SalePrice','YrSold','PoolArea']])
# df = data1.groupby(['SalePrice','YrSold','PoolArea']).count()

df = data1.loc[:,['SalePrice','YrSold','PoolArea']]
print(df.head())

#задаем маску
# priceMask = df['SalePrice'] > 300000
# YrMask = df['YrSold'] == 2007
# PoolMask = df['PoolArea'] != 0

priceMask = df['SalePrice'] > 300000
YrMask = df[priceMask]['YrSold'] == 2007
PoolMask = df[priceMask][YrMask]['PoolArea'] != 0
type(PoolMask)

print(df[YrMask].head(15))



# fig, ax = plt.subplots(figsize=(20,12))
# sns_heatmap = sns.heatmap(data1.isnull(), yticklabels=False, cbar=False, cmap='viridis')
# plt.show()

