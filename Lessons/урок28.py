import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

second="""
CREATE TABLE IF NOT EXISTS Products(
    ProductID INT PRIMARY KEY,
    Name TEXT,
    Category INTEGER
);
"""

insert2="""
INSERT OR IGNORE INTO Products(ProductID,Name,Category) 
VALUES
(1,'Laptop',999.99),
(2,'Smartphone',888.88),
(3,'Keyboard',599.99),
(4,'Mouse',159.99);
"""

cursor.execute(second)
cursor.execute(insert2)

select_second="SELECT * FROM Products"

cursor.execute(select_second)
rows=cursor.fetchall()
for row in rows:
    print(row)

try:
    cursor.execute('UPDATE Products SET Category = Category -100 WHERE ProductID = 1')
    cursor.execute('UPDATE Products SET Category = Category +100 WHERE ProductID = 2')

    conn.commit()
    cursor.execute(select_second)
    rows=cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    conn.rollback()
    print(f"Error: {e}")

finally:
    cursor.close()
    conn.close()  