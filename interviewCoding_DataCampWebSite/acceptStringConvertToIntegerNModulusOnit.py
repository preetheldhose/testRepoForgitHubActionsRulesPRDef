#!/usr/local/bin/python3


def perfectSquare(number):
   return number %2 == 0;

user_input = input("Return TRUE if value inputted is a square orelse FALSE : ")
print(type(user_input));
print(type(int(user_input)));
print(perfectSquare(int(user_input))); # this line converts an inputted string to integer and print true if its a pefect square.