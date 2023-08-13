## 1. Reading Files in Python ##

# Open the file
file = open("dialog.txt", "r")

# Read all lines and assign them to a variable
lines = list(file)

# Close the file
file.close()

## 2. Reading with a Context Manager ##

filename = "dialog.txt"

# Open the file and assign its lines to the variable 'lines'
with open(filename, "r") as file:
    lines = list(file)

# Print the lines
print(lines)

## 3. Reading with the Wrong Encoding ##

import csv


with open('kyoto_restaurants.csv', newline='') as file:
    # File operations will be performed here
    pass

with open('kyoto_restaurants.csv', newline='') as file:
    reader = csv.reader(file)

    
with open('kyoto_restaurants.csv', newline='') as file:
    
    reader = csv.reader(file)
    rows = list(reader)


with open('kyoto_restaurants.csv', newline='') as file:
    reader = csv.reader(file)
    rows = list(reader)

print(len(rows))


## 4. Finding the Right Encoding ##

import chardet

# Read the file in bytes mode
with open('kyoto_restaurants.csv', 'rb') as file:
    raw_bytes = file.read()

# Detect the encoding
detected_encoding = chardet.detect(raw_bytes)

print(detected_encoding)


## 5. Reading with the Right Encoding ##

import csv

with open('kyoto_restaurants.csv', encoding='utf16') as file:
    
    csv_reader = csv.reader(file)
    rows = list(csv_reader)
    num_rows = len(rows)
    first_row = rows[1]
    print(first_row)

## 6. Encoding Identification Workflow ##

import csv
import chardet

# Read the first 32 bytes of the CSV file
with open('kyoto_restaurants.csv', 'rb') as file:
    raw_bytes = file.read(32)

# Detect the encoding of the CSV file
encoding_result = chardet.detect(raw_bytes)
encoding_name = encoding_result['encoding']

# Read the CSV file using the detected encoding
with open('kyoto_restaurants.csv', encoding=encoding_name) as file:
    rows = list(csv.reader(file))

# Printing the rows as an example
for row in rows:
    print(row)

## 7. Writing to a file ##

# Open the file using a context manager
with open("my_file.txt", "w") as file:
    # Write the first line
    file.write("first line\n")
    
    # Write the second line
    file.write("second line\n")

## 8. Appending to a File ##

# Write to the file using a context manager
with open("append.txt", "a") as file:
    # Write the line to the file
    file.write("my line\n")

# Read the file using another context manager
with open("append.txt", "r", encoding="utf-8") as file:
    # Read all lines from the file
    lines_appended = file.readlines()

# Print the value of lines_appended
print(lines_appended)

## 9. Converting the Dataset to UTF-8 ##

import csv

original_file = 'kyoto_restaurants.csv'
original_encoding = 'utf-16'

new_file = 'kyoto_restaurants_utf8.csv'
new_encoding = 'utf-8'

# Read the original file with the specified encoding
with open(original_file, encoding=original_encoding) as file:
    rows = list(csv.reader(file))

# Write the data to the new file with the new encoding
with open(new_file, mode='w', encoding=new_encoding, newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("Conversion complete. The file", new_file, "has been created.")