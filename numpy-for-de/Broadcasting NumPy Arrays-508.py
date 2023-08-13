## 1. Introduction ##

import numpy as np

x = np.array([
    [7., 9., 2., 2.],
    [3., 2., 6., 4.],
    [5., 6., 5., 7.]
])

# Create an ndarray of ones with the same shape as x
ones = np.ones_like(x)

# Subtract one from each entry of x using the ones ndarray
x = x - ones

print("Updated x:")
print(x)

## 2. Broadcasting With a Single Value ##

import numpy as np

x = np.array([3, 2, 4, 5])

# Calculate the reciprocals of the values in x using the division operator
r = 1 / x

print("Reciprocals of x:")
print(r)

## 3. Broadcasting Mental Model ##

import numpy as np

x = np.array([
    [4, 2, 1, 5],
    [6, 7, 3, 8]
])

y = np.array([
    [1],
    [2]
])

# Add x and y and assign the result to z
z = x + y

print("Result of adding x and y:")
print(z)

## 4. Broadcasting Horizontally ##

import numpy as np

x = np.array([
    [4, 2, 1, 5],
    [6, 7, 3, 8]
])

y = np.array([1, 2, 3, 4])

# Add x and y and assign the result to z
z = x + y

print("Result of adding x and y:")
print(z)

## 5. Broadcasting Vertically ##

import numpy as np

x = np.array([
    [1],
    [2],
    [3]
])

y = np.array([1, 2, 3])

# Add x and y and assign the result to z
z = x + y

print("Result of adding x and y:")
print(z)

## 6. Broadcasting on Both ##

import numpy as np

dice1 = np.array([1, 2, 3, 4, 5, 6])
dice2 = np.array([[1], [2], [3], [4], [5], [6]])

dice_sums = dice1 + dice2

print("dice_sums:")
print(dice_sums)

## 7. Broadcasting Rules ##

import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([[1], [2], [3], [4]])

# Get the initial shapes of x and y
shape_x = x.shape
shape_y = y.shape

print("Shape of x:", shape_x)
print("Shape of y:", shape_y)

# Perform step 1 of broadcasting
shape_x_step1 = (4, 1)
shape_y_step1 = (4, 1)

# Perform step 2 of broadcasting
shape_x_step1 = (1, 4)
shape_y_step2 = (4, 4)


# Perform step 3 of broadcasting
error = False

print("Shape after step 1 - x:", shape_x_step1)
print("Shape after step 1 - y:", shape_y_step1)
print("Shape after step 2 - x:", shape_x_step2)
print("Shape after step 2 - y:", shape_y_step2)
print("Error:", error)

## 8. Reshaping ##

import numpy as np

dice1 = np.array([i for i in range(1, 7)])
dice2 = dice1.reshape(6, 1)
dice_sums = dice1 + dice2

print("dice_sums:")
print(dice_sums)

## 9. Compatible Shapes ##

import numpy as np

cell_numbers = np.array([i for i in range(1, 37)])
numbering_by_row = cell_numbers.reshape(6, 6)
numbering_by_col = cell_numbers.reshape(6, 6, order='F')

print("Numbering by row:")
print(numbering_by_row)

print("\nNumbering by column:")
print(numbering_by_col)