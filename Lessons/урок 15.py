"""class Person():
    def __init__(self,name,age):
        self.name=name
        self.age= age

    def display_info(self):
        print(f"Имя: {self.name}. Возраст: {self.age}")

    def have_birthday(self):
        self.age+=1
        print(f"с днем рождения {self.name} теперь вам исполнилось {self.age} лет")



person1=Person("Ivan", 30)
# С заменой
person3=person1
person3.name="Petr"

person1.display_info()
person1.have_birthday()
"""


"""class Rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
    def perimetr(self):
        return 2*(self.height+self.width)
    
rect1=Rectangle(5,10)
rect2=Rectangle(3,7)

area1=rect1.area()
perimetr1=rect1.perimetr()

area2=rect2.area()
perimetr2=rect2.perimetr()

print(f"Площадь rect1: {area1}; Периметр rect1: {perimetr1}")
print(f"Площадь rect2: {area2}; Периметр rect2: {perimetr2}")
"""


"""class Person():
    def __init__(self,name,age):
        self.name=name
        self.age= age

    def greet(self):
        return f"Привет меня зовут {self.name} и мне {self.age}"
    

person1=Person("Ivan", 30)

greeting=person1.greet()
print(greeting)"""


"""class Person():
    def __init__(self,name,age):
        self.name=name
        self.age= age

    def set_adress(self,address):
        self.address=address

person1=Person("Ivan", 30)

person1.set_adress("Orbita 1")
print(person1.address)"""

"""class Counter():
    def __init__(self):
        self.value=0

    def increment(self):
        self.value+=1

counter=Counter()
counter.increment()

print(counter.value)
"""
# Возврат значения из методов

"""class Calculator():
    def add(self,a,b):
        result= a+b
        return result
    
calc=Calculator()
result=calc.add(5,3)
print(result)"""

# Изменение состояния обьекта с аргументами

class BankAccount():
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount

account=BankAccount(1000)

account.deposit(500)
print(account.balance)

# Изменение состояния обькта с возвратом значения

class ShoppingCart():
    def __init__(self):
        self.items=[]

    def add_items(self,item):
        self.items.append(item)
        return len(self.items)
cart=ShoppingCart()

item_count=cart.add_items("Молоко")
print(f"Количество товаров в корзине: {item_count}")

# Геттеры - Методы получения
"""class Person():
    def __init__(self,name,age):
        self._name=name
        self._age= age

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    

person1=Person("Ivan", 30)

name= person1.get_name()
age=person1.get_age()
print(f"Имя {name}; Возраст {age}")"""



#Сеттеры - Методы установки 
class Person():
    def __init__(self,name,age):
        self._name=name
        self._age= age

    def set_name(self,name):
        if isinstance(name,str):
            self._name=name
        else:
            print("Ошибка имя должно быть строкой")
    def set_age(self,age):
        if age >=0:
            self.age=age 
        else:
            print("Ошибка возраст должен быть не отрицательным числом")


person1=Person("Ivan", 30)

person1.set_name("Petr")
person1.set_age(35)
print(f"Имя {person1._name} Возраст {person1._age}")