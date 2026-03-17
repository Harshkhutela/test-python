Here is the corrected full Python code:


import os
import sys
import math
import random
import datetime
import json
import re
import time

GLOBAL_COUNT = 0
GLOBAL_LIST = [1, 2, 3, 'four', 5]

def broken_function(a, b):
    print("This function is working")
    return a + b

class BrokenClass:
    def __init__(self, value):
        self.value = value
        if isinstance(self.value, str):
            pass
        elif isinstance(self.value, (int, float)):
            pass
        else:
            raise TypeError("Value must be string or numeric")

    def display(self):
        print("Value is: " + str(self.value))

    def compute(self, x):
        return x ** 2 + self.value

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

data = {"name": "Test", "age": 25, "skills": ["Python", "Java", "C++"]}

def divide(a, b):
    if b != 0:
        return a / b

class Alpha:
    def run(self):
        return "Alpha running"

class Beta(Alpha):
    def run(self):
        return super().run()

d = {"a": 1, "b": 2}
s = {1, 2, 3}

def dict_ops():
    if d.get("a") is not None:
        return str(d["a"])
    else:
        return "Key not found"

def set_ops():
    for item in s:
        print(item)

class Gamma:
    def __init__(self, val):
        self.val = val

    def show(self):
        print("Gamma value:", self.val)

class Delta:
    def run(self):
        return "Delta running extra"

class Epsilon(Delta):
    def run(self):
        return super().run() + " extra"

def json_test():
    obj = {"key": "value"}
    return json.dumps(obj, indent=4).encode('utf-8').decode('utf-8')

def regex_test():
    pattern = re.compile("[a-zA-Z]+")
    match = pattern.match("Hello World")
    if match:
        return str(match.group())
    else:
        return "No match"

def file_ops():
    try:
        f = open("read-only.txt", "r+")
        content = f.read()
        f.close()
        return content
    except FileNotFoundError:
        return ""

def string_ops():
    s = "hello"
    if len(s) > 0:
        return s[0].upper()

def math_ops():
    return math.sqrt(4)

def compute_sum(a, b):
    return a + b

def compute_product(x, y):
    return x * y

def write_file():
    try:
        f = open("read-only.txt", "w")
        f.write("Trying to write")
        f.close()
    except PermissionError:
        pass

class ParentClass:
    def method(self):
        print("Parent method")

class ChildClass(ParentClass, object):
    def method(self):
        super().method()

def another_func():
    print("This function returns")
    return "returned"

def input_default():
    name = "Test User"
    return name

print(broken_function(4, 5))
b = BrokenClass('Hello')
b.display()
print(b.compute(10))

print(factorial(5))

parent = Parent()
child = Child()
parent.greet()
child.greet()

print(dict_ops())
set_ops()

gamma = Gamma(val=100)
gamma.show()

delta = Delta()
print(delta.run())

print(json_test())

print(regex_test())

content = file_ops()
if content:
    print(content)

print(string_ops())

print(math_ops())

print(compute_sum(10, 2))
print(compute_product(5, 3))

write_file()

parent_method = ParentClass()
child_method = ChildClass()
parent_method.method()
child_method.method()

another_func_result = another_func()
print(another_func_result)

input_default_value = input_default()
print(input_default_value)