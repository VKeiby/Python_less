import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('train_test.csv', index_col = 0)
data_backup = data.copy()

data1 = data_backup.copy()
lCol = data_backup.columns.tolist()

for el in lCol:
  name = data1[el].isna().sum()
  if name > 200:
    data1 = data1.drop(columns=[el])

# print(data.describe())
print(data1.head())

data1.dropna(axis = 0, how ='any', inplace=True)
print(data1.info())
print(data1.isna().sum().sum())

# fig, ax = plt.subplots(figsize=(20,12))
# sns_heatmap = sns.heatmap(data1.isnull(), yticklabels=False, cbar=False, cmap='viridis')
# plt.show()

