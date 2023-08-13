## 1. Introduction ##

class Book:
    def __init__(self, name, num_pages):
        self.name = name
        self.num_pages = num_pages
        
        
book = Book("Lord of the Flies", 228)

## 2. Linked Structure ##

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

        
node = Node(42)

## 3. Head and Tail ##

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
lst = LinkedList()

## 4. Appending to a Linked List ##

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        
lst = LinkedList()

lst.append(10)
print(lst.length)  # Output: 1
print(lst.head.data)  # Output: 10
print(lst.tail.data)  # Output: 10

lst.append(11)
print(lst.length)  # Output: 2
print(lst.head.data)  # Output: 10
print(lst.tail.data)  # Output: 11

## 5. Iterating Over List Elements Part 1 ##

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def __iter__(self):
        self._iter_node = self.head
        return self

## 6. Iterating Over List Elements Part 2 ##

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    
    def __iter__(self):
        self._iter_node = self.head
        return self
    
    def __next__(self):
        if self._iter_node is None:
            raise StopIteration
        ret = self._iter_node.data
        self._iter_node = self._iter_node.next
        return ret

    
    
lst = LinkedList()
lst.append(5)
lst.append(3)
lst.append(8)

for value in lst:
    print(value)

## 7. Prepending Elements ##

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
        
        
lst = LinkedList()

lst.prepend(10)
print(lst.length)  # Output: 1
print(lst.head.data)  # Output: 10
print(lst.tail.data)  # Output: 10

lst.prepend(11)
print(lst.length)  # Output: 2
print(lst.head.data)  # Output: 11
print(lst.tail.data)  # Output: 10

## 8. Length of a List ##

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    
    def __len__(self):
        return self.length

    
lst = LinkedList()

lst.append(10)
print(len(lst))  # Output: 1

## 9. String Representation ##

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        self._iter_node = self.head
        return self
    
    def __next__(self):
        if self._iter_node is None:
            raise StopIteration
        ret = self._iter_node.data
        self._iter_node = self._iter_node.next
        return ret
    
    def __str__(self):
        return str([value for value in self])


    
lst = LinkedList()
print(lst)  # Output: []

lst.append(1)
print(lst)  # Output: [1]

lst.append(2)
print(lst)  # Output: [1, 2]