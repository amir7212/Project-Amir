"""class Person:
    name = ""
    age = 0

    def display_info(self):
        print(f"Имя : {self.name}; Возраст: {self.age}")

person1 = Person()
person1.name="Иван"
person1.age=30

person1.display_info()"""


"""class Cirle:
    #Атрибуты класса
    radius=0
    color=""

    def area(self):
        return 3.14* self.radius **2
    
circle1=Cirle()
circle1.radius=5
circle1.color= "red"

area1=circle1.area()

print(f"Площпдь круга радиусом{circle1.radius} (цвет {circle1.color}): {area1}")"""


"""class Person:
    name = ""
    age = 0

    def display_info(self):
        print(f"Имя : {self.name}; Возраст: {self.age}")

person1 = Person()
person1.name="Иван"
person1.age=30

person2 = Person()
person2.name="Nina"
person2.age=24

person1.display_info()
person2.display_info()"""

"""class Person():
    def __init__(self,name,age):
        self.name=name
        self.age= age

    def display_info(self):
        print(f"Имя: {self.name}. Возраст: {self.age}")


person1=Person("Ivan", 30)
person2=Person("Nina", 24)
# С заменой
person3=person1
person3.name="Petr"

person1.display_info()
person2.display_info()"""

class Car():
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def display_info(self):
        print(f"Марка машины: {self.make} Модель машины {self.model}")


car1=Car("Toyota","Camry")
car2=Car("Chevrolet","Nexia")
car3=Car("Lexus", "RX350")

car1.display_info()
car2.display_info()
car3.display_info()