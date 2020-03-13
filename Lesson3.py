# Определим файл в переменную

with open("text.txt", "r") as f:
    origin = f.read()
print(type(origin))
list_txt = list(origin)
print(len(list_txt),type(list_txt))

# Собираем знаки пунктуации в кучу
marks = ['«','»','.','!','?','—',':',';',',','(',')']

# Перебираем текст для анализа на знаки и создаем новый текст
new_list = []
for e in list_txt:
    if e not in marks:
        new_list.append(e)
print(''.join(new_list))