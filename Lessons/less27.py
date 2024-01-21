import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

first=("""
CREATE TABLE IF NOT EXISTS orders(
    order_id INT PRIMARY KEY,
    product_name TEXT,
    quantity INTEGER
);
""")

second="""
CREATE TABLE IF NOT EXISTS Products(
    ProductID INT PRIMARY KEY,
    Name TEXT,
    Category INTEGER
);
"""
third="""
CREATE TABLE IF NOT EXISTS Employees(
    EmployeeID INT PRIMARY KEY,
    Name TEXT,
    Last_name TEXT,
    Salary INTEGER
);
"""

insert1="""
INSERT OR IGNORE INTO orders(order_id, product_name, quantity)
VALUES
(1,'Salt',10),
(2,'Sugar',25),
(3,'Rice',20);
"""
insert2="""
INSERT OR IGNORE INTO Products(ProductID,Name,Category) 
VALUES
(1,'Laptop',999.99),
(2,'Smartphone',888.88),
(3,'Keyboard',599.99),
(4,'Mouse',159.99);
"""
insert3="""
INSERT OR IGNORE INTO Employees(EmployeeID,Name,Last_name,Salary)
VALUES
(1,'Fedor','Fedorov',2000),
(2,'Amir','Amirov',2500),
(3,'Karina','Karinova',2700),
(4,'Liza','Lizova',3000);
"""
update_salary = """
UPDATE Employees
SET Salary = Salary * 1.05;
"""

cursor.execute(first)
cursor.execute(second)
cursor.execute(third)
cursor.execute(insert1)
cursor.execute(insert2)
cursor.execute(insert3)
cursor.execute(update_salary)

select_first="SELECT * FROM orders"
select_second="SELECT Category FROM Products"
select_third="SELECT Name,Last_name,Salary FROM Employees ORDER BY Salary DESC;"

cursor.execute(select_first)
rows=cursor.fetchall()
for row in rows:
    print(row)

print("===========================================================================")

cursor.execute(select_second)
rows=cursor.fetchall()
for row in rows:
    print(row)

print("===========================================================================")

cursor.execute(select_third)
rows=cursor.fetchall()
for row in rows:
    print(row)

print("===========================================================================")

conn.commit()
cursor.close()
conn.close()  
