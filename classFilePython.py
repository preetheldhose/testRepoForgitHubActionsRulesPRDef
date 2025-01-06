#!/usr/local/bin/python3

class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")


obj = MyClass(10)
obj.display()  # Output: Value: 10
