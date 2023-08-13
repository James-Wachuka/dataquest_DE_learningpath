## 1. Incorrect Data Types ##

query_string = """
    INSERT INTO ign_reviews VALUES(
        5249979066121302000, 
        'Amazing', 
        'LittleBigPlanet PS Vita', 
        '/games/littlebigplanet-vita/vita-98907', 
        'PlayStation Vita', 
        9.0,
        'Platformer', 
        'Y', 
        2012, 
        9, 
        12
    );
"""
import psycopg2

# Connect to the dq database with user dq
conn = psycopg2.connect("dbname=dq user=dq")

# Obtain a cursor object
cur = conn.cursor()

# Execute the query contained in the query_string variable
# query_string = """
#     INSERT INTO ign_reviews 
#     (id, score_phrase, title, url, platform, score, genre, editors_choice, release_year, release_month, release_day)
#     VALUES 
#     (52499790661213, 'Amazing', 'LittleBigPlanet PS Vita', '/games/littlebigplanet-vita/vita-98907', 'PlayStation Vita', 9.0, 'Platformer', 'y', 2012, 9, 12);
# """
cur.execute(query_string)

# Close the connection
conn.close()

## 2. Describing a Table ##

import psycopg2

# Connect to the dq database using the dq user
conn = psycopg2.connect("dbname=dq user=dq")

# Obtain a cursor object
cur = conn.cursor()

# Execute the query to select all columns of the ign_reviews table
query = "SELECT * FROM ign_reviews"
cur.execute(query)

# Print the description attribute of the cursor object
print(cur.description)

# Close the connection
conn.close()

## 3. Understanding the Description ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Assuming you already have the 'conn' connection object and 'cur' cursor object

# Query to fetch the name of the data type for type code 25
query_type_25 = "SELECT typname FROM pg_catalog.pg_type WHERE oid = 25"
cur.execute(query_type_25)
type_name_25 = cur.fetchone()[0]

# Query to fetch the name of the data type for type code 700
query_type_700 = "SELECT typname FROM pg_catalog.pg_type WHERE oid = 700"
cur.execute(query_type_700)
type_name_700 = cur.fetchone()[0]

# Inspect the variables
print("Data type name for code 25:", type_name_25)
print("Data type name for code 700:", type_name_700)

# Close the connection
conn.close()

## 4. Finding the Right ID Data Type ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()


# Connect to the dq database with user dq
conn = psycopg2.connect("dbname=dq user=dq")

# Obtain a cursor object
cur = conn.cursor()

