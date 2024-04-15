import tkinter as tk 

root=tk.Tk()

root.title("Мое главное окно")
root.geometry("800x600")

button=tk.Button(root,text="Нажми меня")
button.pack()

def on_button_click():
    print("Кнока была нажата")

button.config(command=on_button_click)

canvas=tk.Canvas(root,width=200,height=200)
canvas.pack()

def on_canvas_click(event):
    x,y = event.x,event.y
    print(f"Щелчок по координатам ({x},{y})")

canvas.bind("<Button-1>",on_canvas_click)

# отвязка обработчка
#button.unbind("<Button-1>",on_button_click)

root.mainloop()