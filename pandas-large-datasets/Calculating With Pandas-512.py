## 1. Introduction ##

import pandas as pd

# Read the cars.csv file
cars = pd.read_csv('cars.csv')

# Set index starting from 1
cars.set_index(pd.Index(range(1, len(cars) + 1)), inplace=True)

# Inspect the updated dataframe
print(cars)

## 3. Arithmetic and Summary Statistics ##

# Calculate the weight of the heaviest car
max_weight = cars['Weight'].max()

# Calculate the weight of the lightest car
min_weight = cars['Weight'].min()

# Calculate the weight ratio
weight_ratio = max_weight / min_weight

## 4. Value Counts ##

# Count the number of cars for each origin
origin_counts = cars['Origin'].value_counts()

# Convert origin_counts to a dictionary
origin_counts_dict = origin_counts.to_dict()

# Print the origin_counts_dict variable
print(origin_counts_dict)

## 5. Filtering Rows ##

# Select cars with European origin
european_cars = cars[cars['Origin'] == 'Europe']

# Print the shape of european_cars
print(european_cars.shape)

## 6. Logical Operators ##

# Select cars whose origin is not the US
non_us_cars = cars[~(cars['Origin'] == 'US')]

# Select cars that satisfy the conditions for low MPG and horsepower
low_mpg_horsepower = cars[(cars['MPG'] > 0) & (cars['MPG'] < 10) & (cars['Horsepower'] >= 150)]

# Select cars that satisfy the conditions for light or fast
light_or_fast = cars[(cars['Weight'] <= 2000) | (cars['Acceleration'] >= 30)]

## 7. Masks with Column Selection ##

# Select Name and Origin columns for cars satisfying the conditions
name_and_origin = cars[(cars['MPG'] > 0) & (cars['MPG'] < 12) & (cars['Horsepower'] >= 200)][['Name', 'Origin']]

## 8. Adding Columns ##

# Calculate the power-to-weight ratio
cars['PW_ratio'] = cars['Horsepower'] / cars['Weight']

# Calculate the maximum value of the PW_ratio column
max_pw_ratio = cars['PW_ratio'].max()

## 9. Column with Partial Data ##

mpg_l100_constant = 235.214583

# Filter out rows with MPG equal to 0
mpg_non_zero = cars.loc[cars['MPG'] > 0, 'MPG']

# Calculate L/100 values
L100 = 235.214583 / mpg_non_zero

# Add L/100 column to the dataframe
cars['L/100'] = L100