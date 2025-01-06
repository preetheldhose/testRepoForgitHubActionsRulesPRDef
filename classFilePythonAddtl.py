#!/usr/local/bin/python3

class Employee:

    # Constructor
    def __init__(self, empTitle):
        self.empTitle = empTitle

    # Method
    def printemployeetitle(self):
        print("This is the employee's title : ", {self.empTitle})


emp = Employee("DepartmentHead");
emp.printemployeetitle();
