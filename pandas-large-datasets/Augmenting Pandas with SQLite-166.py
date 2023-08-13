## 1. Augmenting Pandas with SQLite ##

import sqlite3
import pandas as pd
# import sqlite3
# import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('moma.db')

# Create an iterator to process chunks of 1000 rows from moma.csv
moma_iter = pd.read_csv('moma.csv', chunksize=1000)

# Iterate over the chunks and append them to the "exhibitions" table
for chunk in moma_iter:
    chunk.to_sql('exhibitions', conn, if_exists='append', index=False)

# Close the database connection
conn.close()

## 2. Pandas Types vs. SQLite Types ##

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('moma.db')

# Query the column types for the exhibitions table
query = "PRAGMA table_info(exhibitions)"
results_df = pd.read_sql(query, conn)

# Close the database connection
conn.close()

# Display the results
print(results_df)

## 3. Setting Appropriate Types ##

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('moma.db')

# Create an iterator using pandas.read_csv() to process chunks of 1000 rows from moma.csv
moma_iter = pd.read_csv('moma.csv', chunksize=1000)

# Iterate over the dataframe chunks
for chunk in moma_iter:
    # Convert the ExhibitionSortOrder column to int16
    chunk['ExhibitionSortOrder'] = chunk['ExhibitionSortOrder'].astype('int16')
    
    # Append each dataframe chunk to the exhibitions table in moma.db
    chunk.to_sql('exhibitions', conn, if_exists='append', index=False)

# Query the column types for the exhibitions table
query = "PRAGMA table_info(exhibitions)"
results_df = pd.read_sql(query, conn)

# Close the database connection
conn.close()

# Display the results
print(results_df)

## 4. Computing Primarily in SQL ##

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('moma.db')

# Query the ExhibitionID column and its counts
query = "SELECT ExhibitionID, COUNT(*) AS counts FROM exhibitions GROUP BY ExhibitionID ORDER BY counts DESC"
eid_counts = pd.read_sql(query, conn)

# Display the first 10 rows of the dataframe
print(eid_counts.head(10))

## 5. Computing Primarily in Pandas ##

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('moma.db')

# Query the ExhibitionID column from the exhibitions table
query = "SELECT ExhibitionID FROM exhibitions"
exhibition_id_df = pd.read_sql(query, conn)

# Calculate the unique value counts using pandas
eid_pandas_counts = exhibition_id_df['ExhibitionID'].value_counts()

# Display the first 10 rows of the value counts
print(eid_pandas_counts.head(10))