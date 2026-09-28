# lab6_task1.py

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Celsius temperatures
celsius = [0, 10, 20, 30, 40]

# Use map() with a named function
fahrenheit = list(map(celsius_to_fahrenheit, celsius))

print("Celsius temperatures:", celsius)
print("Fahrenheit temperatures:", fahrenheit)


# Function to convert string to uppercase
def to_uppercase(text):
    return text.upper()


# List of strings
words = ["python", "programming", "function", "map"]

# Use map() to convert to uppercase
uppercase_words = list(map(to_uppercase, words))

print("\nOriginal words:", words)
print("Uppercase words:", uppercase_words)


# Output:
# Celsius temperatures: [0, 10, 20, 30, 40]
# Fahrenheit temperatures: [32.0, 50.0, 68.0, 86.0, 104.0]
#
# Original words: ['python', 'programming', 'function', 'map']
# Uppercase words: ['PYTHON', 'PROGRAMMING', 'FUNCTION', 'MAP']


# lab6_task2.py

# Helper function to check whether a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Numbers from 1 to 50
numbers = list(range(1, 51))

# Use filter() to extract prime numbers
prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers from 1 to 50:")
print(prime_numbers)


# Function to check whether a word is palindrome
def is_palindrome(word):
    return word == word[::-1]


words = [
    "madam",
    "hello",
    "level",
    "python",
    "radar",
    "world",
    "civic"
]

# Use filter() to extract palindromes
palindromes = list(filter(is_palindrome, words))

print("\nPalindrome words:")
print(palindromes)


# Output:
# Prime numbers from 1 to 50:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
#
# Palindrome words:
# ['madam', 'level', 'radar', 'civic']


# lab6_task3.py

from functools import reduce


numbers = [2, 4, 6, 8]

# (a) Calculate product using reduce()
product = reduce(lambda a, b: a * b, numbers)

print("Numbers:", numbers)
print("Product:", product)


# (b) Find maximum without using max()
maximum = reduce(lambda a, b: a if a > b else b, numbers)

print("Maximum:", maximum)


# (c) Concatenate strings into a sentence
words = ["Python", "is", "easy", "to", "learn"]

sentence = reduce(lambda a, b: a + " " + b, words)

print("Sentence:", sentence)


# Output:
# Numbers: [2, 4, 6, 8]
# Product: 384
# Maximum: 8
# Sentence: Python is easy to learn


# lab6_task4.py

from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Filter even numbers
evens = filter(lambda x: x % 2 == 0, nums)

# Step 2: Square the even numbers
squares = map(lambda x: x ** 2, evens)

# Step 3: Add all squared values
total = reduce(lambda a, b: a + b, squares)

print("Using filter(), map() and reduce():")
print("Total:", total)


# Same problem using list comprehension and sum()
total_comprehension = sum(x ** 2 for x in nums if x % 2 == 0)

print("\nUsing list comprehension and sum():")
print("Total:", total_comprehension)


# Output:
# Using filter(), map() and reduce():
# Total: 220
#
# Using list comprehension and sum():
# Total: 220
#
# Comparison:
# Both approaches produce the same result.
# The list comprehension with sum() is shorter and easier to read.
# The filter(), map() and reduce() approach clearly demonstrates
# the individual functional programming operations.


# lab6_task5.py

from functools import reduce


# Employee records
employees = [
    {"name": "Asha", "department": "IT", "salary": 50000},
    {"name": "Ravi", "department": "HR", "salary": 45000},
    {"name": "Priya", "department": "IT", "salary": 60000},
    {"name": "Amit", "department": "Sales", "salary": 40000},
    {"name": "Sita", "department": "IT", "salary": 55000}
]

# Department to select
department = "IT"

# Step 1: Filter employees from IT department
it_employees = list(
    filter(lambda employee: employee["department"] == department, employees)
)

print("Employees in IT department:")
for employee in it_employees:
    print(employee)


# Step 2: Give selected employees a 10% salary hike
# Create new dictionaries without modifying the originals
hiked_employees = list(
    map(
        lambda employee: {
            **employee,
            "salary": employee["salary"] * 1.10
        },
        it_employees
    )
)

print("\nEmployees after 10% salary hike:")
for employee in hiked_employees:
    print(employee)


# Step 3: Calculate total salary expenditure
total_salary = reduce(
    lambda total, employee: total + employee["salary"],
    hiked_employees,
    0
)

print("\nTotal salary expenditure after hike:", total_salary)


# Output:
# Employees in IT department:
# {'name': 'Asha', 'department': 'IT', 'salary': 50000}
# {'name': 'Priya', 'department': 'IT', 'salary': 60000}
# {'name': 'Sita', 'department': 'IT', 'salary': 55000}
#
# Employees after 10% salary hike:
# {'name': 'Asha', 'department': 'IT', 'salary': 55000.00000000001}
# {'name': 'Priya', 'department': 'IT', 'salary': 66000.0}
# {'name': 'Sita', 'department': 'IT', 'salary': 60500.00000000001}
#
# Total salary expenditure after hike: 181500.00000000003
