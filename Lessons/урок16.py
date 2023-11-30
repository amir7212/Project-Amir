# Наследование

"""class Vehicle():
    def __init__(self,color):
        self.color=color

    def start_engine(self):
        print("Двигатель запущен")

class Car(Vehicle):
    def __init__(self,color,brand):
        super().__init__(color)
        self.brand=brand

    def honk(self):
        print("Бт-бип")

vehicle=Vehicle("Синий")
car=Car("Красный","Toyota")
print(vehicle.color)

vehicle.start_engine()

print(car.color)
print(car.brand)
car.start_engine()
car.honk()"""

# Создание подкласса

"""class Animal():
    def __init__(self,name):
        self.name=name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} говорит Гав!"

animal = Animal("Неизветное животное")
dog = Dog("Шарик")

print(animal.name)
animal.speak()
print(dog.name)
dog.speak()"""

# Переопределение метода

"""class Shape():
    def area(self):
        return 0 
class Rectangle(Shape):
    def __init__(self,widht,height):
        self.widht=widht
        self.height=height

    def area(self):
        return self.widht*self.height
    
shape = Shape()
rectangle = Rectangle(5,4)

print("Площадь фигуры", shape.area())
print("Площадь прямоугольника:", rectangle.area())"""

# Множественное наследие

"""class Bird:
    def fly(self):
        return "Птицы могут летать"
    
class Mammal:
    def run(self):
        return "Млекапитающие могут бегать"
    
class Bat(Bird,Mammal):
    def __init__(self,specials):
        self.specials=specials

bat = Bat("Летучая мышь")

print(bat.fly())
print(bat.run())"""

# НЕ понл что такое абстрактный метод и как его делать