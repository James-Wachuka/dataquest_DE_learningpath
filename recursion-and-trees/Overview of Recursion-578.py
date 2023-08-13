## 2. Recursive Sum ##

fruits = ["apple", "orange", "pear", "fig", "passionfruit"]

def list_len(lst):
    if not lst:  # Base case: empty list
        return 0
    else:  # General case: non-empty list
        return 1 + list_len(lst[1:])

# Test the function

num_fruits = list_len(fruits)
print(f"The number of fruits is: {num_fruits}")

## 3. Stack Overflow ##

fruits = ["apple", "orange", "pear", "fig", "passionfruit"]

def list_len(lst):
    return 1 + list_len(lst[1:])

num_fruits = list_len(fruits)

## 4. Towers of Hanoi ##

def solve_hanoi(num_disks, first_peg, middle_peg, last_peg):
    if num_disks == 1:
        # Base case
        print("Move the top disk from peg {} to peg {}.".format(first_peg, last_peg))
    else:
        # General Case
        # Instruction 1: Move a stack of size num_disks - 1 from first_peg to middle_peg using last_peg as temporary peg
        solve_hanoi(num_disks - 1, first_peg, last_peg, middle_peg)

        # Second subproblem: Move disk num_disks from first_peg to last_peg
        print("Move the top disk from peg {} to peg {}.".format(first_peg, last_peg))

        # Instruction 2: Move a stack of size num_disks - 1 from middle_peg to last_peg using first_peg as temporary peg
        solve_hanoi(num_disks - 1, middle_peg, first_peg, last_peg)

# Call the solve_hanoi function with arguments 3, 'A', 'B', and 'C' to solve the Tower of Hanoi puzzle with three disks
solve_hanoi(3, 'A', 'B', 'C')

## 6. Listing All Files in a Directory ##

import os

def list_files(current_path):
    if not os.path.isdir(current_path):  # Base case: current_path is not a directory
        print(current_path)
    else:  # General case: current_path is a directory
        for name in os.listdir(current_path):
            path = os.path.join(current_path, name)  # Join current_path and name
            list_files(path)  # Recursively call list_files() on the joined path

# Test the function by calling it on the "folder1"
list_files("folder1")

## 7. Merge Sort (Part 1) ##

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = 0
    j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Add the remaining elements from list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # Add the remaining elements from list2, if any
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

# Test the merge_sorted_lists() function on lists [2, 4, 7, 8] and [1, 3, 5, 6]
list1 = [2, 4, 7, 8]
list2 = [1, 3, 5, 6]
merged_lists = merge_sorted_lists(list1, list2)
print(merged_lists)

## 8. Merge Sort (Part 2) ##

def merge_sort(values):
    if len(values) < 2:  # Base case: list is sorted if length is smaller than 2
        return values
    
    midpoint = len(values) // 2  # Calculate the midpoint
    
    sorted_first_half = merge_sort(values[:midpoint])  # Sort the first half
    sorted_second_half = merge_sort(values[midpoint:])  # Sort the second half
    
    return merge_sorted_lists(sorted_first_half, sorted_second_half)  # Merge the sorted halves

# Test the merge_sort() function on list [2, 4, 7, 8, 1, 3, 5, 6]
values = [2, 4, 7, 8, 1, 3, 5, 6]
sorted_values = merge_sort(values)
print(sorted_values)