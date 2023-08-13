## 1. Introduction ##

class Node:
    def __init__(self, keys=None, values=None):
        self.keys = keys if keys is not None else []
        self.values = values if values is not None else []
    
    def __len__(self):
        return len(self.values)

## 2. Implementing Children References ##

class Node:
    def __init__(self, keys=None, values=None, children=None):
        self.keys = keys or []
        self.values = values or []
        self.set_children(children)
    
    def __len__(self):
        return len(self.values)
    
    def set_children(self, children):
        self.children = children if children is not None else []
    
    def is_leaf(self):
        return len(self.children) == 0

## 3. Setting Parent References ##

class Node:
    def __init__(self, keys=None, values=None, children=None, parent=None):
        self.keys = keys or []
        self.values = values or []
        self.parent = parent
        self.set_children(children)
    
    def set_children(self, children):
        self.children = children or []
        for child in self.children:
            child.parent = self
    
    def __len__(self):
        return len(self.values)
    
    def is_leaf(self):
        return len(self.children) == 0

## 4. Key Lookup in Node ##

class Node:
    def __init__(self, keys=None, values=None, children=None, parent=None):
        self.keys = keys or []
        self.values = values or []
        self.parent = parent
        self.set_children(children) 
        
    def set_children(self, children): 
        self.children = children or []
        for child in self.children:
            child.parent = self
    
    def __len__(self):
        return len(self.values)

    def is_leaf(self):
        return len(self.children) == 0
    
    def contains_key(self, key):
        return key in self.keys


## 5. Value Lookup in Node ##

class Node:
    def __init__(self, keys=None, values=None, children=None, parent=None):
        self.keys = keys or []
        self.values = values or []
        self.parent = parent
        self.set_children(children) 
        
    def set_children(self, children): 
        self.children = children or []
        for child in self.children:
            child.parent = self
    
    def __len__(self):
        return len(self.values)

    def is_leaf(self):
        return len(self.children) == 0
    
    def contains_key(self, key):
        return key in self.keys
    
    def get_value(self, key):
        index = self.keys.index(key) if key in self.keys else -1
        return self.values[index] if index != -1 else None

## 6. Inserting Values ##

import bisect

class Node:
    def __init__(self, keys=None, values=None, children=None, parent=None):
        self.keys = keys or []
        self.values = values or []
        self.parent = parent
        self.set_children(children) 
        
    def set_children(self, children): 
        self.children = children or []
        for child in self.children:
            child.parent = self
    
    def __len__(self):
        return len(self.values)

    def is_leaf(self):
        return len(self.children) == 0
    
    def contains_key(self, key):
        return key in self.keys
    
    def get_value(self, key):
        for i, k in enumerate(self.keys):
            if k == key:
                return self.values[i]
        return None
    
    def get_insert_index(self, key):
        return bisect.bisect(self.keys, key)
    
    def insert_entry(self, key, value):
        insert_index = self.get_insert_index(key)
        self.keys.insert(insert_index, key)
        self.values.insert(insert_index, value)
        return insert_index

## 7. Splitting Parentless Nodes ##

import bisect

class Node:
    
    def __init__(self, keys=None, values=None, children=None, parent=None):
        self.keys = keys or []
        self.values = values or []
        self.parent = parent
        self.set_children(children) 
        
    def set_children(self, children): 
        self.children = children or []
        for child in self.children:
            child.parent = self
    
    def __len__(self):
        return len(self.values)

    def is_leaf(self):
        return len(self.children) == 0
    
    def contains_key(self, key):
        return key in self.keys
    
    def get_value(self, key):
        for i, k in enumerate(self.keys):
            if k == key:
                return self.values[i]
        return None
    
    def get_insert_index(self, key):
        return bisect.bisect(self.keys, key)

    def insert_entry(self, key, value):
        insert_index = self.get_insert_index(key)
        self.keys.insert(insert_index, key)
        self.values.insert(insert_index, value)
        return insert_index
    
    def split_no_parent(self):
        split_index = len(self) // 2
        key_to_move_up = self.keys[split_index]
        value_to_move_up = self.values[split_index]
        
        right_node = Node(
            keys=self.keys[split_index+1:],
            values=self.values[split_index+1:],
            children=self.children[split_index+1:],
        )
        
        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]
        self.children = self.children[:split_index+1]
        
        parent = Node(
            keys=[key_to_move_up],
            values=[value_to_move_up],
            children=[self, right_node],
        )
        
        return parent

## 8. Inserting a Child ##

import bisect

