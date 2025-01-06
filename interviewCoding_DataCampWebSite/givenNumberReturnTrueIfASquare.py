#!/usr/local/bin/python3


def perfectSquare(number):
   return number %2 == 0;

number = 8
print(perfectSquare(number));
number = 9
print(perfectSquare(number));

user_input = input("Return TRUE if value inputted is a square orelse FALSE : ")
print(type(user_input));
print(type(int(user_input)));
print(perfectSquare(int(user_input)));
