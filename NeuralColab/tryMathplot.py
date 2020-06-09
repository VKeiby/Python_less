plt.figure(1, figsize=(10,8))

plt.subplot(221)
plt.title(df.columns[0])
plt.scatter(df['sepal length (cm)'], df.index, label = y, c=y)
plt.legend = scatter.legend_elements()[0], labels  = list(target_names)

plt.subplot(222)
plt.title(df.columns[1])
plt.scatter(df['sepal width (cm)'], df.index, label =data.target_names, c=y)
plt.legend(data.target_names)

plt.subplot(223)
plt.title(df.columns[2])
plt.scatter(df['petal length (cm)'], df.index, c=y)
plt.legend()

plt.subplot(224)
plt.title(df.columns[3])
plt.scatter(df['petal width (cm)'], df.index, label =data.target_names, c=y)
# Было так:
plt.legend(handles = [0,1,2], labels  = list(target_names))

plt.show()

# Подсказали так, но пока не понимаю кода.. пытаюсь распутать) :
plt.legend (handles = scatter.legend_elements()[0], labels  = list(target_names))