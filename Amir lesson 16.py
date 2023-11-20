# 1 
"""class Vehicle():
    def __init__(self,model,year):
        self.model=model
        self.year=year

class Car(Vehicle):
    def __init__(self,model,year,fuel_type):
        super().__init__(model,year)
        self.fuel_type=fuel_type
    def display_info1(self):
        print(f"Модель {self.model}; Год выпуска - {self.year}, Тип топлива - {self.fuel_type}")


car1=Car("Honda",2018,"Бензин")
car2=Car("BMW",1999,"Газ")

car1.display_info1()
car2.display_info1()"""
# 3

class Vehicle():
    def __init__(self,model,year):
        self.model=model
        self.year=year
    
    def display_info1(self):
        pass

class Car(Vehicle):
    def __init__(self,model,year,fuel_type):
        super().__init__(model,year)
        self.fuel_type=fuel_type
    def display_info1(self):
        print(f"Модель {self.model}; Год выпуска - {self.year}, Тип топлива - {self.fuel_type}")

class Toyota(Car):
    def __init__(self,model, year,fuel_type,model_name):
        super().__init__(model, year,fuel_type)
        self.model_name=model_name

    def display_info1(self):
        print(f"Модель {self.model}\nГод выпуска - {self.year}\nТип топлива - {self.fuel_type}\nНазвание модели - {self.model_name}")

class Zeekr(Car):
    def __init__(self,model,year,fuel_type,fuel_efficiency,model_name):
        super().__init__(model,year,fuel_type)
        self.model_name=model_name
        self.fuel_efficiency=fuel_efficiency
    
    def display_info1(self):
        print(f"Модель {self.model}\nГод выпуска - {self.year}\nТип топлива - {self.fuel_type},{self.fuel_efficiency}\nНазвание модели - {self.model_name}")    

toyota=Toyota("Тойота:",2022,"Бензин","Камри")
zeekr=Zeekr("Zeekr:","2023;","Электричество;", "Не загрязняет окружающую среду, экономия денежных средств;","001;")

toyota.display_info1()
print("=============================================================================")
zeekr.display_info1()


    
