# This Python file uses the following encoding: utf-8
#
import matplotlib.pyplot as plt

# создаем синтетические данные
import numpy as np
x = np.linspace(0,15,100) # Возвращает равномерно распределенные числа в указанном интервале
print(x.shape)
print(x)
# рисуем график по умолчанию
# plt.plot(x)
y = np.cos(x) # задаем значения, соответсвующие функции косинус

z = 0.5 * np.sin(x)

# рисуем график
# заранее объявим объект для регулирования размер полотна для отображения графика
plt.figure(figsize=(12,4)) # параметры в скобках определяют размер графика
# следующие три строки будут выводить три графика функции на одном полотне
plt.plot(x, y, label='cos(x)')
plt.plot(x, z, label='0.5 * sin(x)')
plt.plot(x, 4*z, label='2 * sin(x)')
plt.title('Синусоиды')
plt.xlabel('х')
plt.ylabel('y, z, 4z')
plt.legend()
plt.show()