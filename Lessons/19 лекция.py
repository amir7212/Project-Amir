"""import tkinter as tk 

def closewindow():
    window.destroy()

window = tk.Tk()
window.title("First window")
window.geometry("800x600")

button = tk.Button(window,text="Push me", command=closewindow)
Label = tk.Label(window, text="Go Away!!!")

button.pack()
Label.pack()

window.mainloop()"""

import tkinter as tk

window = tk.Tk()
window.title("Окно")
window.geometry("1000x800")

label = tk.Label(window,text="Привет пользователь!")
label.pack()

window.mainloop()
