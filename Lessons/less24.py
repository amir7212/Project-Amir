"""import tkinter as tk """

"""def show_selection():
    selection_label.config(text=f"выбрано:{var.get()}")

root=tk.Tk()

root.title("Тестовое окно")

var=tk.IntVar()
checkbutton=tk.Checkbutton(root,text="Выбрать",variable=var, onvalue=1, offvalue=0)
checkbutton.pack()

select_button= tk.Button(root, text="Показать выбор",command=show_selection)
select_button.pack()

selection_label= tk.Label(root,text="")
selection_label.pack()

root.mainloop()"""

"""def show_selection():
    selected_items=[item for item, value in checkboxes.items() if value.get()==1]
    selection_label.config(text=f"Выбрано: {','.join(selected_items)}")

root=tk.Tk()
root.title("Группа кнопок проверки")

options = ["Вариант 1","Вариант 2","Вариант 3"]

checkboxes = {}

for option in options:
    checkboxes[option]=tk.IntVar()
    checkbox = tk.Checkbutton(root, text=option, variable=checkboxes[option],onvalue=1,offvalue=0)
    checkbox.pack()

select_button = tk.Button(root, text="показать выбор", command=show_selection)
select_button.pack()

selection_label = tk.Label(root,text="")
selection_label.pack()

root.mainloop()"""

"""import tkinter as tk

def show_selection():
    selected_options = [option.get() for option in options]
    selection_label.config(text=f"Выбрано: {', '.join(selected_options)}")

root = tk.Tk()
root.title("Тестовое окно")

options = []

# Добавляем три Checkbutton с разными вариантами
for option_text in ["Вариант 1", "Вариант 2", "Вариант 3"]:
    option_var = tk.StringVar()
    option_checkbutton = tk.Checkbutton(root, text=option_text, variable=option_var, onvalue="Да", offvalue="Нет")
    option_checkbutton.pack()
    options.append(option_var)

select_button = tk.Button(root, text="Показать выбор", command=show_selection)
select_button.pack()

selection_label = tk.Label(root, text="")
selection_label.pack()

root.mainloop()
"""

"""def show_state():
    result_label.config(text=f"Опция 1: {var1.get()}, Опция 2: {var2.get()}")

root=tk.Tk()
root.title("Пример кнопокпроверки")

var1=tk.IntVar()
var2=tk.IntVar()

checkbutton1=tk.Checkbutton(root,text="Опция 1",variable=var1, onvalue=1,offvalue=0)
checkbutton2=tk.Checkbutton(root,text="Опция 2", variable=var2, onvalue=1,offvalue=0)

checkbutton1.pack()
checkbutton2.pack()

show_button=tk.Button(root, text="Показать состояние", command=show_state)
show_button.pack()

result_label=tk.Label(root, text="")
result_label.pack()

root.mainloop()"""

"""def on_checkbox_click():
    if var.get()==1:
        result_label.config(text="Кнопка проверки отмечена")
    else:
        result_label.config(text="Кнопка проверки не отмечена")

root = tk.Tk()
root.title("Регистрация обработчиков событий для кнопок проверки")

var = tk.IntVar()
checkbutton=tk.Checkbutton(root, text="Отметить", variable=var, command=on_checkbox_click)
checkbutton.pack()

result_label=tk.Label(root,text="")
result_label.pack()

root.mainloop()"""

import tkinter as tk
from tkinter import messagebox

def file_menu_callback():
    messagebox.showinfo("Файл", "Выбран пункт меню 'Файл'")

def settings_menu_callback():
    messagebox.showinfo("Настройки", "Выбран пункт меню 'Настройки'")

def help_menu_callback():
    messagebox.showinfo("Справка", "Выбран пункт меню 'Справка'")

# Создаем основное окно
root = tk.Tk()

# Устанавливаем заголовок окна
root.title("Пример с меню")

# Устанавливаем размеры окна
root.geometry("400x300")

# Создаем объект меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Добавляем пункты меню
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=file_menu_callback)
file_menu.add_command(label="Сохранить", command=file_menu_callback)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.destroy)

settings_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Настройки", menu=settings_menu)
settings_menu.add_command(label="Настройка 1", command=settings_menu_callback)
settings_menu.add_command(label="Настройка 2", command=settings_menu_callback)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Справка", menu=help_menu)
help_menu.add_command(label="О программе", command=help_menu_callback)

# Запускаем цикл обработки событий
root.mainloop()

