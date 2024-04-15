"""def summ(a,b):
    return a+b

def raz(a,b):
    return a-b

def dell(a,b):
    return a/b

def umnoj(a,b):
    return a*b"""

"""class To_do_list():
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

# Создаем несколько задач для примера
task1 = Task("Пробежка", "Пробежать 2 км", "Пробежать за 10 мин", "В процессе")
task2 = Task("Уборка", "Помыть посуду", "Сегодня", "Не начата")
task3 = Task("Учеба", "Подготовиться к экзамену", "Завтра", "Не начата")

# Список всех задач
tasks = [task1, task2, task3]

# Получаем ввод для задания пользователя
user_input = input("Введите задание: ")

# Проверяем ввод пользователя и выводим информацию
for task in tasks:
    if user_input.lower() == task.name.lower():
        task.display_info()
        break
else:
    print("Задание не найдено.")"""

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