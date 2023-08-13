## 1. Introduction ##

import multiprocessing

## 2. Creating a Process ##

import time
import multiprocessing

def wait():
    time.sleep(0.5)
    print("Done waiting")

process = multiprocessing.Process(target=wait)
process.start()  # Start the process
print("Finished")
process.join()  # Wait for the process to finish

## 3. Parallel Execution ##

import time
import multiprocessing

def wait():
    time.sleep(0.5)
    print("Done waiting")

process = multiprocessing.Process(target=wait)

# Add code below
process.start()  # Start the process
process.join()  # Wait for the process to finish
print("Finished")

## 4. Running Two Processes ##

import time
import multiprocessing

def wait():
    time.sleep(0.5)
    print("Done waiting")

start = time.time()  # Calculate the start time

p1 = multiprocessing.Process(target=wait)  # Create process 1
p2 = multiprocessing.Process(target=wait)  # Create process 2

p1.start()  # Start process 1
p2.start()  # Start process 2

p1.join()  # Wait for process 1 to finish
p2.join()  # Wait for process 2 to finish

end = time.time()  # Calculate the end time

elapsed = end - start  # Calculate the execution time

print(f"Execution time: {elapsed} seconds")

## 5. Running Multiple Processes ##

import time
import multiprocessing

def wait():
    time.sleep(0.5)
    print("Done waiting")

start = time.time()  # Calculate the start time

processes = [multiprocessing.Process(target=wait) for _ in range(6)]  # Create a list with six processes

for process in processes:
    process.start()  # Start all six processes

for process in processes:
    process.join()  # Wait for all six processes to finish

end = time.time()  # Calculate the end time

elapsed = end - start  # Calculate the execution time

print(f"Execution time: {elapsed} seconds")

## 6. Process Function Arguments ##

import multiprocessing

def sum3(x, y, z):
    print(x + y + z)

def list_average(values):
    print(sum(values) / len(values))

sum3_process = multiprocessing.Process(target=sum3, args=(3, 2, 5))
list_average_process = multiprocessing.Process(target=list_average, args=([1, 2, 3, 4, 5],))

sum3_process.start()
list_average_process.start()

sum3_process.join()
list_average_process.join()

## 7. Sharing Memory ##

import multiprocessing

def sum3(x, y, z, shared_value):
    shared_value.value = x + y + z

float_value = multiprocessing.Value("f")  # Create a shared value of type "float"

process = multiprocessing.Process(target=sum3, args=(5, 7, 4, float_value))  # Create a process

process.start()  # Start the process
process.join()  # Wait for the process to finish

print(float_value.value)  # Print the value attribute of float_value

## 8. Sharing Memory Caveats ##

import multiprocessing

def sum_values(first, last, shared_value):
    for i in range(first, last):
        shared_value.value += i

def sum_with_two_processes():
    N = 10000

    shared_value = multiprocessing.Value("i")
    process1 = multiprocessing.Process(target=sum_values, args=(1, N // 2, shared_value))
    process2 = multiprocessing.Process(target=sum_values, args=(N // 2, N, shared_value))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    return shared_value.value

results = []  # Create an empty list to store the results

for _ in range(10):
    result = sum_with_two_processes()  # Call sum_with_two_processes()
    results.append(result)  # Store the result in the results list

print(results)  # Print the results list

## 9. Using a Lock ##

import multiprocessing
import time

def sum_values(first, last, shared_value):
    for i in range(first, last):
        with shared_value.get_lock():
            shared_value.value += i

def sum_values_improved(first, last, shared_value):
    value_sum = 0
    for i in range(first, last):
        value_sum += i
    with shared_value.get_lock():
        shared_value.value += value_sum

def measure_runtime(function_to_measure):
    N = 10000
    shared_value = multiprocessing.Value("i")
    process1 = multiprocessing.Process(target=function_to_measure, args=(1, N // 2, shared_value))
    process2 = multiprocessing.Process(target=function_to_measure, args=(N // 2, N, shared_value))
    start = time.time()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.time()
    return end - start

time_sum_values = measure_runtime(sum_values)  # Measure execution time of sum_values()
time_sum_values_improved = measure_runtime(sum_values_improved)  # Measure execution time of sum_values_improved()

print("Execution time of sum_values():", time_sum_values)
print("Execution time of sum_values_improved():", time_sum_values_improved)