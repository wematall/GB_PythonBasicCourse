"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, time, rate, bonus = argv

def salary(time, rate, bonus):
  time = int(time)
  rate = int(rate)
  bonus = int(bonus)
  return ((time * rate) + bonus)


a = salary(time, rate, bonus)

print(f"Your salary: {a}")

