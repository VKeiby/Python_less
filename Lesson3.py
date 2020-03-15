# Определим файл в переменную
with open("text.txt", "r") as f:
    origin = f.read()
#print(type(origin))                                     #str
list_txt = list(origin)
#print(len(list_txt),type(list_txt))                     #list

# Собираем знаки пунктуации в кучу
marks = ['«','»','.','!','?','—',':',';',',','(',')','-','\n']

# Перебираем текст для анализа на знаки и создаем новый текст
new_list = []
for el in list_txt:
    if el == '-' or el == '\n': new_list.append(' ')
    if el not in marks:
       new_list.append(el)
#print(''.join(new_list))

# ----------Split
splitText=origin.split()
#print(type(splitText),splitText)                       #list

# -----------lower
#print(origin.lower())
#low_listTxt = (map(lambda x: x.lower(),new_list))
low_listTxt = list((map(lambda x: x.lower(),new_list)))
#print(type(low_listTxt),''.join(low_listTxt))
# print(low_listTxt)

# ------------dict
dictText = str(''.join(low_listTxt))
listD = dictText.rsplit(" ")
DictOut = dict()

for key in listD:
    if not key in DictOut:
        DictOut[key] = 1
    else:
        DictOut[key] += 1

print(DictOut)
print(len(DictOut),type(DictOut))

# -------------Freq PH

