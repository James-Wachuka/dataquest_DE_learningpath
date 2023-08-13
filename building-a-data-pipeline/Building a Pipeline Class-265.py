## 3. Function Closures ##

def partial(func, *args):
    def inner(*more_args):
        return func(*(args + more_args))
    return inner

def add(a, b):
    return a + b

add_two = partial(add, 2)
print(add_two(7))

## 4. Python Decorators ##

def catch_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return e
    return inner

@catch_error
def throws_error():
    raise Exception('Throws Error')

print(throws_error())

## 5. Method Decorators ##

class Pipeline:
    def __init__(self):
        self.tasks = []

    def task(self, func):
        self.tasks.append(func)
        return func

pipeline = Pipeline()

@pipeline.task
def first_task():
    return 'First Task'

print(pipeline.tasks)

## 6. Decorator Arguments ##

class Pipeline:
    def __init__(self):
        self.tasks = []

    def task(self, depends_on=None):
        def inner(func):
            if depends_on:
                index = self.tasks.index(depends_on) + 1
                self.tasks.insert(index, func)
            else:
                self.tasks.append(func)
            return func
        return inner

pipeline = Pipeline()

@pipeline.task()
def first_task(x):
    return x + 1

@pipeline.task(depends_on=first_task)
def second_task(x):
    return x * 2

@pipeline.task(depends_on=second_task)
def last_task(x):
    return x - 4

print(pipeline.tasks)

## 7. Running the Pipeline ##

class Pipeline:
    def __init__(self):
        self.tasks = []

    def task(self, depends_on=None):
        def inner(func):
            if depends_on:
                index = self.tasks.index(depends_on) + 1
                self.tasks.insert(index, func)
            else:
                self.tasks.append(func)
            return func
        return inner

    def run(self, input_):
        output = input_
        for task in self.tasks:
            output = task(output)
        return output

pipeline = Pipeline()

@pipeline.task()
def first_task(x):
    return x + 1

@pipeline.task(depends_on=first_task)
def second_task(x):
    return x * 2

@pipeline.task(depends_on=second_task)
def last_task(x):
    return x - 4

print(pipeline.run(20))