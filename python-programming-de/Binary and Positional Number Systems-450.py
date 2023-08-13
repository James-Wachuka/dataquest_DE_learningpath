## 1. The Bit ##

num_states = 2 ** 32
print(num_states)

## 2. The Decimal Number System ##

number = 645231

# Weight of digit 2
weight_digit_2 = 10 ** 2

# Value of digit 2
value_digit_2 = 2 * weight_digit_2

# Weight of digit 5
weight_digit_5 = 10 ** 3

# Value of digit 5
value_digit_5 = 5 * weight_digit_5

## 3. The Binary Number System ##

binary_1 = "11001"
binary_2 = "1110"

# Convert binary_1 to base 10
decimal_1 = int(binary_1, 2)

# Convert binary_2 to base 10
decimal_2 = int(binary_2, 2)

# Print the values of decimal_1 and decimal_2
print(decimal_1)
print(decimal_2)

## 4. Bits and the Binary Number System ##

decimal_1 = 12345
decimal_2 = 1337

# Convert decimal_1 to base 2
bin_1 = bin(decimal_1)

# Convert decimal_2 to base 2
bin_2 = bin(decimal_2)

# Print the values of bin_1 and bin_2
print(bin_1)
print(bin_2)

## 5. Other Number Bases ##

# Convert base 8 number to base 10
base_8 = "435"
base_8_to_10 = int(base_8, 8)

# Convert base 7 number to base 10
base_7 = "10"
base_7_to_10 = int(base_7, 7)

# Print the values of base_8_to_10 and base_7_to_10
print(base_8_to_10)
print(base_7_to_10)

## 6. Special Cases ##

# Convert decimal 3501 to hexadecimal
hex_3501 = hex(3501)

# Convert hexadecimal F to decimal
decimal_F = int('F', 16)

# Print the values of hex_3501 and decimal_F
print(hex_3501)
print(decimal_F)

## 7. Hexadecimal ##

red_decimal = 213
green_decimal = 111
blue_decimal = 56

# Convert red_decimal to hexadecimal
red_hex = hex(red_decimal)

# Convert green_decimal to hexadecimal
green_hex = hex(green_decimal)

# Convert blue_decimal to hexadecimal
blue_hex = hex(blue_decimal)

## 8. Octal ##

decimal_number = 999

# Convert decimal_number to octal
octal_999 = oct(decimal_number)

# Convert octal_999 back to decimal
original = int(octal_999, 8)

# Print the values of octal_999 and original
print(octal_999)
print(original)