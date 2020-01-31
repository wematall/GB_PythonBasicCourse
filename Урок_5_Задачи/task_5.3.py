"""
3. Создать текстовый файл (не программно), 
построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""
low_rate_empls = {}
empls = {}
salary = []

test_file = "test_file_5.3.txt"

try:
    with open(test_file) as my_file:
        for el in my_file:
            s = el.split()
            # print(s)
            salary.append(int(s[1]))       
            empls.update({s[0]: int(s[1])})
    average = sum(salary) / len(salary)

    print(f"People with a salary less than 20000: ")

    for name, salary in empls.items():
        if salary < 20000:
            print(f"{name} : {salary}")
            low_rate_empls.update({name : salary})

    
    print(f"Salary avarage: {average}")

except IOError:
    print("Error while input output")

finally:
    print("поиск выполнен")
