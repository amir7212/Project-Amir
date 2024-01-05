import tkinter as tk 

root=tk.Tk()

root.title("Тестовое окно")
root.geometry("600x400")

def on_pressed(event):
    text=entry.get()
    label.config(text="Привет "+text+"!!!"  )
    

def delete():
    text=entry.get()
    label.config(text="Вы нажали на кнопу <Очистить>")
    entry.delete(0, tk.END)

def closewindow():
    root.destroy()

label=tk.Label(root, text="Для привествия введите свое имя:\nЗатем нажмите клавишу Enter",background="pink")
label.pack(side="top", pady=30)

entry=tk.Entry(root, width=50) 
entry.pack(side="top", pady=10,anchor="center")
entry.bind("<Return>", on_pressed)

button=tk.Button(root,text="Очистить", command=delete, bg="lightblue")
button.pack(side="bottom",anchor="se")

button1 = tk.Button(root,text="Закрыть окно", command=closewindow,bg="lightgreen")
button1.pack(side="bottom",anchor="sw")


canvas=tk.Canvas(root,width=600,height=400)
canvas.pack()

def on_canvas_click(event):
    x,y = event.x,event.y
    print(f"Щелчок по координатам ({x},{y})")

canvas.bind("<Button-1>",on_canvas_click)


root.mainloop()
