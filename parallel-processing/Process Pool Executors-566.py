## 1. Introduction ##

import pandas as pd

# Read the CSV file
job_postings = pd.read_csv('DataEngineer.csv')

# Get the number of rows and columns
num_rows = job_postings.shape[0]
num_cols = job_postings.shape[1]

print("Number of rows:", num_rows)
print("Number of columns:", num_cols)

## 2. Counting Word Occurrences ##

# Make Job Description column lowercase
job_postings["Job Description"] = job_postings["Job Description"].str.lower()

# Initialize frequency dictionary
frequency = {}

# Calculate frequency of "postgres"
frequency["postgres"] = job_postings["Job Description"].str.count("postgres").sum()

# Calculate frequency of "sql"
frequency["sql"] = job_postings["Job Description"].str.count("sql").sum()

# Print the frequency
print(frequency)

## 3. Counting All Skills ##

import pandas as pd

# Read Skills.csv
skills = pd.read_csv("Skills.csv")

# Initialize frequency dictionary
frequency = {}

# Calculate frequency of each skill in job_postings
for skill_name in skills["Name"]:
    frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()

# Print the frequency of "programming"
print(frequency["programming"])

## 4. Functionize the Code ##

import pandas as pd
import time

# Declare count_skills function
def count_skills(job_postings, skills):
    frequency = {}
    for skill_name in skills["Name"]:
        frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
    return frequency

# Measure execution time of count_skills function
start_time = time.time()
result = count_skills(job_postings, skills)
end_time = time.time()
runtime = end_time - start_time

print("Execution time:", runtime)

## 5. Splitting a DataFrame into Chunks ##

import math

def make_chunks(df, num_chunks):
    num_rows = df.shape[0]
    chunk_size = math.ceil(num_rows / num_chunks)
    chunks = [df[i:i+chunk_size] for i in range(0, num_rows, chunk_size)]
    return chunks

# Test the function
skill_chunks = make_chunks(skills, 8)

## 6. Process Pool Executor ##

import concurrent.futures

def increment(value):
    return value + 1

values = [1, 2, 3, 4, 5, 6, 7, 8]

# Create a list to store the Future objects
futures = []

# Create an Executor
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit tasks to the executor and store the Future objects in the futures list
    for value in values:
        future = executor.submit(increment, value)
        futures.append(future)

# Retrieve the results from the Future objects
results = [future.result() for future in futures]

# Inspect the results
print(results)

## 7. Multiprocessing Job Posting Analysis ##

import concurrent.futures

import concurrent.futures

# Your job_postings and skills DataFrames should be available at this point
# The make_chunks() and count_skills() functions should also be available

# Use the make_chunks() function to break the skills DataFrame into 8 chunks
skill_chunks = make_chunks(skills, 8)

def count_skills_wrapper(args):
    job_postings, skill_chunk = args
    return count_skills(job_postings, skill_chunk)

# Create an Executor
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Create a list to store the Future objects
    futures = []
    
    # Submit tasks to the executor and store the Future objects in the futures list
    for chunk in skill_chunks:
        future = executor.submit(count_skills_wrapper, (job_postings, chunk))
        futures.append(future)

# Retrieve the results from the Future objects
results = [future.result() for future in futures]

# Print the value of the first result
print(results[0])

## 8. Merging Results ##

merged_results = {}

for result in results:
    merged_results.update(result)

print(merged_results)

## 9. Performance Improvement ##

def count_skills(job_postings, skills):
    frequency = {}
    for skill_name in skills["Name"]:
        frequency[skill_name] = job_postings["Job Description"].str.count(skill_name).sum()
    return frequency

def count_skills_parallel(job_postings, skills, num_processes=4):
    # Calculate results using paralleld processing
    skill_chunks = make_chunks(skills, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(count_skills, job_postings, skill_chunk) for skill_chunk in skill_chunks]
    results = [future.result() for future in futures]
    # Merge results
    merged_results = {}
    for result in results:
        merged_results.update(result)
    return merged_results

import time

# Measure execution times here
import time

# Measure execution time of count_skills
start_normal = time.time()
frequency_normal = count_skills(job_postings, skills)
end_normal = time.time()
time_normal = end_normal - start_normal

# Measure execution time of count_skills_parallel
start_parallel = time.time()
frequency_parallel = count_skills_parallel(job_postings, skills)
end_parallel = time.time()
time_parallel = end_parallel - start_parallel

# Print the ratio
ratio = time_normal / time_parallel
print("Ratio: ", ratio)