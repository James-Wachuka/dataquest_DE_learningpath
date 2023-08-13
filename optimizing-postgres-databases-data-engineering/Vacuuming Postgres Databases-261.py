## 1. Destructive Queries ##

import psycopg2

import psycopg2

# Connect to the hud database
conn = psycopg2.connect(dbname='hud', user='hud_admin', password='hud123')

# Get the connection cursor
cur = conn.cursor()

# Select every row from the table homeless_by_coc
cur.execute("SELECT * FROM homeless_by_coc")

# Get the number of rows before deletion
num_rows_before = len(cur.fetchall())

# Delete all rows on the homeless_by_coc table
cur.execute("DELETE FROM homeless_by_coc")

# Select again every row from the table homeless_by_coc
cur.execute("SELECT * FROM homeless_by_coc")

# Get the number of rows after deletion
num_rows_after = len(cur.fetchall())

# Print the values of num_rows_before and num_rows_after
print("Number of rows before deletion:", num_rows_before)
print("Number of rows after deletion:", num_rows_after)

# Close the cursor and connection
cur.close()
conn.close()

## 3. Counting Dead Rows ##

import psycopg2

import psycopg2

# Connect to the hud database
conn = psycopg2.connect(dbname='hud', user='hud_admin', password='hud123')

# Get the connection cursor
cur = conn.cursor()

# Select n_dead_tup from pg_stat_all_tables where relname is equal to homeless_by_coc
cur.execute("SELECT n_dead_tup FROM pg_stat_all_tables WHERE relname = 'homeless_by_coc'")

# Assign the result to homeless_dead_rows
homeless_dead_rows = cur.fetchone()[0]

# Print the value of homeless_dead_rows
print("Number of dead rows in homeless_by_coc:", homeless_dead_rows)

# Close the cursor and connection
cur.close()
conn.close()

## 4. Vacuuming Dead Rows ##

import psycopg2
import psycopg2

# Connect to the hud database
conn = psycopg2.connect(dbname='hud', user='hud_admin', password='hud123')

# Set autocommit to True
conn.autocommit = True

# Get the connection cursor
cur = conn.cursor()

# Execute VACUUM VERBOSE on table homeless_by_coc
cur.execute("VACUUM VERBOSE homeless_by_coc")

# Loop over each element in the connection's notices attribute and print it
for notice in conn.notices:
    print(notice)

# Close the cursor and connection
cur.close()
conn.close()

## 5. Transaction IDs ##

import psycopg2

# Connect to the hud database
conn = psycopg2.connect(dbname='hud', user='hud_admin', password='hud123')

# Set autocommit to True
conn.autocommit = True

# Get the connection cursor
cur = conn.cursor()

# Define the row data
row = (1, '2007-01-01', 'AK', 'AK-500', 'Anchorage CoC', 'Chronically Homeless Individuals', 224)

# Insert the row data into the homeless_by_coc table
cur.execute("INSERT INTO homeless_by_coc VALUES (%s, %s, %s, %s, %s, %s, %s)", row)

# Execute VACUUM VERBOSE on table homeless_by_coc
cur.execute("VACUUM VERBOSE homeless_by_coc")

# Loop over each element in the connection's notices attribute and print it
for notice in conn.notices:
    print(notice)

# Select the xmin column from the homeless_by_coc table
cur.execute("SELECT xmin FROM homeless_by_coc")

# Fetch the result of xmin
xmin = cur.fetchone()

# Print the value of xmin
print(xmin[0])



# Close the cursor and connection
cur.close()
conn.close()

## 6. Updating Statistics ##

import json
import psycopg2

# Connect to the hud database
conn = psycopg2.connect(dbname='hud', user='hud_admin', password='hud123')
conn.autocommit = True

# Create a cursor
cur = conn.cursor()

# Execute EXPLAIN command on the query
cur.execute("EXPLAIN SELECT * FROM homeless_by_coc")
plan_before = cur.fetchall()

# Execute VACUUM ANALYZE on table homeless_by_coc
cur.execute("VACUUM ANALYZE homeless_by_coc")

# Execute EXPLAIN command on the query again
cur.execute("EXPLAIN SELECT * FROM homeless_by_coc")
plan_after = cur.fetchall()

# Print the query plans
print("Plan before VACUUM ANALYZE:")
print(plan_before)
print("Plan after VACUUM ANALYZE:")
print(plan_after)

# Close the cursor and the connection
cur.close()
conn.close()

## 7. Full Vacuum ##

import psycopg2

# Connect to the hud database
conn = psycopg2.connect(dbname='hud', user='hud_admin', password='hud123')
conn.autocommit = True

# Create a cursor
cur = conn.cursor()

# Select all rows from the homeless_by_coc table and print the results
cur.execute("SELECT * FROM homeless_by_coc")
results = cur.fetchall()
print("Data before: ")
for row in results:
    print(row)

# Execute pg_total_relation_size on the homeless_by_coc table before vacuum
cur.execute("SELECT pg_size_pretty(pg_total_relation_size('homeless_by_coc'))")
space_before = cur.fetchone()

# Execute full vacuum on the homeless_by_coc table
cur.execute("VACUUM FULL homeless_by_coc")

# Execute pg_total_relation_size on the homeless_by_coc table after vacuum
cur.execute("SELECT pg_size_pretty(pg_total_relation_size('homeless_by_coc'))")
space_after = cur.fetchone()

# Print the values of space_before and space_after
print("Space before: ", space_before[0])
print("Space after: ", space_after[0])

# Close the cursor and the connection
cur.close()
conn.close()

## 8. Autovacuum ##

import psycopg2
import time

# Connect to the hud database
conn = psycopg2.connect(dbname='hud', user='hud_admin', password='hud123')
conn.autocommit = True

# Create a cursor
cur = conn.cursor()

# Vacuum the homeless_by_coc table
cur.execute("VACUUM homeless_by_coc")

# Wait for one second
time.sleep(1)

# Select last_vacuum and last_autovacuum from pg_stat_user_tables
cur.execute("SELECT last_vacuum, last_autovacuum FROM pg_stat_user_tables WHERE relname = 'homeless_by_coc'")
timestamps = cur.fetchone()

# Print the value of timestamps
print("Last Vacuum: ", timestamps[0])
print("Last Autovacuum: ", timestamps[1])

# Close the cursor and the connection
cur.close()
conn.close()