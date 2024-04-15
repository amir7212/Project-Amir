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