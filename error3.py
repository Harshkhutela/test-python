import math
import csv
import random

def read_csv(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def write_csv(filename, data):
    f = open(filename, "w")
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()

def calculate_mean(numbers):
    total = sum(numbers)
    return total / len(numbers)

def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2] + numbers[n//2 - 1]) / 2
    else:
        median = numbers[n//2]
    return median

def normalize(numbers):
    max_val = max(numbers)
    min_val = min(numbers)
    return [(x - min_val) / (max_val-min_val) for x in numbers]

def matrix_multiply(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                s += a[i][k] * b[k][j]
            row.append(s)
        result.append(row)
    return result

def power_list(numbers, exp):
    return [n**exp for n in numbers]

def count_occurrences(lst, value):
    count = 0
    for i in lst:
        if i == value:
            count += 1
    return count

def factorial_iterative(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result

def is_palindrome(s):
    return s == s[::-1]

def generate_random_strings(n, length):
    chars = "abcdefghijklmnopqrstuvwxyz"
    strings = []
    for i in range(n):
        s = ""
        for j in range(length):
            s += random.choice(chars)
        strings.append(s)
    return strings

def main_data():
    numbers = [random.randint(1, 100) for _ in range(10)]
    print("Numbers:", numbers)
    print("Mean:", calculate_mean(numbers))
    print("Median:", calculate_median(numbers))
    print("Normalized:", normalize(numbers))
    print("Factorial of 5:", factorial_iterative(5))
    print("Is 'radar' palindrome?", is_palindrome("radar"))
    strings = generate_random_strings(5, 6)
    print("Random strings:", strings)

if __name__ == "__main__":
    main_data()