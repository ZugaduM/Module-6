class Car:
  price = 1000000

  def horse_powers(self, car_power):
    self.power = car_power
    return f'This car have {self.power} horse power'


class Nissan(Car):
  price = 2000000

  def horse_powers(self, car_power):
    self.power = car_power
    return f'This car have {self.power} horse power'


class Kia(Car):
  price = 500000

  def horse_powers(self, car_power):
    self.power = car_power
    return f'This car have {self.power} horse power'

