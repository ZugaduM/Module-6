class Vehicle:
  vehicle_type = 'none'


class Car:
  price = 1000000

  def horse_powers(self):
    return self.power


class Nissan(Car, Vehicle):
  vehicle_type = 'car'
  price = 2000000

  def horse_powers(self):
    return self.power

my_car = Nissan()
print(my_car.vehicle_type)
print(my_car.price)
