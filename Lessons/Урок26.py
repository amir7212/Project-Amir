import sqlite3 
import csv

conn= sqlite3.connect("mydatabase.db")

cursor=conn.cursor()

create_table_query="""
CREATE TABLE IF NOT EXISTS Products(
    ProductID INT PRIMARY KEY,
    Name TEXT,
    Price REAL
);
"""

create_table_query1="""
CREATE TABLE IF NOT EXISTS Test(
    ProdID INT PRIMARY KEY,
    Name TEXT,
    Price REAL
);
"""
insert_data_quary="""
INSERT OR IGNORE INTO Products(ProductID,Name,Price) 
VALUES
(1,'Laptop',999.99),
(2,'Smartphone',888.88),
(3,'Keyboard',599.99),
(4,'Mouse',159.99);
"""

insert_data_quary2="""
INSERT INTO Test(ProdID,Name,Price)
SELECT ProductID,Name,Price
FROM Products;

"""

update="""
UPDATE Products
SET Name = Laptop
WHERE Name = Laptop; 
""" 

#cursor.execute(create_table_query)

#cursor.execute(create_table_query1)

#cursor.execute(insert_data_quary)

#cursor.execute(insert_data_quary2)

cursor.execute(update)

select_data_quary="SELECT * FROM Products;"

select_data_quary1="SELECT * FROM Test"


cursor.execute(select_data_quary)
rows=cursor.fetchall()
for row in rows:
    print(row)


cursor.execute(select_data_quary1)
rows=cursor.fetchall()
for row in rows:
    print(row)

conn.commit()

cursor.close()
conn.close()  
