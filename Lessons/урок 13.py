"""class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
my_car = Car("Toyota", "Camry", 2022)
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}")"""


# Атрибуты
"""class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

person = Person("Python",30)
print(f"{person.name} is {person.age} years old")"""

# Методы

"""class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        return 3.14*self.radius**2
    def calculate_circumference(self):
        return 2 *3.14*self.radius
    
circle = Circle(5)
area = circle.calculate_area()
circumference= circle.calculate_circumference()

print(f"The area of the cirle is {area}")
print(f" The circumference of the circle is {circumference}")"""

"""class Person:
    def __init__(self,name="Unkown",age=0):
        self.name=name
        self.age=age

person3=Person()
print(person3.name)
print(person3.age)
"""

#Наследование

class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woooof!"
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
dog = Dog("111")
cat = Cat("777")

print(dog.speak())
print(cat.speak())
    
print("=======================================================================")
# Полиморфизм
def animal_sound(animal):
    return animal.speak()

dog = Dog("111")
cat = Cat("777")

print(animal_sound(cat))
print(animal_sound(dog))


