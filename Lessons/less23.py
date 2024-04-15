import tkinter as tk 

"""def show_selection():
    selected_items=listbox.curselection()
    selected_values=[listbox.get(i) for i in selected_items]
    label.config(text=f"Выбранные элементы: {','.join(selected_values)}")

root=tk.Tk()
root.title("простой список")

listbox=tk.Listbox(root,selectmode=tk.MULTIPLE)
listbox.pack()

for item in ["Элемент 1","Элемент 2","Элемент 3","Элемент 4"]:
    listbox.insert(tk.END,item)

button= tk.Button(root,text="Показать выбор", command=show_selection)
button.pack()

label=tk.Label(root,text="")
label.pack()

root.mainloop()"""


'''root= tk.Tk()
root.title("Список с прокруткой")

scrollbar=tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox=tk.Listbox(root,selectmode=tk.SINGLE,yscrollcommand=scrollbar.set)
listbox.pack()
scrollbar.config(command=listbox.yview)

for i in range(1,21):
    listbox.insert(tk.END,f"Элемент {i}")

root.mainloop()
'''
"""
from tkinter import ttk

def on_select(event):
    selected_value.set(combobox.get())

root=tk.Tk()
root.title("Простой комбобокс")

values=["Вариакнт 1","Вариант 2","Вариант 3"]

selected_value=tk.StringVar()
combobox=ttk.Combobox(root, textvariable=selected_value, values=values)
combobox.pack()

button=tk.Button(root, text="Показать выбранный вариант", command=lambda: on_select(None))
button.pack()

root.mainloop()"""

"""from tkinter import ttk

root=tk.Tk()
root.title("Простой комбобокс")

values=["Apple","Banana","Orange","Mango","Kiwi"]

combobox=ttk.Combobox(root,values=values)
combobox.pack()

root.mainloop()"""

"""root=tk.Tk()
root.title("Простой комбобокс")

canvas= tk.Canvas(root, width=300, height= 200)
canvas.pack()

canvas.create_line(50,50,250,150,fill="blue")

root.mainloop()"""

"""root=tk.Tk()
root.title("Простой комбобокс")

canvas= tk.Canvas(root, width=300, height= 200)
canvas.pack()

canvas.create_rectangle(50,50,250,150,fill="orange")

root.mainloop()"""


"""root=tk.Tk()
root.title("Рисование текста на холсте")

canvas= tk.Canvas(root, width=300, height= 200)
canvas.pack()

canvas.create_text(150,100,text="Hello Tkinter" ,fill="green", font=("helvetica",16))

root.mainloop()"""

"""def update_value(value):
    label.config(text=f"Значение: {value}")

root=tk.Tk()
root.title("Ползунок горизантальный")

scale=tk.Scale(root, from_=0, to=100,orient=tk.HORIZONTAL, command=update_value)
scale.pack()

label=tk.Label(root, text="Значение: 0")
label.pack()

root.mainloop()"""

"""def update_value(value):
    label.config(text=f"Значение: {value}")

root=tk.Tk()
root.title("Ползунок вертикальный")

scale=tk.Scale(root, from_=0, to=100,orient=tk.VERTICAL, command=update_value,resolution=5)
scale.pack()

label=tk.Label(root, text="Значение: 0")
label.pack()

root.mainloop()"""

"""def hello():
    print("Hello")

root=tk.Tk()
root.title("Простое главное меню")

menu=tk.Menu(root)
menu.add_command(label="Привет", command=hello)
menu.add_command(label="Выход", command=root.quit)

root.config(menu=menu)

root.mainloop()"""


"""def do_nothing():
    pass

root=tk.Tk()
root.title("Простое главное меню")

menu=tk.Menu(root)
root.config(menu=menu)

submenu=tk.Menu(root)
menu.add_cascade(label="Файл",menu=submenu)
submenu.add_command(label="Новый", command=do_nothing)
submenu.add_command(label="Открыть",command=do_nothing)
submenu.add_separator()
submenu.add_command(label="Выход", command=root.quit)

edit_menu=tk.Menu(menu)
menu.add_cascade(label="Правка",menu=edit_menu)
edit_menu.add_command(label="Отменить",command=do_nothing)
edit_menu.add_command(label="Повторить", command=do_nothing)

root.mainloop()"""

"""root=tk.Tk()
root.title("Логическая группировка виджетов")

frame=tk.Frame(root)
frame.pack()

label1=tk.Label(frame,text="Метка")
label1.pack()

label2=tk.Label(frame, text="Метка 2")
label2.pack()

button=tk.Button(frame, text="Кнопка")
button.pack()

root.mainloop()"""

"""root=tk.Tk()
root.title("Организаци фреймов")

frame1=tk.Frame(root)
frame1.pack(side=tk.LEFT)

label1=tk.Label(frame1,text="Метка 1")
label1.pack()

frame2=tk.Frame(root)
frame2.pack(side=tk.RIGHT)


label2=tk.Label(frame2, text="Метка 2")
label2.pack()


root.mainloop()"""

"""root=tk.Tk()
root.title("Организаци фреймов")

frame=tk.Frame(root)
frame.pack()

label=tk.Label(frame,text="Метка внутри фрейма")
label.pack()

entry=tk.Entry(frame)
entry.pack()

root.mainloop()"""

root=tk.Tk()
root.title("Создание комплексных структур")

frame1=tk.Frame(root)
frame1.pack(side=tk.LEFT)

label1=tk.Label(frame1,text="Метка 1")
label1.pack()

frame2=tk.Frame(root)
frame2.pack(side=tk.RIGHT)

label2=tk.Label(frame2, text="Метка 2")
label2.pack()

frame3=tk.Frame(root)
frame3.pack()

button=tk.Button(frame3, text="Кнопка")
button.pack()

root.mainloop()











