## 1. Fixed Bit Integers ##

import numpy as np

x = np.int8(100)
y = np.int8(28)
z = x + y

print(z)

## 2. Two's Complement Representation ##

# Convert 2-bit two's complement number 10 to decimal
x = (-1) * 2**1 + 0 * 2**0
print(x)

# Convert 4-bit two's complement number 1010 to decimal
y = (-1) * 2**3 + 0 * 2**2 + 1 * 2**1 + 0 * 2**0
print(y)

# Convert 4-bit two's complement number 0110 to decimal
z = 0 * 2**3 + 1 * 2**2 + 1 * 2**1 + 0 * 2**0
print(z)

## 3. Range of Two's Complement ##

import numpy as np

min_value_32bit = np.iinfo(np.int32).min
max_value_32bit = np.iinfo(np.int32).max

binary_min_value = np.binary_repr(min_value_32bit, width=32)
binary_max_value = np.binary_repr(max_value_32bit, width=32)

print(binary_min_value)
print(binary_max_value)

## 4. Why Two's Complement ##

import sys


max_value_32bit = 2147483647

num_bytes = sys.getsizeof(max_value_32bit)
num_mb = (num_bytes * 1000000000) / 1000000

print("Number of bytes required to represent the maximum value of a 32-bit integer:", num_bytes)
print("Number of megabytes required to store one billion 32-bit integers:", num_mb)

## 5. Identifying the Number of Bits ##

def minimum_required_bits(list_of_integers):
    min_req_bits = 0
    for value in list_of_integers:
        nb_bits = int.bit_length(value)
        min_req_bits = max(min_req_bits, nb_bits)
    return min_req_bits

# Read the file and convert values to integers
with open('identifiers.txt', 'r', encoding='utf-8') as file:
    values = [int(line) for line in file]

# Calculate the minimum number of bits required
min_bits_required = minimum_required_bits(values)

print("Minimum number of bits required:", min_bits_required)

## 6. Memory Consumption of Textual Data ##

import sys
s = "你"



size_s = sys.getsizeof(s)
size_ss = sys.getsizeof(s + s)

print("Number of bytes used by s:", size_s)
print("Number of bytes used by s + s:", size_ss)

## 7. Python Internal String Representation ##

import sys
message = "I really like learning about Python! 🐍\n Me too! 😀😀\n I can't wait to see what we will learn in the next course 🙃\n"



# Encode the message using 'Latin-1'
message_latin_bytes = message.encode(encoding='Latin-1', errors='ignore')

# Decode the encoded bytes using 'Latin-1'
cleaned_message = message_latin_bytes.decode(encoding='Latin-1')

# Calculate the size of the original message
message_size = sys.getsizeof(message)

# Calculate the size of the cleaned message
cleaned_message_size = sys.getsizeof(cleaned_message)

## 8. Disk Consumption of Textual Data ##

import os
messages = "I really like learning about Python! 🐍\n Me too! 😀😀\n I can't wait to see what we will learn in the next course 🙃\n"



# Writing to utf8.txt with UTF-8 encoding
with open("utf8.txt", mode="w", encoding="utf-8") as file_utf8:
    file_utf8.write(messages)

# Getting the size of utf8.txt in bytes
size_utf8 = os.path.getsize("utf8.txt")

# Writing to utf32.txt with UTF-32 encoding
with open("utf32.txt", mode="w", encoding="utf-32") as file_utf32:
    file_utf32.write(messages)

# Getting the size of utf32.txt in bytes
size_utf32 = os.path.getsize("utf32.txt")

## 9. Estimating the Disk Requirements ##

num_days_in_a_year = 365
num_years = 20+1
bytes_per_char = 32 / 8
num_transactions = 1000000
username_size = 20
product_name_size = 50

# Calculate the size of each transaction in bytes
transaction_size = (username_size * bytes_per_char) + (username_size * bytes_per_char) + (product_name_size * bytes_per_char)

# Calculate the total size of transactions for 20 years
total_size = num_transactions * transaction_size * num_days_in_a_year * num_years

# Convert bytes to gigabytes
num_gb = total_size / (1024**3)

# Print the result
print("Estimated disk space required: {:.2f} GB".format(num_gb))