## 1. Introduction ##

import psycopg2

# Connect to the hud database
conn = psycopg2.connect(dbname="hud", user="hud_admin", password="hud_pwd")

# Close the connection
conn.close()

## 2. Investigating the Tables ##

import psycopg2
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
cur = conn.cursor()


# Perform SELECT query on pg_tables
query = "SELECT tablename FROM pg_catalog.pg_tables ORDER BY tablename"
cur.execute(query)

# Fetch all results
table_names = cur.fetchall()

# Print the number of tables
print("Number of tables:", len(table_names))

# Loop through table_names and print each table name
for table_name in table_names:
    print(table_name[0])

## 3. Working with Schemas ##

import psycopg2
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
cur = conn.cursor()
#cur.execute("""
#    SELECT tablename FROM information_schema.tables 
#    ORDER BY tablename;
#""")
# Perform SELECT query on pg_tables with filters and ordering
query = "SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname NOT IN ('pg_catalog', 'information_schema') ORDER BY tablename"
cur.execute(query)

# Fetch all results
table_names = cur.fetchall()

# Print the number of tables
print("Number of tables:", len(table_names))

# Loop through table_names and print each table name
for table_name in table_names:
    print(table_name[0])

## 4. Describing the Tables ##

import psycopg2
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
cur = conn.cursor()

import psycopg2
from psycopg2.extensions import AsIs

# conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
# cur = conn.cursor()
table_names = ['homeless_by_coc','state_info','state_household_incomes']  # List of table names in the public schema

col_descriptions = {}  # Empty dictionary to store column descriptions

for table_name in table_names:
    cur.execute(f"SELECT * FROM {AsIs(table_name)} LIMIT 0")
    col_descriptions[table_name] = cur.description

cur.close()
conn.close()

## 5. Type Code Mappings ##

import psycopg2
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
cur = conn.cursor()

type_mappings = {}  # Empty dictionary to store type mappings

# Execute query to fetch oid and typname columns from pg_catalog.pg_type
cur.execute("SELECT oid, typname FROM pg_catalog.pg_type")

# Fetch all results from the query
results = cur.fetchall()

# Populate the dictionary with type mappings
for oid, typname in results:
    type_mappings[oid] = typname

# Print the type name corresponding to the date column (type code 1082)
date_type_name = type_mappings.get(1082)
print(date_type_name)

## 6. Readable Description Types ##

# variables: table_names, type_mappings and col_descriptions from the previous screens are available

readable_description = {}

for table_name in table_names:
    table_description = []
    columns = col_descriptions[table_name]

    for column in columns:
        column_description = {
            'name': column.name,
            'type': type_mappings[column.type_code],
            'internal_size': column.internal_size
        }
        table_description.append(column_description)

    readable_description[table_name] = {'columns': table_description}

## 7. Number of Rows ##

import psycopg2
from psycopg2.extensions import AsIs
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
cur = conn.cursor()
# variables: table_names and readable_description from the previous screens are available

# import psycopg2
# from psycopg2.extensions import AsIs

# conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
# cur = conn.cursor()

for table_name in readable_description.keys():
    cur.execute(f"SELECT COUNT(*) FROM {AsIs(table_name)}")
    number_of_rows = cur.fetchone()[0]
    readable_description[table_name]['number_of_rows'] = number_of_rows

print(readable_description)

## 8. The JSON Format ##

# the variable readable_description is available for you
import json

# Print the readable_description dictionary with different indent values
print(json.dumps(readable_description, indent=None))  # No indentation
print(json.dumps(readable_description, indent=2))     # Indent with 2 spaces
print(json.dumps(readable_description, indent=4))     # Indent with 4 spaces