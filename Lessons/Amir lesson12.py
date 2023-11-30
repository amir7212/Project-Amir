#1
"""import math_operations

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

ans = input("Какую операцию хатите выполнить? ")

if ans == "сложение":
    summary = math_operations.summ(a,b)
    print("Сумма", summary)
elif ans == "разность":
    raznost=math_operations.raz(a,b)
    print("Разность", raznost)
elif ans == "умножение":
    umnojenie=math_operations.umnoj(a,b)
    print("Умножение", umnojenie)
else:
    delenie=math_operations.dell(a,b)
    print("Деление", delenie)"""


# 2 









# 3

class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"Студент {self.name}, {self.age} лет")

st1=Student("Миша",21)
st2 = Student("Катя",20)

st1.info()
st2.info()


