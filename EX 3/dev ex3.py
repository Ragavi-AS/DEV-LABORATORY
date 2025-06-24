import numpy as np

arr1d = np.array([1, 2, 3, 4])
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6]])

sum_arr = arr1d + np.array([10, 20, 30, 40])
prod_arr = arr2d * 2

slice_1d = arr1d[1:3]        
slice_2d = arr2d[:, 1]       

reshaped = arr1d.reshape(2, 2)  

print("1D:", arr1d)
print("2D:\n", arr2d)
print("Sum:", sum_arr)
print("Product:\n", prod_arr)
print("Slice 1D:", slice_1d)
print("Slice 2D:", slice_2d)
print("Reshaped:\n", reshaped)

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85.5, 92.3, 88.0]
}
df = pd.DataFrame(data)

print(df.head())       
print(df.info())       
print(df.describe())   

print(df['Name'])              
print(df.loc[0])               
print(df.iloc[1:3, 0:2])       

df['AgePlus5'] = df['Age'] + 5
df_mean = df['Score'].mean()

print("Added AgePlus5 column:\n", df)
print("Mean score:", df_mean)

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
categories = ['A', 'B', 'C']
values = [20, 35, 45]

plt.figure()
plt.plot(x, y, marker='o')
plt.title('Line Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.show()

plt.figure()
plt.bar(categories, values, color=['red', 'green', 'blue'])
plt.title('Bar Plot')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

plt.figure()
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart')
plt.axis('equal')  
plt.show()