# Execute the query to alter the type of the id column to bigint
query = "ALTER TABLE ign_reviews ALTER COLUMN id TYPE bigint"
cur.execute(query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 5. Float-like Types ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Assuming you already have the 'cur' cursor object

# Execute the query to alter the datatype of the score column to DECIMAL(3, 1)
query = "ALTER TABLE ign_reviews ALTER COLUMN score TYPE DECIMAL(3, 1)"
cur.execute(query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 6. Finding the Max Length ##

# import csv
# with open('ign.csv', 'r') as f:
#     next(f) # skip the row containing column headers
#     reader = csv.reader(f)
#     # create a set to contain all score phrases
#     unique_words_in_score_phrase = set()
#     for row in reader:
#         # add the score phrase from this row to the set
#         score_phrase = row[1]
#         unique_words_in_score_phrase.add(score_phrase)

import csv

with open('ign.csv', 'r') as f:
    next(f) # skip the row containing column headers
    reader = csv.reader(f)
    
    # Initialize a variable to store the maximum length
    max_length = 0
    
    for row in reader:
        score_phrase = row[1]
        
        # Compute the length of the current score phrase
        length = len(score_phrase)
        
        # Update the maximum length if necessary
        if length > max_length:
            max_length = length

# Print the maximum length
print("Maximum length of score phrase:", max_length)

## 7. Max String-like Datatypes ##

# import psycopg2
# conn = psycopg2.connect("dbname=dq user=dq")
# cur = conn.cursor()


import psycopg2

# Connect to the dq database with user dq
conn = psycopg2.connect("dbname=dq user=dq")

# Obtain a cursor object
cur = conn.cursor()

# Execute the query to alter the type of the score_phrase column to varchar(11)
query = "ALTER TABLE ign_reviews ALTER COLUMN score_phrase TYPE varchar(11)"
cur.execute(query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 8. Enumerated Datatypes ##

import psycopg2

# Connect to the dq database with user dq
conn = psycopg2.connect("dbname=dq user=dq")

# Obtain a cursor object
cur = conn.cursor()

# Create the evaluation_enum datatype
cur.execute("""
    CREATE TYPE evaluation_enum AS ENUM (
    'Great',       'Mediocre', 'Bad', 
    'Good',        'Awful',    'Okay', 
    'Masterpiece', 'Amazing',  'Unbearable', 
    'Disaster',    'Painful');
""")

# Alter the type of the score_phrase column to evaluation_enum
cur.execute("""
    ALTER TABLE ign_reviews
    ALTER COLUMN score_phrase
    TYPE evaluation_enum
    USING score_phrase::evaluation_enum
""")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 9. Understanding Enumerated Datatypes ##

import psycopg2

# Connect to the dq database with user dq
conn = psycopg2.connect("dbname=dq user=dq")

# Obtain a cursor object
cur = conn.cursor()

# Create the genre_enum and platform_enum datatypes
cur.execute("""
    CREATE TYPE genre_enum AS ENUM (
    'Adventure', 'Strategy', 'Shooter', 'genre', 'Virtual Pet', 'Hardware', 'Adult', 'Baseball', 
    'Sports', 'Flight', 'Unknown', 'Racing', 'Battle', 'Fighting', 'Simulation', 'Party', 'Card', 
    'Productivity', 'Puzzle', 'Educational', 'Casino', 'RPG', 'Board', 'Other', 'Pinball', 'Platformer', 
    'Hunting', 'Action', 'Music', 'Compilation', 'Wrestling', 'Trivia');
""")

cur.execute("""
    CREATE TYPE platform_enum AS ENUM (
    'PC', 'Game Boy', 'Sega CD', 'Saturn', 'DVD / HD Video Game', 'Nintendo DSi', 
    'Arcade', 'Wii U', 'Lynx', 'Super NES', 'WonderSwan Color', 'TurboGrafx-CD', 
    'Windows Phone', 'TurboGrafx-16', 'N-Gage', 'Xbox One', 'Atari 2600', 
    'Pocket PC', 'Vectrex', 'Nintendo DS', 'Wireless', 'Ouya', 'Nintendo 64DD', 
    'Atari 5200', 'PlayStation 4', 'GameCube', 'Android', 'Wii', 'Game Boy Color', 
    'PlayStation 2', 'New Nintendo 3DS', 'Linux', 'Dreamcast VMU', 'Game Boy Advance', 
    'Windows Surface', 'Genesis', 'Xbox 360', 'Macintosh', 'Web Games', 'Nintendo 3DS', 'iPhone', 
    'SteamOS', 'Commodore 64/128', 'Dreamcast', 'PlayStation 3', 'NES', 'NeoGeo Pocket Color', 
    'Game.Com', 'PlayStation Portable', 'Master System', 'Sega 32X', 'NeoGeo', 'WonderSwan', 'iPad', 
    'Nintendo 64', 'PlayStation Vita', 'Xbox', 'iPod', 'PlayStation');
""")

# Change the type of the title column to varchar(200)
cur.execute("""
    ALTER TABLE ign_reviews
    ALTER COLUMN title
    TYPE varchar(200)
""")

# Change the type of the url column to varchar(200)
cur.execute("""
    ALTER TABLE ign_reviews
    ALTER COLUMN url
    TYPE varchar(200)
""")

# Change the type of the platform column to platform_enum
cur.execute("""
    ALTER TABLE ign_reviews
    ALTER COLUMN platform
    TYPE platform_enum
    USING platform::platform_enum
""")

# Change the type of the genre column to genre_enum
cur.execute("""
    ALTER TABLE ign_reviews
    ALTER COLUMN genre
    TYPE genre_enum
    USING genre::genre_enum
""")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 10. Boolean Types ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Change the datatype of the editors_choice column to boolean
cur.execute("""
    ALTER TABLE ign_reviews
    ALTER COLUMN editors_choice
    TYPE boolean
    USING editors_choice::boolean
""")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 11. Date Type ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# Create a new column release_date with datatype date
cur.execute("""
    ALTER TABLE ign_reviews
    ADD COLUMN release_date date
""")

# Delete columns release_year, release_month, and release_day
cur.execute("""
    ALTER TABLE ign_reviews
    DROP COLUMN release_year,
    DROP COLUMN release_month,
    DROP COLUMN release_day
""")

# Commit the changes
conn.commit()

# Close the connection
conn.close()

## 12. Loading the Data ##

import datetime
import psycopg2
import csv
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()

# import csv
# import psycopg2

# # Connect to the database
# conn = psycopg2.connect("dbname=dq user=dq")
# cur = conn.cursor()

# Open the CSV file
with open('ign.csv', 'r') as f:
    next(f)  # Skip the row containing column headers
    reader = csv.reader(f)
    
    # Process and insert each row into the table
    for row in reader:
        # Process the date
        release_date = '-'.join([row[8], row[9], row[10]])
        
        # Insert the processed row into the table
        cur.execute("""
            INSERT INTO ign_reviews (id, score_phrase, title, url, platform, score, genre, editors_choice, release_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], release_date))
    
    # Commit the changes
    conn.commit()

# Close the connection
conn.close()