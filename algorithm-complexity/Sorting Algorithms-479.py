## 1. Sorting in Python ##

values = [6, 8, 7, 4, 3, 5, 2, 1, 9]

values = [6, 8, 7, 4, 3, 5, 2, 1, 9]

sorted_values = sorted(values)
sorted_values_reverse = sorted(values, reverse=True)

print("sorted_values:", sorted_values)
print("sorted_values_reverse:", sorted_values_reverse)

## 2. Swapping ##

def swap(values, i, j):
    values[i], values[j] = values[j], values[i]
    
value_list = [1, 4, 5, 2, 3]
i = 1
j = 3

swap(value_list, i, j)
print(value_list)

## 3. Selecting the Minimum ##

def swap(values, i, j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp

def select_minimum_index_in_range(values, range_start):
    minimum = None
    minimum_index = None
    N = len(values)
    for i in range(range_start, N):
        if minimum == None or values[i] < minimum:
            minimum = values[i]
            minimum_index = i
    return minimum_index

values = [5, 4, 6, 1, 3, 2]

index = select_minimum_index_in_range(values, 0)
swap(values, 0, index)

print(values)

## 4. Selection Sort ##

def swap(values, i, j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp

def select_minimum_index_in_range(values, range_start):
    minimum = None
    minimum_index = None
    N = len(values)
    for i in range(range_start, N):
        if minimum == None or values[i] < minimum:
            minimum = values[i]
            minimum_index = i
    return minimum_index

def selection_sort(values):
    N = len(values)
    for i in range(N):
        min_index = select_minimum_index_in_range(values, i)
        swap(values, i, min_index)

values = [5, 4, 6, 1, 3, 2]
selection_sort(values)
print(values)

## 5. Complexity of Selection Sort ##

import matplotlib.pyplot as plt

def plot_values(values):
    plt.plot(values, label='1+2+...+N', color='y')
    plt.ylabel('1+2+...+N')
    plt.xlabel('N')
    plt.legend()
    plt.show()

sum_first_N = 0
values = []

for N in range(1, 1001):
    sum_first_N += N
    values.append(sum_first_N)

plot_values(values)

## 6. Sum of The First N Naturals ##

# Variable values is avaiable

values_formula = []

for N in range(1, 1001):
    value = N**2 / 2 + N / 2
    values_formula.append(value)

same_values = values == values_formula

print(same_values)

## 7. Find Equal Pairs of Indexes ##

def num_if_executions(N):
    count = 0
    for i in range(N):
        count += (N - 1) - i
    return count

count_1000 = num_if_executions(1000)
print(count_1000)

## 8. Comparing Insertion Sort with Python Sort ##

import time
import random
import matplotlib.pyplot as plt

def plot_times(times_python, times_selection):
    plt.plot(times_python, label='time sorted()')
    plt.plot(times_selection, label='time selection_sort()')
    plt.ylabel('runtime')
    plt.xlabel('N')
    plt.legend()
    plt.show()

def selection_sort(values):
    N = len(values)
    for range_start in range(N):
        index = select_minimum_index_in_range(values, range_start)
        swap(values, range_start, index)

def select_minimum_index_in_range(values, start):
    min_index = start
    for i in range(start + 1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

def swap(values, i, j):
    values[i], values[j] = values[j], values[i]

times_python = []
times_selection = []

for N in range(1, 501):
    values = [random.randint(1, 10000) for _ in range(N)]

    start_time = time.time()
    sorted_values = sorted(values)
    end_time = time.time()
    times_python.append(end_time - start_time)

    start_time = time.time()
    selection_sort(values)
    end_time = time.time()
    times_selection.append(end_time - start_time)

plot_times(times_python, times_selection)