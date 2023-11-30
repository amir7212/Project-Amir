'''def hello(name):
    print("Привет," +name+ "!")
hello("python")'''

'''def hello(имя="Python"):
    print("Привет, " + имя +"!")
hello("Amir")'''

'''def sum(*args):
    result=0
    for i in args:
        result+=i
    return result

result=sum(1,2,3,4,5)
print(result)'''

'''def hello(name="Гость",age=18):
    print("Привет, " + name + "! Тебе"+ " "  +  str (age) +" " +  "лет")

hello(age= 32,name="Python")'''

'''def inf(**kwargs):
    for key, znc in kwargs.items():
        print(f"{key}:{znc}")

inf(a="amir", b=29, c="Krg")'''

"""def komb(параметр1,*args,**kwargs):
    print("Параметры: ", параметр1)
    print("Позиционные аргументы(*args): ",args)
    print("Именованные аргументы (**kwargs): ",kwargs)

komb("Значения",1,2,3, имя="Киллиан", возраст=25)
print()"""

'''def spisok(zn,*el):
    sp=[zn]
    sp.extend(el)
    return sp
reuslt=spisok(1,2,3,4,5)
print(reuslt)'''


"""def komb(параметр1,*args,**kwargs):
    print("Параметры: ", параметр1)
    print("Позиционные аргументы(*args): ",args)
    print("Именованные аргументы (**kwargs): ",kwargs)

komb("Значения",1,2,3, имя="Киллиан", возраст=25)
print()"""

"""def fukcia():
    x=10
    print(x)
fukcia()"""
#Не понял как должно вывести 20
def родительская_функция():
    переменная_родителя = 20
    def вложенная_функция():
        print(переменная_родителя)

родительская_функция()

"""global_x = 30
def функция():
    print(global_x)
функция()
print(global_x)"""

"""def sl(a,b):
    summa=a+b
    return summa
t=sl(2,3)
print(t)"""

"""def dell(a,b):
    частное=a/b
    остаток=a%b
    return частное, остаток
t=dell(16,4)
print(t)"""

"""def privet():
    print("Privet mir")

result=privet()
print(result)"""

"""def poka():
    print("Do svidania")
    return

poka()"""



##############################################################################################
##############################################################################################
##############################################################################################


#Задание №1
#Найти четные числа

'''def num(a,b):
    for i in range(a,b):
        if i%2==0:
            print(i)
num(1,10+1)'''

#Задание 2

'''def factorial(n):
    res = 1
    for i in range(1,n+1):
        res*=i
    return res

print(factorial(10))'''

#Задание 2.1




