class To_do_list():
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Task(To_do_list):
    def __init__(self, name, description, dead_line, status):
        super().__init__(name, description)
        self.dead_line = dead_line
        self.status = status

    def display_info(self):
        print(f"Название задачи: {self.name}\nОписание задачи: {self.description}\nСрок выполнения: {self.dead_line}\nСтатус: {self.status}")

# Создаем пустой словарь для задач
tasks_dict = {}

# Функция для добавления или редактирования задачи
def add_or_edit_task():
    task_name = input("Введите Название задачи: ")
    task_description = input("Введите Описание задачи: ")
    task_deadline = input("Введите Срок выполнения: ")

    # Проверяем, существует ли задача в словаре
    if task_name in tasks_dict:
        print("Задача уже существует. Редактирование задачи.")
        tasks_dict[task_name].description = task_description
        tasks_dict[task_name].dead_line = task_deadline
    else:
        tasks_dict[task_name] = Task(task_name, task_description, task_deadline, "В процессе")
        print("Задача добавлена.")

# Функция для просмотра всех задач
def display_all_tasks():
    for task_name, task_instance in tasks_dict.items():
        task_instance.display_info()

# Главный цикл программы
while True:
    print("\nВыберите действие:")
    print("1. Добавить или отредактировать задачу")
    print("2. Просмотреть все задачи")
    print("3. Выйти")
    
    choice = input("Введите номер действия: ")

    if choice == '1':
        add_or_edit_task()
    elif choice == '2':
        display_all_tasks()
    elif choice == '3':
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")


"""from First_Project import *

class Task(To_do_list):
    def __init__(self, name, description, dead_line, status):
        super().__init__(name, description)
        self.dead_line = dead_line
        self.status = status

    def display_info(self):
        print(f"Название задачи {self.name}\n Описание задачи: {self.description}\n Срок выполнения: {self.dead_line}\n Статус {self.status}")

tasks = {}

def add_task(tasks):
    task_name = input("Введите название задания: ")
    task_desc = input("Введите описание задачи: ")
    task_time = input("Введите сроки выполнения задания:")
    task_status = input("Введите статус задачи:")

    # Используем словарь для представления задачи
    tasks[task_name] = {
        'description': task_desc,
        'deadline': task_time,
        'status': task_status
    }

def del_task(tasks, task_name):
    if task_name in tasks:
        del tasks[task_name]
        print(f"Задача '{task_name}' удалена.")
    else:
        print(f"Задачи с именем '{task_name}' не существует.")

# Добавление задачи
add_task(tasks)

# Удаление задачи
task_to_delete = input("Введите название задачи для удаления: ")
del_task(tasks, task_to_delete)

# Вывод текущего списка задач
print("Текущий список задач:")
for task_name, task_info in tasks.items():
    print(f"Задача {task_name}:")
    print(f"Описание: {task_info['description']}")
    print(f"Срок выполнения: {task_info['deadline']}")
    print(f"Статус: {task_info['status']}")
"""