## 1. The Mogrify Method ##

from datetime import date
import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

game_data = (
    52499790661213,
    'Amazing',
    'LittleBigPlanet PS Vita',
    '/games/littlebigplanet-vita/vita-98907',
    'PlayStation Vita',
    9.0,
    'Platformer',
    'y',
    date(2012, 12, 9)
)

mogrified_values = cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", game_data)

print(mogrified_values)

## 2. The Connection Encoding ##

from datetime import date
import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

game_data = (
    52499790661213,
    'Amazing',
    'LittleBigPlanet PS Vita',
    '/games/littlebigplanet-vita/vita-98907',
    'PlayStation Vita',
    9.0,
    'Platformer',
    'y',
    date(2012, 12, 9)
)

conn_encoding = conn.encoding

mogrified_values = cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", game_data)
mogrified_values_decoded = mogrified_values.decode(conn_encoding)

print(conn_encoding)
print(mogrified_values_decoded)

## 3. Inserting with Mogrify ##

import csv
import psycopg2

# Connect to the database
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Load the ign.csv into a list of lists
rows = []
with open('ign.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    rows = list(reader)

# Mogrify each row of the list
mogrified_rows = [cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", row) for row in rows]

# Create the insert string for inserting all rows
insert_string = b"INSERT INTO ign_reviews VALUES " + b",".join(mogrified_rows)

# Execute the insert string with the cursor
cur.execute(insert_string)

# Commit changes and close the connection
conn.commit()
conn.close()

## 4. Postgres Copy Method ##

import psycopg2

# Connect to the database
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Load the ign.csv file into the ign_reviews table
with open('ign.csv', 'r') as file:
    next(file)  # Skip the header row
    cur.copy_from(file, 'ign_reviews', sep=',')

# Commit changes and close the connection
conn.commit()
conn.close()

## 5. The COPY Statement ##

import psycopg2
import csv

# Connect to the database
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Load the ign.csv file into the ign_reviews table
copy_statement = """
COPY ign_reviews FROM STDIN WITH (FORMAT CSV, HEADER);
"""
with open('ign.csv', 'r') as file:
    cur.copy_expert(copy_statement, file)

# Commit changes and close the connection
conn.commit()
conn.close()

## 6. Which Method Is Faster? ##

import csv
import psycopg2
import timeit

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Multiple single insert statements
def multiple_inserts():
    with open("ign.csv", "r") as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO ign_reviews VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", row)
    conn.rollback()

# Multiple mogrify insert
def mogrified_insert():
    with open("ign.csv", "r") as f:
        next(f)
        reader = csv.reader(f)
        mogrified = [
            cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s)", row).decode(conn.encoding)
            for row in reader
        ]
        mogrified_values = ",".join(mogrified)
        cur.execute("INSERT INTO ign_reviews VALUES " + mogrified_values + ";")
    conn.rollback()

# Copy expert method
def copy_expert():
    with open("ign.csv", "r") as f:
        cur.copy_expert("COPY ign_reviews FROM STDIN WITH CSV HEADER;", f)
    conn.rollback()

# Evaluate the runtime of the functions
time_multiple_inserts = timeit.timeit(multiple_inserts, number=1)
time_mogrified_insert = timeit.timeit(mogrified_insert, number=1)
time_copy_expert = timeit.timeit(copy_expert, number=1)

# Print the runtime values
print("Runtime of multiple_inserts:", time_multiple_inserts)
print("Runtime of mogrified_insert:", time_mogrified_insert)
print("Runtime of copy_expert:", time_copy_expert)

# Close the connection
conn.close()

## 7. Extracting Table to CSV File ##

import psycopg2
import psycopg2

# Connect to the database
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Copy the contents of the ign_reviews table to ign_copy.csv
copy_statement = """
COPY ign_reviews TO STDOUT WITH (FORMAT CSV, HEADER);
"""
with open('ign_copy.csv', 'w') as file:
    cur.copy_expert(copy_statement, file)

# Close the connection
conn.close()

## 8. Making a Copy of a Table ##

import psycopg2
# the query for you to create the empty table copy
create_string = """
CREATE TABLE ign_reviews_copy (
    id bigint PRIMARY KEY,
    score_phrase evaluation_enum,
    title varchar(200),
    url varchar(200),
    platform platform_enum,
    score decimal(3, 1),
    genre genre_enum,
    editors_choice boolean,
    release_date date
);
"""

import os
import psycopg2

# Connect to the database
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Specify the absolute path to the file
file_path = os.path.abspath('temp.csv')

# Copy the contents of the ign_reviews table to temp.csv
copy_to_statement = """
COPY ign_reviews TO '{}' WITH (FORMAT CSV, HEADER);
""".format(file_path)
cur.execute(copy_to_statement)

# Execute the query to create the ign_reviews_copy table
create_table_statement = """
{}
""".format(create_string)
cur.execute(create_table_statement)

# Load the data from temp.csv into the ign_reviews_copy table
copy_from_statement = """
COPY ign_reviews_copy FROM '{}' WITH (FORMAT CSV, HEADER);
""".format(file_path)
cur.execute(copy_from_statement)

# Commit changes and close the connection
conn.commit()
conn.close()

## 9. Copy with Insert and Select ##

import psycopg2

import psycopg2

# Connect to the database
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Create the ign_restricted table
create_table_statement = """
CREATE TABLE ign_restricted (
    id bigint PRIMARY KEY,
    title varchar(200),
    release_date date
);
"""
cur.execute(create_table_statement)

# Copy data from ign_reviews to ign_restricted
insert_statement = """
INSERT INTO ign_restricted (id, title, release_date)
SELECT id, title, release_date
FROM ign_reviews;
"""
cur.execute(insert_statement)

# Commit changes and close the connection
conn.commit()
conn.close()