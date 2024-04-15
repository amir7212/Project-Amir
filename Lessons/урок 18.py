"""def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль не допустимо")
    return x//y 

try:
    result = divide(10,2)
except ZeroDivisionError as e:
    print(f"Произошла ошибка: {e}")
finally:
    print("Этот блок будет выполнен всегда")"""

#обработка нескольких иключений 
"""def divide(x,y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль не допустимо")
    return x//y 

try:
    result = divide(10,2)
except ZeroDivisionError as e:
    print(f"Произошла ошибка: {e}")
except TypeError as e:
    print(f"Произошла ошибка типа данных: {e}")"""

#Пользовательские исключения 

"""class MyCustomError(Exception):
    pass

try:
    if something_bad_happened:
        raise MyCustomError("Что то пошло не так")
except MyCustomError as e:
    print(f"Произошла пользовательская ошибка: {e}")"""

# Получение информации об исключении 

try:
    result = divide(10,0)
except ZeroDivisionError as e:
    print(f"Произошла ошибка типа {type(e).__name__}:{e}")

