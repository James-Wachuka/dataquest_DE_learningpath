## 1. Constant Time Complexity ##

def average(values):
    average = 0
    for value in values:
        average += value
    return average / len(values)

coefficients = [2,2]

order = "O(N)"

## 2. Constant Time Complexity in Python ##

def function1(N):
    for i in range(N):
        print(i)

def function2():
    for i in range(100000):
        print(i)

def function3(N):
    for i in range(100000):
        print(i)
constant1 = False
constant2 = True
constant3 = True

## 3. Complexity of Function Calls ##

def sum_values(values):
    total = 0            # 1
    for value in values: # N
        total += value   # N
    return total         # 1

def num_values(values):
    total = 0            # 1
    for _ in values:     # N
        total += 1       # N
    return total         # 1

def average(values):
    value_sum = sum_values(values)  # N
    num_values = num_values(values) # N
    return value_sum / num_values   # 1

## 4. Hidden Function Calls ##

N = 10
M = 20

list1 = [_ for i in range(0)]
list2 = [i for i in range(3)]
list3 = [i * i for i in range(M)]
list4 = [[i + j for j in range(M)] for i in range(N)]
list5 = [min(list4[i]) for i in range(N)]
list6 = [i for i in range(1000)]

complexity1 = 'O(1)'
complexity2 = 'O(N)'
complexity3 = 'O(M)'
complexity4 = 'O(N + M)'
complexity5 = 'O(N * M)'

# Example answer for list1
answer2 = complexity1
answer3 = complexity3
answer4 = complexity5
answer5 = complexity5
answer6 = complexity1

## 6. Amortized Analysis of Append ##

import matplotlib.pyplot as plt

def plot_costs(times):
    plt.plot(times, label='append cost')
    plt.ylabel('cost')
    plt.xlabel('N')
    plt.show()

def append_cost(array_length, list_length):
    if array_length == list_length:
        return array_length
    return 1

def append_N_list_cost(N):
    array_length = 1  # initially the array will have length 1
    list_length = 0  # initially the list has 0 elements
    total_cost = 0  # this variable will keep track of the total cost
    for i in range(N):
        cost = append_cost(array_length, list_length)
        total_cost += cost
        # update the array and list lengths
        if array_length == list_length:
            array_length *= 2
        list_length += 1
    return total_cost

# Initialize an empty list named costs
costs = []

# Use a for loop over range(5000) using a variable named N
for N in range(5000):
    # Call append_N_list_cost() by passing the current value of N as an argument
    cost = append_N_list_cost(N)
    # Append the result to the costs list
    costs.append(cost)

# Use the provided plot_costs() function to plot the costs list
plot_costs(costs)

## 7. List Complexities ##

import time

def add_with_append(N):
    values = []
    for i in range(N):
        values.append(i)
    return values

def add_with_insert(N):
    values = []
    for i in range(N):
        values.insert(0, i)
    return values

# Time add_with_append(50000)
start = time.time()
add_with_append(50000)
end = time.time()
time_append = end - start

# Time add_with_insert(50000)
start = time.time()
add_with_insert(50000)
end = time.time()
time_insert = end - start

print("Time taken with append:", time_append)
print("Time taken with insert:", time_insert)

## 8. Arithmetic Operations ##

import time
import matplotlib.pyplot as plt

def plot_times(times):
    plt.plot(times)
    plt.ylabel('multiplication runtime')
    plt.xlabel('number of digits')
    plt.yscale('log')
    plt.yticks([])
    plt.show()

times = []

# Iterate over pairs
for pair in pairs:
    x, y = pair

    # Measure the time before multiplication
    start = time.time()

    # Multiply x and y together
    result = x * y

    # Measure the time after multiplication
    end = time.time()

    # Add the elapsed time to the times list
    elapsed_time = end - start
    times.append(elapsed_time)

# Plot the times
plot_times(times)

## 9. String Concatenation ##

import time

def concat_with_add(word_list):
    concat = ''
    for word in word_list:
        concat += word
    return concat

def concat_with_join(word_list):
    return ''.join(word_list)

print(random_strings[:5])

# Timing concat_with_add()
start = time.time()
concat_with_add(random_strings)
end = time.time()
time_add = end - start

# Timing concat_with_join()
start = time.time()
concat_with_join(random_strings)
end = time.time()
time_join = end - start

print("Time taken by concat_with_add():", time_add)
print("Time taken by concat_with_join():", time_join)

if time_add < time_join:
    print("concat_with_add() was faster.")
else:
    print("concat_with_join() was faster.")

## 10. Hidden Python Optimizations ##

import time

with open('random_words.txt', mode='r') as f:
   word_list = f.readlines()
 
def concat_with_add(word_list):
   concat = ''
   for word in word_list:
       concat += word
       temp = concat  # New variable assignment
   return concat

def concat_with_join(word_list):
   return ''.join(word_list)

start = time.time()
concat_with_add(word_list)
end = time.time()
time_add = end - start

start = time.time()
concat_with_join(word_list)
end = time.time()
time_join = end - start
    
print(time_add)
print(time_join)