"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно. 
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

class Clouth:
  def __inti__(self, size, height):
    self.size = size
    self.height = height
  
  def get_square_coat(self):
    return self.size / 6.5 + 5

  def get_square_suit(self):
    return  self.height * 2 + 0.3

  @property
  def get_square_full(self):
    return str(f'Общая площадь ткани \n' f'{(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clouth):
    def __init__(self, size, height):
        #super().__init__(self)
        self.size = size
        self.height = height
        self.square_coat = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани для пальто {self.square_coat}'


class Suit(Clouth):
    def __init__(self, size, height):
        #super().__init__(self)
        self.size = size
        self.height = height
        self.square_suit = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани для костюма {self.square_suit}'

coat = Coat(46, 160)
suit = Suit(46, 160)
print(coat)
print(suit)
print(coat.get_square_full)
print(suit.get_square_full)
print(suit.get_square_coat())
print(suit.get_square_suit())

