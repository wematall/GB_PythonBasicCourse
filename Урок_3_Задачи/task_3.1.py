"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. 
Числа запрашивать у пользователя, 
предусмотреть обработку ситуации деления на ноль.
"""

def division(a, b):
  try: 
    result = a / b
  except ZeroDivisionError:
    print("На ноль делить нельзя!!!")
  else:
    print(f"Результат деления: {result}")


  

# Start of the program
print("Будем делить...")

while True:
  a = input("Введите число: ")

  if a.isdigit():
    a = int(a)
    break
  else:
    print("Это не число...")



while True:
  b = input("Введите ещё число: ")

  if b.isdigit():
    b = int(b)
    break
  else:
    print("Это не число...")


division(a, b)
