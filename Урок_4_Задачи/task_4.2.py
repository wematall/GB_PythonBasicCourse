"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""

my_list = [2, 4, 7, 3, 1, 5]
new_list1 = []

# using ordinary way
for i in range(len(my_list)-1):
  if my_list[i] < my_list[i+1]:
    new_list1.append(my_list[i+1])

# one_line expression
new_list2 = [my_list[i + 1] for i in range(len(my_list)-1) if my_list[i + 1] > my_list[i]]

print(f"Old list: {my_list}")
print(f"First variant: {new_list1}")
print(f"Second variant: {new_list2}")

