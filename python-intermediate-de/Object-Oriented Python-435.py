## 1. Introduction ##

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}
my_set = {2, 3, 5}

print(type(l))
print(type(s))
print(type(d))
print(type(my_set))

## 2. Sets ##

tri_num_sequence = [1, 3, 6, 10, 15, 10, 6, 3, 1]
odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]\

trinum_5 = set(tri_num_sequence)

odd_20 = set()

for item in odd_numbers:
    if item < 20:
        odd_20.add(item)
        
print(odd_20)


odd_trinum = set()

for item in trinum_5:
    if item % 2 != 0:
        odd_trinum.add(item)

print(odd_trinum)

## 4. Defining a Class ##

class NewList():
    pass

## 5. Instantiating a Class ##

class NewList(DQ):
    pass


newlist_1 = NewList()

print(newlist_1)

## 6. Creating Methods ##

my_string = "hello"   # an object of the str class
my_list = [1, 2, 3]   # an object of the list class

my_list.append(4)
# print(my_list)

my_string = my_string.replace("h","H")
# print(my_string)

'''
class MyClass():
    def greet():
        return "hello"
'''

class NewList(DQ):
    def first_method():
        return "This is my first method"
    
newlist = NewList()

## 7. Understanding 'self' ##

class NewList(DQ):
    def first_method(self):
        return "This is my first method"
        
newlist = NewList()

result = newlist.first_method()

print(result)

## 8. Creating a Method That Accepts an Argument ##

class NewList(DQ):
    def return_list(self,input_list):
        return input_list
    
newlist = NewList()


result = newlist.return_list([1,2,3])

print(result)

## 9. Attributes and the Init Method ##

# my_int = int("3")
# print(my_int)


'''
class MyClass():
    def __init__(self, string):
        self.my_attribute = string

mc = MyClass("Hola!")
print(mc.my_attribute)
'''

class NewList(DQ):
    def __init__(self, initial_state ):
        self.data = initial_state

my_list = NewList([1,2,3,4,5])
print(my_list.data)

## 10. Creating an Append Method ##

# The NewList definition from the previous
# screen is copied here for your convenience

class NewList(DQ):
    def __init__(self, initial_state):
        self.data = initial_state
        self.data.append(6)

my_list = NewList([1,2,3,4,5])
print(my_list)

## 11. Creating and Updating an Attribute ##

class NewList(DQ):
    """
    A Python list with some extras!
    """
    def __init__(self, initial_state):
        self.data = initial_state
        self.calc_length()

    def append(self, new_item):
        """
        Append `new_item` to the NewList
        """
        self.data = self.data + [new_item]
        self.calc_length()

    def calc_length(self):
        """
        Calculate the length of the list and store it in the `length` attribute
        """
        self.length = len(self.data)

        
# Create a new NewList object
fibonacci = NewList([1, 1, 2, 3, 5])

# Display the length attribute of the fibonacci object
print(fibonacci.length)  # Output: 5

# Append the value 8 to fibonacci
fibonacci.append(8)

# Display the updated length attribute of the fibonacci object
print(fibonacci.length)  # Output: 6