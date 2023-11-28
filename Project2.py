from First_Project import *
class Task(To_do_list):
    def __init__(self,name,description,dead_line,status):
        super().__init__(name,description)
        self.dead_line=dead_line
        self.status=status

    def display_info(self):
        print(f"Название задачи {self.name}\n Описание задачи: {self.description}\n Срок выполнения: {self.dead_line}\n Статус {self.status}")

tasks={}

def add_task(tasks):
    task_name=input("Введите название задания: ")
    task_desc=input("Введите описание задачи: ")
    task_time=input("Введите сроки выполнения задания:")
    tasks[task_name]=[task_desc,task_time,]

def del_task(tasks,task_name):
    if task_name in tasks:
        del tasks[task_name]
        print(f"Задача '{task_name}' удалена.")
    else:
        print(f"Задачи с именем '{task_name}' не существует.")


add_task(tasks)

task_to_delete = input("Введите название задачи для удаления: ")
del_task(tasks,task_to_delete)

for task_name,task_desc in tasks.items():
    print(f"Задача 1:\n {task_name},{task_desc}" )





