import matplotlib.pyplot  as plt 
import seaborn as sns 
import pandas as pd

tips = sns.load_dataset("tips")

"""sns.scatterplot(x="total_bill", y="tip", data=tips,hue="sex",style="time",size="size",palette="viridis")

plt.legend(title="Legend")
plt.title("Scatter Plot with Seaborn")
plt.show()
"""
"""sns.lineplot(x="day", y="total_bill",data=tips,hue="sex",style="time",markers=True)

plt.title("График линий с Seaborn")
plt.show()"""

"""sns.barplot(x="day", y="total_bill",data=tips,hue="sex",ci=None,palette="husl")

plt.title("Гистограмма с Seaborn")
plt.show()"""

"""sns.boxplot(x="day", y="total_bill",data=tips,hue="sex",palette="coolwarm")

plt.title("Ящик с усами с Seaborn")
plt.show()"""

"""data = {
    'A':[1,2,3,4],
    'B':[5,6,7,8],
    'C':[9,10,11,12],
    'D':[13,14,15,16]
}
df = pd.DataFrame(data)

#Создаем тепловую карту
sns.heatmap(df,annot=True, cmap='viridis')

#Добавляем заголовок и метки осей 
plt.title('Пример тепловой карты')
plt.xlabel('Колонки')
plt.ylabel('Строки')

plt.show()"""

sns.pairplot(tips,hue='sex',palette='husl')

plt.suptitle('Матрица диаграмм рассеяния с Seaborn',y=1.02)
plt.show()
