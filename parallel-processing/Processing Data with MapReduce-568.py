## 1. Introduction ##

values = [98, 63, 55, 80, 45, 51, 91, 64, 65, 48, 48, 92, 76, 99, 57, 42, 79, 61, 63, 49]


# Example list of numbers
values = [98, 63, 55, 80, 45, 51, 91, 64, 65, 48, 48, 92, 76, 99, 57, 42, 79, 61, 63, 49]

import concurrent.futures

values = [98, 63, 55, 80, 45, 51, 91, 64, 65, 48, 48, 92, 76, 99, 57, 42, 79, 61, 63, 49]

def mapper(chunk):
    return min(chunk)

def reducer(result1, result2):
    return min(result1, result2)

def make_chunks(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    return chunks

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(mapper, chunks)
    overall_result = functools.reduce(reducer, results)
    return overall_result

min_value = map_reduce(values, 4, min, min)
print(min_value)

## 2. Length of Longest English Word ##

import concurrent.futures
import functools

def map_max_length(words_chunk):
    return len(max(words_chunk, key=len))

def reducer(result1, result2):
    return max(result1, result2)

def make_chunks(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    return chunks

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(mapper, chunks)
    overall_result = functools.reduce(reducer, results)
    return overall_result

with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]

max_len = map_reduce(words, 4, map_max_length, max)
print(max_len)

## 3. Longest English Word ##

import concurrent.futures
import functools

def map_max_len_str(words_chunk):
    return max(words_chunk, key=len)

def reduce_max_len_str(word1, word2):
    return word1 if len(word1) >= len(word2) else word2

def make_chunks(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    return chunks

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(mapper, chunks)
    overall_result = functools.reduce(reducer, results)
    return overall_result

with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]

max_len_str = map_reduce(words, 4, map_max_len_str, reduce_max_len_str)
print(max_len_str)

## 4. Searching with MapReduce ##

import concurrent.futures
import functools

def map_contains(words_chunk):
    return target in words_chunk

def reduce_contains(contains1, contains2):
    return contains1 or contains2

def make_chunks(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    return chunks

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(mapper, chunks)
    overall_result = functools.reduce(reducer, results)
    return overall_result

with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]

target = "pneumonoultramicroscopicsilicovolcanoconiosis"

is_contained = map_reduce(words, 4, map_contains, reduce_contains)
print(is_contained)

## 5. Counting Character Frequencies ##

import concurrent.futures
import functools

def map_char_count(words_chunk):
    char_freq = {}
    for word in words_chunk:
        for c in word:
            if c not in char_freq:
                char_freq[c] = 0
            char_freq[c] += 1
    return char_freq

def reduce_char_count(freq1, freq2):
    for c in freq2:
        if c in freq1:
            freq1[c] += freq2[c]
        else:
            freq1[c] = freq2[c]
    return freq1

def make_chunks(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    return chunks

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(mapper, chunks)
    overall_result = functools.reduce(reducer, results)
    return overall_result

with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]

char_freq = map_reduce(words, 4, map_char_count, reduce_char_count)
print(char_freq)

## 6. Average Word Length ##

import concurrent.futures
import functools

def map_average(words_chunk):
    word_sum = sum(len(word) for word in words_chunk)
    average = word_sum / len(words)
    return average

def reduce_average(res1, res2):
    return res1 + res2

def make_chunks(data, num_chunks):
    chunk_size = len(data) // num_chunks
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    return chunks

def map_reduce(data, num_processes, mapper, reducer):
    chunks = make_chunks(data, num_processes)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(mapper, chunks)
    overall_result = functools.reduce(reducer, results)
    return overall_result

with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]

average_word_len = map_reduce(words, 4, map_average, reduce_average)
print(average_word_len)

## 7. Rare Adjacent Characters ##

with open("english_words.txt") as f:
    words = [word.strip() for word in f.readlines()]
    
# def map_adjacent(words_chunk):
#     freq = {}
#     for word in words_chunk:
#         for i in range(len(word) - 1):
#             pair = word[i:i+2]
#             freq[pair] = freq.get(pair, 0) + 1
#     return freq



def map_adjacent(words_chunk):
    freq = {}
    for word in words_chunk:
        for i in range(len(word) - 1):
            pair = word[i:i+2]
            if pair not in freq:
                freq[pair] = 1
            else:
                freq[pair] += 1
    return freq


def reduce_adjacent(freq1, freq2):
    merged_freq = {}
    for pair, count in freq1.items():
        if pair in merged_freq:
            merged_freq[pair] += count
        else:
            merged_freq[pair] = count

    for pair, count in freq2.items():
        if pair in merged_freq:
            merged_freq[pair] += count
        else:
            merged_freq[pair] = count

    return merged_freq



pair_freq = map_reduce(words, 4, map_adjacent, reduce_adjacent)

unique_pairs = [pair for pair, count in pair_freq.items() if count == 1]