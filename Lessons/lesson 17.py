# 1
def add(a,b):
    return a + b

def subtraction(x,y):
    return x - y 

def multiplication(c,d):
    return c * d

result_add= add("Hello", "World")
result_subtraction=subtraction(10.5,5.5)
result_multiplication=multiplication(5,10)

print(result_add)
print(result_subtraction)
print(result_multiplication)

print("=============================================================================")
# 2 
import math

class Shape():
    def area(self):
        return 0 
class Rectangle(Shape):
    def __init__(self,widht,height):
        self.widht=widht
        self.height=height

    def area(self):
        return self.widht*self.height

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2

class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))       

rectangle = Rectangle(5,4)
circle=Circle(10)
triangle=Triangle(4,5,6)

print("Площадь прямоугольника:", rectangle.area())
print("Площадь круга: ",circle.area())
print("Площадь треугольника: ", triangle.area())

print("=============================================================================")

# 3 