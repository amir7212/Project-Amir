

# Задание 4
import datetime

data = datetime.datetime.today() + datetime.timedelta(days=7)
print(f"Через семь дне будет: {data}")

#Задание 5
import datetime

data1 = datetime.date(23,11,12)
data2 = datetime.date(23,11,15)
raznica = data2 - data1
print(raznica)

# Задание 6

import datetime

data = datetime.datetime.now()
formmated_date = data.strftime("%A")
print(formmated_date)


# Задание 7

"""import random

rand_num = random.randint(1,6)
target_num = int(input("Загадайте число:" ))
if target_num == rand_num:
    print("Выпало число:",rand_num)
    print("Поздравляем вы выиграли!!!")
else:
    print("Выпало число:",rand_num)
    print("Повезет в следующий раз")
"""

# Задание 8
import random

random_name = ["Amir777","Fedor999","Nina888"]
random_element=random.choice(random_name)
print(f"Случайное имя пользователя: {random_element}")

# Задание 9
import random

random_name = ["Amir777","Fedor999","Nina888"]
a = random.randint(0,len(random_name))
print(f"Победитель: {a}")

# Задание 10
import time 
for i in range(60):
    print(time.strftime("%H:%M:%S",time.localtime()))
    time.sleep(1)

    
# Задание 11
import datetime

time = datetime.datetime.now()
time1 = time.time()
formatted_time=time1.strftime("%I:%M:%S %p")
formatted_time1=time1.strftime("%H:%M:%S")
print(formatted_time)
print(formatted_time1)

# Задание 12


