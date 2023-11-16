class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет"
    
person1=Person("Pytgon",32)
person2=Person("Ira",25)

greet1= person1.introduce()
greet2 = person2.introduce()
print(greet1)
print(greet2)