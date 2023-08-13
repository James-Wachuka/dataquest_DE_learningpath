## 1. Introduction ##

import pandas as pd

## 2. Read a CSV with Pandas ##

import pandas as pd

cars = pd.read_csv("cars.csv")

## 3. Dataframes ##

# Get the shape of the cars dataframe
cars_shape = cars.shape

# Get the first six rows of the cars dataframe
first_six_rows = cars.head(6)

# Get the last four rows of the cars dataframe
last_four_rows = cars.tail(4)

# Print the results
print("Shape of cars dataframe:", cars_shape)
print("\nFirst six rows of cars dataframe:")
print(first_six_rows)
print("\nLast four rows of cars dataframe:")
print(last_four_rows)

## 4. Accessing Data with Indexes ##

# Extract rows with odd indexes and first three columns
cars_odd = cars.iloc[1::2, :3]

# Get the name of the car in the fifth row
fifth_odd_car_name = cars_odd.iat[4, 0]

# Get the last four rows
last_four = cars_odd.tail(4)

# Print the last four rows
print(last_four)

## 5. Accessing Data with Names ##

# Set the "Name" column as row labels
cars.set_index("Name", inplace=True)

# Access the weight of the car named "Ford Torino"
weight_torino = cars.loc["Ford Torino", "Weight"]

## 6. Dataframe Indexes ##

# Get the Horsepower of cars named "Honda Civic"
honda_civic_hp = cars.loc["Honda Civic", "Horsepower"]

# Print the value of honda_civic_hp
print(honda_civic_hp)

# Delete the index
cars.reset_index(inplace=True)

## 7. Delving Deeper into Loc ##

# Select all rows and numeric columns
numeric_data = cars.loc[:, 'MPG':'Acceleration']

# Print the first five rows of numeric_data
print(numeric_data.head())

## 8. Selecting Columns ##

# Select the Weight column
weights = cars['Weight']

# Select the Name and Origin columns of the first and fourth rows
name_origin_0_and_3 = cars.loc[[0, 3], ['Name', 'Origin']]

## 9. Selecting Rows ##

# Select the 100th row
car_100 = cars.loc[99]

# Select the second through tenth rows
cars_2_to_10 = cars.loc[1:9]

## 10. Index Locations and Label Locations ##

num_rows = cars.shape[0]

one_index = pd.Index([i+1 for i in range(num_rows)])

cars.set_index(one_index, inplace=True)

car_100 = cars.loc[100]
cars_2_to_10 = cars.loc[2:10]