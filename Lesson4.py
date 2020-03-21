import random

def f(names,intX):
    integer_list = []
    for i in range(intX):
        rnd = random.randint(0,(len(names)-1))
        integer_list.append(names[rnd])
    print(integer_list)
    return

dbase = ['Yana','Marina','Vasiliy', 'Alex', 'Egor', 'Yaroslav', 'Daiya', 'Nina', 'Katerine', 'Fodor', 'Antot','Victoria',
         'Vera', 'Boris', 'Yasha','Grisha', 'Tolik','Timofey','Sandra','Nastya','Kseniya','Kristina','Polina','Tanya']
f(dbase,50)
print()
