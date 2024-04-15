import pandas as pd
#1
"""data = [1,2,3,4,5]
index = ['a','b','c','d','e']

series = pd.Series(data,index=index)
print(series)
"""
#2
"""data = {'Name':['Marla','Bob','Tayler'],
        'Age':[25,30,35],
        'City':['New York','San Francisco','Los Angeles']}
df=pd.DataFrame(data)
print(df)"""

#3 Csv файлы
"""df_csv= pd.read_csv('employees.csv')

print(df_csv.head())"""

#4Excel 
"""df_excel = pd.read_excel('example.xlsx', sheet_name="Sheet1")

print(df_excel.head())
"""
#5 SQL соединение
from sqlalchemy import create_engine

#Установка соединения с базой

"""engine = create_engine("sqlite:\\example.db")

#Загрузка данных с использованием SQL запроса
quary = "SELECT * FROM table_name"
df_sql = pd.read_sql(quary,engine)

print(df_sql.head())"""

#6 Json
#Загрузка данных из JSON-файла
"""df_json=pd.read_json('example.json')

print(df_json.head())"""

#7 Создание DataFrame
# Из списка списков
data = [['John',28,'New York'],
        ['Anna',30,'Balhash'],
        ['Peter',25,'Paris'],
        ['Linda',45,'London']
]
columns = ['Name','Age','City']
df=pd.DataFrame(data,columns=columns)

print(df)
#Сортировка по столбцу "Age" по убыванию
"""df_sorted=df.sort_values(by='Age', ascending=False)
print(f"Неотсортированый датафрейм{df}")
print(f"Отсортированный датафрейм{df_sorted}")"""
#Применение функции к каждому элементу столбца
"""df['Age']=df['Age'].apply(lambda x:x*2)"""
#Примениние функции к каждой строке 
"""df['Combined_Info']=df.apply(lambda row:f"{row['Name']}({row['Age']}years)",axis=1)"""
#Удаление столбца
"""df=df.drop('City',axis=1)"""
#Удаление строки по индексу
"""df=df.drop(2)"""
#Удаление строк по условию
"""df = df[df['Age']<35]"""
#Добавление нового столбца
"""df['Gender']=['Male','Female','Male','Female']"""
#Добавление новой строки
"""new_row=pd.Series(["Mike",35,"Toronto","Male"],index=df.columns)
df=df._append(new_row,ignore_index=True)"""
#Обновление значений в ячейке
"""df.at[1,'Age']=23"""
#Обновление столбца
"""df['Age']=df['Age']+1"""
#Выбор столбца по названию
"""name_column=df["Name"]"""
#Выбор нескольких столбцов
"""selected_columns=df[['Name','Age']]"""
#Выбор строки по индексу
"""selected_row=df.loc[0]"""
#Выбор данных по условию
"""filtered_data=df[df['Age']>30]"""

"""print("====================================================================================")
print(name_column)
print("====================================================================================")
print(selected_columns)
print("====================================================================================")
print(selected_row)
print("====================================================================================")
print(filtered_data)"""

# Сохранение в CSV файле
data = {'Name':['Marla','Bob','Tayler'],
        'Age':[25,30,35],
        'City':['New York','San Francisco','Los Angeles']}
df=pd.DataFrame(data)

"""df.to_csv('data.csv', index=False)"""
#Сохранение в SQL
"""engine = create_engine('sqlite:///data.db')

df.to_sql('students',con=engine,index=False,if_exists='replace')"""