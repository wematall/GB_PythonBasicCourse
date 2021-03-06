"""
5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма 
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. 
Если фирма отработала с прибылью, вычислите рентабельность выручки
 (соотношение прибыли к выручке).
 Далее запросите численность сотрудников фирмы
 и определите прибыль фирмы в расчете на одного сотрудника.

profitability - рентабельность
revenue - выручка
costs - издержки
employees - сотрудники

"""

# Программа выручка издержки

revenue = int(input('Введите значение выручки, например, 5000: '))
costs = int(input('Введите значение издержек, например, 2000: '))

profitability = revenue / costs


if revenue == costs:
    print('У фирмы нет прибыли. Фирма работает в "ноль"')

elif revenue < costs:
    print('Фирма работает с убытком')

else:
    print('Фирма работает с прибылью')
    print('Рентабельность: ', profitability)
    employees = int(input('Введите, сколько человек работает в фирме: '))
    profit_per_employee = (revenue - costs) // employees
    print('Прибыль в расчете на одного сотрудника: ', profit_per_employee)


