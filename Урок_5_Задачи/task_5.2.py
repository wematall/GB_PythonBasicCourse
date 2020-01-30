"""
2. Создать текстовый файл (не программно), 
сохранить в нем несколько строк,
 выполнить подсчет количества строк, 
количества слов в каждой строке.
"""
file_name = "test_file.txt"
lines = 0
words = 0

try:
    my_file = open(file_name, "r")
    context = my_file.readlines()
	
    for el in context:
        lines += 1
        words += len(el.split())

    print(f"Файл содержит строк: {lines} ")
    print(f"Файл содержит слов:  {words} ")

except IOError:
    print("произошла ошибка ввода вывода")

finally:
    my_file.close()
