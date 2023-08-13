## 1. Introduction ##

import csv

with open('ratings.csv') as file:
    reader = csv.reader(file)
    rows = list(reader)
    header = rows[0]
    rows = rows[1:]

print(len(rows))

## 2. Extending the B-tree ##

from btree import BTree

class CSVIndex(BTree):
    def __init__(self, split_threshold):
        super().__init__(split_threshold)

# Outside of the class definition
index = CSVIndex(10)

## 3. Reading the CSV Into the Tree ##

from btree import BTree
import csv

class CSVIndex(BTree):
    def __init__(self, split_threshold, csv_filename, col_name):
        super().__init__(split_threshold)
        self.col_name = col_name

        with open(csv_filename) as file:
            reader = csv.reader(file)
            rows = list(reader)
            header = rows[0]
            rows = rows[1:]
            col_index = header.index(col_name)

            for row in rows:
                key = float(row[col_index])
                value = row
                self.add(key, value)

# Outside of the class definition
metacritic_index = CSVIndex(2, 'ratings.csv', 'Metacritic')
print(len(metacritic_index))

## 4. Movie Lookup ##

index = CSVIndex(3, 'ratings.csv', 'Imdb')
movie_6_3 = index.get_value(6.3)
movie_8_5 = index.get_value(8.5)

print(movie_6_3)
print(movie_8_5)

## 5. Implementing Range Queries ##

import csv

class CSVIndex(BTree):

    def __init__(self, split_threshold, csv_filename, col_name):
        super().__init__(split_threshold)
        self.col_name = col_name
        with open(csv_filename) as file:
            rows = list(csv.reader(file))
            header = rows[0]
            rows = rows[1:]
            col_index = header.index(col_name)
            for row in rows:
                self.add(float(row[col_index]), row)

    def _range_query(self, range_start, range_end, current_node, min_key, max_key):
        if range_end < min_key or range_start > max_key:
            return []
        
        results = []
        
        for i, key in enumerate(current_node.keys):
            if range_start <= key <= range_end:
                results.append(current_node.values[i])
        
        return results

## 6. Implementing Range Queries ##

import csv

class CSVIndex(BTree):

    def __init__(self, split_threshold, csv_filename, col_name):
        super().__init__(split_threshold)
        self.col_name = col_name
        with open(csv_filename) as file:
            rows = list(csv.reader(file))
            header = rows[0]
            rows = rows[1:]
            col_index = header.index(col_name)
            for row in rows:
                self.add(float(row[col_index]), row)
                
    def _range_query(self, range_start, range_end, current_node, min_key, max_key):
        if range_start > max_key or range_end < min_key:
            return []
        results = []
        for i, key in enumerate(current_node.keys):
            if range_start <= key <= range_end:
                results.append(current_node.values[i])
        
        if not current_node.is_leaf():
            for i, child in enumerate(current_node.children):
                new_min_key = min_key if i == 0 else current_node.keys[i - 1]
                new_max_key = max_key if i == len(current_node) else current_node.keys[i]
                results += self._range_query(range_start, range_end, child, new_min_key, new_max_key)
        
        return results

## 7. Polishing the Range Query Method ##

import csv

class CSVIndex(BTree):

    def __init__(self, split_threshold, csv_filename, col_name):
        super().__init__(split_threshold)
        self.col_name = col_name
        with open(csv_filename) as file:
            rows = list(csv.reader(file))
            header = rows[0]
            rows = rows[1:]
            col_index = header.index(col_name)
            for row in rows:
                self.add(float(row[col_index]), row)
                
    def _range_query(self, range_start, range_end, current_node, min_key, max_key):
        if range_start > max_key or range_end < min_key:
            return []
        results = []
        for i, key in enumerate(current_node.keys):
            if range_start <= key <= range_end:
                results.append(current_node.values[i])
        
        if not current_node.is_leaf():
            for i, child in enumerate(current_node.children):
                new_min_key = min_key if i == 0 else current_node.keys[i - 1]
                new_max_key = max_key if i == len(current_node) else current_node.keys[i]
                results += self._range_query(range_start, range_end, child, new_min_key, new_max_key)
        
        return results
    
    def range_query(self, range_start, range_end):
        return self._range_query(range_start, range_end, self.root, float('-inf'), float('inf'))

## 8. Complexity of Range Queries ##

import csv

