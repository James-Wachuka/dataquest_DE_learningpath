## 1. Introduction ##

from csv import reader
from csv import reader

# Open the CSV file
with open('potus_visitors_2015.csv', 'r') as file:
    # Read the opened file using reader() function
    csv_reader = reader(file)
    
    # Convert the read file into a list of lists format
    potus = list(csv_reader)

# Remove the first row (column names) from the dataset
potus = potus[1:]

## 3. The Datetime Module ##

import datetime as dt

## 4. The Datetime Class ##

import datetime as dt

ibm_founded = dt.datetime(1911, 6, 16, 0, 0)  # Midnight on June 16, 1911
man_on_moon = dt.datetime(1969, 7, 20, 20, 17)  # 8:17 p.m. on July 20, 1969

## 5. Using Strptime to Parse Strings as Dates ##

# The `potus` list of lists is available from
# the earlier screen where we created it

from datetime import datetime

date_format = "%m/%d/%y %H:%M"
"""
potus = [
    ["John Doe", 42, "06/20/23 15:30"],
    ["Jane Smith", 37, "06/21/23 09:45"],
    ["Robert Johnson", 55, "06/22/23 18:00"]
]
"""

for row in potus:
    appt_start_date = row[2]
    datetime_obj = datetime.strptime(appt_start_date, date_format)
    row[2] = datetime_obj

# Print the modified potus list
for row in potus:
    print(row)

## 6. Using Strftime to format dates ##

from datetime import datetime

visitors_per_month = {}

for row in potus:
    appt_start_date = row[2]
    month_year = appt_start_date.strftime("%B, %Y")
    
    if month_year not in visitors_per_month:
        visitors_per_month[month_year] = 1
    else:
        visitors_per_month[month_year] += 1

## 7. The Time Class ##

from datetime import datetime, time
""""
potus = [
    [1, 'John Doe', datetime(2023, 6, 20, 9, 0, 0)],
    [2, 'Jane Smith', datetime(2023, 6, 20, 10, 30, 0)],
    [3, 'Alice Johnson', datetime(2023, 6, 20, 14, 15, 0)]
]
"""

appt_times = []

for row in potus:
    datetime_obj = row[2]
    time_obj = datetime_obj.time()
    appt_times.append(time_obj)

## 8. Comparing time objects ##

#appt_times = ['09:00', '10:30', '11:15', '13:45', '14:30']

min_time = min(appt_times)
max_time = max(appt_times)

print("Earliest appointment time:", min_time)
print("Latest appointment time:", max_time)

## 9. Calculations with Dates and Times ##

import datetime as dt

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

# Calculate the time difference between dt_2 and dt_1
time_diff = dt_2 - dt_1
answer_1 = time_diff

# Add 56 days to dt_3
dt_3_plus_56_days = dt_3 + dt.timedelta(days=56)
answer_2 = dt_3_plus_56_days

# Subtract 3600 seconds from dt_4
dt_4_minus_3600_seconds = dt_4 - dt.timedelta(seconds=3600)
answer_3 = dt_4_minus_3600_seconds

## 10. Summarizing Appointment Lengths ##

import datetime as dt

# Instantiate an empty dictionary for the frequency table
appt_lengths = {}

# Convert appt_end_date to datetime objects
for row in potus:
    end_date = row[3]
    end_date = dt.datetime.strptime(end_date, "%m/%d/%y %H:%M")
    row[3] = end_date

    # Calculate the length of the appointment
    start_date = row[2]
    length = end_date - start_date

    # Update the frequency table
    if length not in appt_lengths:
        appt_lengths[length] = 1
    else:
        appt_lengths[length] += 1

# Calculate the minimum and maximum lengths
min_length = min(appt_lengths.keys())
max_length = max(appt_lengths.keys())