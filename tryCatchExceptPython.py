#!/usr/local/bin/python3

try:
    num1 = int(input('Enter Numerator: '));
    num2 = int(input('Enter Denominator: '));
    division = num1/num2;
except:
    print('Invalid input!')
else:
    print('Division is successful. ')