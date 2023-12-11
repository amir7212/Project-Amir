import tkinter as tk 

root=tk.Tk()

root.title("Тестовое окно")
root.geometry("400x200")

def on_pressed(event):
    text=entry.get()
    label.config(text="Привет "+text+"!!!")
    

def delete():
    text=entry.get()
    label.config(text="Вы нажали на кнопу <Очистить>")
    entry.delete(0, tk.END)

label=tk.Label(root, text="Для привествия введите свое имя:\nЗатем нажмите клавишу Enter")
label.pack()

entry=tk.Entry(root)
entry.pack()
entry.bind("<Return>", on_pressed)

button=tk.Button(root,text="Очистить", command=delete)
button.pack()

canvas=tk.Canvas(root,width=400,height=200)
canvas.pack()

def on_canvas_click(event):
    x,y = event.x,event.y
    print(f"Щелчок по координатам ({x},{y})")

canvas.bind("<Button-1>",on_canvas_click)

root.mainloop()