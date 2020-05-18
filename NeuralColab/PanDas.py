import pandas as pd
import numpy as np

# columns = ['country', 'province', 'region_1', 'region_2', 'smth']
# index = [0, 1, 10, 100, 40]
# data = [['Italy', 'Sicily & Sardinia', 'Etna', 'NaN', 'NaN'],
#         ['Portugal', 'Douro', 'NaN', 'NaN', 'NaN'],
#         ['US', 'California', 'Napa Valley', 'Napa', 'NaN'],
#         ['US', 'New York', 'Finger Lakes', 'Finger Lakes', 'Null'],
#         ['RUS', 'New Piter', 'Ladoga Lakes', '', 0]]


# data = pd.DataFrame(data, columns = columns, index = index)
# print(type(data))
# print(data)

data = pd.read_csv('train.csv')
data = pd.read_csv('train.csv', index_col = 0)
# print(data.head())
# print(data.count())
# print(data.shape)
# print(data.info())
print(data.isna().sum())
# print(data.isnull())
# data.describe()

import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

# fig, ax = plt.subplots(figsize=(20,12))
# sns_heatmap = sns.heatmap(data.isnull(), yticklabels=False, cbar=False, cmap='viridis')
# plt.show()
#
# mask = data['LotFrontage'] == 'NaN'
# print(mask)
# print(data[mask])