## 1. Introduction ##

class Stack(LinkedList):
    pass

stack = Stack()
print(stack.length)

## 2. Push Method ##

class Stack(LinkedList):
    def push(self, data):
        self.append(data)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

## 3. Peeking a Stack ##

class Stack(LinkedList):
    def push(self, data):
        self.append(data)
        
    def peek(self):
        return self.tail.data
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.peek())  # Output: 3

## 4. Removing the Top Element ##

class Stack(LinkedList):
    def push(self, data):
        self.append(data)
        
    def peek(self):
        return self.tail.data
    
    def pop(self):
        ret = self.tail.data
        if self.length == 1:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return ret
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

top = stack.pop()
print(stack.peek())  # Output: 2

## 5. LCFS Process Scheduling ##

import pandas as pd

# Read the CSV file into a DataFrame
processes = pd.read_csv("processes.csv", index_col="Pid")

# Print the shape of the DataFrame
print(processes.shape)

## 6. Initializing the LCFS Algorithm ##

cur_time = 0
num_processes_done = 0
wait_stack = Stack()
cur_pid = None

## 7. LCFS Implementation ##

cur_time = 0
num_processes_done = 0
wait_stack = Stack()
cur_pid = None

while num_processes_done < processes.shape[0]:
    # Check if the current process finished
    if cur_pid is not None:
        if processes.loc[cur_pid, "Start"] + processes.loc[cur_pid, "Duration"] == cur_time:
            # Step 1: Handle the end of the process
            processes.loc[cur_pid, "End"] = cur_time
            cur_pid = None
            num_processes_done += 1
    
    # Step 2: Handle arriving processes
    ready_processes = processes.loc[processes["Arrival"] == cur_time]
    for pid in ready_processes.index:
        wait_stack.push(pid)
    
    # Step 3: Assign a process to the CPU
    if cur_pid is None and len(wait_stack) > 0:
        cur_pid = wait_stack.pop()
        processes.loc[cur_pid, "Start"] = cur_time
    
    cur_time += 1

## 8. Calculating Wait Times ##

processes['Wait'] = processes['Start'] - processes['Arrival']
average_wait_time = processes['Wait'].mean()

## 9. Maximum Wait Time ##

fcfs_max_wait = processes['FCFS Wait'].max()
lcfs_max_wait = processes['Wait'].max()
print("FCFS Maximum Wait Time:", fcfs_max_wait)
print("LCFS Maximum Wait Time:", lcfs_max_wait)

## 10. Calculating Turnaround Times ##

processes['Turnaround'] = processes['End'] - processes['Arrival']
average_turnaround_time = processes['Turnaround'].mean()