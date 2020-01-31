"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

print("Программа считает сумму введенных чисел")

file_name = "test_file_5.5.txt"
user_num = None


try:
    fl_obj = open(file_name, 'w')

    while user_num != 'q':
        print("для выхода из программы введите q")

    
        user_num = input("Введите число: ")
    
        if user_num == "q":
            break
        else:
            fl_obj.write(user_num)
            fl_obj.write(" ")

except IOError:
    print("Error while input output")  

finally:
    fl_obj.close()



def count_summ(file_name):
    summ = 0
    try:
        with open(file_name, 'r') as num_obj:
            for el in num_obj:
                nums = el.split()
                # print(nums)

                for i in nums:
                    summ = summ + int(i)
    except IOError:
        print("Error while input output")

    return summ

print(count_summ(file_name))
