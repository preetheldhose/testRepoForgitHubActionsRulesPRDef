#!/usr/local/bin/python3

'''
str = "hello"
for char in str:
    revStr = ""
    print(char)
    #revStr = revStr + char;
    #print(revStr)
    #revStr = ""
    revStr = char + revStr;
    print(revStr)
'''


def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        print("char : " + char)
        print("reversed_str pre : " + reversed_str)
        reversed_str = char + reversed_str
        print("reversed_str post : " + reversed_str)
    return reversed_str


# Example
print(reverse_string_loop("hello"))  # Output: "olleh"
