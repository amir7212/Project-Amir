from First_Project import *
class Task(To_do_list):
    def __init__(self,name,description,dead_line,status):
        super().__init__(name,description)
        self.dead_line=dead_line
        self.status=status

    def display_info(self):
        print(f"Название задачи {self.name}\n Описание задачи: {self.description}\n Срок выполнения: {self.dead_line}\n Статус {self.status}")



"""quest1=Task(input(f"Введите Название задачи: "))
quest2=Task(input(f"Введите Описание задачи: "))
quest3=Task(input(f"Введите Срок выполнения: "))"""


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
        
else:
    print("Задание не найдено.")

"""name_task=Task("Пробежка","Пробежать 2 км", "Пробежать за 10 мин",True)

name_task.display_info()"""






