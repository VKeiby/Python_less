# Определим файл в переменную

with open("text.txt", "r") as f:
    origin = f.read()
print(type(origin))
list_txt = list(origin)
print(len(list_txt),type(list_txt))

# Собираем знаки пунктуации в кучу
marks = ['"','.','!','?','-',':',';',',','(',')']

# Перебираем файл для анализа на знаки и удаляем их
for i in range(len(list_txt)):
    print(list_txt[i])
        if list_txt[i] in marks:
        list.txt=list_txt.remove(i)
