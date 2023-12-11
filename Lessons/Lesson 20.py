# 1
"""import tkinter as tk

def on_pressed(event):
    text=entry.get()
    label.config(text="Enter нажат. Текст"+text)

window=tk.Tk()
window.geometry("400x400")

entry=tk.Entry(window)
entry.pack()
entry.bind("<Return>", on_pressed)

label=tk.Label(window, text="")
label.pack()

window.mainloop()"""

# 2

import tkinter as tk

def delete():
    text=entry.get()
    label.config(text="Вы нажали на кнопу <Очистить>")
    entry.delete(0, tk.END)


window = tk.Tk()
window.title("Тестовое окно")
window.geometry("600x600")

label = tk.Label(window,text="Введите что нибудь:")
label.pack()

entry = tk.Entry(window)
entry.pack()


button = tk.Button(window, text="Очистить",command=delete)
button.pack()

window.mainloop()





