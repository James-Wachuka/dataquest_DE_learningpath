## 1. The EXPLAIN Query ##

import psycopg2
import psycopg2

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute the EXPLAIN command for SELECT on the homeless_by_coc table
cur.execute("EXPLAIN SELECT * FROM homeless_by_coc")

# Fetch all rows from the cursor
output = cur.fetchall()

# Print the output
for row in output:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()

## 2. The Path of a Query ##

import psycopg2
import psycopg2

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute the EXPLAIN command on the query
cur.execute("EXPLAIN SELECT COUNT(*) FROM homeless_by_coc WHERE year > '2012-01-01'")

# Fetch all rows from the cursor
query_plan = cur.fetchall()

# Loop over the rows and print the first element of each row
for row in query_plan:
    print(row[0])

# Close the cursor and connection
cur.close()
conn.close()

## 3. Additional Output Formats ##

import psycopg2
import psycopg2
import json

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute the EXPLAIN command with JSON format option on the query
cur.execute("EXPLAIN (FORMAT JSON) SELECT COUNT(*) FROM homeless_by_coc WHERE year > '2012-01-01'")

# Fetch the query result
query_plan = cur.fetchone()

# Print the query_plan using json.dumps()
print(json.dumps(query_plan, indent=2))

# Close the cursor and connection
cur.close()
conn.close()

## 4. Understanding Cost Estimations ##

import psycopg2

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Select reltuples and relpages from pg_class for the homeless_by_coc table
cur.execute("SELECT reltuples, relpages FROM pg_class WHERE relname = 'homeless_by_coc'")

# Fetch the result
result = cur.fetchone()
n_tuple, n_page = result

# Default values for the cost formula
cpu_tuple_cost = 0.01
cpu_operator_cost = 0.0025
seq_page_cost = 1.0

# Compute the estimated cost using the formula
total_cost = (cpu_tuple_cost + cpu_operator_cost) * n_tuple + seq_page_cost * n_page

# Print the total cost
print(total_cost)

# Close the cursor and connection
cur.close()
conn.close()

## 5. Obtaining Exact Runtimes ##

import psycopg2
import json

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute the EXPLAIN command with JSON format and ANALYZE option
cur.execute("EXPLAIN (FORMAT JSON, ANALYZE) SELECT COUNT(*) FROM homeless_by_coc WHERE year > '2012-01-01'::date")

# Fetch the query plan
query_plan = tuple(cur.fetchone())  # Convert list into a tuple

# Print the query plan with indent=2
print(json.dumps(query_plan, indent=2))

# Close the cursor and connection
cur.close()
conn.close()

## 6. Test and Rollback ##

import psycopg2
import json

import psycopg2
import json

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute the EXPLAIN command with JSON format and ANALYZE option
cur.execute("EXPLAIN (FORMAT JSON, ANALYZE) DELETE FROM state_household_incomes")

# Fetch the query plan
query_plan = cur.fetchone()

# Rollback the transaction
conn.rollback()

# Print the query plan with indent=2
print(json.dumps(query_plan, indent=2))

# Close the cursor and connection
cur.close()
conn.close()

## 7. Analyzing a Join Statement ##

import psycopg2
import json

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute the EXPLAIN command with JSON format and ANALYZE option
cur.execute("""
    EXPLAIN (FORMAT JSON, ANALYZE)
    SELECT homeless_by_coc.state, homeless_by_coc.coc_number, homeless_by_coc.coc_name, state_info.name
    FROM homeless_by_coc
    INNER JOIN state_info ON homeless_by_coc.state = state_info.postal
""")

# Fetch the query plan
query_plan = cur.fetchone()

# Print the query plan with indent=2
print(json.dumps(query_plan, indent=2))

# Close the cursor and connection
cur.close()
conn.close()