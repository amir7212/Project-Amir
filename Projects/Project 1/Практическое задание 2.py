import tkinter as tk 
from tkinter import messagebox
from tkinter import ttk

root=tk.Tk()

root.title("Практическое задание №2")
root.geometry("800x400")
root.configure(bg='lightblue')

def file_menu():
    messagebox.showinfo("Файл", "Новое окно открыто")

def spravka_menu():
    messagebox.showinfo("Справка", "Это программа предназначена только в рамках тестового окна, если все будет хорошо и я завершу учебу на пайтон разработчика то напишу настоящую программу за которую будет не стыдно;)")

def on_pressed(event):
    text=entry.get()
    label.config(text="Привет "+text+"!!!"  )
    
def delete():
    text=entry.get()
    label.config(text="Вы нажали на кнопу <Отменить>")
    entry.delete(0, tk.END)

def closewindow():
    root.destroy()

def show_selection():
    selection_label.config(text=f"Выбрано:{var.get()}",background="lightblue")

menu=tk.Menu(root)
root.config(menu=menu)
menu.config(background="grey")

submenu=tk.Menu(root,tearoff=0)
menu.add_cascade(label="Файл",menu=submenu)
submenu.add_command(label="Новое окно",command=file_menu)
submenu.add_command(label="Выход", command=root.quit)

edit_menu=tk.Menu(menu,tearoff=0)
menu.add_cascade(label="Настройки",menu=edit_menu)
edit_menu.add_command(label="Отменить", command=delete)

edit_menu2=tk.Menu(menu,tearoff=0)
menu.add_cascade(label="Справка",menu=edit_menu2)
edit_menu2.add_command(label="О программе", command=spravka_menu)


label=tk.Label(root, text="Для привествия введите свое имя:\nЗатем нажмите клавишу Enter",bg="lightblue")
label.pack(side="top", pady=30)

entry=tk.Entry(root, width=50)
entry.config(bg="lightblue")
entry.pack(side="top", pady=10,anchor="center")
entry.bind("<Return>", on_pressed)

button1 = tk.Button(root,text="Закрыть окно", command=closewindow,bg="lightgreen")
button1.pack(side="bottom")

var=tk.IntVar()
checkbutton=tk.Checkbutton(root,text="Выбрать",variable=var, onvalue=1, offvalue=0,bg="lightblue")
checkbutton.pack()

select_button= tk.Button(root, text="Показать выбор",command=show_selection,bg="pink")
select_button.pack()

selection_label= tk.Label(root,text="")
selection_label.pack()

values=["Как дела?","Что делаешь?","Почему?"]

combobox=ttk.Combobox(root,values=values)
combobox.config(background="lightblue")
combobox.pack()

canvas= tk.Canvas(root, width=700, height= 70)
canvas.config(background="lightblue")
canvas.pack()

canvas.create_text(350,40,text="Просто список с вопросами",fill="green",font=("helvetica",16))

root.mainloop()





