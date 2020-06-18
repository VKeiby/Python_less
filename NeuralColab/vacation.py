# This Python file uses the following encoding: utf-8
#

def trip_cost(nights,city,Rdays):
    def hotel_cost(nights):
        costNight = 140
        costNight *= nights
        return costNight

    def plane_ride_cost(city):
        cityDB = {'Крым': 120,
                  'Шри-Ланка': 800,
                  'Каир': 400,
                  'Сочи': 120}
        transferCost = cityDB.get(city)
        return transferCost

    def rental_car_cost(Rdays):
        renta = 40
        tax = renta / 100
        carCost = Rdays * (tax + renta)
        if Rdays > 6:
            carCost = carCost - 50
        elif Rdays >= 3:
            carCost = carCost - 20
        return carCost

    return hotel_cost(nights) + plane_ride_cost(city) + rental_car_cost(Rdays)



nights = int(input('Введите количество ночей: '))
city = input('Куда летим?\nКрым обойдется в 120 у.е.\nШри-Ланка - 800 у.е.\nКаир - 400 у.е.\nСочи - 120 у.е.\nНаберите город:  ')
Rdays = int(input('На сколько дней хотите арендовать авто?\nУ нас действует система скидок от 3 дней  '))

print('Ваша поездка обойдется вам в ',trip_cost(nights,city,Rdays),'у.е')
