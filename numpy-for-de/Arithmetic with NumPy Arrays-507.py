## 1. Introduction ##

import numpy as np
table = np.array([
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])

col = table[:, 1]
print(col)

row = table[2, :]
print(row)

center = table[1:3, 1:4]
print(center)

## 2. Adding ndarrays ##

def add_list_values(list1, list2):
    result = []
    for i in range(len(list1)):
        sum_value = list1[i] + list2[i]
        result.append(sum_value)
    return result

## 3. Comparing Ndarrays to Lists ##

import time
import random
import numpy as np

random.seed(0)

# Generate test lists
list1 = [random.randint(0, 1000) for _ in range(100000)]
list2 = [random.randint(0, 1000) for _ in range(100000)]

# Measure the execution time of adding lists with add_list_values
start = time.time()
add_list_values(list1, list2)
end = time.time()
time_list = end - start

# Convert lists to NumPy arrays
x1 = np.array(list1)
x2 = np.array(list2)

# Measure the execution time of adding ndarrays
start = time.time()
x3 = x1 + x2
end = time.time()
time_array = end - start

# Compute the ratio between time_list and time_array
ratio = time_list / time_array

print("Ratio (time_list / time_array):", ratio)

## 5. Arithmetic Operations ##

import numpy as np

people_data = np.array([
    [27, 67, 1.65],
    [35, 81, 1.84],
    [29, 55, 1.60],
    [41, 73, 1.79]
])

# Extract the weight column (column index 1)
w = people_data[:, 1]

# Extract the height column (column index 2)
h = people_data[:, 2]

# Compute the BMI using ndarray arithmetic
BMI = w / h**2

print("BMI:", BMI)

## 6. Arithmetic in Higher Dimensions ##

import numpy as np

scores = np.array([
    [46, 74, 52, 81],
    [75, 45, 67, 53],
    [67, 80, 73, 63],
    [59, 94, 43, 78]
])

# Get the first two columns of scores
scores_day1 = scores[:, :2]

# Get the last two columns of scores
scores_day2 = scores[:, 2:]

# Get the shape of scores_day1
shape1 = scores_day1.shape

# Get the shape of scores_day2
shape2 = scores_day2.shape

print("Shape of scores_day1:", shape1)
print("Shape of scores_day2:", shape2)

# Calculate the total score of each person for each game
total_scores = scores_day1 + scores_day2

print("Total scores:")
print(total_scores)

## 7. Minimum and Maximum ##

import numpy as np

total_scores = np.array([
    [98, 155],
    [142, 98],
    [140, 143],
    [102, 172]
])

# Get the total scores of game 1
scores_game1 = total_scores[:, 0]

# Get the total scores of game 2
scores_game2 = total_scores[:, 1]

# Compute the minimum and maximum total scores of game 1
min_game1 = np.min(scores_game1)
max_game1 = np.max(scores_game1)

# Compute the minimum and maximum total scores of game 2
min_game2 = np.min(scores_game2)
max_game2 = np.max(scores_game2)

print("Scores of game 1:", scores_game1)
print("Scores of game 2:", scores_game2)
print("Minimum score of game 1:", min_game1)
print("Maximum score of game 1:", max_game1)
print("Minimum score of game 2:", min_game2)
print("Maximum score of game 2:", max_game2)

## 8. The Axis Parameter ##

import numpy as np

total_scores = np.array([
    [98, 155],
    [142, 98],
    [140, 143],
    [102, 172]
])

# Calculate the maximum score of both games
max_game_scores = total_scores.max(axis=0)

# Calculate the minimum score of both games
min_game_scores = total_scores.min(axis=0)

# Calculate the maximum score that each person obtained overall games
max_people_scores = total_scores.max(axis=1)

# Calculate the minimum score that each person obtained overall games
min_people_scores = total_scores.min(axis=1)

# Print the results
print("Maximum scores of both games:", max_game_scores)
print("Minimum scores of both games:", min_game_scores)
print("Maximum scores for each person:", max_people_scores)
print("Minimum scores for each person:", min_people_scores)

## 9. Sum ##

import numpy as np

total_scores = np.array([
    [98, 155],
    [142, 98],
    [140, 143],
    [102, 172]
])

# Calculate the total score of each person over the two games (sum over the rows)
total_people_score = np.sum(total_scores, axis=1)

# Assign the maximum score over the two games to a variable named max_score
max_score = np.max(total_people_score)

print("Total score of each person:", total_people_score)
print("Maximum score over the two games:", max_score)