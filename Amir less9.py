

"""a={1:"one",2:"two",3:"three"}
for key,value in a.items():
    print(key,":",value)"""


# Добавление в конец словаря
"""a={1:"one",2:"two",3:"three"}
a[4]="four"
print(len(a))
"""

# Выводит через цикл for ключи
"""a={1:"one",2:"two",3:"three"}
a[4]="four"
for key in a.keys():
    print(key)"""

# Выводит через цикл for значения
"""a={1:"one",2:"two",3:"three"}
a[4]="four"
for val in a.values():
    print(val)"""

# Находит элементы в словаре

"""a={1:"one",2:"two",3:"three"}
a[4]="four"
print(2 in a)
print(4 in a)
print(5 in a)"""

# Сортировка словаря
"""import operator
a={2:"two",1:"one",3:"three"}
b=sorted(a.items(), key=operator.itemgetter(0))
print(b)
b=sorted(a.items(), key=operator.itemgetter(1))
print(b)"""

# Сравнение
#Не видет Cmp
"""a = {1:"one",2:"two",3:"three"}
b = {4:"four", 5:"five"}
c = {1:"one",2:"two",3:"three"}
print(cmp(a,b))
print(cmp(b,c))
print(cmp(a,c))"""

# Копия
"""a = {1:"one",2:"two",3:"three"}
b = a.copy()
print(a,b)"""

# Очистка
"""a = {1:"one",2:"two",3:"three"}
a.clear()
print(a)"""

# Перебор словаря

"""users = {
    "+11111111":"Tom",
    "+22222222":"Bob",
    "+33333333":"Alice"
}
for key in users:
    print(f"Phone:{key} User:{users[key]}")"""

"""users = {
    "+11111111":"Tom",
    "+22222222":"Bob",
    "+33333333":"Alice"
}
for a,b in users.items():
    print(f"Phone:{a},User:{b}")"""

# Множества

"""ok_set = set("helloworld")
print(ok_set.pop())"""

'''ok_set = set("helloworld")
ok_set.clear()
print(ok_set)'''

# Обьединение множеств "|"
"""a = {1,2,3,4,5}
b = {4,5,6,7,8,9,10}
print(b.union(a))
"""
# Пересечение множеств "&"

"""a = {1,2,3,4,5}
b = {4,5,6,7,8,9,10}
print(a&b)
"""
"""a = {1,2,3,4,5}
b = {4,5,6,7,8,9,10}
print(a.intersection(b))"""

"""a = {1,2,3,4,5}
b = {4,5,6,7,8,9,10}
print(b.intersection(a))"""

# Определение разницы множеств "-"
"""a = {1,2,3,4,5}
b = {4,5,6,7,8,9,10}
print(b-a)"""

"""a = {1,2,3,4,5}
b = {4,5,6,7,8,9,10}
print(a.difference(b))"""

# Симметричная разница множеств "^"
"""a = {1,2,3,4,5}
b = {4,5,6,7,8,9,10}
print(a^b)
"""
"""a = {1,2,3,4,5}
b = {4,5,6,7,8,9,10}
print(b.symmetric_difference(a))"""

