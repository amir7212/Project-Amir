# Полиморфизм времени выполнения 
"""class Animal():
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Гав!"
class Cat(Animal):
    def speak(self):
        return "Мяу!"
    
    def animal_sound(animal):
        return animal.speak()
    
dog=Dog()
cat=Cat()

print(animal_sound(dog))
print(animal_sound(cat))"""

# Полиморфизм времени компиляции (позднее связывание)

"""def add(x,y):
    return x+y

result=add(5,3)

print(result)"""

# Параметрический полиморфизм 

"""def get_firat_element(sequence:list):
    return sequence[0]
def get_last_element(sequence:tuple):
    return sequence[-1]
"""
# Подтиповый полиморфизм
"""
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

my_pets=[Dog(),Cat()]
for pet in my_pets:
    print(pet.speak())"""

"""class Bird:
    def fly(self):
        pass

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")
def make_bird_fly(bird):
    bird.fly()

ostrich=Ostrich()
make_bird_fly(ostrich)"""

from abc import ABC, abstractmethod

class Drawble(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Drawble):
    def draw(self):
        print("Рисую круг")

class Rectangle(Drawble):
    def draw(self):
        print("Рисую прямоуголник")

shapes=[Circle(),Rectangle()]
for shape in shapes:
    shape.draw()
