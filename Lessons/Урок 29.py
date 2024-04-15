import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

test="""
CREATE TABLE IF NOT EXISTS employees(
employeeid INTEGER PRIMARY KEY,
first_name TEXT,
last_name TEXT,
salary INTEGER
);
"""

insert_test="""
INSERT INTO employees(first_name,last_name,salary)
VALUES
('John','Doe',50000),
('Jane','Smith',60000),
('Bob','Johnson',55000);
"""

cursor.execute(test)
cursor.execute(insert_test)

ind="CREATE INDEX idx_last_name ON employees (last_name);"

cursor.execute(ind)
rows=cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
cursor.close()
conn.close()  

