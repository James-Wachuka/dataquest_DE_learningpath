## 2. Processing Chunks ##

import pandas as pd
import matplotlib.pyplot as plt

memory_footprints = []

# import pandas as pd
# import matplotlib.pyplot as plt

# Define chunk size
chunk_size = 250

# Create an iterator object to read chunks from "moma.csv"
moma_iterator = pd.read_csv("moma.csv", chunksize=chunk_size)

# List to store memory footprints
memory_footprints = []

# Iterate over the chunks
for chunk in moma_iterator:
    # Calculate memory footprint and append to list
    memory_footprint = chunk.memory_usage(deep=True).sum() / (1024 * 1024)  # Convert to megabytes
    memory_footprints.append(memory_footprint)

# Generate and display histogram
plt.hist(memory_footprints)
plt.xlabel("Memory Footprint (MB)")
plt.ylabel("Frequency")
plt.title("Histogram of Memory Footprints")
plt.show()

## 3. Counting Across Chunks ##

# num_rows = 0
import pandas as pd

# Define chunk size
chunk_size = 250

# Create an iterator object to read chunks from "moma.csv"
moma_iterator = pd.read_csv("moma.csv", chunksize=chunk_size)

# Variable to store the total number of rows
num_rows = 0

# Iterate over the chunks
for chunk in moma_iterator:
    # Retrieve the number of rows for the current chunk and add it to num_rows
    num_rows += len(chunk)

# Display the total number of rows
print(num_rows)

## 4. Batch Processing ##

import pandas as pd

# Define chunk size
chunk_size = 250

# Create an iterator object to read chunks from "moma.csv"
moma_iterator = pd.read_csv("moma.csv", chunksize=chunk_size)

# List to store series objects representing lifespans
lifespans = []

# Iterate over the chunks
for chunk in moma_iterator:
    # Calculate the lifespans for the current chunk
    chunk_lifespans = chunk["ConstituentEndDate"] - chunk["ConstituentBeginDate"]
    # Add the series object to the lifespans list
    lifespans.append(chunk_lifespans)

# Concatenate the series objects in lifespans into a single series
lifespans_dist = pd.concat(lifespans)

# Display the resulting series object
print(lifespans_dist)

## 6. Counting Unique Values ##

chunk_iter = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])


import pandas as pd

# Define chunk size
chunk_size = 250

# Create an iterator object to read chunks from "moma.csv"
moma_iterator = pd.read_csv("moma.csv", chunksize=chunk_size)

# List to store series objects representing unique value counts
overall_vc = []

# Iterate over the chunks
for chunk in moma_iterator:
    # Calculate unique value counts for the "Gender" column in the current chunk
    chunk_vc = chunk["Gender"].value_counts()
    # Append the resulting series object to the overall_vc list
    overall_vc.append(chunk_vc)

# Concatenate the series objects in overall_vc into a single series
combined_vc = pd.concat(overall_vc)

# Display the combined series object
print(combined_vc)

## 7. Combining Chunks Using GroupBy ##

import pandas as pd

# Create an iterator object to read chunks from "moma.csv"
chunk_iter = pd.read_csv("moma.csv", chunksize=250, usecols=['Gender'])

# List to store series objects representing unique value counts
overall_vc = []

# Iterate over the chunks
for chunk in chunk_iter:
    # Calculate unique value counts for the "Gender" column in the current chunk
    chunk_vc = chunk['Gender'].value_counts()
    # Append the resulting series object to the overall_vc list
    overall_vc.append(chunk_vc)

# Concatenate the series objects in overall_vc into a single series
combined_vc = pd.concat(overall_vc)

# Aggregate the values in combined_vc by the unique index values
final_vc = combined_vc.groupby(combined_vc.index).sum()

# Display the final series object
print(final_vc)

## 8. Working With Intermediate Dataframes ##

import pandas as pd

# Create an iterator object to read chunks from "moma.csv"
chunk_iter = pd.read_csv("moma.csv", chunksize=1000, usecols=["ExhibitionID", "Gender"])

# List to store intermediate series objects
intermediate_series = []

# Iterate over the chunks
for chunk in chunk_iter:
    # Group each unique value in the "Gender" column by each unique value in the "ExhibitionID" column
    grouped = chunk["Gender"].groupby(chunk["ExhibitionID"]).value_counts()
    # Append the resulting series object to the intermediate_series list
    intermediate_series.append(grouped)

# Combine the intermediate series objects into a single series object
combined_series = pd.concat(intermediate_series)

# Sum the gender counts for each unique index value
id_gender_counts = combined_series.groupby(level=[0, 1]).sum()

# Display the final series object
print(id_gender_counts)