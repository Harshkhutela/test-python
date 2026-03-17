import os
from math import sqrt
from random import randint

def calculate_values(x, y):
    if isinstance(x, str):
        print("Error: Input must be a number.")
    else:
        result = x ** y
        print("Result is ", result)
        return result

def main():
    nums = [1, 2, 3, 4]
    for n in nums:
        calculate_values(n, 2)

    for i in range(10):
        if i % 2 == 0:
            print("Even", i)
        else:
            print("Odd", i)

if __name__ == "__main__":
    main()