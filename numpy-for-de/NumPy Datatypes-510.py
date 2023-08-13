## 1. Introduction ##

import numpy as np
x = np.array([1, 2, 3, 4])

import numpy as np

x = np.array([1, 2, 3, 4])
x[0] = 5.5

print(x)

## 2. Fixed NumPy Datatypes ##

import numpy as np

values = [1, 2, 3, 4]
x = np.array(values, dtype=np.float64)

x[0] = 5.5

print(x)

## 3. Finding the Datatype ##

import numpy as np

boolean_list = [True, False, True, False]
integer_list = [6, -5, -9, 10]
float_list = [0.5, 10.74, 65.5, 0.2]

boolean_array = np.array(boolean_list)
integer_array = np.array(integer_list)
float_array = np.array(float_list)

print(boolean_array.dtype)
print(integer_array.dtype)
print(float_array.dtype)


## 4. Ndarray From Mixed Lists ##

import numpy as np

values = [3.14, 6.42, 5.0, 0.5]
x = np.array(values, dtype=np.int64)

print(x)

## 5. Fixed-Length Bit Representations ##

import numpy as np
value_list = [-127, -57, -6, 0, 9, 42, 125]

value_array = np.array(value_list, dtype=np.int8)
print(value_array.dtype)

## 6. Memory Consumption ##

import numpy as np

x = np.array([-127, -57, -6, 0, 9, 42, 125], dtype=np.int8)

print(x - 2)
print(x + 3)

## 9. Calculating Memory Requirements ##

num_rows = 1_000_000_000
num_columns = 8
num_values = num_rows * num_columns


bits_per_value = 64
num_bits = num_values * bits_per_value


bits_in_gb = 8_000_000_000
gb = num_bits / bits_in_gb

num_rows = 1_000_000_000
num_columns = 8
num_values = num_rows * num_columns

bits_per_value = 64
num_bits = num_values * bits_per_value

bits_in_gb = 8_000_000_000
gb = num_bits / bits_in_gb

print(gb)