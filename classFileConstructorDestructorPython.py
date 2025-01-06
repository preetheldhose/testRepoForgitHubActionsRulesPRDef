#!/usr/local/bin/python3

class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object {self.name} destroyed")

# Create an object
obj = MyClass("A")
# Output: Object A created

# Delete the object
del obj
# Output: Object A destroyed
