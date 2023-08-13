## 1. Querying with Multiple Filters ##

import json
import psycopg2
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
cur = conn.cursor()


import psycopg2
import json

# Assume conn and cur are already created

# Create index state_index
cur.execute("CREATE INDEX state_index ON homeless_by_coc(state)")

# Commit the changes
conn.commit()

# Execute EXPLAIN command with JSON format
cur.execute("""
    EXPLAIN (FORMAT json)
    SELECT *
    FROM homeless_by_coc
    WHERE state = 'CA' AND year < '2008-01-01';
""")

# Fetch the query plan
query_plan = cur.fetchone()

# Print the query plan in JSON format
print(json.dumps(query_plan, indent=2))

# Close the cursor and connection
cur.close()
conn.close()

## 3. Multi-Column Indexes ##

import psycopg2
import json
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
cur = conn.cursor()

import psycopg2
import json

# Assume conn and cur are already created

# Execute EXPLAIN command with ANALYZE and JSON format on the query
cur.execute("""
    EXPLAIN (ANALYZE, FORMAT json)
    SELECT *
    FROM homeless_by_coc
    WHERE state = 'CA' AND year < '2008-01-01';
""")

# Fetch the query plan with execution time for single-column index
plan_single_index = cur.fetchone()

# Print the execution time for single-column index plan
print(plan_single_index[0][0]["Execution Time"])

# Create multi-column index state_year_index
cur.execute("CREATE INDEX state_year_index ON homeless_by_coc(state, year)")

# Commit the changes
conn.commit()

# Execute EXPLAIN command with ANALYZE and JSON format on the query again
cur.execute("""
    EXPLAIN (ANALYZE, FORMAT json)
    SELECT *
    FROM homeless_by_coc
    WHERE state = 'CA' AND year < '2008-01-01';
""")

# Fetch the query plan with execution time for multi-column index
plan_multi_index = cur.fetchone()

# Print the execution time for multi-column index plan
print(plan_multi_index[0][0]["Execution Time"])

# Close the cursor and connection
cur.close()
conn.close()

## 5. Index on More Than Two Columns ##

import psycopg2
import json
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
cur = conn.cursor()
import psycopg2
import json

# Assume conn and cur are already created

# Create multi-column index state_count_year_index
cur.execute("CREATE INDEX state_count_year_index ON homeless_by_coc(state, count, year)")

# Commit the changes
conn.commit()

# Execute EXPLAIN command with ANALYZE and JSON format on the query
cur.execute("""
    EXPLAIN (ANALYZE, FORMAT json)
    SELECT *
    FROM homeless_by_coc
    WHERE year > '2011-01-01' AND count > 5000;
""")

# Fetch the query plan
query_plan = cur.fetchone()

# Print the query plan
print(json.dumps(query_plan, indent=2))

# Close the cursor and connection
cur.close()
conn.close()

## 6. Index on Expressions ##

import psycopg2
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
cur = conn.cursor()

import psycopg2

# Assume conn and cur are already created

# Create case-insensitive expression index measures_index
cur.execute("CREATE INDEX measures_index ON homeless_by_coc (LOWER(measures))")

# Commit the changes
conn.commit()

# Execute SELECT query with filter on LOWER(measures)
cur.execute("SELECT * FROM homeless_by_coc WHERE LOWER(measures) = 'total homeless'")

# Fetch all rows and assign the results to total_homeless variable
total_homeless = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()

## 7. Partial Indexes ##

import psycopg2
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
cur = conn.cursor()

import psycopg2

# Assume conn and cur are already created

# Create partial expression index partial_state_index
cur.execute("CREATE INDEX partial_state_index ON homeless_by_coc (state) WHERE count = 0")

# Commit the changes
conn.commit()

# Execute SELECT query with filter on state = 'CA' and count = 0
cur.execute("SELECT * FROM homeless_by_coc WHERE state = 'CA' AND count = 0")

# Fetch all rows and assign the results to ca_zero_count variable
ca_zero_count = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()

## 8. Building a Multi-Column Index ##

import psycopg2
conn = psycopg2.connect("dbname=hud user=hud_admin password=hud_pwd")
cur = conn.cursor()



import psycopg2
import json

# Assume conn and cur are already created

state = "AK"  # Replace with the actual state value
measures = "Homeless"  # Replace with the actual measures value

# Create the multi-column index on state, count, and LOWER(measures)
cur.execute("""
    CREATE INDEX state_count_measures_index
    ON homeless_by_coc (state, count, LOWER(measures));
""")

# Commit the changes
conn.commit()

# Execute the EXPLAIN command with JSON format on the query
cur.execute("""
    EXPLAIN (ANALYZE, FORMAT json)
    SELECT hbc.year, si.name, hbc.count
    FROM homeless_by_coc AS hbc
    INNER JOIN state_info AS si
    ON hbc.state = si.postal
    WHERE hbc.state = %s AND LOWER(hbc.measures) = %s AND hbc.count = 0;
""", (state, measures))

# Fetch the query plan
query_plan = cur.fetchone()

# Print the query plan with indent=2
print(json.dumps(query_plan, indent=2))

# Close the cursor and connection
cur.close()
conn.close()