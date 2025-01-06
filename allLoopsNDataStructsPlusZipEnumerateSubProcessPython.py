#!/usr/local/bin/python3

'''
For Loop
'''

# Iterate over a range
for i in range(5):
    print("Print the range : ", i);

# Iterate over a string
for char in "hello":
    print("List of char from a string : ", char)

# Iterate over a list
numbers = [1, 2, 3]
for num in numbers:
    print("List : ", num)

# Iterate over a tuple
myTuple = (1, 2, 3)
for te in myTuple:
    print("Tuple : ", te)

# Iterate over a set
mySet = {1, 2, 3, }
for st in mySet:
    print("Set : ", st)

# Iterate over a dictionary
myDict = {"Jan": 1, "Feb": 2, "Mar": 3}
for key, value in myDict.items():
    print(f"Key => {key} Value => {value}")

# Usage of Zip function
names = ['Salmaan', 'Abdul', 'Razzak'];
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Usage of enumerate function:
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

'''

1. Modify Values in a Dictionary

If you want to update the values of a dictionary based on a condition:

'''

my_dict = {"a": 1, "b": 2, "c": 3}

for key in my_dict:
    my_dict[key] *= 2

print(my_dict)
# Output: {'a': 2, 'b': 4, 'c': 6}

'''

2. Filtering a Dictionary

Create a new dictionary with key-value pairs that meet a specific condition.

'''

my_dict = {"a": 1, "b": 2, "c": 3}

filtered_dict = {key: value for key, value in my_dict.items() if value > 1}

print(filtered_dict)
# Output: {'b': 2, 'c': 3}

'''

3. Combining Keys and Values

Print a sentence for each key-value pair.

'''


my_dict = {"name": "Alice", "age": 25, "city": "New York"}

for key, value in my_dict.items():
    print(f"The {key} is {value}.")
# Output:
# The name is Alice.
# The age is 25.
# The city is New York.

'''

Nested Dictionaries

If the dictionary contains nested dictionaries, you can use nested loops to iterate through all levels.
Example:

'''

nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

for person, details in nested_dict.items():
    print(f"{person}:")
    for key, value in details.items():
        print(f"  {key}: {value}")
# Output:
# person1:
#   name: Alice
#   age: 25
# person2:
#   name: Bob
#   age: 30

'''

While Loop:

'''

# Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
# Output: 1, 2, 3, 4, 5

# Infinite loop (requires a break condition)
while True:
    print("Running...")
    break