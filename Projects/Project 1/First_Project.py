from Project2 import *
answer = int(input("Выберите действие\n 1. Добавить или отредактировать задачу\n 2. Просмотреть все задачи\n 3. Удалить задачу\n 4. Выйти\n "))
while answer != 4:
    if answer == 1:
        print("Добавить или отредактировать задачу")
        add_task(tasks)
    elif answer == 2:
        print("Просмотреть все задачи")
        display_info(tasks)
    elif answer == 3:
        print("Удалить задачу")
        del_task(tasks)
    else:
        print("Введите еще раз")
    answer = int(input("Выберите действие\n 1. Добавить или отредактировать задачу\n 2. Просмотреть все задачи\n 3. Удалить задачу\n 4. Выйти\n "))