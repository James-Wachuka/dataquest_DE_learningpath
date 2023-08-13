## 1. Introduction ##

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

my_entry = Entry(12345, "my value")

## 2. Internal Structure ##

class Dictionary:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [None] * num_buckets
        self.length = 0

my_dict = Dictionary(5)

## 3. Separate Chaining ##

class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, key, value):
        new_node = LinkedListNode(key, value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

class Dictionary:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [LinkedList() for _ in range(num_buckets)]
        self.length = 0

my_dict = Dictionary(5)

## 4. Hashing ##

class Dictionary:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [LinkedList() for _ in range(num_buckets)]
        self.length = 0
        
    def _get_index(self, key):
        hashcode = hash(key)
        index = hashcode % self.num_buckets
        return index

my_dict = Dictionary(5)
index = my_dict._get_index("data engineering")

## 5. Adding an Entry ##

class Dictionary:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [LinkedList() for _ in range(num_buckets)]
        self.length = 0
        
    def _get_index(self, key):
        hashcode = hash(key)
        return hashcode % self.num_buckets
    
    def put(self, key, value):
        index = self._get_index(key)
        found_key = False
        
        for entry in self.buckets[index]:
            if entry.key == key:
                entry.value = value
                found_key = True
                break
        
        if not found_key:
            new_entry = Entry(key, value)
            self.buckets[index].append(new_entry)
            self.length += 1

my_dict = Dictionary(5)
my_dict.put("my key", 1)

## 6. Locating an Entry ##

class Dictionary:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [LinkedList() for _ in range(num_buckets)]
        self.length = 0
        
    def _get_index(self, key):
        hashcode = hash(key)
        return hashcode % self.num_buckets
    
    def put(self, key, value):
        index = self._get_index(key)
        found_key = False
        
        for entry in self.buckets[index]:
            if entry.key == key:
                entry.value = value
                found_key = True
                break
        
        if not found_key:
            new_entry = Entry(key, value)
            self.buckets[index].append(new_entry)
            self.length += 1
    
    def get_value(self, key):
        index = self._get_index(key)
        
        for entry in self.buckets[index]:
            if entry.key == key:
                return entry.value
        
        raise KeyError(key)

my_dict = Dictionary(5)
my_dict.put("my key", 1)
print(my_dict.get_value("my key"))
my_dict.put("my key", 2)
print(my_dict.get_value("my key"))

## 7. Deleting an Entry ##

class Dictionary:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [LinkedList() for _ in range(num_buckets)]
        self.length = 0
        
    def _get_index(self, key):
        hashcode = hash(key)
        return hashcode % self.num_buckets
    
    def put(self, key, value):
        index = self._get_index(key)
        found_key = False
        
        for entry in self.buckets[index]:
            if entry.key == key:
                entry.value = value
                found_key = True
                break
        
        if not found_key:
            new_entry = Entry(key, value)
            self.buckets[index].append(new_entry)
            self.length += 1
    
    def get_value(self, key):
        index = self._get_index(key)
        
        for entry in self.buckets[index]:
            if entry.key == key:
                return entry.value
        
        raise KeyError(key)
    
    def delete(self, key):
        index = self._get_index(key)
        new_bucket = LinkedList()
        
        for entry in self.buckets[index]:
            if entry.key != key:
                new_bucket.append(entry)
        
        if len(new_bucket) < len(self.buckets[index]):
            self.length -= 1
        
        self.buckets[index] = new_bucket
    
my_dict = Dictionary(5)
my_dict.put("my key", 1)
my_dict.delete("my key")
print(my_dict.length)

## 8. Polishing the Dictionary ##

class Dictionary:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [LinkedList() for _ in range(num_buckets)]
        self.length = 0
        
    def _get_index(self, key):
        hashcode = hash(key)
        return hashcode % self.num_buckets
    
    def put(self, key, value):
        index = self._get_index(key)
        found_key = False
        
        for entry in self.buckets[index]:
            if entry.key == key:
                entry.value = value
                found_key = True
                break
        
        if not found_key:
            new_entry = Entry(key, value)
            self.buckets[index].append(new_entry)
            self.length += 1
    
    def get_value(self, key):
        index = self._get_index(key)
        
        for entry in self.buckets[index]:
            if entry.key == key:
                return entry.value
        
        raise KeyError(key)
    
    def delete(self, key):
        index = self._get_index(key)
        new_bucket = LinkedList()
        
        for entry in self.buckets[index]:
            if entry.key != key:
                new_bucket.append(entry)
        
        if len(new_bucket) < len(self.buckets[index]):
            self.length -= 1
        
        self.buckets[index] = new_bucket
    
    def __getitem__(self, key):
        return self.get_value(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __len__(self):
        return self.length

my_dict = Dictionary(5)
my_dict["my key"] = 2
print(my_dict["my key"])
print(len(my_dict))

## 9. Dictionary Time Complexity ##

import time
import random
import matplotlib.pyplot as plt

random.seed(0)

times = []
number_of_entries = 1000
keys = range(number_of_entries)

d = dict()

def plot_times(times):
    plt.plot(times)
    plt.xlabel('Insertion Number')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time for Dictionary Insertion')
    plt.show()

for key in keys:
    start = time.time()
    d[key] = key
    end = time.time()
    times.append(end - start)

plot_times(times)

## 10. Selecting the Table Size ##

import matplotlib.pyplot as plt
import pandas as pd

def plot_buckets_sizes(dictionary):
    plt.bar(range(dictionary.num_buckets), [len(dictionary.buckets[i]) for i in range(dictionary.num_buckets)])
    plt.xlabel('Bucket Index')
    plt.ylabel('Number of Elements')
    plt.title('Number of Elements in Each Bucket')
    plt.show()

employees = pd.read_csv("employees.csv", index_col="Id")

dictionary = Dictionary(100)

for identifier, data in employees.iterrows():
    dictionary[identifier] = data

plot_buckets_sizes(dictionary)