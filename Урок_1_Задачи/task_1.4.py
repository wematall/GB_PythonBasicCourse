"""
4. Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.

"""
print('Найдем самую большую цифру в числе...')

user_num = input('Введите число, например, 345: ')
user_num = int(user_num)

n = 0 

while user_num > 0:
    tmp = user_num % 10

    if tmp == 9:
        n = tmp
        break
    else:
        if tmp >= n:
            n = tmp
        else:
            n = n
        user_num = user_num // 10

print('Самая большая цифра в заданном числе: ', n)
    
