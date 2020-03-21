def add(x,y):
    return x+y

from functools import reduce


list_temp = [23,234,543,123,653,12,72,11]
max = reduce(lambda a,b: a if a>b else b,list_temp)
print(max)

# filter

list_50 = list(filter(lambda x: x>50, list_temp))
print(list_50)

#Простейшая функция и описание
def add(x,y):
    '''
    :param x:
    :param y:
    :return:
    '''
    return x+y

help(add) # просмотр описания функции

# Вызов функции
print(add(100,101))
print(add('Dima','+Kate'))

# Функция возвращает функцию
def f1(n):
    def f2(m):
        return n+m
    return f2
new_f = f1(100)
print(type(new_f))
new_f = f1(100)
print(new_f(250))

#Даже без return функция вернет None
def f():
    pass

print(f())


#Аргументы функций-------------
-------------------------------

# Обязательные аргументы и не обязательные
def add(x,y, z = 10):
    '''
    :param x:
    :param y:
    :return:
    '''
    return x+y+z

print(add(1,2))
print(add(1,2,3))


# args

def func(*args):
    print(type(args), args)
    return args

func(1,2,3,'Volvo')


# kwargs
def func(**kwargs):
    print(type(kwargs), kwargs)
    return kwargs

func(a = 1, b = 2, c = 'Volvo', d = 1.5)


# Все вместе
def func_difficult(x, y = 2, *args, **kwargs):
    print(type(x), x)
    print(type(y), y)
    print(type(args), args)
    print(type(kwargs), kwargs)
    return kwargs

func_difficult(1,3, (1,2,3), temp = 12, temp_1 = 13)

# ------------------------------------------LAMBDA
def ident(x):
    return x

print(ident(10))

print( (lambda x: x)(10)  )

ident_lambda = lambda x: x

print(ident_lambda(10))

car = lambda brend, engine_volume, price: f'Car: {brend.title()}, Engine volume: {engine_volume}, Price: {price}'

print(car('volvo', 1.5, 1300000))

print(type(ident_lambda), type(ident))

# --------------------------------------------------------map
def miles_to_km(miles):
    return miles*1.6

mile_dist = [1.0, 1.6, 2.3]

km_dist = list(map(miles_to_km, mile_dist))
print(type(km_dist), km_dist)

km_dist = list(map(lambda x: 1.6*x, mile_dist))
print(type(km_dist), km_dist)

list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = list(map(lambda x,y: x*y, list_1, list_2))

print(list_3)

# reduce
from functools import reduce # начиная с 3...

list_temp = [43,12,41,100,101,4]
max = reduce(lambda a,b: a if a>b else b,list_temp)
print(max)

# filter

list_50 = list(filter(lambda x: x %10 == 1, list_temp))
print(list_50)

# sorted

list_temp_sort = sorted(list_temp)
print(list_temp_sort)

list_temp_sort_reverse = sorted(list_temp, reverse = True)
print(list_temp_sort_reverse)

# KEY

list_names = ['Kate', 'Dima', 'Ivan', 'Mike']
list_names_sort = sorted(list_names)
print(list_names_sort)

list_names_sort_key = sorted(list_names, key = lambda x: x[3])
print(list_names_sort_key)


# ---------------------REC.Func
# factorial

def fact(num):
    if num == 0:
        return 1
    else:
        return num*fact(num-1)

print(fact(10))

factorial = 1
for i in range(1,11):
    factorial*=i # +=
print(factorial)

# a^b

def degree(a,b):
    if b == 0:
        return 1
    else:
        return a* degree(a,b-1)

print(degree(2,10))

deg = 1
for i in range(1,11):  # b = 10+1 = 11
    deg*=2 # a
print(deg)

# ------------------------------------Global VAR
global_var = 10

def function_example(local_var_1, local_var_2):
    print(local_var_1, local_var_2, global_var)

function_example(11, 12)


def function_example_1(local_var_1, local_var_2):
    global global_var
    global_var = 20
    print(local_var_1, local_var_2, global_var, id(global_var))


function_example_1(11, 12)
print(global_var, id(global_var))

# nonlocal

def counter():
    num = 0
    def plus_one():
        nonlocal num
        num+=1
        return num
    return plus_one

count = counter()

print(count)
print(count())
print(count())

