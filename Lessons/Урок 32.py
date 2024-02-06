import numpy as np  
#1
def sum_row(arr):
    rows_sums=np.sum(arr,axis=1)
    return rows_sums

arr1=np.random.randint(1,10, size=(3,3))
arr2=np.random.randint(1,10, size=(3,3))

result=np.multiply(arr1,arr2)

print(f"Array1:{arr1}")
print(f"Array2:{arr2}")

sums_arr1=sum_row(arr1)
sums_arr2=sum_row(arr2)

#print(f"\nResult:{result}")

print(f"Summa1:{sums_arr1}")
print(f"Summa2:{sums_arr2}")

#2
data=np.random.randint(1,100, size=(3,3))

#Среднее значение элементов
data_mean=np.mean(data)
#Медиана
data_median=np.median(data)
#Стандартное отклонение
data_deviation = np.std(data)
print("====================================================================================")
print(f"Data:{data}")
print(f"Среднее знавение:{data_mean}")
print(f"Медиана:{data_median}")
print(f"Стандартное отклонение:{data_deviation}")






#Одномерный массив
#Двумерный массив
"""arr_1d = np.array([1,2,3,4,5])

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("Одномерный массив")
print(arr_1d)

print("\nДвумерный массив")
print(arr_2d)"""

#Матрица
"""matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

result = 2 * matrix

print("Исходная матрица")
print(matrix)

print("\nРезультат умножения на число")
print(result)
"""
#Массивы
#создание массива из списка
"""arr_from_list=np.array([1,2,3,4,5])

#создание массива из кортежа
arr_from_tuple = np.array((1,2,3,4,5))

print("Массив из списка:")
print(arr_from_list)

print("\nМассив из кортежа")
print(arr_from_tuple)
"""
#Арифметические операции

"""arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

#Сложение 
sum_arr = arr1 + arr2
#Вычитание 
diff_arr= arr2 - arr1
#Умножение 
prod_arr = arr1 * arr2
#Деление
div_arr = arr1 / arr2

print("Сложение:", sum_arr)
print("Вычитание:", diff_arr)
print("Умножение:", prod_arr)
print("Деление:", div_arr)"""

#Унарные операции
"""arr = np.array([1,4,9,16])

#Квадратный корень
sqrt_arr = np.sqrt(arr)
#Экспонента
exp_arr=np.exp(arr)
#Натуральные лагорифмы
log_arr=np.log(arr)

print("Квадратный корень:",sqrt_arr)
print("Экспонента:",exp_arr)
print("Натуральный логарифм:",log_arr)
"""
# Сравнение 

"""arr1=np.array([1,2,3])
arr2=np.array([2,2,2])

#Сравнение поэлементно
equal_arr=arr1==arr2
qreater_arr=arr1>arr2

print("Равенство",equal_arr)
print("Больше", qreater_arr)"""

#Математические функции
"""arr=np.array([1,2,3,4,5])
#Сумма элементов массива
arr_sum=np.sum(arr)
#Среднее значение элементов
arr_mean=np.mean(arr)
#Минимальное и максимальное значение 
arr_min=np.min(arr)
arr_max=np.max(arr)

print("Сумма:",arr_sum)
print("Среднее значение:",arr_mean)
print("Минимальное значение:",arr_min)
print("Максимальное значение:",arr_max)"""
