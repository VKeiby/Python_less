import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('datatraining.txt', sep=r',', engine='python', header=None,
                 names=['id', 'date', 'Temperature', 'Humidity', 'Light', 'CO2', 'HumidityRatio', 'Occupancy'])
df = df.drop([0])
df.index = pd.to_datetime(df.date)
df.drop('date', axis=1, inplace=True)
df = df.apply(pd.to_numeric)
df2 = df.copy()
print(df2.head())

# funcs = dict(Temperature ="mean", Humidity ="mean", Light="mean", CO2 ="mean", HumidityRatio ="mean",  Occupancy ="asfreq")
# df2.resample('30min').agg(funcs)

funcs = dict(Temperature ="mean", Humidity ="mean", Light="mean", CO2 ="mean", HumidityRatio ="mean",  Occupancy ="bfill")
df2.resample('30min').agg(funcs).dropna()