## 1. Execute Method Placeholders ##

import psycopg2

# Define the dictionary of row values
row_values = {
    'identifier': 1,
    'mail': 'adam.smith@dataquest.io',
    'name': 'Adam Smith',
    'address': '42 Fake Street'
}

# Connect to the database
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Execute the query to insert a user into the users table using the values in row_values
cur.execute("""
    INSERT INTO users (id, email, name, address)
    VALUES (%(identifier)s, %(mail)s, %(name)s, %(address)s);
""", row_values)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 2. SQL Injections ##

import psycopg2
def get_email(name):
    import psycopg2
    conn = psycopg2.connect("dbname=dq user=dq")
    cur = conn.cursor()
    query_string = "SELECT email FROM users WHERE name = '" + name + "';"
    cur.execute(query_string)
    res = cur.fetchall()
    conn.close()
    return res

# Get the email address of all users in the database
all_emails = get_email("'; SELECT email FROM users WHERE '1' = '1")

print(all_emails)

## 3. Getting the Address ##

def get_email_and_address(name):
    import psycopg2
    conn = psycopg2.connect("dbname=dq user=dq")
    cur = conn.cursor()
    query_string = "SELECT email, address FROM users WHERE name = %s;"
    cur.execute(query_string, (name,))
    res = cur.fetchall()
    conn.close()
    return [(email,) for email, _ in res] + [(address,) for _, address in res]

name = "Larry Cain"
email_and_address = get_email_and_address(name)
print(email_and_address)

## 4. Avoiding SQL Injections ##

def get_email_fixed(name):
    import psycopg2
    conn = psycopg2.connect("dbname=dq user=dq")
    cur = conn.cursor()
    query_string = "SELECT email FROM users WHERE name = %s;"
    cur.execute(query_string, (name,))
    res = cur.fetchall()
    conn.close()
    return res

# Example usage:
name = "Joseph Kirby"
email = get_email_fixed(name)
print(email)

## 5. Prepared Statements ##

import psycopg2
user = (10003, 'alice@dataquest.io', 'Alice', '102, Fake Street')



# Connect to the database
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Prepare the insert_user statement
insert_user = """
    INSERT INTO users (id, email, name, address)
    VALUES (%s, %s, %s, %s)
"""

# Execute the insert_user statement with user data

cur.execute(insert_user, user)

# Commit the changes (if necessary)
conn.commit()

## 6. Prepared Statements Table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Prepare the get_email statement
cur.execute("PREPARE get_email AS SELECT email FROM users WHERE name = $1;")

# Execute the get_email query for a user named Anna Carter
cur.execute("EXECUTE get_email('Anna Carter');")

# Fetch the result
anna_email = cur.fetchone()

# Execute a query to select all rows from the pg_prepared_statements table
cur.execute("SELECT * FROM pg_prepared_statements;")

# Print all rows in the table
print(cur.fetchall())

## 7. Runtime Gain ##

import timeit
import psycopg2
import csv

# function that inserts all users using a prepared statement
def prepared_insert():
    conn = psycopg2.connect("dbname=dq user=dq")
    cur = conn.cursor()           
    cur.execute("""
        PREPARE insert_user(integer, text, text, text) AS
        INSERT INTO users VALUES ($1, $2, $3, $4)
    """)
    for user in users:
        cur.execute("EXECUTE insert_user(%s, %s, %s, %s)", user)
    conn.close()

# function that insert all users using a new INSERT query for each user
def regular_insert():
    conn = psycopg2.connect("dbname=dq user=dq")
    cur = conn.cursor()           
    for user in users:
        cur.execute("""
            INSERT INTO users VALUES (%s, %s, %s, %s)
        """, user)
    conn.close()

# read the users into a list
users = []
with open('user_accounts.csv', 'r') as file:
    next(file) # skip csv header
    reader = csv.reader(file)
    for row in reader:
        users.append(row)

# Time the prepared_insert function
time_prepared = timeit.timeit(prepared_insert, number=1)

# Time the regular_insert function
time_regular = timeit.timeit(regular_insert, number=1)

# Print the runtimes
print("Time for prepared_insert:", time_prepared)
print("Time for regular_insert:", time_regular)