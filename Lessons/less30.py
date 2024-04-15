"""import pandas as pd 

data = {'Name':['John','Anna','Peter','Linda'],
        'Age':[28,33,32,45],
        'City':['New York','Paris','Berlin','London']}

df = pd.DataFrame(data)

print(df.head())
"""
"""import numpy as np

arr = np.array([1,2,3,4,5])

arr_squared = np.square(arr)
arr_sum = np.sum(arr)

print(arr_squared)
print(arr_sum)"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

plt.plot(x,y)
plt.title('Sin Function')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
