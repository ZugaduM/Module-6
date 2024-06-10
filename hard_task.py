class Figure:
  sides_count = 0

  def __init__(self, color: list, sides: list):
    self._sides = sides
    self._color = color
    self.filled = False
    self._perimetr = 0

  def get_color(self):
    return self._color

  def __is_valid_color(self, r: int, g: int, b: int):
    return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

  def __is_valid_sides(self, *args):
    if len(args) == self.sides_count and all(
        isinstance(side, int) for side in args):
      return True

  def set_color(self, r: int, g: int, b: int):
    if self.__is_valid_color(r, g, b):
      self._color = [r, g, b]
    else:
      self._color = [self._color[0], self._color[1], self._color[2]]

  def get_sides(self):
    temp_val = list(self._sides)
    return temp_val

  def set_sides(self, *args):
    if self.__is_valid_sides(*args):
      self._sides = args

  def __len__(self):
    self._perimetr = 0
    for i in self._sides:
      self._perimetr += i
    return self._perimetr


class Circle(Figure):
  sides_count = 1

  def __init__(self, color, *sides):
    super().__init__(color, *sides)
    self._radius = sides[0] / 2 * 3.14

  def get_square(self):
    return 3.14 * self._radius**2


class Triangle(Figure):
  sides_count = 3
  p = 0

  def __init__(self, color, *sides):
    super().__init__(color, *sides)
    self._height = self.get_sqare(sides) * 2 / sides[0]

  def get_sqare(self, sides):
    Triangle.p = (sides[0] + sides[1] + sides[2]) / 2
    return (2 * (Triangle.p * (Triangle.p - sides[0]) *
                 (Triangle.p - sides[1]) * (Triangle.p - sides[2]))**0.5)


class Cube(Figure):
  sides_count = 12

  def __init__(self, color, *sides):
    super().__init__(color, *sides)
    self._sides = sides * self.sides_count

  def get_volume(self):
    return self._sides[0] * self._sides[1] * self._sides[2]


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
