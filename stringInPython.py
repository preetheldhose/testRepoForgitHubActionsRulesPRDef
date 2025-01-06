#!/usr/local/bin/python3

import re;

# Define a string in Python

stringA = "This is a string";
print(stringA);

stringB = "Without any issues"
'''
How to concatenate strings in python
'''

print(stringA + " " + stringB);

'''
How to find the length of a string in python & 
also how to covert a integer to string in python
'''

length = len(stringA);
print("Length value is as follows : " + str(length));

'''
ways to slice characters from a string in python
'''

# Below line slices characters 1 to 3
print(stringA[1:4])

'''
How to reverse a string in python
'''
print(stringA);
print(stringA[::-1]);

'''
How to convert string to upper and lower string.
'''

print(stringA.upper());
print(stringA.lower());

stringC = " thisisit ";
print(stringC.strip());

stringD = "World with a bunch of foolS";

if stringD.startswith("W"):
    print("The String starts with W : " + stringD);
else:
    print("The String does not start with W");

if stringD.endswith("S"):
    print("The String ends with S : " + stringD);
else:
    print("The String does not end with S");

'''
Split() method - here the split is done based on space.
'''

splitedString = stringA.split();
print(splitedString);

text = "Python is fun";

match = re.match(r"Python", text);

if(match):
    print("Matched:", match.group());
else:
    print("No matches found");

matches = re.findall(r"Python", text);

if(matches):
    print("Matched findall()")
else:
    print("No matches found this time over");