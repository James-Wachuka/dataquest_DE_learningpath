## 2. Comparing Object-Oriented to Functional ##

def read(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def count(lst):
    return len(lst)

example_lines = read('example_log.txt')
lines_count = count(example_lines)

print(example_lines)
print(lines_count)

## 4. The Lambda Expression ##

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

lines = read('example_log.txt')

sorted_lines = sorted(lines, key=lambda line: line.split(' ')[5])
print(sorted_lines)

## 5. The Map Function ##

lines = read('example_log.txt')

ip_addresses = list(map(lambda line: line.split(' ')[0], lines))
print(ip_addresses)

## 6. The Filter Function ##

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))

filtered_ips = list(filter(lambda ip: int(ip.split('.')[0]) <= 20, ip_addresses))
print(filtered_ips)

## 7. The Reduce Function ##

from functools import reduce

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))

total_lines = reduce(lambda count, _: count + 1, lines, 0)
total_filtered_ips = reduce(lambda count, _: count + 1, filtered_ips, 0)

ratio = total_filtered_ips / total_lines
print(ratio)

## 8. Rewriting with List Comprehension ##

lines = read('example_log.txt')

ip_addresses = [x.split()[0] for x in lines]
filtered_ips = [ip for ip in ip_addresses if int(ip.split('.')[0]) <= 20]

count_all = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, lines)
count_filtered = reduce(lambda x, _: 2 if isinstance(x, str) else x + 1, filtered_ips)

ratio = count_filtered / count_all
print(ratio)

## 9. Writing Function Partials ##

from functools import partial

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: int(x.split('.')[0]) <= 20, ip_addresses))

count = partial(reduce, lambda x, _: 2 if isinstance(x, str) else x + 1)

count_all = count(lines)
count_filtered = count(filtered_ips)

ratio = count_filtered / count_all
print(ratio)

## 10. Using Functional Composition ##

from functools import reduce, partial

def compose(*functions):
    def inner(arg):
        result = arg
        for f in functions:
            result = f(result)
        return result
    return inner

def count_filtered(lst):
    return len(list(lst))

def filter_condition(ip):
    return int(ip.split('.')[0]) <= 20

lines = read('example_log.txt')
ip_addresses = list(map(lambda x: x.split()[0], lines))
filtered_ips = list(filter(lambda x: filter_condition(x), ip_addresses))

composed = compose(
    partial(map, lambda x: x.split()[0]),
    partial(filter, filter_condition),
    partial(count_filtered)
)

counted = composed(lines)