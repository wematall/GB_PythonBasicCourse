"""
Создать (не программно) текстовый файл со следующим содержимым: 
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

file_name = "test_file_5.4.txt"
new_file = "test_file_5.4.new.txt"

translate = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}

try:
    new_obj = open(new_file, 'w')

    with open(file_name) as my_file:
        for line in my_file:
            s = line.split()
            # Replace element 
            s[0] = translate.get(s[0], "No translation")
            print(s)
            for el in s:
                new_obj.write(el)
            new_obj.write('\n')



except IOError:
    print("Error while input output")

finally:
    new_obj.close() 


