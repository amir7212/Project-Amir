import sqlite3
import tkinter as tk
from tkinter import ttk
from datetime import datetime

def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            last_name TEXT,
            age INTEGER,
            data TEXT      
        )
    ''')
    conn.commit()

def add_user():
    name = name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if name and last_name and age and data:
        cursor.execute('INSERT INTO users (name, last_name, age,data) VALUES (?, ?, ?, ?)', (name, last_name, age, data))
        conn.commit()
        update_treeview()

def delete_user():
    selected_item = treeview.selection()
    if selected_item:
        user_id = treeview.item(selected_item, 'values')[0]
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        update_treeview()

def update_treeview():
    for row in treeview.get_children():
        treeview.delete(row)
    cursor.execute('SELECT * FROM users ORDER BY data DESC') #Здесь так же можно добавить "ASC" чтобы сортировка была по дата записанной ранее 
    for row in cursor.fetchall():
        treeview.insert('', 'end', values=row)

def update():
    name = name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    selected_item = treeview.selection()
    if selected_item:
        user_id = treeview.item(selected_item, 'values')[0]
        cursor.execute('UPDATE users SET name = ?, last_name=?, age=?  WHERE id=?',(name, last_name, age,user_id))
        conn.commit()
        update_treeview()

def search_users():
    keyword = search_entry.get()
    if keyword:
        query = "SELECT * FROM users WHERE name LIKE ? OR last_name LIKE ? OR data LIKE ?"
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
        for row in treeview.get_children():
            treeview.delete(row)
        for row in cursor.fetchall():
            treeview.insert('', 'end', values=row)


conn = sqlite3.connect('example.db')
cursor = conn.cursor()

create_table()

root = tk.Tk()
root.title('SQL + Tkinter Example')
root.geometry("1000x400")

name_label = tk.Label(root, text='Name:')
name_label.grid(row=0, column=0, padx=5, pady=5, sticky='E')

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

last_name_label = tk.Label(root, text='Last Name:')
last_name_label.grid(row=1, column=0, padx=5, pady=5, sticky='E')

last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

add_button = tk.Button(root, text='Add User', command=add_user)
add_button.grid(row=0, column=2, padx=5, pady=5)

age_label = tk.Label(root, text='Age:')
age_label.grid(row=2, column=0, padx=5, pady=5, sticky='E')

age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text='Delete User', command=delete_user)
delete_button.grid(row=1, column=2, padx=5, pady=5)

update_button= tk.Button (root, text='Update User', command=update)
update_button.grid(row=2, column=2, padx=5, pady=5)

search_label = tk.Label(root, text='Search:')
search_label.grid(row=3, column=0, padx=5, pady=5, sticky='E')

search_entry = tk.Entry(root)
search_entry.grid(row=3, column=1, padx=5, pady=5)

search_button = tk.Button(root, text='Search', command=search_users)
search_button.grid(row=3, column=2, padx=5, pady=5)

columns = ('ID', 'Name', 'Last Name', 'Age', 'Data')
treeview = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    treeview.heading(col, text=col)
treeview.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

update_treeview()

root.mainloop()

conn.close()
