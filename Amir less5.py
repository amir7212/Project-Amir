#Задание №1.1
'''a = int(input("Введите число: "))
b = 0
while b<=a:
    print(b)
    b+=2'''
    
#Задание №1.2

'''a = int(input("Введите число: "))
b = 0
c = 1
while c<=a:
    b+=c
    c+=1
print(b)'''

#Задание №2.1
'''for i in range(0,20,2):
    print(i)'''

#Задание №2.2
'''a = int(input("Введите число: "))
for i in range(1,11):
    print(i,"*",a,"=",i*a)'''

#Задание №3.1
'''for i in "python":
    print(i)'''

#Задание №3.2

'''a = 1
b = 0
while a<=100:
    b+=a
    a+=2
print(b)'''

#Задание №4.1
'''a = ("*")
for i in range(1,6):
    for j in range(1):
        print(i*a)'''

#Задание №4.2
"""a = 5
for i in range(1,6):
    for j in range(1):
        print(i,"*",a,"=",i*a)"""

#Задание №4.3
# Не понял
number = int(input('Введите число чтобы проверить является ли число до него (включительно) простыми: '))
prime = True
for i in range(2, number + 1):
    for j in range(2, number + 1):
        if i != j and i % j == 0:
            prime = False
            break
    if prime:
        print('Число', i, 'простое')
    else:
        print('Число', i, 'не простое')
        prime = True


#Задание со ***

'''a = int(input("Введите число: "))
for i in range(2,a+1,2):
    print(i)'''

    
    

    



    



