"""import module

print(module.greed("Python"))
print(module.square(5))
print(module.my_variable)

from module import greed,square

print(greed("Python"))
print(square((3)))"""


# 2 
"""import requests

responce = requests.get("https://www.example.com")
print(responce.status_code)
print(responce.text)"""
#3
"""import math
print(math.sqrt(25))"""
#4
"""from math import sqrt
print(sqrt(25))"""

#5 Импорт всех элементов из модуля с помощью *

"""from math import *

print(sqrt(25))"""

#6 Импорт с псевдонимом
"""import math as m

print(m.sqrt(25))"""

#7 Импорт только определенных элементов с псевдонимами

"""from math import sqrt as squre_root, pi as circle_constant
print(squre_root(25))
print(circle_constant)
"""
from module import greed

def main():
    name=input("Введите имя:")
    messagee = greed(name)
    print(messagee)
if __name__=="__main__":
    main()






