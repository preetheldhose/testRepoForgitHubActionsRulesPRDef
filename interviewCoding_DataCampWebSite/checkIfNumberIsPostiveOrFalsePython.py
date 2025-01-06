#!/usr/local/bin/python3

def checkNumberIsPostiveOrNegative(number):
    if number > 0:
        print(f"Given {number} is Positive")
    elif number < 0:
        print(f"Given {number} is Negative")
    else:
        print("Nothing")

value = checkNumberIsPostiveOrNegative(1)

value = checkNumberIsPostiveOrNegative(-1)