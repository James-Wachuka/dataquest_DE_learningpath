## 2. Intro to DAGs ##

cycle = [4,6,7]

## 3. The DAG Class ##

class DAG(DQ):
    def __init__(self):
        self.graph = {}
    
    def add(self, node, to=None):
        if node not in self.graph:
            self.graph[node] = []
        if to is not None:
            self.graph[node].append(to)
            if to not in self.graph:
                self.graph[to] = []
dag = DAG()
dag.add(1)
dag.add(1, 2)
dag.add(1, 3)
dag.add(1, 4)
dag.add(3, 5)
dag.add(2, 6)
dag.add(4, 7)
dag.add(5, 7)
dag.add(6, 7)

print(dag.graph)

## 5. Finding Number of In Degrees ##

class DAG(BaseDAG):
    def in_degrees(self):
        self.degrees = {node: 0 for node in self.graph}
        for node in self.graph:
            for to_node in self.graph[node]:
                self.degrees[to_node] += 1


dag = DAG()
dag.add(1)
dag.add(1, 2)
dag.add(1, 3)
dag.add(1, 4)
dag.add(3, 5)
dag.add(2, 6)
dag.add(4, 7)
dag.add(5, 7)
dag.add(6, 7)
dag.in_degrees()
print(dag.degrees)

## 6. Challenge: Sorting Dependencies ##

from collections import deque

class DAG(BaseDAG):
    def sort(self):
        self.in_degrees()
        queue = deque()
        for node, degree in self.degrees.items():
            if degree == 0:
                queue.append(node)
        sorted_nodes = []
        while queue:
            node = queue.popleft()
            sorted_nodes.append(node)
            for to_node in self.graph[node]:
                self.degrees[to_node] -= 1
                if self.degrees[to_node] == 0:
                    queue.append(to_node)
        if len(sorted_nodes) != len(self.graph):
            raise Exception("Graph contains a cycle")
        return sorted_nodes


dag = DAG()
dag.add(1)
dag.add(1, 2)
dag.add(1, 3)
dag.add(1, 4)
dag.add(3, 5)
dag.add(2, 6)
dag.add(4, 7)
dag.add(5, 7)
dag.add(6, 7)
dependencies = dag.sort()
print(dependencies)

## 7. Enhance the Add Method ##

class DAG(BaseDAG):
    def add(self, node, to=None):
        if not node in self.graph:
            self.graph[node] = []
        if to:
            if not to in self.graph:
                self.graph[to] = []
            self.graph[node].append(to)
            if len(self.sort()) != len(self.graph):
                raise Exception("Cycle detected")


dag = DAG()
dag.add(1)
dag.add(1, 2)
dag.add(1, 3)
dag.add(1, 4)
dag.add(3, 5)
dag.add(2, 6)
dag.add(4, 7)
dag.add(5, 7)
dag.add(6, 7)
# Add a pointer from 7 to 4, causing a cycle.
try:
    dag.add(7, 4)
except Exception as e:
    print(e) # "Cycle detected"

## 8. Adding DAG to the Pipeline ##

class Pipeline(DAG):
    def __init__(self):
        self.tasks = DAG()
        
    def task(self, depends_on=None):
        def inner(f):
            self.tasks.add(f)
            if depends_on:
                self.tasks.add(depends_on, f)
            return f
        return inner

pipeline = Pipeline()

@pipeline.task()
def first():
    return 20

@pipeline.task(depends_on=first)
def second(x):
    return x * 2

@pipeline.task(depends_on=second)
def third(x):
    return x // 3

@pipeline.task(depends_on=second)
def fourth(x):
    return x // 4

graph = pipeline.tasks.graph

## 9. Challenge: Running the Pipeline ##

class Pipeline(DAG):
    def __init__(self):
        self.tasks = DAG()
        
    def task(self, depends_on=None):
        def inner(f):
            self.tasks.add(f)
            if depends_on:
                self.tasks.add(depends_on, f)
            return f
        return inner
    
    def run(self):
        visited = self.tasks.sort()
        completed = {}
        for task in visited:
            args = []
            for node, edges in self.tasks.graph.items():
                if task in edges:
                    args.append(completed[node])
            if args:
                completed[task] = task(*args)
            else:
                completed[task] = task()
        return completed
    
pipeline = Pipeline()

@pipeline.task()
def first():
    return 20

@pipeline.task(depends_on=first)
def second(x):
    return x * 2

@pipeline.task(depends_on=second)
def third(x):
    return x // 3

@pipeline.task(depends_on=second)
def fourth(x):
    return x // 4

outputs = pipeline.run()