class CSVIndex(BTree):

    def __init__(self, split_threshold, csv_filename, col_name):
        super().__init__(split_threshold)
        self.col_name = col_name
        with open(csv_filename) as file:
            rows = list(csv.reader(file))
            header = rows[0]
            rows = rows[1:]
            col_index = header.index(col_name)
            for row in rows:
                self.add(float(row[col_index]), row)
                
    def _range_query(self, range_start, range_end, current_node, min_key, max_key):
        if range_start > max_key or range_end < min_key:
            return []
        results = []
        for i, key in enumerate(current_node.keys):
            if range_start <= key <= range_end:
                results.append(current_node.values[i])
        
        if not current_node.is_leaf():
            for i, child in enumerate(current_node.children):
                new_min_key = min_key if i == 0 else current_node.keys[i - 1]
                new_max_key = max_key if i == len(current_node) else current_node.keys[i]
                results += self._range_query(range_start, range_end, child, new_min_key, new_max_key)
        
        return results
    
    def range_query(self, range_start, range_end):
        return self._range_query(range_start, range_end, self.root, float('-inf'), float('inf'))

# Create the index
index = CSVIndex(2, 'ratings.csv', 'Rotten_Tomatoes')

# Perform low rating range query
low_rating = index.range_query(0, 15)
#print("Movies with low Rotten Tomatoes ratings (0-15):")
for movie in low_rating:
    print(movie)

# Perform high rating range query
high_rating = index.range_query(90, 100)
#print("Movies with high Rotten Tomatoes ratings (90-100):")
for movie in high_rating:
    print(movie)

## 9. Saving the Index ##

import pickle
import csv

class CSVIndex(BTree):

    def __init__(self, split_threshold, csv_filename, col_name):
        super().__init__(split_threshold)
        self.col_name = col_name
        with open(csv_filename) as file:
            rows = list(csv.reader(file))
            header = rows[0]
            rows = rows[1:]
            col_index = header.index(col_name)
            for row in rows:
                self.add(float(row[col_index]), row)
                
    def _range_query(self, range_start, range_end, current_node, min_key, max_key):
        if range_start > max_key or range_end < min_key:
            return []
        results = []
        for i, key in enumerate(current_node.keys):
            if range_start <= key <= range_end:
                results.append(current_node.values[i])
        
        if not current_node.is_leaf():
            for i, child in enumerate(current_node.children):
                new_min_key = min_key if i == 0 else current_node.keys[i - 1]
                new_max_key = max_key if i == len(current_node) else current_node.keys[i]
                results += self._range_query(range_start, range_end, child, new_min_key, new_max_key)
        
        return results
    
    def range_query(self, range_start, range_end):
        return self._range_query(range_start, range_end, self.root, float('-inf'), float('inf'))

    def save(self, filename):
        with open(f"{filename}.pickle", "wb") as file:
            pickle.dump(self, file)
            

# Create the fandango_index
fandango_index = CSVIndex(10, 'ratings.csv', 'Fandango')

# Save the fandango_index to a file
fandango_index.save("fandango")

## 10. Loading the Index ##

import csv
import pickle 

class CSVIndex(BTree):

    def __init__(self, split_threshold, csv_filename, col_name):
        super().__init__(split_threshold)
        self.col_name = col_name
        with open(csv_filename) as file:
            rows = list(csv.reader(file))
            header = rows[0]
            rows = rows[1:]
            col_index = header.index(col_name)
            for row in rows:
                self.add(float(row[col_index]), row)
                
    def _range_query(self, range_start, range_end, current_node, min_key, max_key):
        if range_start > max_key or range_end < min_key:
            return []
        results = []
        for i, key in enumerate(current_node.keys):
            if range_start <= key <= range_end:
                results.append(current_node.values[i])
        
        if not current_node.is_leaf():
            for i, child in enumerate(current_node.children):
                new_min_key = min_key if i == 0 else current_node.keys[i - 1]
                new_max_key = max_key if i == len(current_node) else current_node.keys[i]
                results += self._range_query(range_start, range_end, child, new_min_key, new_max_key)
        
        return results
    
    def range_query(self, range_start, range_end):
        return self._range_query(range_start, range_end, self.root, float('-inf'), float('inf'))

    def save(self, filename):
        with open('{}.pickle'.format(filename), 'wb') as f:
            pickle.dump(self, f)
            
    @staticmethod
    def load(filename):
        with open('{}.pickle'.format(filename), 'rb') as f:
            return pickle.load(f)
            

# Load the CSVIndex object from file
loaded_index = CSVIndex.load("fandango")

# Print the value of col_name for the loaded index
print(loaded_index.col_name)