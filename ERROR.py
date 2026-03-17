Here is the fully corrected Python code:


import math
import random
import datetime
import os
import sys

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []

    def add_friend(self, friend):
        if isinstance(friend, User):
            self.friends.append(friend)
        else:
            print("Not a user!")

    def greet(self):
        print(f"Hello, {self.name}! You are {self.age} years old")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! Now you are {self.age}")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount >= 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit")

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount > self.balance:
                print("Insufficient balance")
            else:
                self.balance -= amount
                print(f"Withdrew {amount}. Remaining: {self.balance}")
        else:
            print("Invalid withdrawal")

    def transfer(self, target, amount):
        if isinstance(target, BankAccount):
            self.withdraw(amount)
            target.deposit(amount)
        else:
            print("Target not valid account")

def generate_random_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(1, 100))
    return numbers

def calculate_stats(nums):
    sum_nums = sum(nums)
    mean = sum_nums / len(nums)
    max_val = max(nums)
    min_val = min(nums)
    return {"sum": sum_nums, "mean": mean, "max": max_val, "min": min_val}

def main():
    users = []
    for i in range(5):
        name = f"User{i}"
        age = random.randint(15, 50)
        u = User(name, age)
        users.append(u)

    # Add friends
    for u in users:
        friend = random.choice(users)
        u.add_friend(friend)

    # Bank accounts
    accounts = []
    for u in users:
        a = BankAccount(u, random.randint(100, 1000))
        accounts.append(a)

    # Transfers
    for i in range(3):
        src = random.choice(accounts)
        dst = random.choice(accounts)
        amt = random.randint(50, 500)
        if isinstance(src, BankAccount) and isinstance(dst, BankAccount):
            src.transfer(dst, amt)

    # Random numbers and stats
    nums = generate_random_numbers(10)
    stats = calculate_stats(nums)
    print("Random numbers:", nums)
    print("Statistics:", stats)

    # Dates and times
    today = datetime.date.today()
    print("Today is", today.strftime("%A, %B %d, %Y"))
    print("Random day of year:", (today - datetime.date(today.year, 1, 1)).days + 1)

def factorial(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * factorial(n-1)
    else:
        raise ValueError('Factorial is not defined for negative integers')

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def write_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)

def read_file(filename):
    with open(filename, "r") as f:
        data = f.read()
    return data

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primes_up_to(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def merge_dicts(d1, d2):
    result = {**d1, **d2}
    return result

def greet_multiple(*names):
    for n in names:
        print("Hello " + n)

def calc_power(x, y):
    if isinstance(y, int) and y >= 0:
        return x ** y
    else:
        raise ValueError('Power calculation is not defined for negative or non-integer exponents')

def main_loop():
    for i in range(10):
        print("Loop", i)
        if i == 5:
            print("Middle of loop")

class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2

    def circumference(self):
        return 2 * math.pi * self.radius

def find_max_in_list(lst):
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

def sort_desc(lst):
    return sorted(lst, reverse=True)

def capitalize_words(s):
    words = s.split(" ")
    result = ""
    for w in words:
        result += w.capitalize() + " "
    return result.strip()

def remove_whitespace(s):
    return s.replace(" ", "")

if __name__ == "__main__":
    main()
    main_loop()
    print("Factorial of 5:", factorial(5))
    print("Reverse 'hello':", reverse_string("hello"))
    print("Vowels in 'Programming':", count_vowels("Programming"))
    print("Fibonacci 10:", fibonacci(10))
    print("Primes up to 20:", primes_up_to(20))
    print("2^8:", calc_power(2, 8))
    print("Capitalized:", capitalize_words("hello world python"))
    print("No spaces:", remove_whitespace("  hello world  "))