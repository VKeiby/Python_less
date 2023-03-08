import random,time

Ebar = 'Our bar is Empty'
alco = {'Cognac': 300, 'Vodka': 100}
while Ebar != 0:
    print('Now in bar:\n','Available Vodka:', alco['Vodka'],'ml\n','Available Cognac:', alco['Cognac'],'ml\n')
    print('1-Cognac -50ml\n','2-Vodka -50ml\n','3-Pour me something at once!\n')
    zakaz=int(input('What do U want?\n'))
    if zakaz == 3:
        zakaz = random.randint(1,2)
    if zakaz == 1:
        if alco['Cognac'] > 0:
            print('There is your Cognac')
        else: print(Ebar)
    else:
        if alco['Vodka'] > 0:
            print('There is your Vodka')
        else: print(Ebar)



