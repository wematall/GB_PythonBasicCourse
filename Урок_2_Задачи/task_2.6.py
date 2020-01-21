my_dict = {}
tmp_goods = []
goods = []
n = 0

# for analitics
goods_names = []
prices = []
amounts = []
pices = []

user_n = int(input("Сколько наименований товара хотите ввести, например 3: "))

while n < user_n:
    name = input("Введите наименование товара: ")
    price = int(input("Введите цену товара: "))
    amount = int(input("Введите количество единиц: "))
    pc = input("Введите единицы измерения, например, шт.: ")

    my_dict = {"Наименование" : name, "Цена" : price, "Количество" : amount,  "ед" : pc }

    tmp_goods.append(my_dict)
    n = n + 1


for el in enumerate(tmp_goods, 1):
  goods.append(el)
  # print(el)

print("----------------Товары---------------------------")
print(goods)


# Собираем аналитику по товарам
for element in goods:
    data = element[1]
    goods_names.append(data.get("Наименование", ""))
    prices.append(data.get("Цена", ""))
    amounts.append(data.get("Количество", ""))
    pices.append(data.get("ед", ""))

# print(goods_names)
# print(prices)
# print(amounts)
# print(pices)

result_2 = {
    "Наименование" : goods_names,
    "Цена" : prices,
    "Количество" : amounts,
    "ед" : pices
}

print("-------------Аналитика---------------------------")
print(result_2)
    
