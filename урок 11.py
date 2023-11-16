# Вычесление квадратного корня

import math

x = 25
sqrt_x=math.sqrt(x)
print(f"Квадратный корень из {x} = {sqrt_x}")

print("===============================================")
# Вычисление синису и косинуса угла
import math

angle = 45 #угол в градусах 
radians= math.radians(angle)
sin_angle = math.sin(radians)
cos_angle = math.cos(radians)
print(f"Синус угла {angle} градусов =  {sin_angle   } ")
print(f"Косинус угла {angle} градусов = {cos_angle}")

print("=======================================================================")

#Вычисление экспоненты (marh.exp(x))

import math

x = 2
exp_x = math.exp(x)
print(f"e в степени {x} = {exp_x}")

print("=======================================================================")

# Вычисление логорифма (math.log(x,base))

import math

x = 10 
base = 2
log_x_base_2 = math.log(x,base)
print(f"Логорифм {x} по основанию {base} = {log_x_base_2}")

print("=======================================================================")

# Возведение в степень 

import math 

x = 2 
y = 3
result = math.pow(x,y)
print(f"{x} в степени {y} = {result}")

print("=======================================================================")

# Преоброзование угла из градусов в радианы (math.radians(degrees)) и обратно (math.degrees(radians))

import math 

angle_degrees = 90
radians = math.radians(angle_degrees)
print(f"{angle_degrees} градусов = {radians} радиан")

radians = math.pi/2
angle_degrees = math.degrees(radians)
print(f"{radians} радиан = {angle_degrees} градусов")

print("=======================================================================")


# Datetime

#Получение текущей даты и времени 
 
import datetime
now = datetime.datetime.now()
print(f"Текущаю дата и время: {now}")


print("=======================================================================")

#Получение текущей даты и времени отдельно 

import datetime

today = datetime.datetime.today()
current_time = datetime.datetime.now().time()

print(f"Текущаю дата: {today}")
print(f"Текущее время: {current_time}")

print("=======================================================================")

# Создание обьекта datetime с определенной датой и временем
import datetime

custom_date = datetime.datetime(2023,8,15,10,30,0)
print(f"Заданная дата и время {custom_date}")

print("=======================================================================")

# Извлечение компонентов даты и времени из обькта datetime

import datetime

custom_date = datetime.datetime(2023,8,15,10,30,0)
year  = custom_date.year
month = custom_date.month
day = custom_date.day
hour = custom_date.hour
minute = custom_date.minute
second = custom_date.second
print(f"Год: {year}")
print(f"Месяц: {month}")
print(f"День: {day}")
print(f"Час: {hour}")
print(f"Минута:{minute}")
print(f"Секунда:{second}")

print("=======================================================================")

# Форматирование обьекта datetime в строку

import datetime

custom_date = datetime.datetime(2023,8,15,10,30,0)
formatted_date=custom_date.strftime("%Y-%m-%d %H:%M:%S")
print(f"Форматированная дата и время {formatted_date}")

print("=======================================================================")

# Работа сдельтой времени (timedelta)
# Вычесление между двумя датами и временем  

import datetime

start_date = datetime.datetime(2023,8,15,10,0,0)
end_date = datetime.datetime(2023,8,15,12,30,0)

time_differnce = end_date - start_date
print(f"Разница во времени: {time_differnce}")

print("=======================================================================")

# Генерация случайногоцелого числа в заданном диапозоне с помощью функции (random)

import random

# Генерация случайногоцелого числа от 1 до 100
random_number=random.randint(1,100)
print(f"Случайное целое число: {random_number}")

print("=======================================================================")

# Генерация случайногоцелого числа c плавающей запятой в заданном диапозоне с помощью функции (random)

import random

#Генерация случайногоцелого числа c плавающей запятой от 0,0 до 1,0

random_float=random.random()
print(f"Случайное число с плавающей запятой: {random_float}")


print("=======================================================================")

#Выбор случайного элемента из списка 

import random

a = ["apple","banana","kiwi","orange"]
random_element=random.choice(a)
print(f"Случайный элемент из списка: {random_element}")

print("=======================================================================")

# Перемешивание элементов из списка
import random

a = [1,2,3,4,5]
random.shuffle(a)
print(f"Перемешанный список: {a}")

print("=======================================================================")

#Получение текущего времени в секундахс начала эпохи
# С 1970года начало отчета информационной эпохи

import time

current_time = time.time()
print(f"Текущее время в секундах сначала эпохи: {current_time}")

print("=======================================================================")

# Задержка выполнения программы на 2 секунды

import time
 
print("Начало выполнения программы")
time.sleep(2)
print("Завершение выпонения программы")

print("=======================================================================")

# Измерение времени выполнения кода

import time

start_time = time.time()

for i in range(1000000):
    pass
end_time = time.time()

elapsed_time = end_time-start_time
print(f"прошло {elapsed_time:.4f} секунд")
print("=======================================================================")

# Преобразование времени в строку
import time

timestamp = time.time()
foremmated_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
print(f"Отформатированное время: {foremmated_time}")