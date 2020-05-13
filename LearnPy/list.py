# This Python file uses the following encoding: utf-8
#

# listX = [1,2,3,4,5,6,7,8,9,10]
# print(listX)
# short version:
# doubleList = [i**2 for i in listX]
# doubleList = []
# res = 0
# for i in range(len(listX)):
#     doubleList.append(listX[i]**2)
#     res += listX[i] ** 2
# print(doubleList, res, sep='\n')
#
# words = ['madam', 'topot', 'test', 'word', 'maxam']
# palindromes = []
#
# for word in words:
#     if word == word[::-1]:
#         palindromes.append(word)
#
# print(palindromes)

my_str = ['Oko za oko', 'А роза упала на лапу Азора', 'Около Миши молоко']
palindromes = []
for word in my_str:
    word_r = word.replace(' ','').lower()
    if word_r == word_r[::-1]:
        palindromes.append(word)

print(palindromes)