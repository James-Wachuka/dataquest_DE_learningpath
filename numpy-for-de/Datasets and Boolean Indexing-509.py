## 1. Introduction ##

import numpy as np

x = np.array([
    [44, 70, 49,  2, 19],
    [62, 68, 64, 18, 12],
    [91, 90, 63, 98, 69],
    [22,  9, 98, 16, 58],
    [47, 92, 39,  8, 19],
    [ 1, 41,  3, 15, 71],
    [92, 18, 37, 42,  5]
])

first_four = x[:4]
last_column = x[:, -1]

print("First four rows:")
print(first_four)

print("\nLast column:")
print(last_column)

## 2. Loading CSV Data ##

import numpy as np
import numpy as np

sars = np.genfromtxt('sars.csv', delimiter=',')

first_five = sars[:5]
print(first_five)

## 3. Removing Invalid Data ##

import numpy as np

np.set_printoptions(suppress=True)

# Removing the first row
sars = sars[1:]

# Removing the first column
sars = sars[:, 1:]

# Printing the first five rows
print(sars[:5])

## 4. NumPy Limitations ##

total = sars[:, 2]
max_cases = total.max()

## 5. Comparing Column Values ##

# Select Female column
female = sars[:, 0]

# Select Male column
male = sars[:, 1]

# Compare female and male arrays using the > operator
more_female_cases = female > male

# Compare female and male arrays using the == operator
equal_cases = female == male

# Count how many countries had more female cases using the sum() method
num_more_female = more_female_cases.sum()

# Count how many countries had the same number of female and male cases using the sum() method
num_equal = equal_cases.sum()

# Count how many countries had more male cases
num_more_male = len(sars) - num_more_female - num_equal

## 6. Comparing With a Single Value ##

# Check if there are countries with a case fatality ratio smaller than 1%
any_less_1 = (sars[:, 4] < 1).any()

# Check if all countries have a case fatality ratio of at most 50%
all_less_50 = (sars[:, 4] <= 50).all()

## 7. Logical Connectors ##

deaths = sars[:, 3]
fatality_ratio = sars[:, 4]
death_gt_100_ratio_lt_10 = (deaths >= 100) & (fatality_ratio <= 10)
count = death_gt_100_ratio_lt_10.sum()
deaths = sars[:, 3]
fatality_ratio = sars[:, 4]
death_gt_100_ratio_lt_10 = (deaths >= 100) & (fatality_ratio <= 10)
count = death_gt_100_ratio_lt_10.sum()

## 8. Boolean Masks ##

mask = fatality_ratio >= 10
num_deaths = deaths[mask]
mask = fatality_ratio >= 10
num_deaths = deaths[mask]

## 9. Boolean Masks in Higher Dimensions ##

mask_zeros = sars == 0
zeros = sars[mask_zeros]
num_zeros = len(zeros)
mask_zeros = sars == 0
zeros = sars[mask_zeros]
num_zeros = len(zeros)

## 10. 1D Mask on 2D Array ##

non_zero_deaths = sars[:, 3] > 0
sars_subtable = sars[non_zero_deaths, -3:]
non_zero_deaths = sars[:, 3] > 0
sars_subtable = sars[non_zero_deaths, -3:]