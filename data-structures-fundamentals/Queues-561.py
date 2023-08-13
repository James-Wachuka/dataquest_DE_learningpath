## 1. Introduction ##

class Queue(LinkedList):
    pass

queue = Queue()
print(queue.length)

## 2. Enqueue Method ##

class Queue(LinkedList):
    def enqueue(self, data):
        self.prepend(data)

        
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

## 3. Getting the Front Element ##

class Queue(LinkedList):
    def enqueue(self, data):
        self.prepend(data)
        
    def get_front(self):
        return self.tail.data

    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.get_front())  # Output: 1

## 4. Removing the Front Element ##

class Queue(LinkedList):
    def enqueue(self, data):
        self.prepend(data)
        
    def get_front(self):
        return self.tail.data
    
    def dequeue(self):
        ret = self.tail.data
        if self.length == 1:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return ret

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

front = queue.dequeue()
print(queue.get_front())  # Output: 2

## 5. FCFS Process Scheduling ##

import pandas as pd

# Read the CSV file into a DataFrame
processes = pd.read_csv("processes.csv", index_col="Pid")

# Print the shape of the DataFrame
print(processes.shape)

## 6. Initializing the FCFS Algorithm ##

cur_time = 0
num_processes_done = 0
wait_queue = Queue()
cur_pid = None

## 7. FCFS Implementation ##

cur_time = 0
num_processes_done = 0
wait_queue = Queue()
cur_pid = None

while num_processes_done < processes.shape[0]:
    # Check if current process finished
    if cur_pid is not None:
        if processes.loc[cur_pid, "Start"] + processes.loc[cur_pid, "Duration"] == cur_time:
            # Step 1: Handle the end of the process
            processes.loc[cur_pid, "End"] = cur_time
            cur_pid = None
            num_processes_done += 1
    
    # Handle arriving processes
    # Step 2: Handle arriving processes
    ready_processes = processes.loc[processes["Arrival"] == cur_time]
    for pid in ready_processes.index:
        wait_queue.enqueue(pid)
    
    # Assign a process to the processor
    if cur_pid is None and len(wait_queue) > 0:
        # Step 3: Assign a process to the CPU
        cur_pid = wait_queue.dequeue()
        processes.loc[cur_pid, "Start"] = cur_time
    
    cur_time += 1

# Display the first five rows of the processes DataFrame
print(processes.head())

## 8. Calculating Wait Times ##

processes['Wait'] = processes['Start'] - processes['Arrival']
average_wait_time = processes['Wait'].mean()

## 9. Calculating Turnaround Times ##

processes['Turnaround'] = processes['End'] - processes['Arrival']
average_turnaround_time = processes['Turnaround'].mean()