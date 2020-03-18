def add(x,y):
    return x+y

from functools import reduce


list_temp = [23,234,543,123,653,12,72,11]
max = reduce(lambda a,b: a if a>b else b,list_temp)
print(max)

# filter

list_50 = list(filter(lambda x: x>50, list_temp))
print(list_50)