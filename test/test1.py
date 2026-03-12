# Giant Python Practice Script
# Part 1: Lines 1–500
# Warning: This file intentionally contains MANY errors (syntax, logic, undefined variables, indentation, etc.)
# Your challenge: Debug and fix them!

import os
import sys
import math
import random
import datetime
import json
import re

# Start with some broken imports
import non_existent_module
from math import squareroot  # wrong function name

# Global variables
GLOBAL_COUNT = 0
GLOBAL_LIST = [1, 2, 3, "four", five]  # 'five' undefined

def broken_function(a, b):
print("This function is broken")   # indentation error
    return a + b + c   # 'c' undefined

class BrokenClass:
    def __init__(self, value):
        self.value = value
        self.missing_attr = not_defined_var   # undefined variable

    def display(self):
        print("Value is: " + self.value)   # type error if value not str

    def compute(self, x):
        return x ** 2 + self.value   # type error if self.value not numeric

# Random nonsense functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial(n):   # duplicate function definition
    return "factorial of " + str(n)

# More broken code
for i in range(10)
    print("Loop missing colon")   # syntax error

while True
    break   # syntax error

# Fake data structures
data = {
    "name": "Test",
    "age": 25,
    "skills": ["Python", "Java", "C++"],
    "invalid": some_undefined_var
}

# Functions with logical errors
def divide(a, b):
    return a / 0   # division by zero

def recursive_error(x):
    return recursive_error(x)   # infinite recursion

# Classes with broken inheritance
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent, NonExistentBase):   # NonExistentBase undefined
    def greet(self):
        super().greet()
        print("Hello from Child")

# Generate lots of filler broken code
for i in range(100):
    def temp_func(x):
        return x + i + undefined_var   # undefined_var error

    class TempClass:
        def method(self):
            print("Method with error" + 123)   # type error

# More nonsense
def json_test():
    obj = {"key": "value"}
    return json.dumps(obj, indent="two")   # wrong type for indent

def regex_test():
    pattern = re.compile("[A-Z")
    return pattern.match("Hello")   # unclosed regex bracket

# Broken file operations
def file_ops():
    f = open("nonexistent.txt", "r")
    content = f.read()
    f.close()
    return content

# Continue filler until ~500 lines
for i in range(200):
    print("Line filler", i)
    if i % 2 == 0
        print("Even number")   # missing colon
    else
        print("Odd number")    # missing colon

# Giant Python Practice Script
# Part 2: Lines 501–1000

# More broken functions
def strange_func(a, b, c):
    result = a + b + c + d   # 'd' not defined
    return result

def another_func():
    print("This function forgets to return")

def another_func():   # duplicate definition
    return missing_variable

# Broken class hierarchy
class Base:
    def method(self):
        print("Base method")

class Derived(Base, UnknownBase):   # UnknownBase not defined
    def method(self):
        super().method()
        print("Derived method")

# Random filler with errors
for j in range(50):
    def inner_func(y):
        return y * j / zero_divisor   # zero_divisor not defined

    class InnerClass:
        def __init__(self):
            self.attr = "broken" + 123   # type error

        def show(self):
            print("Attr is", self.attr)

# More nonsense
def string_ops():
    s = "hello"
    return s[100]   # index out of range

def math_ops():
    return math.sqrt("not a number")   # type error

# Broken recursion
def infinite_recursion(x):
    return infinite_recursion(x+1)

# File handling again
def write_file():
    f = open("readonly.txt", "w")
    f.write("Trying to write")
    f.close()

# More filler
for k in range(300):
    print("Filler line", k)
    if k % 3 == 0
        print("Divisible by 3")   # missing colon
    elif k % 5 == 0
        print("Divisible by 5")   # missing colon
    else
        print("Other")            # missing colon

# Giant Python Practice Script
# Part 3: Lines 1001–1500

# More broken definitions
def calc_area(radius):
    return 3.14159 * radius * radious   # typo in variable

def list_ops():
    lst = [1, 2, 3]
    return lst[10]   # index out of range

class WeirdClass:
    def __init__(self, name):
        self.name = name
        self.value = int("not_a_number")   # ValueError

    def show(self):
        print("Name is", self.nam)   # typo in attribute

# More filler
for m in range(100):
    def filler_func(z):
        return z + m + missing   # missing variable

    class FillerClass:
        def method(self):
            print("Broken filler" + 456)   # type error

# More nonsense
def dict_ops():
    d = {"a": 1, "b": 2}
    return d["c"]   # key error

def set_ops():
    s = set([1, 2, 3])
    return s[0]   # sets not subscriptable

# Broken loops
for n in range(20)
    print("Loop error")   # missing colon

while True
    print("Infinite loop")   # missing colon
    break

# Classes with broken methods
class Alpha:
    def run(self):
        return "Alpha running"

class Beta(Alpha):
    def run(self):
        return super().rn()   # typo in method

# More filler
for p in range(200):
    print("Line filler", p)
    if p % 4 == 0
        print("Divisible by 4")   # missing colon
    elif p % 7 == 0
        print("Divisible by 7")   # missing colon
    else
        print("Other")            # missing colon

# Giant Python Practice Script
# Part 4: Lines 1501–2500+

# More broken functions
def compute_sum(a, b):
    return a + b + c   # c not defined

def compute_product(x, y):
    return x * y * z   # z not defined

# Broken class
class Gamma:
    def __init__(self, val):
        self.val = val
        self.extra = undefined_attr

    def show(self):
        print("Gamma value:", self.val)
        print("Extra:", self.extr)   # typo

# More filler loops
for q in range(400):
    print("Filler line", q)
    if q % 2 == 0
        print("Even filler")   # missing colon
    else
        print("Odd filler")    # missing colon

# More nonsense
def broken_math():
    return math.log(-1)   # domain error

def broken_string():
    s = "abc"
    return s + 123   # type error

# Classes with broken inheritance
class Delta:
    def run(self):
        return "Delta running"

class Epsilon(Delta, MissingBase):   # MissingBase not defined
    def run(self):
        return super().run() + 456   # type error

# More filler
for r in range(300):
    def filler_func2(t):
        return t + r + not_found

    class FillerClass2:
        def method(self):
            print("Broken filler2" + 789)

# More nonsense
def dict_error():
    d = {"x": 1}
    return d["y"]

def list_error():
    l = [10, 20]
    return l["string_index"]

# Broken recursion again
def recurse_forever(n):
    return recurse_forever(n+1)

# More filler until 2500+
for s in range(600):
    print("Line filler", s)
    if s % 10 == 0
        print("Divisible by 10")
    elif s % 15 == 0
        print("Divisible by 15")
    else
        print("Other filler")

