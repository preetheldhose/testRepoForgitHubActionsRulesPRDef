#!/usr/local/bin/python3

print("dataStructuresPython");

'''
List example as below
'''
a_list = ["Data", "Camp", "Tutorial"];
a_list.append("Session");
print("mylist : ", a_list);

#A List created using a for loop
my_list = [i for i in range(1, 10)]
print(my_list);
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


'''
Tuple example as below
'''

a_tuple = ("Data", "Camp", "Tutorial");
print("my tuple", a_tuple);

#Generate a tuple using for loop
my_tuple = (i for i in range(1, 10))
print("my tuple", my_tuple)

'''
Create a set 
'''

my_set = {1, 2, 3, 4, 5};
print("my set", my_set);

'''
Create a dictionary
'''

# Using curly braces
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Using the dict() constructor
another_dict = dict(name="Bob", age=30, city="Los Angeles")

print(my_dict)       # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(another_dict)  # Output: {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}

mynew_dic = {"name": "nameType", "age": "42", "height": "4.2", "weight": "65"}
print(mynew_dic);


'''
Creating a dictionary using a for loop - as in Creating a dictionary using dictionary comprehension
'''

my_dict = {i: i**2 for i in range(1, 10)}
print(my_dict);


