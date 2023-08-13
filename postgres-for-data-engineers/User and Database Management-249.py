## 1. Connection String ##

import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname='dq',
    user='postgres',
    password='abc123'
)

# Print the connection object
print(conn)

## 2. Creating a User ##

import psycopg2
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname='dq',
    user='postgres',
    password='abc123'
)

# Create a cursor object
cur = conn.cursor()

# Create the data_viewer user
cur.execute("CREATE USER data_viewer WITH SUPERUSER PASSWORD 'secret'")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 3. The Users Table ##

import psycopg2
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname='dq',
    user='postgres',
    password='abc123'
)

# Create a cursor object
cur = conn.cursor()

# Select all rows from the pg_user table
cur.execute("SELECT * FROM pg_user")

# Fetch all rows
users = cur.fetchall()

# Print each row
for row in users:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()

## 4. User Privileges ##

import psycopg2
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname='dq',
    user='postgres',
    password='abc123'
)

# Create a cursor object
cur = conn.cursor()

# Revoke all privileges from user data_viewer on the users table
cur.execute("REVOKE ALL PRIVILEGES ON users FROM data_viewer")

# Grant SELECT privileges to user data_viewer on the users table
cur.execute("GRANT SELECT ON users TO data_viewer")

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

## 5. Checking User Privileges ##

import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname='dq',
    user='postgres',
    password='abc123'
)

# Create a cursor object
cur = conn.cursor()

# Select grantor, grantee, and privilege_type from table_privileges
cur.execute("""
    SELECT grantor, grantee, privilege_type
    FROM information_schema.table_privileges
    WHERE table_name = 'users'
""")

# Fetch all the results
privileges = cur.fetchall()

# Print the results
for row in privileges:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()

## 6. Privileges and Superusers ##

import psycopg2
conn = psycopg2.connect(dbname="dq", user="data_viewer", password="secret")
cur = conn.cursor()
cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", 
            (10002, 'alice@dataquest.io', 'Alice', '100, Fake St'))
cur.execute("SELECT * FROM users;")
print(cur.fetchall()[-1])
# add code below here


import psycopg2

# Connect to the database as the superuser
conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")
cur = conn.cursor()

# Alter the data_viewer user to make it a non-superuser
cur.execute("ALTER USER data_viewer WITH NOSUPERUSER;")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

# Connect to the database as the data_viewer user
conn = psycopg2.connect(dbname="dq", user="data_viewer", password="secret")
cur = conn.cursor()

# Execute the INSERT statement (should raise an error)
cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", 
            (10002, 'alice@dataquest.io', 'Alice', '100, Fake St'))

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 7. Postgres Groups ##

import psycopg2
import psycopg2

# Connect to the database as the superuser
conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")
cur = conn.cursor()

# Create the readonly group
cur.execute("CREATE GROUP readonly NOLOGIN;")

# Revoke all privileges on the users table from the readonly group
cur.execute("REVOKE ALL PRIVILEGES ON TABLE users FROM readonly;")

# Grant SELECT privileges on the users table to the readonly group
cur.execute("GRANT SELECT ON TABLE users TO readonly;")

# Assign user data_viewer to the readonly group
cur.execute("GRANT readonly TO data_viewer;")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 8. Creating a Read-Write Group ##

import psycopg2

# Connect to the database as the postgres user
conn = psycopg2.connect(dbname="dq", user="postgres", password="abc123")
cur = conn.cursor()

# Create the readwrite group with NOLOGIN option
cur.execute("CREATE GROUP readwrite NOLOGIN;")

# Revoke all privileges of the readwrite group on the users table
cur.execute("REVOKE ALL PRIVILEGES ON TABLE users FROM readwrite;")

# Grant SELECT, INSERT, DELETE, and UPDATE privileges to the readwrite group on the users table
cur.execute("GRANT SELECT, INSERT, DELETE, UPDATE ON TABLE users TO readwrite;")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 9. Creating a Database ##

import psycopg2

# Connect to the dq database as the dq user
conn = psycopg2.connect(dbname="dq", user="dq")

# Set the autocommit attribute to True
conn.autocommit = True

# Create the my_database database with postgres as the owner
cur = conn.cursor()
cur.execute("CREATE DATABASE my_database OWNER postgres;")

# Set the autocommit attribute back to False
conn.autocommit = False

# Do not close the connection

## 10. Managing Connection Rights ##

import psycopg2

# Connect to the my_database database as the postgres user with password abc123
conn = psycopg2.connect(dbname="my_database", user="postgres", password="abc123")

# Revoke all privileges from the public group
cur = conn.cursor()
cur.execute("REVOKE ALL PRIVILEGES ON DATABASE my_database FROM PUBLIC;")

# Revoke connection privileges from the readonly group
cur.execute("REVOKE CONNECT ON DATABASE my_database FROM readonly;")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 11. Creating Schemas ##

import psycopg2

# Connect to the my_database database as the postgres user with password abc123
conn = psycopg2.connect(dbname="my_database", user="postgres", password="abc123")

# Create a schema named my_schema
cur = conn.cursor()
cur.execute("CREATE SCHEMA my_schema;")

# Commit the changes
conn.commit()

# Close the connection
conn.close()