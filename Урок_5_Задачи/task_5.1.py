"""
1. Создать программно файл в текстовом формате, 
записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
"""


file = open("test_file.txt", "a")


while True:

    s = input("Print in your string here: ")

    if s == ' ':
        file.close()
        break
    else:
        file.write(s)
        file.write('\n')


f = open("test_file.txt", "r")
print(f.read())

f.close()
