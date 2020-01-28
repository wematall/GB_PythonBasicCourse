"""
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""

from itertools import cycle,count


def my_count(a, b):
  for el in count(a):
    if  el > b:
      break
    else:
      print(el)


def my_cycle(s, k):
  c = 0
  for el in cycle(s):
    if c > k:
      break
    else:
      print(el, c)
      c += 1

my_count(3, 10)
my_cycle("and", 10)

