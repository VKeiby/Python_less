def Palindrom(string):
    marks = [' ']
    # Перебираем текст для анализа на знаки и создаем новый текст
    new_list = []
    for el in string:
        if el != ' ':
            new_list.append(el)
    new_list = list((map(lambda x: x.lower(), new_list)))
    string = str(''.join(new_list))
    l = len(new_list)
    for i in range(l//2):
        if new_list[i] != new_list[-1-i]:
            print("It's not palindrome")
            quit()
    print("It's palindrome")

# Palindrom('Мороз в узел, лезу взором')
# Palindrom(palindrom)
# Palindrom('А роза упала на лапу Азора')
s = 'anaNa'
Palindrom(s)