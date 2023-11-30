# Задание 1
"""students = {"Alice": 20,
            "Bob": 18,
            "Jhon": 21,
            "Fred": 22
}
del students["Bob"]
print(students)"""

# Задание 2

"""num = {1,2,3,4,5}
num1 = {1,2,6,7,8,9}
print("Обьединение",num|num1)
print("Перечение",num&num1)"""

# Задание 3
# Не понял задания
"""countries_and_cities = {
    "America":"new york" " " "las vegas",
    "Kazakhstan": "astana" " " "almaty",
    "France": "paris" " " "marsel"
}
for k,v in countries_and_cities.items():
    print(f"Страна:{k}  Город: {v}")"""

# Задание 4
inv = {
    "Продукты":
        {"Name":"Хлеб",
        "Sum": 20,
        "Price": 180},
    
    "Хозтовары":
        {"Name":"Мыло",
        "Sum": 50,
        "Price": 300},
    
    "Авто товары":
        {"Name":"Щетка",
        "Sum": 10,
        "Price": 500}
    }
for k,v in inv.items():
    print("Товары: ", k)
    print("Название товара: ",v ["Name"])
    print("Количество товара: ",v["Sum"])
    print("Цена товара: ",v["Price"])
# Задание 5
"""tovar = {
    "Iphone 15":"White",
    "Iphone 13":"Black",
    "Iphone 14":"Brown"
}
print("Iphone 15" in tovar)"""

# Задание 6
"""fruits = {"Orange":200,"Kiwi":250,"Apple":150}
total = sum(fruits.values())
print(total)"""

# Задание 7
"""a = {1,2,3,9,99,63,15,14}
b = {11,25,3,54,78,99}

print("Разность: ",a-b)
print("Общие: ",a&b)"""

# Задание 8,9

"""a = {1,2,3,9,99,63,15,14}
b = {11,25,3,54,78,99}

print("Пересечение: ", a&b)
print("Обьединение: ", a|b)"""
