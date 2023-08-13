## 2. Estimating Memory Consumption ##

import pandas as pd


# Read the moma.csv file into a dataframe
moma = pd.read_csv('moma.csv')

# Display the memory usage of the moma dataframe
moma.info()

## 3. How Pandas Represents Values in a Dataframe ##

print(moma._data)

## 5. Estimating The Memory Manually ##

# Get the total number of values in the dataframe
num_entries = moma.size

# Calculate the total number of bytes
total_bytes = num_entries * 8

# Convert total_bytes to megabytes
total_megabytes = total_bytes / (2**20)

# Display total_megabytes
print(total_megabytes)

## 7. Memory Footprint of Non-numerical Data ##

# Select object columns from the moma dataframe
obj_cols = moma.select_dtypes(include='object')

# Calculate the memory usage of each column in obj_cols
obj_cols_mem = obj_cols.memory_usage(deep=True)

# Sum the memory usage values and convert to megabytes
obj_cols_sum = obj_cols_mem.sum() / (2**20)

# Print the value of obj_cols_sum
print(obj_cols_sum)

## 9. Optimizing Integer Columns With Subtypes ##

import numpy as np

def change_to_int(df, col_name):
    # Get the minimum and maximum values
    col_max = df[col_name].max()
    col_min = df[col_name].min()
    
    # Find the datatype
    for dtype_name in ['int8', 'int16', 'int32', 'int64']:
        # Check if this datatype can hold all values
        if col_max <  np.iinfo(dtype_name).max and col_min > np.iinfo(dtype_name).min:
            df[col_name] = df[col_name].astype(dtype_name)
            break

# Select numerical columns of moma with float64 dtype
float_moma = moma.select_dtypes(include=['float64'])

# Print the count of missing values for each column
print(float_moma.isnull().sum())

# Identify the column with no missing values
column_no_missing = 'ExhibitionSortOrder'  # Replace 'column_name' with the actual column name

# Convert the identified column to the smallest integer datatype
change_to_int(moma, column_no_missing)

# Print the datatype of the converted column
print(moma[column_no_missing].dtype)

# float_moma.isnull().sum()

## 10. Optimizing Float Columns With Subtypes ##

# float_cols = moma.select_dtypes(include=['float']).columns

# Write you code below


float_cols = moma.select_dtypes(include=['float']).columns

for col in float_cols:
    moma[col] = pd.to_numeric(moma[col], downcast='float')

## 12. Converting To DateTime ##

# Convert ExhibitionBeginDate and ExhibitionEndDate columns to datetime type
moma['ExhibitionBeginDate'] = pd.to_datetime(moma['ExhibitionBeginDate'])
moma['ExhibitionEndDate'] = pd.to_datetime(moma['ExhibitionEndDate'])

# Display memory usage for the converted columns
print(moma['ExhibitionBeginDate'].memory_usage())
print(moma['ExhibitionEndDate'].memory_usage())

## 14. Converting to Categorical to Save Memory ##

# Identify object columns with less than half of unique values
object_cols = moma.select_dtypes(include=['object']).columns
for col in object_cols:
    if moma[col].nunique() < len(moma[col]) / 2:
        moma[col] = moma[col].astype('category')

# Print the deep memory footprint using DataFrame.info()
moma.info(memory_usage='deep')

## 15. Selecting Types While Reading the Data In ##

keep_cols = ['ExhibitionID', 'ExhibitionNumber', 'ExhibitionBeginDate', 'ExhibitionEndDate', 'ExhibitionSortOrder', 'ExhibitionRole', 'ConstituentType', 'DisplayName', 'Institution', 'Nationality', 'Gender']

import pandas as pd

# keep_cols = ['ExhibitionID', 'ExhibitionNumber', 'ExhibitionBeginDate', 'ExhibitionEndDate', 'ExhibitionSortOrder', 'ExhibitionRole', 'ConstituentType', 'DisplayName', 'Institution', 'Nationality', 'Gender']

moma = pd.read_csv("moma.csv", usecols=keep_cols, parse_dates=['ExhibitionBeginDate', 'ExhibitionEndDate'])

# Display the deep memory footprint in megabytes
print(moma.info(memory_usage='deep'))