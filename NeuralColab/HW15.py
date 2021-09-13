from tensorflow.keras.datasets import mnist #Библиотека с базой Mnist
from tensorflow.keras.models import Sequential # Подлючаем класс создания модели Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout # Подключаем классы
from tensorflow.keras.optimizers import Adam # Подключаем оптимизатор Adam
from tensorflow.keras import utils #Утилиты для to_categorical
from tensorflow.keras.preprocessing import image #Для отрисовки изображения
import numpy as np # Подключаем библиотеку numpy
import pandas as pd # Библиотека pandas
from sklearn.preprocessing import LabelEncoder, StandardScaler # Функции для нормализации данных
from sklearn import preprocessing # Пакет предварительной обработки данных
from sklearn.model_selection import train_test_split
import pylab # Модуль для построения графиков
from mpl_toolkits.mplot3d import Axes3D # Модуль для трехмерной графики
# from google.colab import files #Для загрузки своей картинки
import matplotlib.pyplot as plt #Отрисовка изображений
from PIL import Image #Отрисовка изображений
#Отрисовывать изображения в ноутбуке, а не в консоль или файл
# %matplotlib inline
(x_train_org, y_train_org), (x_test_org, y_test_org) = mnist.load_data() #Загрузка данных Mnist
#Меняем формат входных картинок с 28х28 на 784х1
x_train = x_train_org.reshape(60000, 784)
x_test = x_test_org.reshape(10000, 784)
print(x_train_org.shape)
print(x_train.shape)
#Нормализуем входные картинки
x_train = x_train.astype('float32')
x_train = x_train / 255
x_test = x_test.astype('float32')
x_test = x_test / 255
# one_hot_encoding
y_train = utils.to_categorical(y_train_org, 10)
y_test = utils.to_categorical(y_test_org, 10)
x_val1 = x_train[50000:int(50000*1.2)] #  Обучающая выборка 50.000 примеров
y_val1 = y_train[50000:int(50000*1.2)]
# print(x_val1.shape,x_train[:50000].shape)
x_val2 = x_train[10000:int(10000*1.2)] #  Обучающая выборка 10.000 примеров
y_val2 = y_train[10000:int(10000*1.2)]
x_val3 = x_train[500:int(500*1.2)] #  Обучающая выборка 500 примеров
y_val3 = y_train[500:int(500*1.2)]
model = Sequential()
model.add(Dense(800, input_dim=784, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary()) #Вывод структуры модели
data = []
model.fit(x_train[:50000], y_train[:50000], batch_size=128, epochs=10, verbose=1, validation_data=(x_val1, y_val1))
data = data + [['1-Dense', 50000, round(model.evaluate(x_test, y_test, verbose = 0)[1], 3)]]
model.fit(x_train[:10000], y_train[:10000], batch_size=128, epochs=10, verbose=1, validation_data=(x_val2, y_val2))
data = data + [['1-Dense', 10000, round(model.evaluate(x_test, y_test, verbose = 0)[1], 3)]]
df = pd.DataFrame(data, columns = ['model', 'size_data','val_accuracy'])
print(df)