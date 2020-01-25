"""
3. Реализовать функцию my_func(), 
которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
  my_l = [a, b, c]
  minim = min(my_l)
  my_l.remove(minim)
  result = sum(my_l)
  return result


result = my_func(5, 1, 12)
print(result)
