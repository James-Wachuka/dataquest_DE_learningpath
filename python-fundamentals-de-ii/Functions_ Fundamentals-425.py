## 1. Functions ##

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]
#print(sum(a_list))

sum_manual=0

for item in a_list:
    sum_manual +=item
    
    
print(sum_manual)
print(sum(a_list))

## 2. Built-in Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']


content_ratings ={}

for rating in ratings:
    if rating in content_ratings:
        content_ratings[rating] +=1
    else:
        content_ratings[rating] = 1

print(content_ratings)

## 3. Creating Our Own Functions ##

def square(a_number):
    squared_number = a_number * a_number
    return squared_number

squared_10 = square(a_number=10)
squared_16= square(a_number=16)

print(squared_10)
print(squared_16)

## 4. The Structure of a Function ##

def add_10(num):
    num += 10
    return num



add_30 = add_10(30)
add_90 = add_10(90)

## 5. Parameters and Arguments ##

def square(a_number):
    # Variable assignment step omitted
    return a_number * a_number 

squared_6 = square(6)
squared_11 = square(11)
print(square(6))

## 6. Extract Values From Any Column ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
'''
def extract(index):
    
    content_ratings = []
    for row in apps_data[1:]:
        content_rating = row[index]
        content_ratings.append(content_rating)
    return content_ratings
'''

def extract(index):
    
    genres_ = []
    for row in apps_data[1:]:
        genre = row[index]
        genres_.append(genre)
    return genres_
genres = extract(11)
print(extract(11))

## 7. Creating Frequency Tables ##

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

genres = extract(11)

'''
def freq_table(list):
    content_ratings = {}
    ratings = ['4+', '4+', '4+', '9+', '9+', '12+', '17+']

    for c_rating in ratings:
        if c_rating in content_ratings:
            content_ratings[c_rating] += 1
        else:
            content_ratings[c_rating] = 1
    return content_ratings
'''

frequency_table = {}
def freq_table(list):
    #print(genres)
    for genre in genres:
        if genre in frequency_table:
            frequency_table[genre] += 1
        else:
            frequency_table[genre] = 1
    return frequency_table

genres_ft=freq_table(genres)
print(genres_ft)

## 8. Writing a Single Function ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    user_rating=column
    
    frequency_table = {}
    #print(genres)
    for rating in user_rating:
        if rating in frequency_table:
            frequency_table[rating] += 1
        else:
            frequency_table[rating] = 1
    return frequency_table

ratings_ft=freq_table(7)
print(ratings_ft)

## 9. Reusability and Multiple Parameters ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
#print(apps_data)
#print(type(apps_data))

# INITIAL FUNCTION
def freq_table(index,data_set):
    column = []       
    user_rating=column
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

ratings_ft = freq_table(7,apps_data)
print(ratings_ft)

## 10. Keyword and Positional Arguments ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

content_ratings_ft = freq_table(apps_data,10)
ratings_ft = freq_table(apps_data,7)
genres_ft = freq_table(apps_data,11)

## 11. Combining Functions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(dataset,index):
    price_column = extract(dataset,index)
    sum_list = find_sum(a_list = price_column)
    len_list = find_length(a_list = price_column)
    mean_list = sum_list / len_list

    return mean_list

avg_price = mean(apps_data,4)
print(avg_price)

## 12. Debugging Functions ##

avg_price = None
avg_rating = None

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set,index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)