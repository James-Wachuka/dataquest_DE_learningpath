## 1. Introduction ##

import numpy as np

## 2. Introduction to ndarrays ##

import numpy as np

x = np.array([10, 20, 30])
length = len(x)

print(x)
print(length)

## 3. Accessing Values in an ndarray ##

x = np.array([10, 20, 30])

import numpy as np



x0 = x[0]
x2 = x[2]

x[1] = 42

print("x0 =", x0)
print("x2 =", x2)
print("Updated x =", x)

## 4. Slicing ndarrays ##

# x = np.array([9, 1, 5, 6, 2, 0, 4, 3, 8, 7])

import numpy as np

x = np.array([9, 1, 5, 6, 2, 0, 4, 3, 8, 7])

first_half = x[:len(x)//2]
last_8 = x[-8:]
middle = x[1:-1]

print("first_half =", first_half)
print("last_8 =", last_8)
print("middle =", middle)

## 5. The Slicing Increment ##

# x = np.array([9, 1, 5, 6, 2, 0, 4, 3, 8, 7])

import numpy as np

x = np.array([9, 1, 5, 6, 2, 0, 4, 3, 8, 7])

even = x[::2]
odd = x[1::2]
mul_3 = x[::3]
every_2 = x[3:9:2]

print("even =", even)
print("odd =", odd)
print("mul_3 =", mul_3)
print("every_2 =", every_2)

## 6. Copying an ndarray ##

# x = np.array([1, 0, 0, 0, 1])

import numpy as np

x = np.array([1, 0, 0, 0, 1])

y = x[1:-1]
z = y.copy()

z[0] = 9

print("x =", x)
print("y =", y)
print("z =", z)

y[1] = 7

print("x =", x)
print("y =", y)
print("z =", z)

## 7. Negative Indexes and Steps ##

# x = np.array([9, 1, 5, 6, 2, 0, 4, 3, 8, 7])


import numpy as np

x = np.array([9, 1, 5, 6, 2, 0, 4, 3, 8, 7])

second_to_last = x[-2]
reversed_x = x[::-1]
first_5_reversed = x[4::-1]
last_5_reversed = x[-1:-6:-1]

print("second_to_last =", second_to_last)
print("reversed_x =", reversed_x)
print("first_5_reversed =", first_5_reversed)
print("last_5_reversed =", last_5_reversed)

## 8. Two Dimensional Arrays ##

import numpy as np

my_2d_array = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])

my_2d_array[1, 1] = 42

print(my_2d_array)

## 9. Slicing Two Dimensional Arrays ##

array2d = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])

x = array2d[:3, 3:]
print(x)
y = array2d[0:3:2, :]
print(y)
z = array2d[0:3:2, ::2]
print(z)

## 10. Setting The Slice Value ##

array2d = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
])

array2d[:,:2]=1
print(array2d)

array2d[2:, :]=2
print(array2d)

array2d[:3, 1:4]=3
print(array2d)

## 11. Selecting Rows and Columns ##

people_data = np.array([
    [27, 67, 1.65],
    [35, 81, 1.84],
    [29, 55, 1.60],
    [41, 73, 1.79]
])

    
anna_row = people_data[2, :]
print(anna_row)


bob_age_height = people_data[3, [0,2]]
print(bob_age_height)

ages_col = people_data[:, 0]
print(ages_col)

weight_dexter_bob = people_data[[1,3],1]
print(weight_dexter_bob)