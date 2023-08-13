## 1. Introducing Data Cleaning ##

# Read the text on the left, and then scroll to the bottom
# to find the instructions for the coding exercise

# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

print(len(moma))
num_rows = len(moma)

## 2. Reading our MoMA Dataset ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('artworks.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
moma = list(read_file)

#close the opened file
opened_file.close()

# remove the first row of the data, which
# contains the column names

# Write your code here
moma = moma[1:]

print(moma[:3])

## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"

age2 = age1.replace("thirty-one","thirty-two")

print(age2)

## 4. Cleaning the Nationality and Gender Columns ##

# Variables you create in previous screens
# are available to you, so you don't need
# to read the CSV again

for row in moma:
    nationality = row[2]
    nationality = nationality.replace("(","")
    nationality = nationality.replace(")","")
    row[2] = nationality
  
for row in moma:
    Gender = row[5]
    Gender = Gender.replace("(","")
    Gender = Gender.replace(")","")
    row[5] = Gender
moma[:3]

## 5. String Capitalization ##

for row in moma:
    gender = row[5]

    # convert the gender to title case
    gender = gender.title()

    # if there is no gender, set
    # a descriptive value
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender
    
for row in moma:
    Nationality = row[2]

    # convert the gender to title case
    Nationality = Nationality.title()

    # if there is no gender, set
    # a descriptive value
    if not Nationality:
        Nationality = "Nationality Unknown"
    row[2] = Nationality

## 6. Errors During Data Cleaning ##

def clean_and_convert(date):
    # check that we don't have an empty string
        
    if date != "":
        # move the rest of the function inside
        # the if statement
        date = date.replace("(", "")
        date = date.replace(")", "")
        date = int(date)
    return date

for row in moma:
    begin_date = row[3]
    end_date = row[4]

    # convert begin_date and end_date
    begin_date = clean_and_convert(begin_date)
    end_date = clean_and_convert(end_date)
    
    # set the columns with the new values
    row[3] = begin_date
    row[4] = end_date
    
print(moma[:2])
    

## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]


def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string


stripped_test_data= []
for s in test_data:
    s = strip_characters(s)
    stripped_test_data.append(s)

print(stripped_test_data)

## 8. Parsing Numbers from Complex Strings, Part Two ##

test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]



bad_chars = ["(",")","c","C",".","s","'", " "]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

def process_date(string):
    
    if "-" in string:
        sum = 0
        count = 0
        string = string.split("-")
        for value in string:
            value = int(value)
            sum += value
            count += 1
        average = sum/count
        value=int(round(average,0))
    else:
        value = int(string)
    return value

processed_test_data = []
stripped_test_data=[]

for value in test_data:
    new_string = strip_characters(value)
    stripped_test_data.append(new_string)
    
for value in stripped_test_data:
    processed_date = process_date(value)
    processed_test_data.append(processed_date)
    
for index, date in enumerate (stripped_test_data):
    stripped_test_data[index] = process_date(date)
    
for row in moma:
    Date = row[6]
    cleaned_date = strip_characters(Date)
    row[6] = process_date(cleaned_date)
    

        

    
    
    
    

    

## 9. Inserting Variables Into Strings ##

artist = "Pablo Picasso"
birth_year = 1881

template = "{name}'s birth year is {num}"

output = template.format(name = artist, num=birth_year)

print(output)

## 10. Formatting Numbers Inside Strings ##

pop_millions = [
    ["China", 1379.302771],
    ["India", 1281.935991],
    ["USA",  326.625791],
    ["Indonesia",  260.580739],
    ["Brazil",  207.353391],
]

template = "The population of {country_name} is {pop:,.2f} million"


for row in pop_millions:
    country =  row[0]
    population = row[1]
    output = template.format(country_name = country, pop = population)
    print(output)
    
    