## 2. Generators in Python ##

def squares(N):
    i = 0
    while True:
        yield i ** 2
        i += 1
        if i >= N:
            break

squared_values = []
generator = squares(20)

while True:
    try:
        value = next(generator)
        squared_values.append(value)
    except StopIteration:
        break

## 4. Manipulating Generators in Tasks ##

#log = open('example_log.txt')

# def parse_log(log_file):
#     for line in log_file:
#         fields = line.strip().split()
#         log_tuple = tuple(fields)
#         yield log_tuple

def parse_log(log_file):
    for line in log_file:
        fields = line.strip().split()
        ip_address = fields[0]
        timestamp = fields[3] + ' ' + fields[4]
        request_path = fields[5]
        request = fields[6] 
        status_code = fields[8]
        size = fields[9]
        referrer = fields[10]
        user_agent = ' '.join(fields[11:])
        log_tuple = (ip_address, timestamp, request_path, request, status_code, size, referrer, user_agent)
        yield log_tuple



        
log_file = open('example_log.txt')
log_generator = parse_log(log_file)
first_line = next(log_generator)
log_file.close()

print(first_line)

## 5. Data Cleaning in Parse Log ##

from datetime import datetime

def parse_log(log_file):
    for line in log_file:
        fields = line.strip().split()
        ip_address = fields[0]
        timestamp = datetime.strptime(fields[3] + ' ' + fields[4], '[%d/%b/%Y:%H:%M:%S %z]')
        request_path = fields[5].strip('"')
        request = fields[6].strip('"')
        status_code = int(fields[8])
        size = int(fields[9])
        referrer = fields[10].strip('"')
        user_agent = ' '.join(fields[11:]).strip('"')
        log_tuple = (ip_address, timestamp, request_path, request, status_code, size, referrer, user_agent)
        yield log_tuple

log_file = open('example_log.txt')
log_generator = parse_log(log_file)
first_line = next(log_generator)
log_file.close()

print(first_line)

## 6. Write to CSV ##

import csv

def build_csv(lines, file, header=None):
    if header:
        lines = [header] + list(lines)
    writer = csv.writer(file)
    writer.writerows(lines)
    file.seek(0)
    return file

log = open('example_log.txt')
parsed = parse_log(log)

with open('temporary.csv', 'w+') as csv_file:
    header = ('ip', 'time_local', 'request_type', 'request_path', 'status', 'bytes_sent', 'http_referrer', 'http_user_agent')
    csv_file = build_csv(parsed, csv_file, header)
    contents = csv_file.readlines()
    print(contents[:5])

## 7. Chaining Iterators ##

import csv
import itertools

def parse_log(log_file):
    for line in log_file:
        fields = line.strip().split()
        ip_address = fields[0]
        timestamp = datetime.strptime(fields[3] + ' ' + fields[4], '[%d/%b/%Y:%H:%M:%S %z]')
        request_path = fields[5].strip('"')
        request = fields[6].strip('"')
        status_code = int(fields[8])
        size = int(fields[9])
        referrer = fields[10].strip('"')
        user_agent = ' '.join(fields[11:]).strip('"')
        log_tuple = (ip_address, timestamp, request_path, request, status_code, size, referrer, user_agent)
        yield log_tuple

def build_csv(lines, file, header=None):
    if header:
        lines = itertools.chain([header], lines)
    writer = csv.writer(file)
    writer.writerows(lines)
    file.seek(0)
    return file

log = open('example_log.txt')
parsed = parse_log(log)

with open('temporary.csv', 'w+') as csv_file:
    header = ('ip', 'time_local', 'request_type', 'request_path', 'status', 'bytes_sent', 'http_referrer', 'http_user_agent')
    csv_file = build_csv(parsed, csv_file, header)
    contents = csv_file.readlines()
    print(contents[:5])

## 8. Counting Unique Request Types ##

import csv
from collections import defaultdict

def count_unique_requests(csv_file):
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # skip header
    uniques = defaultdict(int)
    for row in csv_reader:
        uniques[row[2]] += 1
    return dict(uniques)

log = open('example_log.txt')
parsed = parse_log(log)

with open('temporary.csv', 'w+') as csv_file:
    header = ('ip', 'time_local', 'request_type', 'request_path', 'status', 'bytes_sent', 'http_referrer', 'http_user_agent')
    csv_file = build_csv(parsed, csv_file, header)
    uniques = count_unique_requests(csv_file)
    print(uniques)

## 9. Task Reusability ##

import csv

def count_unique_requests(csv_file):
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # skip header
    uniques = defaultdict(int)
    for row in csv_reader:
        uniques[row[2]] += 1
    return list(uniques.items())

def build_csv(lines, file, header=None):
    if header:
        lines = itertools.chain([header], lines)
    writer = csv.writer(file)
    writer.writerows(lines)
    file.seek(0)
    return file

log = open('example_log.txt')
parsed = parse_log(log)

with open('temporary.csv', 'w+') as csv_file:
    header = ('ip', 'time_local', 'request_type', 'request_path', 'status', 'bytes_sent', 'http_referrer', 'http_user_agent')
    csv_file = build_csv(parsed, csv_file, header)
    uniques = count_unique_requests(csv_file)

with open('summarized.csv', 'w+') as summary_file:
    header = ('request_type', 'count')
    build_csv(uniques, summary_file, header)
    summary_file.seek(0)
    print(summary_file.read())