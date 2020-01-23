"""
2. Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
"""

def user_data(name, last_name, byear, city, email, phone):
  result = f"user name: {name}, user lastname: {last_name}, user birth year: {byear}, user sity: {city}, user email: {email}, user phone: {phone}"
  print(result)


user_data(name="Andrey", last_name="T", byear=1999, city='Moscow', email="email@google.com", phone=777777777)
