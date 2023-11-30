
'''class Task():
    def __init__(self,name,description,dead_line,status):
        super().__init__(name,description)
        self.dead_line=dead_line
        self.status=status'''

tasks={}

def add_task(tasks):
    task_name=input("Введите название задания: ")
    task_desc=input("Введите описание задачи: ")
    task_time=input("Введите сроки выполнения задания:")
    tasks[task_name]=[task_desc,task_time,]
    

def del_task(tasks):
    task_name=input("Введите название задания: ")

    if task_name in tasks:
        del tasks[task_name]
        print(f"Задача '{task_name}' удалена.")
    else:
        print(f"Задачи с именем '{task_name}' не существует.")

def display_info(tasks):
        for k,v in tasks.items():
            print (f"Задание: {k}")
            print (f"Задача: {v[0]}\nСроки: {v[1]}")







