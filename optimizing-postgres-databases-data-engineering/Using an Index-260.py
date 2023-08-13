## 1. Alternate Table Scans ##

import psycopg2
import json

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute the EXPLAIN command with JSON format and ANALYZE option
cur.execute("""
    EXPLAIN (FORMAT JSON, ANALYZE)
    SELECT *
    FROM homeless_by_coc
    WHERE id = 10
""")

# Fetch the query plan
query_plan = cur.fetchone()

# Print the query plan with indent=2
print(json.dumps(query_plan, indent=2))

# Close the cursor and connection
cur.close()
conn.close()

## 2. Index Scan ##

import psycopg2
import json

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute the EXPLAIN command with ANALYZE and JSON format on query 1
cur.execute("""
    EXPLAIN (ANALYZE, FORMAT JSON)
    SELECT *
    FROM homeless_by_coc
    WHERE coc_name='Chester County CoC'
    LIMIT 1
""")

# Fetch the query plan for query 1
coc_name_plan = cur.fetchone()

# Print the execution time of query 1
print(coc_name_plan[0][0]["Execution Time"])

# Execute the EXPLAIN command with ANALYZE and JSON format on query 2
cur.execute("""
    EXPLAIN (ANALYZE, FORMAT JSON)
    SELECT *
    FROM homeless_by_coc
    WHERE id=42704
""")

# Fetch the query plan for query 2
id_plan = cur.fetchone()

# Print the execution time of query 2
print(id_plan[0][0]["Execution Time"])

# Close the cursor and connection
cur.close()
conn.close()

## 4. Indexing ##

import psycopg2

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Create an index on the coc_name column of the homeless_by_coc table
cur.execute("CREATE INDEX coc_name_index ON homeless_by_coc (coc_name)")

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

## 5. Comparing the Queries ##

import psycopg2
import json

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute the EXPLAIN (ANALYZE, FORMAT json) command
cur.execute("EXPLAIN (ANALYZE, FORMAT json) SELECT * FROM homeless_by_coc WHERE coc_name = 'Chester County CoC' LIMIT 1")

# Fetch the query plan
coc_name_plan = cur.fetchone()

# Print the execution time
execution_time = coc_name_plan[0][0]["Execution Time"]
print("Execution Time:", execution_time)

# Close the cursor and connection
cur.close()
conn.close()

## 6. The Indexes Table ##

import psycopg2
import json
import psycopg2

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute the query to fetch indexes for the homeless_by_coc table
cur.execute("SELECT * FROM pg_indexes WHERE tablename = 'homeless_by_coc'")

# Fetch all the results
indexes = cur.fetchall()

# Loop over each element in indexes and print it
for index in indexes:
    print(index)

# Close the cursor and connection
cur.close()
conn.close()

## 7. Dropping Indexes ##

import psycopg2
import json

import psycopg2

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Drop the index coc_name_index if it exists
cur.execute("DROP INDEX IF EXISTS coc_name_index")

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

## 8. Index Performance on Joins ##

import psycopg2
import json

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute EXPLAIN command without index
cur.execute("""
    EXPLAIN (ANALYZE, FORMAT json)
    SELECT homeless_by_coc.state, homeless_by_coc.coc_number, homeless_by_coc.coc_name, state_info.name 
    FROM homeless_by_coc, state_info
    WHERE homeless_by_coc.state = state_info.postal;
""")

# Fetch the query plan
no_index_plan = cur.fetchone()

# Print the execution time
print("Execution time without index:", no_index_plan[0][0]["Execution Time"])

# Create index state_index
cur.execute("CREATE INDEX state_index ON homeless_by_coc(state)")

# Execute EXPLAIN command with index
cur.execute("""
    EXPLAIN (ANALYZE, FORMAT json)
    SELECT homeless_by_coc.state, homeless_by_coc.coc_number, homeless_by_coc.coc_name, state_info.name 
    FROM homeless_by_coc, state_info
    WHERE homeless_by_coc.state = state_info.postal;
""")

# Fetch the query plan
index_plan = cur.fetchone()

# Print the execution time
print("Execution time with index:", index_plan[0][0]["Execution Time"])

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

## 9. Understanding Index Performance on Joins ##

import psycopg2
import json

# Connect to the hud database
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud123")

# Get the connection cursor
cur = conn.cursor()

# Execute EXPLAIN command without index
cur.execute("""
    EXPLAIN (ANALYZE, FORMAT json)
    SELECT homeless_by_coc.state, homeless_by_coc.coc_number, homeless_by_coc.coc_name, state_info.name
    FROM homeless_by_coc
    INNER JOIN state_info
    ON homeless_by_coc.state = state_info.postal
    WHERE homeless_by_coc.count > 5000;
""")

# Fetch the query plan
no_index_plan = cur.fetchone()

# Print the execution time
print("Execution time without index:", no_index_plan[0][0]["Execution Time"])

# Create index count_index
cur.execute("CREATE INDEX count_index ON homeless_by_coc(count)")

# Execute EXPLAIN command with index
cur.execute("""
    EXPLAIN (ANALYZE, FORMAT json)
    SELECT homeless_by_coc.state, homeless_by_coc.coc_number, homeless_by_coc.coc_name, state_info.name
    FROM homeless_by_coc
    INNER JOIN state_info
    ON homeless_by_coc.state = state_info.postal
    WHERE homeless_by_coc.count > 5000;
""")

# Fetch the query plan
index_plan = cur.fetchone()

# Print the execution time
print("Execution time with index:", index_plan[0][0]["Execution Time"])

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()