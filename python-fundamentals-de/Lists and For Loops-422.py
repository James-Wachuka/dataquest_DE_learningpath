## 1. Lists ##

row_2 = ['Instagram',0.0,'USD',2161558,4.5]

row_3 = ['Clash of Clans',0.0,'USD',2130805,4.5]

        

## 2. Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]

import math
ratings_1 = row_1[3]

ratings_2 = row_2[3]

ratings_3 = row_3[3]

print(ratings_3)

total = ratings_1 + ratings_2 + ratings_3
#print(total)
average = total/3
print(average)

## 3. Negative Indexing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]


rating_1 = row_1[-1]

rating_2 = row_2[-1]

rating_3 = row_3[-1]

total_rating = rating_1 + rating_2 + rating_3

average_rating = total_rating/3

## 4. Retrieving Multiple List Elements ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

fb_rating_data = [row_1[0],row_1[3],row_1[4]]

insta_rating_data = [row_2[0],row_2[3],row_2[4]]

pandora_rating_data = [row_5[0], row_5[3],row_5[4]]
                       
avg_rating = (pandora_rating_data[2] + insta_rating_data[2] + fb_rating_data[2])/3

print(avg_rating)

## 5. List Slicing ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

first_4_fb = row_1[:4]

last_3_fb = row_1[2:]

pandora_3_4 = row_5[2:4]

print(last_3_fb)

## 6. List of Lists ##

row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

avg_rating = (app_data_set[0][-1]+app_data_set[1][-1]+app_data_set[2][-1]+app_data_set[3][-1]+app_data_set[4][-1])/5

## 7. Opening and Reading a File ##

opened_file = open('AppleStore.csv')
read_file = opened_file.read()
print(read_file[:300])
opened_file.close()

## 8. From Strings to Lists ##

opened_file = open('AppleStore.csv')
read_file = opened_file.read()
new_line_split = read_file.split("\n")


header = new_line_split[0]
data_row_1 = new_line_split[1]
data_row_2 = new_line_split[2]

first_three = [header, data_row_1, data_row_2]
#print(first_three)

first_three_lists = [first_three[0].split(","),first_three[1].split(","),first_three[2].split(",")]

print(first_three_lists)

## 9. For Loops ##

header = new_line_split[0]
data_row_1 = new_line_split[1]
data_row_2 = new_line_split[2]
first_three = [header, data_row_1, data_row_2]
print(first_three)
index = 0 

for each_string in first_three:
    first_three[index] = each_string.split(",")
    print(first_three[index])
    index += 1
    
print(first_three)

## 10. Reading CSV files ##

opened_file = open('AppleStore.csv')

from csv import reader
read_file = reader(opened_file)

apps_data = list(read_file)

opened_file.close()

#print(len(apps_data))

print(apps_data[2:4])

## 11. The Average App Rating ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

#print(len(apps_data))

rating = 0
rating_sum = 0
count = 0
for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum = rating_sum + rating
    #avg_rating = (rating_sum/count)
    count += 1

print(rating_sum)
print (rating)
print(count)

avg_rating = rating_sum/count

## 12. Alternative Way to Compute an Average ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

opened_file.close()

all_ratings=[]
for row in apps_data[1:]:
    rating = float(row[7])
    all_ratings.append(rating)
    
avg_rating =  sum(all_ratings)/len(all_ratings)
print(avg_rating)
    
    