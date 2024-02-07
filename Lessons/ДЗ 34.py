import pandas as pd

data = [['Fedor',28,'Male',95],
        ['Nikita',30,'Male',80],
        ['Lada',25,'Female',75],
        ['Lisa',45,'Female',85]
]
columns = ['Name','Age','Gender','GPA']
df=pd.DataFrame(data,columns=columns)

#Выбор столбца по названию
name_data=df["Name"]
#Выбор по полу
female_data= df[df['Gender']=='Female']
#Выбор по высшему баллу
highest_data = df['GPA'].max()
#Обновление столбца
df['Age']=df['Age']+1
#Обновление значений в ячейке
df.at[2,'GPA']=97
#Добавление нового студента
new_row=pd.Series(["Mike",35,"Male",83],index=df.columns)
df=df._append(new_row,ignore_index=True)
#Увеличение GPA на 0.5
df['GPA']=df['GPA']*0.5
#Сортировка по столбцу "Age" по убыванию
df_sorted=df.sort_values(by='Age', ascending=False)
#Сортировка по столбцу "GPA" по возрастанию
df_sorted1=df.sort_values(by='GPA', ascending=True)
print(df)
print("====================================================================================")
print(f"Выбор столбца по названию:\n{name_data}")
print("====================================================================================")
print(f"Выбор по полу:\n{female_data}")
print("====================================================================================")
print(f"Выбор по высшему баллу:\n{highest_data}")
print("====================================================================================")
print(f"Сортировка столбца 'Age' по убыванию:\n{df_sorted}")
print("====================================================================================")
print(f"Сортировка столбца 'GPA' по возрастанию:\n{df_sorted1}")

# Сохранение в CSV 
df.to_csv('DZ_34.csv', index=False)