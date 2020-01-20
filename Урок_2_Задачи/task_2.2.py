"""
2. Для списка реализовать обмен значений соседних элементов, 
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
 При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().

"""

user_list = []

while True:
    print('Для выхода из программы введите: q')
    value = input('Введите значение: ')

    if value == 'q':
        break
    else:
        user_list.append(value)

# исходный список
print(user_list)

a = len(user_list)
list_length = (a - 1, a)[a % 2 == 0]

index = 0

while index < list_length:
    user_list[index], user_list[index + 1] = user_list[index + 1], user_list[index]
    index += 2

# список после преобразования
print(user_list)
