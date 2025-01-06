#!/usr/local/bin/python3


'''

Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number)

'''


def checkNumberEvenOdd(number):
    return (number % 2)

'''

# first working logic 

value = int(checkNumberEvenOdd(2));
print(value)
if value == 0:
    print("Even")
else:
    print("False")

value = int(checkNumberEvenOdd(3));
print(value)
if value == 0:
    print("Even")
else:
    print("False")

'''

# Second working logic

value = [0, 1, 2, 3, 4, 5]
for i in value:
    result = int(checkNumberEvenOdd(i))
    if result == 0:
        print(f"value {i} is Even")
    else:
        print(f"value {i} is False")
