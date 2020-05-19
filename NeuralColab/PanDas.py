import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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

# data = pd.read_csv('train.csv')
data = pd.read_csv('train_test.csv', index_col = 0)
data_backup = data.copy()

# print(data.head())
# print(data.count())
# print(data.shape)
# print(data.info())
# print(data.isna().sum())

# print(data.describe())

# axis2 = data.LotFrontage
# a=axis2.isna().sum()
# if a > 200:
#     data.drop(columns=['LotFrontage'])
print(data.describe())

# print(np.round(data.isna().sum() / data.shape[0], 2))
# persent = data.isna().sum().sum() / data.size
# print(round(100*persent,1), '%',sep='')

# importing pandas module
# import pandas as pd
# # importing regex module
# import re
# # making data frame
# data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
# # removing null values to avoid errors
# data.dropna(inplace=True)
# # storing dtype before operation
# dtype_before = type(data["Salary"])
# # converting to list
# salary_list = data["Salary"].tolist()
# # storing dtype after operation
# dtype_after = type(salary_list)
#
# # printing dtype
# print("Data type before converting = {}\nData type after converting = {}".format(dtype_before, dtype_after))
#
# # displaying list
# salary_list
lCol = data.columns.tolist()
# data1 = data_backup.copy()
def Names(ListNames):
    data1 = data_backup.copy()
    for el in ListNames:
        name = data[el].isna().sum()
        if name > 200:
            data1 = data.drop(columns=[el])
    return data1


Names(lCol)
# data1 = data_backup.copy()
print(Names(lCol).describe())



# **********************************************************************************
# %matplotlib inline
# **********************************************************************************
# fig, ax = plt.subplots(figsize=(20,12))
# sns_heatmap = sns.heatmap(data.isnull(), yticklabels=False, cbar=False, cmap='viridis')
# plt.show()


# data = data_backup.copy()