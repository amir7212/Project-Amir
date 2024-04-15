"""import csv
import sqlite3

# 1. Откройте соединение с базой данных
conn = sqlite3.connect('example.db')

# 2. Создайте объект курсора
cursor = conn.cursor()

# 3. Создайте таблицу в базе данных SQLite (если она еще не создана)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS your_table_name (
        column3 INTEGER,
        column1 TEXT,
        column2 TEXT

    )
''')

# 4. Откройте CSV файл и выполните вставку данных
csv_file_path = 'employees.csv'  # Укажите путь к вашему CSV файлу

with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Пропустите заголовок, если он есть
    next(csv_reader, None)

    # Используйте цикл для вставки данных из CSV файла в базу данных
    for row in csv_reader:
        cursor.execute('INSERT INTO your_table_name (column3, column1, column2) VALUES (?, ?, ?)', row)

select_data_quary="SELECT * FROM your_table_name;"

cursor.execute(select_data_quary)
rows=cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()"""

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Создание таблиц
first = """
CREATE TABLE IF NOT EXISTS orders(
    order_id INT PRIMARY KEY,
    product_name TEXT,
    quantity INTEGER
);
"""

second = """
CREATE TABLE IF NOT EXISTS Products(
    ProductID INT PRIMARY KEY,
    Name TEXT,
    Category INTEGER
);
"""

third = """
CREATE TABLE IF NOT EXISTS Employees(
    EmployeeID INT PRIMARY KEY,
    Name TEXT,
    Last_name TEXT,
    Salary INTEGER
);
"""

# Вставка данных
insert1 = """
INSERT OR IGNORE INTO orders(order_id, product_name, quantity)
VALUES
(1,'Salt',10),
(2,'Sugar',25),
(3,'Rice',20);
"""

insert2 = """
INSERT OR IGNORE INTO Products(ProductID,Name,Category) 
VALUES
(1,'Laptop',999.99),
(2,'Smartphone',888.88),
(3,'Keyboard',599.99),
(4,'Mouse',159.99);
"""

insert3 = """
INSERT OR IGNORE INTO Employees(EmployeeID,Name,Last_name,Salary)
VALUES
(1,'Fedor','Fedorov',2000),
(2,'Amir','Amirov',2500),
(3,'Karina','Karinova',2700),
(4,'Liza','Lizova',3000)
"""

# Запрос для увеличения зарплаты на 5%
update_salary = """
UPDATE Employees
SET Salary = Salary * 1.05;
"""

# Выполнение SQL-запросов
cursor.execute(first)
cursor.execute(second)
cursor.execute(third)
cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)
cursor.execute(update_salary)

# Вывод данных
select_first = "SELECT * FROM orders"
select_second = "SELECT Category FROM Products"
select_third = "SELECT Name, Last_name, Salary FROM Employees ORDER BY Salary DESC;"

cursor.execute(select_first)
rows = cursor.fetchall()
print("Orders:")
for row in rows:
    print(row)

print("===========================================================================")

cursor.execute(select_second)
rows = cursor.fetchall()
print("Products:")
for row in rows:
    print(row)

print("===========================================================================")

cursor.execute(select_third)
rows = cursor.fetchall()
print("Employees:")
for row in rows:
    print(row)

print("===========================================================================")

# Сохранение изменений и закрытие соединения
conn.commit()
cursor.close()
conn.close()










