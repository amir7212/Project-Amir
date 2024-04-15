"""from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,Sequence('user_id-seq'), primary_key=True)
    name = Column (String(50))
    age = Column(Integer)


engine = create_engine ('sqlite:///:memory:', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

person1= User(name='Python', age = 50)
person2= User(name='Java', age=60)
person3= User(name='PHP', age=30)
person4= User(name='Go', age=20)

session.add_all([person1, person2,person3,person4])
session.commit()

persons = session.query(User).all()
for person in persons:
    print(f"Персонаж: {person.id}, по имени {person.name},возрастом {person.age}")"""

import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS Products(
    ProductID INT PRIMARY KEY,
    Name TEXT,
    Price REAL
);
'''

create_table_query1="""
CREATE TABLE IF NOT EXISTS  Employees(
    EmployeeID INT PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    BirthDate DATE,
    DepatmentID
);
"""

cursor.execute(create_table_query)
cursor.execute(create_table_query1)

insert_data_query='''
INSERT OR IGNORE INTO Products(ProductID, Name, Price) VALUES
(1, 'Laptop',999.99),
(2, 'Smartphone', 499.99);
'''
insert_data_query1='''
INSERT OR IGNORE INTO Employees (EmployeeID, FirstName, LastName, BirthDate, DepatmentID ) VALUES
(1, 'John', 'Doe', '1990-01-15', 101);
'''

cursor.execute(insert_data_query)
cursor.execute(insert_data_query1)
conn.commit()

select_data_query = 'SELECT * FROM Products;'
select_data_query1 = 'SELECT * FROM Employees;'

cursor.execute(select_data_query)
rows= cursor.fetchall()
for row in rows:
    print(row)

cursor.execute(select_data_query1)
rows= cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()


