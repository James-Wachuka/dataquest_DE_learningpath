## 1. Introduction to Time Complexity ##

def maximum(values):
    answer = None
    for value in values:
        if answer is None or answer < value:
            answer = value
    return answer

test_values = [4, 3, 5, 6, 2, 1]
max_value = maximum(test_values)
print(max_value)

## 2. Measuring the Execution Time ##

import time

# Provided maximum() function
def maximum(values):
    answer = None
    for value in values:
        if answer == None or answer < value:
            answer = value
    return answer

# Variable test_values


# Measure execution time
start = time.time()
max_value = maximum(test_values)
end = time.time()
runtime = end - start

print("Max value:", max_value)
print("Runtime:", runtime, "seconds")


## 3. Generating Random Inputs ##

import time
import random

def maximum(values):
    answer = None
    for value in values:
        if answer is None or answer < value:
            answer = value
    return answer

def gen_input(length):
    return [random.randint(-1000, 1000) for _ in range(length)]

times = []  # Step 1: Create an empty list named times

for length in range(1, 501):  # Step 2: Loop over range(1, 501) with a variable named length
    values = gen_input(length)  # Step 3: Generate a random list by calling gen_input(length)

    start = time.time()  # Step 4: Measure the time before calling the maximum() function
    maximum(values)  # Step 5: Execute the function maximum() on the generated values list
    end = time.time()  # Step 6: Measure the time after calling the maximum() function

    execution_time = end - start  # Step 7: Compute the execution time
    times.append(execution_time)  # Step 8: Append the execution time to the times list

print(times)  # Step 9: Print the value of times

## 5. Modeling Execution Times ##

import time
import random
import matplotlib.pyplot as plt

def plot_times(times):
    plt.plot(times)
    plt.ylabel('runtime')
    plt.xlabel('size')
    plt.show()

def sum_values(values):
    total = 0            
    for value in values: 
        total += value   
    return total  

def gen_input(length):
    return [random.randint(-1000, 1000) for _ in range(length)]

times = []  # Create an empty list to collect execution times

for length in range(1, 501):
    values = gen_input(length)  # Generate random input
    start = time.time()  # Measure start time
    sum_values(values)  # Execute sum_values() function
    end = time.time()  # Measure end time
    execution_time = end - start  # Compute execution time
    times.append(execution_time)  # Append to times list

plot_times(times)  # Plot the execution times

## 6. Worst-Case Analysis ##

def count_zeros(values):
    count = 0            # c1
    for value in values: # c2
        if value == 0:   # c3
            count += 1   # c4
    return count         # c5

model1 = '(c1 + c2) * N + (c3 + c4 + c5)'
model2 = '(c2 + c3) * N + (c1 + c4 + c5)'
model3 = '(c2 + c3 + c4) * N + (c1 + c5)'

# Calculate the execution count for each line
c1_count = 1
c2_count = 1
c3_count = 1
c4_count = 1
c5_count = 1

# Length of values (N)
N = 10  # Replace with the desired value

# Evaluate the models
result1 = (c1_count + c2_count) * N + (c3_count + c4_count + c5_count)
result2 = (c2_count + c3_count) * N + (c1_count + c4_count + c5_count)
result3 = (c2_count + c3_count + c4_count) * N + (c1_count + c5_count)

# Compare the results and assign the correct model
if result1 < result2 and result1 < result3:
    correct = model1
elif result2 < result1 and result2 < result3:
    correct = model2
else:
    correct = model3

print("The correct model is:", correct)

## 7. Quadratic Complexity ##

def sum_pairs(values):
    pair_sums = 0              # c1
    for x in values:           # c2
        for y in values:       # c3
            pair_sums += x + y # c4
    return pair_sums           # c5

model1 = '(c3 + c4) * N^2 + c2 * N + (c1 + c5)'
model2 = 'c4 * N^2 + (c2 + c3) * N + (c1 + c5)'
model3 = '(c2 + c3 + c4) * N^2 + (c1 + c5)'

# Assigning the correct model
correct = model1

## 8. Simplifying Further ##

time1 = 'N^4 + N^2 + 1'
time2 = '7 * N^3 + 0.5 * N^2 + 100'
time3 = 'N^2 + 10000 * N + 999'

# Function to extract the highest power of N from a given expression
def get_highest_power(expression):
    powers = []
    terms = expression.split('+')
    for term in terms:
        term = term.strip()
        if term.endswith('N'):
            powers.append(1)
        elif term.endswith('N^2'):
            powers.append(2)
        elif term.endswith('N^3'):
            powers.append(3)
        elif term.endswith('N^4'):
            powers.append(4)
        elif term.endswith('N^5'):
            powers.append(5)
        # Add more conditions for higher powers if needed
    if powers:
        return max(powers)
    else:
        return 0

# Determine the order of each function
O1 = 'O(N^{})'.format(get_highest_power(time1))
O2 = 'O(N^{})'.format(get_highest_power(time2))
O3 = 'O(N^{})'.format(get_highest_power(time3))

# Print the results
print("O1:", O1)
print("O2:", O2)
print("O3:", O3)

## 9. A Common Misconception ##

def count_triples(values):
    count = 0
    N = len(values)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if values[i] + values[j] + values[k] == 0:
                    count += 1
    return count


coefficients = [3,1,1,3]
order = "O(N^3)"