## 1. Complexity Zoo ##

# proposed complexities
constant_complexity  = "O(1)"
linear_complexity    = "O(N)"
quadratic_complexity = "O(N^2)"
cubic_complexity     = "O(N^3)"

# functions
def function1(N):
    for i in range(N):
        print(i)

def function2(N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                print(i, j, k)

def function3(N):
    for i in range(10000):
        print(i)

def function4(N):
    for i in range(N):
        for j in range(N):
            for k in range(10):
                print(i, j, k)
            
def function5(N):
    for i in range(N):
        for j in range(10000):
            print(i, j)

# Add your answers below

answer1 = linear_complexity
answer2 = cubic_complexity
answer3 = constant_complexity
answer4 = quadratic_complexity
answer5 = linear_complexity

## 3. Excluding Index Ranges ##

ask(10)
ask(50)
ask(30)
ask(45)

range_start = 31
range_end = 44

## 4. Binary Search ##

def binary_search(target):
    range_start = 0
    range_end = 63
    while range_start < range_end:
        range_middle = (range_end + range_start) // 2
        value = ask(range_middle)
        if value == target:
            return range_middle
        elif value < target:
            # Discard the first half of the range
            range_start = range_middle + 1
        else:
            # Discard the second half of the range
            range_end = range_middle - 1
    # At this point range_start = range_end
    return range_start 

# Add your code below
index_32 = binary_search(32)
answer(index_32)

## 5. Binary Search Algorithm ##

def binary_search(values, target):
    range_start = 0
    range_end = len(values) - 1
    while range_start <= range_end:
        range_middle = (range_end + range_start) // 2
        value = values[range_middle]
        if value == target:
            return range_middle
        elif value < target:
            range_start = range_middle + 1
        else:
            range_end = range_middle - 1
    if range_start >= len(values) or values[range_start] != target:
        return -1
    return range_start

values = [1, 2, 4, 5, 8, 10, 13, 15, 17, 20, 23, 24, 25, 26, 30, 31, 32, 36, 37, 38, 41, 42, 43, 44, 45, 47, 50, 52, 54, 55, 56, 57, 58, 59, 61, 62, 64, 66, 67, 69, 70, 73, 75, 76, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 90, 91, 92, 94, 95, 96, 97, 98, 99, 100]
result = binary_search(values, 3)
print(result)

## 6. Binary Search Analysis ##

import matplotlib.pyplot as plt

def plot_list(values):
    plt.plot(values)
    plt.ylabel('number of divisions to reach 1')
    plt.xlabel('N')
    plt.margins(x=0.1, y=0.1)
    plt.show()

def num_div_to_reach_1(N):
    div_count = 0
    while N > 1:
        N /= 2
        div_count += 1
    return div_count

num_div = []  # Initialize the num_div list

for N in range(1000):
    div_count = num_div_to_reach_1(N)  # Compute the number of required divisions
    num_div.append(div_count)  # Append the result to the num_div list

plot_list(num_div)  # Plot the num_div list

## 8. Binary Search in Practice ##

import time

# read the data from the CSV
import csv
with open('netflix2019.csv', mode='r') as f:
    reader = csv.reader(f)
    next(reader)
    titles = [row[1] for row in list(reader)]

# read target titles into a list
with open('target_titles.txt') as f:
    target_titles = [line.strip() for line in f.readlines()]

# linear search algorithm
def linear_lookup(titles, target_title):
    for title in titles:
        if title == target_title:
            return True
    return False

# binary search algorithm modified to return True or False
def binsearch_lookup(sorted_titles, target_title):
    range_start = 0
    range_end = len(sorted_titles) - 1
    while range_start <= range_end:
        range_middle = (range_end + range_start) // 2
        title = sorted_titles[range_middle]
        if title == target_title:
            return True
        elif title < target_title:
            range_start = range_middle + 1
        else:
            range_end = range_middle - 1
    return False

# Measure the linear lookup
start = time.time()
for title in target_titles:
    linear_lookup(titles, title)
end = time.time()
time_linear = end - start

# Measure the binary search
start = time.time()
sorted_titles = sorted(titles)
for title in target_titles:
    binsearch_lookup(sorted_titles, title)
end = time.time()
time_binsearch = end - start

# Print the elapsed times
print("Linear Lookup Time:", time_linear)
print("Binary Search Lookup Time:", time_binsearch)