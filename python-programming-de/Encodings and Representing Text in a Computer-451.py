## 1. The ASCII Encoding ##

data = "QUEST"
for char in data:
    ascii_encoding = ord(char)
    binary_encoding = bin(ascii_encoding)
    print(f"{binary_encoding}")

## 2. ASCII Limitations ##

text = "The Swedish word for quest is sökande"

# Encode text into ASCII using character replacement for error handling
encoded = text.encode(encoding='ascii', errors='replace')

# Print the value of encoded
print(encoded)

# Print the type of encoded
print(type(encoded))

## 3. Bytes ##

# Create bytes object from hexadecimal string '02'
bytes1 = bytes.fromhex('02')
print(bytes1)

# Create bytes object from hexadecimal string '5a'
bytes2 = bytes.fromhex('5a')
print(bytes2)

# Create bytes object from hexadecimal string 'ff'
bytes3 = bytes.fromhex('ff')
print(bytes3)

## 4. Printable Characters ##

# provided inputs
string_1 = 'lowercase'
string_2 = 'UPPERCASE'

def check_uppercase(string):
    if string.isupper():
        return True
    else:
        return False

## 5. Multi-byte encodings ##

trad_chinese = "你好嗎?"



# Encode the string using BIG5 encoding
encoded = trad_chinese.encode("big5")

# Print the number of bytes used in the encoding
print(len(encoded))

## 7. Unicode ##

sentence = "ASCII cannot represent these: 你好嗎"



# Encode and print the string in UTF-8 encoding
encoded_utf8 = sentence.encode("utf-8", errors="replace")
print(encoded_utf8)

# Encode and print the string in ASCII encoding
encoded_ascii = sentence.encode("ascii", errors="replace")
print(encoded_ascii)

## 8. Decoding Bytes ##

# variable named encoded is accessible


# Decode using cp1252 encoding
decoded_cp1252 = encoded.decode('cp1252')
print(decoded_cp1252)

# Import chardet module
import chardet

# Detect the correct encoding
encoding = chardet.detect(encoded)['encoding']

# Decode using the detected encoding
decoded = encoded.decode(encoding)
print(decoded)