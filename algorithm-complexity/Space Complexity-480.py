## 1. Space Complexity ##

def make_table2(N):
    table = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append([1 for _ in range(N)])
        table.append(row)
    return table

# Proposed complexities
space_complexity1 = "O(N)"
space_complexity2 = "O(N^2)"
space_complexity3 = "O(N^3)"

# Assign the space complexity of make_table2() to answer
answer = "O(N^3)"

## 2. Primary and Secondary Memory ##

class Person():
    
    def __init__(self, name, age):
        self.name = name     
        self.age = age      

import csv
def read_persons():
    persons = []
    with open('persons.csv') as f:
        next(f)
        rows = list(csv.reader(f))
        for row in rows:
            person = Person(row[0], int(row[1]))
            persons.append(person)
    return persons

# proposed complexities
space_complexity1 = "O(P)"
space_complexity2 = "O(P + L)"
space_complexity3 = "O(P * L)"
space_complexity4 = "O(L)"

# Assign the space complexity of read_persons() to answer

answer = "O(P * L)"

## 3. Memory and Speed Tradeoff ##

def find_targets_faster(values, targets):
    value_set = set(values)
    found = {}
    
    for target in targets:
        if target in value_set:
            found[target] = True
        else:
            found[target] = False
    
    return found


# Test the function
test_values = [4, 6, 3, 9, 1]
test_targets = [9, 0, 3]

result = find_targets_faster(test_values, test_targets)
print(result)

## 4. Pair Sums Problem ##

# Provided input
test_values = [1, 2, 5]
test_targets = [2, 3, 7, 8]      
# Expected output:
# {2: True, 3: True, 7: True, 8: False}

# Write your code below


def find_sums(values, target_sums):
    sums = {}  # Empty dictionary to store the results

    for target in target_sums:
        sums[target] = False  # Initialize the target sum as False

        # Iterate over all pairs of elements in values
        for i in range(len(values)):
            for j in range(len(values)):
                if values[i] + values[j] == target:
                    sums[target] = True  # Update the target sum as True if a pair is found

    return sums


# Test the function
result = find_sums(values, target_sums)
print(result)

## 5. Precomputing to Reduce Time Complexity ##

# Provided input
test_values = [1, 2, 5]
test_targets = [2, 3, 7, 8]      
# Expected output: 
# ({2: True, 3: True, 7: True, 8: False}, {2, 3, 4, 6, 7, 10})

# Write your code below

def find_sums_precompute(values, target_sums):
    possible_sums = set()  # Empty set to store all possible sums

    # Compute all possible sums of two values from values
    for i in range(len(values)):
        for j in range(len(values)):
            possible_sums.add(values[i] + values[j])

    sums = {}  # Empty dictionary to store the results

    # Check each target sum
    for target in target_sums:
        if target in possible_sums:
            sums[target] = True
        else:
            sums[target] = False

    return sums, possible_sums

result, possible_sums = find_sums_precompute(test_values, test_targets)
print(result)
print(possible_sums)

## 6. Balancing Time and Space ##

# Provided input
test_values = [1, 2, 5]
test_targets = [2, 3, 7, 8]      
# Expected output: 
# ({2: True, 3: True, 7: True, 8: False}, {1, 2, 5})

# Write your code below

def find_sums_balanced(values, target_sums):
    value_set = set(values)  # Convert the values list into a set

    sums = {}  # Empty dictionary to store the results

    for target in target_sums:
        sums[target] = False  # Initialize the target sum as False

        for value1 in values:
            value2 = target - value1  # Calculate the difference between target and value1

            if value2 in value_set:
                sums[target] = True  # Update the target sum as True if value2 exists in value_set

    return sums, value_set

result, value_set = find_sums_balanced(test_values, test_targets)
print(result)
print(value_set)

## 8. Challenge ##

def find_sums_distinct(values, target_sums):
    value_set = set(values)
    sums = {}

    for target in target_sums:
        sums[target] = False

        for value1 in value_set:
            value2 = target - value1

            if value2 in value_set and value1 != value2:
                sums[target] = True

    return sums


# Provided input
values = [1, 2, 5]
targets = [2, 3, 7, 8]      
# Expected output: 
# {2: False, 3: True, 7: True, 8: False}

# Write your code below

result = find_sums_distinct(values, targets)
print(result)