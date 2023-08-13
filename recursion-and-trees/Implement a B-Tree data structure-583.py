## 1. Introduction ##

from node import Node

class BTree:
    def __init__(self):
        self.root = Node()
        self.height = 0
        self.size = 0
    
    def __len__(self):
        return self.size

## 2. Key Lookup ##

from node import Node

class BTree:
    def __init__(self):
        self.root = Node()
        self.height = 0
        self.size = 0

    def __len__(self):
        return self.size
    
    def find_node(self, current_node, key):
        if current_node.contains_key(key):
            return current_node

        if current_node.is_leaf():
            return None

        child_index = current_node.get_insert_index(key)
        return self.find_node(current_node.children[child_index], key)

## 3. Helper Method for Contains ##

from node import Node

class BTree:
    def __init__(self):
        self.root = Node()
        self.height = 0
        self.size = 0

    def __len__(self):
        return self.size
    
    def _find_node(self, current_node, key):
        if current_node.contains_key(key):
            return current_node
        if current_node.is_leaf():
            return None
        child_index = current_node.get_insert_index(key)
        return self._find_node(current_node.children[child_index], key)
    
    def contains(self, key):
        return self._find_node(self.root, key) is not None

## 4. Value Lookup ##

from node import Node

class BTree:
    def __init__(self):
        self.root = Node()
        self.height = 0
        self.size = 0

    def __len__(self):
        return self.size
    
    def _find_node(self, current_node, key):
        if current_node.contains_key(key):
            return current_node
        if current_node.is_leaf():
            return None
        child_index = current_node.get_insert_index(key) 
        return self._find_node(current_node.children[child_index], key)
    
    def contains(self, key):
        node = self._find_node(self.root, key)
        return node is not None
    
    def get_value(self, key):
        node = self._find_node(self.root, key)
        if node is None:
            return None
        return node.get_value(key)

## 5. Adding Entries ##

from node import Node

class BTree:
    def __init__(self):
        self.root = Node()
        self.height = 0
        self.size = 0

    def __len__(self):
        return self.size
    
    def _find_node(self, current_node, key):
        if current_node.contains_key(key):
            return current_node
        if current_node.is_leaf():
            return None
        child_index = current_node.get_insert_index(key) 
        return self._find_node(current_node.children[child_index], key)
    
    def contains(self, key):
        node = self._find_node(self.root, key)
        return node is not None
    
    def get_value(self, key):
        node = self._find_node(self.root, key)
        if node is None:
            return None
        return node.get_value(key)
    
    def add(self, current_node, key, value):
        if current_node.is_leaf():
            current_node.insert_entry(key, value)
        else:
            child_index = current_node.get_insert_index(key)
            child = current_node.children[child_index]
            self.add(child, key, value)

## 6. Helper Method for Add ##

from node import Node

class BTree:
    def __init__(self):
        self.root = Node()
        self.height = 0
        self.size = 0

    def __len__(self):
        return self.size
    
    def _find_node(self, current_node, key):
        if current_node.contains_key(key):
            return current_node
        if current_node.is_leaf():
            return None
        child_index = current_node.get_insert_index(key) 
        return self._find_node(current_node.children[child_index], key)
    
    def contains(self, key):
        node = self._find_node(self.root, key)
        return node is not None
    
    def get_value(self, key):
        node = self._find_node(self.root, key)
        if node is None:
            return None
        return node.get_value(key)
    
    def _add(self, current_node, key, value):
        if current_node.is_leaf():
            current_node.insert_entry(key, value)
        else:
            child_index = current_node.get_insert_index(key)
            self._add(current_node.children[child_index], key, value)
    
    def add(self, key, value):
        self._add(self.root, key, value)
        self.size += 1

## 7. Testing the Implementation ##

bt = BTree()

for i in range(1, 11):
    bt.add(i, i)

print(bt.root.keys)
print(bt.root.children)

## 8. Node Splitting ##

class BTree:
    def __init__(self, split_threshold):
        self.root = Node()
        self.height = 0
        self.size = 0
        self.split_threshold = split_threshold

    def __len__(self):
        return self.size
    
    def _find_node(self, current_node, key):
        if current_node.contains_key(key):
            return current_node
        if current_node.is_leaf():
            return None
        child_index = current_node.get_insert_index(key) 
        return self._find_node(current_node.children[child_index], key)
    
    def contains(self, key):
        node = self._find_node(self.root, key)
        return node is not None
    
    def get_value(self, key):
        node = self._find_node(self.root, key)
        if node is None:
            return None
        return node.get_value(key)
    
    def _add(self, current_node, key, value):
        if current_node.is_leaf():
            current_node.insert_entry(key, value)
        else:
            child_index = current_node.get_insert_index(key)
            self._add(current_node.children[child_index], key, value)
        
        if len(current_node) > self.split_threshold:
            parent = current_node.split()
            if current_node is self.root:
                self.root = parent
    
    def add(self, key, value):
        self._add(self.root, key, value)
        self.size += 1

## 9. Complexity Analysis ##

class BTree:
    def __init__(self, split_threshold):
        self.split_threshold = split_threshold
        self.root = Node()
        self.height = 0
        self.size = 0

    def __len__(self):
        return self.size
    
    def _find_node(self, current_node, key):
        if current_node.contains_key(key):
            return current_node
        if current_node.is_leaf():
            return None
        child_index = current_node.get_insert_index(key) 
        return self._find_node(current_node.children[child_index], key)
    
    def contains(self, key):
        node = self._find_node(self.root, key)
        return node is not None
    
    def get_value(self, key):
        node = self._find_node(self.root, key)
        if node is None:
            return None
        return node.get_value(key)
    
    def _add(self, current_node, key, value):
        if current_node.is_leaf():
            current_node.insert_entry(key, value)
        else:
            child_index = current_node.get_insert_index(key)
            self._add(current_node.children[child_index], key, value)
        
        if len(current_node) > self.split_threshold:
            parent = current_node.split()
            if current_node is self.root:
                self.root = parent
                self.height += 1
    
    def add(self, key, value):
        self._add(self.root, key, value)
        self.size += 1
import matplotlib.pyplot as plt

bt = BTree(2)
heights = []

for i in range(1, 1001):
    bt.add(i, i)
    heights.append(bt.height)

plt.plot(heights)
plt.xlabel('Insertion Count')
plt.ylabel('Tree Height')
plt.title('B-Tree Height')
plt.show()