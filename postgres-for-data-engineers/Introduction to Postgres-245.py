## 2. Connecting to Postgres ##

import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname='dq',
    user='dq'
)

# Close the connection
conn.close()

## 3. Interacting with the Database ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")

# Assuming you already have the 'conn' connection object
cur = conn.cursor()

# Execute the query
cur.execute("SELECT * FROM users;")

# Fetch all the results
users = cur.fetchall()

# Close the connection
conn.close()

# Inspect the users variable
print(users)

## 4. Creating a table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
# Assuming you already have the 'conn' connection object
cur = conn.cursor()

# SQL query to create the 'users' table
create_table_query = '''
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        email TEXT,
        name TEXT,
        address TEXT
    );
'''

# Execute the query
cur.execute(create_table_query)

## 5. SQL transactions ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
# Assuming you already have the 'conn' connection object
cur = conn.cursor()

# Execute the query
cur.execute("SELECT * FROM users;")

# Attempt to fetch the results
# The following line will raise an error since the table does not exist
cur.fetchall()

## 6. The Commit Method ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
query_string = """
    CREATE TABLE users(
        id integer PRIMARY KEY, 
        email text,
        name text,
        address text
    );
"""

# Assuming you already have the 'conn' connection object and the query string to create the 'users' table

# Create a cursor object
cur = conn.cursor()

# Execute the query
cur.execute(query_string)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 7. Local State and Commits ##

import psycopg2
conn1 = psycopg2.connect("dbname=dq user=dq")
cur1 = conn1.cursor()
cur1.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", (1, 'alice@dataquest.io', 'Alice', '99 Fake Street'))
conn2 = psycopg2.connect("dbname=dq user=dq")
cur2 = conn2.cursor()
# add your code here

# import psycopg2

# # Create connections
# conn1 = psycopg2.connect("dbname=dq user=dq")
# conn2 = psycopg2.connect("dbname=dq user=dq")

# # Create cursors
# cur1 = conn1.cursor()
# cur2 = conn2.cursor()

# Step 1: Fetch all rows from users table using cur1
cur1.execute("SELECT * FROM users;")
view1_before = cur1.fetchall()

# Step 2: Fetch all rows from users table using cur2
cur2.execute("SELECT * FROM users;")
view2_before = cur2.fetchall()

# Step 3: Commit the changes made by conn1
conn1.commit()

# Step 4: Fetch all rows from users table using cur2 after committing
cur2.execute("SELECT * FROM users;")
view2_after = cur2.fetchall()

# Close the connections
conn1.close()
conn2.close()

# Inspect the values of the variables
print("view1_before:", view1_before)
print("view2_before:", view2_before)
print("view2_after:", view2_after)

## 9. Inserting Data into a Table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")

# Assuming you already have the 'conn' connection object

# Create a cursor object
cur = conn.cursor()

# SQL query to insert a new user into the 'users' table
insert_query = '''
    INSERT INTO users (id, email, name, address)
    VALUES (1, 'example@example.com', 'John Doe', '123 Main St');
'''

# Execute the query
cur.execute(insert_query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 10. Copying the Data ##

import csv
import psycopg2

# Establish a new connection
conn = psycopg2.connect("dbname=dq user=dq")

# Create a cursor object
cur = conn.cursor()

# Open the CSV file
with open('user_accounts.csv', 'r') as csvfile:
    # Create a CSV reader
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    next(csvreader)
    
    # Iterate over each row in the CSV file
    for row in csvreader:
        # Extract the values from the CSV row
        id, email, name, address = row
        
        # SQL query to insert the user into the 'users' table
        insert_query = f"INSERT INTO users (id, email, name, address) VALUES ({id}, '{email}', '{name}', '{address}');"
        
        # Execute the query
        cur.execute(insert_query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()