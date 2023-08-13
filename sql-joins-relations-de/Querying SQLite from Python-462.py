## 3. Connecting to the Database ##

import sqlite3

# Connect to the database
conn = sqlite3.connect('jobs.db')

## 6. Creating a Cursor and Running a Query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])

# SQL Query as a string
query = "SELECT Major FROM recent_grads;"

# Execute the query
cursor.execute(query)

# Fetch the full results set as a list of tuples
majors = cursor.fetchall()

# Display the first three results
print(majors[:3])

## 8. Fetching a Specific Number of Results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# SQL Query as a string
query = "SELECT Major, Major_category FROM recent_grads;"

# Execute the query
cursor.execute(query)

# Fetch the first five results
five_results = cursor.fetchmany(5)

# Display the results
for result in five_results:
    print(result)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")

conn.close()

## 10. Practice ##

import sqlite3

# Connect to the database
conn = sqlite3.connect('jobs2.db')

# Create a cursor object
cursor = conn.cursor()

# Write and execute the query
query = "SELECT Major FROM recent_grads ORDER BY Major DESC"
cursor.execute(query)

# Fetch the full result set
reverse_alphabetical = cursor.fetchall()

# Print the result set
print(reverse_alphabetical)

# Close the connection
conn.close()