class Node:
    
    def __init__(self, keys=None, values=None, children=None, parent=None):
        self.keys = keys or []
        self.values = values or []
        self.parent = parent
        self.set_children(children) 
        
    def set_children(self, children): 
        self.children = children or []
        for child in self.children:
            child.parent = self
    
    def __len__(self):
        return len(self.values)

    def is_leaf(self):
        return len(self.children) == 0
    
    def contains_key(self, key):
        return key in self.keys
    
    def get_value(self, key):
        for i, k in enumerate(self.keys):
            if k == key:
                return self.values[i]
        return None
    
    def get_insert_index(self, key):
        return bisect.bisect(self.keys, key)

    def insert_entry(self, key, value):
        insert_index = self.get_insert_index(key)
        self.keys.insert(insert_index, key)
        self.values.insert(insert_index, value)
        return insert_index
    
    def split_no_parent(self):
        split_index = len(self) // 2
        key_to_move_up = self.keys[split_index]
        value_to_move_up = self.values[split_index]
        right_node = Node(self.keys[split_index+1:], self.values[split_index+1:], self.children[split_index+1:])
        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]
        self.children = self.children[:split_index+1]
        parent = Node([key_to_move_up], [value_to_move_up], [self, right_node])
        return parent
    
    def insert_child(self, insert_index, child):
        self.children.insert(insert_index, child)
        child.parent = self

## 9. Splitting Nodes ##

import bisect

class Node:
    
    def __init__(self, keys=None, values=None, children=None, parent=None):
        self.keys = keys or []
        self.values = values or []
        self.parent = parent
        self.set_children(children) 
        
    def set_children(self, children): 
        self.children = children or []
        for child in self.children:
            child.parent = self
    
    def __len__(self):
        return len(self.values)

    def is_leaf(self):
        return len(self.children) == 0
    
    def contains_key(self, key):
        return key in self.keys
    
    def get_value(self, key):
        for i, k in enumerate(self.keys):
            if k == key:
                return self.values[i]
        return None
    
    def get_insert_index(self, key):
        return bisect.bisect(self.keys, key)

    def insert_entry(self, key, value):
        insert_index = self.get_insert_index(key)
        self.keys.insert(insert_index, key)
        self.values.insert(insert_index, value)
        return insert_index
    
    def split_no_parent(self):
        split_index = len(self) // 2
        key_to_move_up = self.keys[split_index]
        value_to_move_up = self.values[split_index]
        right_node = Node(self.keys[split_index+1:], self.values[split_index+1:], self.children[split_index+1:])
        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]
        self.children = self.children[:split_index+1]
        parent = Node([key_to_move_up], [value_to_move_up], [self, right_node])
        return parent

    def insert_child(self, insert_index, child):
        self.children.insert(insert_index, child)
        child.parent = self
    
    def split_with_parent(self):
        split_index = len(self) // 2
        key_to_move_up = self.keys[split_index]
        value_to_move_up = self.values[split_index]
        right_node = Node(
            keys=self.keys[split_index+1:],
            values=self.values[split_index+1:],
            children=self.children[split_index+1:],
        )
        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]
        self.children = self.children[:split_index+1]
        
        insert_index = self.parent.insert_entry(key_to_move_up, value_to_move_up)
        self.parent.insert_child(insert_index + 1, right_node)
        
        return self.parent

## 10. Finalizing the Node Implementation ##

import bisect

class Node:
    
    def __init__(self, keys=None, values=None, children=None, parent=None):
        self.keys = keys or []
        self.values = values or []
        self.parent = parent
        self.set_children(children) 
        
    def set_children(self, children): 
        self.children = children or []
        for child in self.children:
            child.parent = self
    
    def __len__(self):
        return len(self.values)

    def is_leaf(self):
        return len(self.children) == 0
    
    def contains_key(self, key):
        return key in self.keys
    
    def get_value(self, key):
        for i, k in enumerate(self.keys):
            if k == key:
                return self.values[i]
        return None
    
    def get_insert_index(self, key):
        return bisect.bisect(self.keys, key)

    def insert_entry(self, key, value):
        insert_index = self.get_insert_index(key)
        self.keys.insert(insert_index, key)
        self.values.insert(insert_index, value)
        return insert_index
    
    def split_no_parent(self):
        split_index = len(self) // 2
        key_to_move_up = self.keys[split_index]
        value_to_move_up = self.values[split_index]
        right_node = Node(self.keys[split_index+1:], self.values[split_index+1:], self.children[split_index+1:])
        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]
        self.children = self.children[:split_index+1]
        parent = Node([key_to_move_up], [value_to_move_up], [self, right_node])
        return parent

    def insert_child(self, insert_index, child):
        self.children.insert(insert_index, child)
        child.parent = self
        
    def split_with_parent(self): 
        split_index = len(self) // 2
        key_to_move_up = self.keys[split_index]
        value_to_move_up = self.values[split_index]
        right_node = Node(self.keys[split_index+1:], self.values[split_index+1:], self.children[split_index+1:])
        self.keys = self.keys[:split_index]
        self.values = self.values[:split_index]
        self.children = self.children[:split_index+1]
        insert_index = self.parent.insert_entry(key_to_move_up, value_to_move_up)
        self.parent.insert_child(insert_index + 1, right_node)
        return self.parent

    def split(self):
        if self.parent is None:
            return self.split_no_parent()
        else:
            return self.split_with_parent()