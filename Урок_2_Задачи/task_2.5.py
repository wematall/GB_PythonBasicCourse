"""

5. Реализовать структуру «Рейтинг», 
представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга.
 Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.

Подсказка. 
Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, 
например, my_list = [7, 5, 3, 3, 2].

"""

my_list = [5, 7, 3, 2, 3]

# отсортируем и развернем начальный список
my_list.sort()
my_list = my_list[::-1]
print(my_list)

num = None

# Попросим пользователя вводить число
while num != 'q':
    print("Для выхода из программы введите: q")
    num = input("введите число, позицию в рейтинге: ")
    
    if num == 'q':
        break
    else:
        num = int(num)
    

        if num > max(my_list):
            my_list.insert(0, float(num))

        elif num < min(my_list):
            my_list.append(float(num))

        else:
            if my_list.count(num) > 0:
                index = my_list.index(num)
                count = my_list.count(num)
                new_index = index + count
                my_list.insert(new_index, float(num))
            else:
                i = 0
                while True:
                    a = my_list[i]
                    b = my_list[i + 1]

                    if num < a and num > b:
                        my_list.insert(i + 1, float(num))
                        break
                    else:
                        i = i + 1            
    print(my_list)

print(my_list)
