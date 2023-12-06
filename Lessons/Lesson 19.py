# 1

"""import tkinter as tk

def closewindow():
    window.destroy()

window = tk.Tk()
window.title("Окно")
window.geometry("1000x800")

label = tk.Label(window,text="Привет пользователь!")
label.pack()

button = tk.Button(window, text="Закрыть окно",command=closewindow)
button.pack()

window.mainloop()"""

# 2

import tkinter as tk

window = tk.Tk()
window.title("Анкета")
window.geometry("800x800")

label = tk.Label(window, text="ФИО:Иванов Иван Иванович\nДата рождения:01.01.1999\nПол: Мужчина\nСемейный статус: Женат\nРод деятельности: Преподователь")
label.pack()

window.mainloop()