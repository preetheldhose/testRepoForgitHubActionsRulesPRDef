#!/usr/local/bin/python3

from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import Counter
from collections import deque

# namedtuple:

# Define a Point with fields x and y
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
p = Point(10, 20)

print(p)  # Output: Point(x=10, y=20)

# Access by name
print(p.x)  # Output: 10
print(p.y)  # Output: 20

# Access by index
print(p[0])  # Output: 10
print(p[1])  # Output: 20

for value in p:
    print(value)  # Output: 10 20

# ordereddict:

od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print(od1 == od2)  # Output: False

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

od.move_to_end('b')
print(od)  # Output: OrderedDict([('a', 1), ('c', 3), ('b', 2)])

od.move_to_end('c', last=False)
print(od)  # Output: OrderedDict([('c', 3), ('a', 1), ('b', 2)])

od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print(od1 == od2)  # Output: False

for key, value in od.items():
    print(key, value)

od.popitem(last=True)  # Removes the last item
od.popitem(last=False)  # Removes the first item

# defaultdict

# Default factory is a list
dd = defaultdict(list)

# Access a missing key
print(dd['a'])  # Output: []

# Add values
dd['a'].append(1)
print(dd)  # Output: defaultdict(<class 'list'>, {'a': [1]})

dd = defaultdict(list)
dd['a'].append(1)
dd['a'].append(2)
print(dd)  # Output: defaultdict(<class 'list'>, {'a': [1, 2]})

dd = defaultdict(set)
dd['a'].add(1)
dd['a'].add(2)
print(dd)  # Output: defaultdict(<class 'set'>, {'a': {1, 2}})

dd = defaultdict(int)
dd['a'] += 1
dd['b'] += 2
print(dd)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})


def default_value():
    return "default"


dd = defaultdict(default_value)
print(dd['missing_key'])  # Output: default

dd = defaultdict(lambda: defaultdict(int))

dd['user1']['views'] += 1
dd['user1']['likes'] += 2
print(
    dd)  # Output: defaultdict(<function <lambda> at 0x...>, {'user1': defaultdict(<class 'int'>, {'views': 1, 'likes': 2})})

# from collections import defaultdict

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count = defaultdict(int)

for item in data:
    count[item] += 1

print(count)  # Output: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'orange': 1})

# from collections import defaultdict

data = [('fruit', 'apple'), ('fruit', 'banana'), ('veg', 'carrot'), ('fruit', 'orange')]
grouped = defaultdict(list)

for category, item in data:
    grouped[category].append(item)

print(grouped)
# Output: defaultdict(<class 'list'>, {'fruit': ['apple', 'banana', 'orange'], 'veg': ['carrot']})

# from collections import defaultdict

nested_dict = defaultdict(lambda: defaultdict(int))

nested_dict['user1']['views'] += 1
nested_dict['user1']['likes'] += 2
nested_dict['user2']['views'] += 3

print(nested_dict)
# Output:
# defaultdict(<function <lambda> at 0x...>, {
#    'user1': defaultdict(<class 'int'>, {'views': 1, 'likes': 2}),
#    'user2': defaultdict(<class 'int'>, {'views': 3})
# })

# from collections import defaultdict

dd = defaultdict(str)

print(dd['missing_key'])  # Output: ''
dd['existing_key'] = 'value'
print(dd)  # Output: defaultdict(<class 'str'>, {'missing_key': '', 'existing_key': 'value'})

# Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

counter = Counter("hello world")
print(counter)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

counter = Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

counter = Counter(apple=3, banana=2, orange=1)
print(counter)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

dq = deque([1, 2, 3])  # Initialize with a list
print(dq)  # Output: deque([1, 2, 3])

dq = deque()  # Initialize empty
print(dq)  # Output: deque([])
