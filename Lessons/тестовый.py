"""x = -5
y = 10
if x>0:
    if y>0:
        print("Оба числа положительные")
    else:
        print("x положительное y отрицательное")
else:
        print("x отрицательное")"""

'''year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0  :
    print("високосный год")
else:
    print("не високосный год")'''

'''for i in range(5):
    print(i)'''

'''count = 0
while count <=5:
    print(count)
    count+=1'''


'''matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in matrix:
    for j in i:
        print(j,end=" ")
print()'''

'''data = [{"name": "Alice","age":25},{"name": "Bob","age":30}]
for person in data:
    if person["age"]<30:
        print(person["name"],"is young")
    else:
        print(person["name"],"is not young")'''

'''students = [
    {"name": "Alice","grades":[85,90,78]},
    {"name": "Bob","grades":[70,60,75]},
    ]
    
for student in students:
    total_grade = sum(student["grades"])
    average_grade = total_grade/len(student["grades"])
    print(student["name"], "average grade:", average_grade)'''

"""image = [[(255,0,0),(0,255,0),(0,0,255)],
         [(0,255,255),(255,0,255),(255,255,0)]]
for row in image:
    for pixel in row:
        print(pixel)"""

"""for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            print("■", end=" ")
        else:
            print("□", end=" ")"""


'''for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="\t")
    print()'''


'''numbers = (5,10,15,20,25,30)
for num in numbers:
    if num>15:
        print(num,"больше 15")
    else:
        print(num,"не больше 15")'''

'''numbers = [1,2,3,4,5,6,7,8,9,10]
even_nubers =[]
for num in numbers: 
    if num%2==0:
        even_nubers.append(num)
print("четные числа:", even_nubers)'''

'''numbers = [10,20,30,90,5,7,6]
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value=num
print("Максимальное значение:", max_value)'''

'''count = 0
while count<5:
    print(count)
    count+=1'''

#бабочка
'''size = int(input("Введите размер половины бабочки: "))

for i in range(1, size + 1):
    print('*' * i + ' ' * (2 * (size - i)) + '*' * i) # Верхняя половина бабочки

for i in range(size, 0, -1):
    print('*' * i + ' ' * (2 * (size - i)) + '*' * i) # Нижняя половина бабочки'''

def get_price_with_vat(price):
    vat_rate = 20
    vat = price * vat_rate / 100
    price_with_vat = price + vat
    return price_with_vat
    
milk_price_vat = get_price_with_vat(100)  # 120
spaghetti_price_vat = get_price_with_vat(150)  # 180


    



