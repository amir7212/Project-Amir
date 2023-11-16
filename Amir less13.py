# 1
class Car():
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def description(self):
        print(f"Автомобиль {self.brand}, марки {self.model}, года выпуска {self.year}")

car1 = Car ("Toyota", "Camry",2022)
car2 = Car ("BMW", "X5","2023")

car1.description()
car2.description()

# 2 

class Person():
    def __init__(self,name,age):
        self.name= name
        self.age=age

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_info(self):
        return f"{self.name}, {self.age} лет получает в месяц {self.salary} тенге"

employee = Employee("Олег", 30, 250000)
print(employee.get_info())

# 3
class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит Гав!"
class Cat(Animal):
    def speak(self):
        return f"{self.name} говорит Мяу!"
    
dog = Dog("Шарик")
cat = Cat("Барсик")

print(dog.speak())
print(cat.speak())



