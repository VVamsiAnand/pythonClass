# lab1_task1.py

def greet(name):
    print(f"Hello, {name}! Welcome to Python.")

greet("Asha")
greet("Ravi")
greet("Priya")

# Output:
# Hello, Asha! Welcome to Python.
# Hello, Ravi! Welcome to Python.
# Hello, Priya! Welcome to Python.


# lab1_task2.py

def simple_interest(principal, rate, time):
    """Calculate and return simple interest."""
    return (principal * rate * time) / 100

principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

si = simple_interest(principal, rate, time)
print("Simple Interest:", si)

# Output:
# Enter principal: 10000
# Enter rate: 5
# Enter time: 2
# Simple Interest: 1000.0

# lab1_task3.py

def is_even(n):
    return n % 2 == 0

for i in range(5):
    number = int(input("Enter a number: "))

    if is_even(number):
        print(number, "is Even")
    else:
        print(number, "is Odd")

# Output:
# Enter a number: 10
# 10 is Even
# Enter a number: 7
# 7 is Odd
# Enter a number: 4
# 4 is Even
# Enter a number: 9
# 9 is Odd
# Enter a number: 12
# 12 is Even

# lab1_task4.py

def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    return minimum, maximum, average


numbers = [10, 20, 30, 40, 50]

minimum, maximum, average = stats(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)

# Output:
# Minimum: 10
# Maximum: 50
# Average: 30.0

# lab1_task5.py

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print("Temperature in Fahrenheit:", f)

    elif choice == "2":
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print("Temperature in Celsius:", c)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")

# Output:
# Temperature Converter
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Exit
# Enter your choice: 1
# Enter temperature in Celsius: 25
# Temperature in Fahrenheit: 77.0
#
# Temperature Converter
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Exit
# Enter your choice: 2
# Enter temperature in Fahrenheit: 98.6
# Temperature in Celsius: 37.0
#
# Temperature Converter
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Exit
# Enter your choice: 3
# Exiting program...
