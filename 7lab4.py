# lab4_task1.py

# (a) Lambda to find square of a number
square = lambda x: x * x

# (b) Lambda to check if a number is even
is_even = lambda x: x % 2 == 0

# (c) Lambda to find the larger of two numbers
larger = lambda x, y: x if x > y else y


# Calling the lambda functions
print("Square of 5:", square(5))

print("Is 8 even?", is_even(8))
print("Is 7 even?", is_even(7))

print("Larger of 10 and 20:", larger(10, 20))


# Output:
# Square of 5: 25
# Is 8 even? True
# Is 7 even? False
# Larger of 10 and 20: 20

# lab4_task2.py

# Lambda function using a conditional expression
grade = lambda marks: "Pass" if marks >= 40 else "Fail"

marks_list = [85, 32, 67, 39, 45, 28]

for marks in marks_list:
    print("Marks:", marks, "Result:", grade(marks))


# Output:
# Marks: 85 Result: Pass
# Marks: 32 Result: Fail
# Marks: 67 Result: Pass
# Marks: 39 Result: Fail
# Marks: 45 Result: Pass
# Marks: 28 Result: Fail

# lab4_task3.py

# List of tuples containing student name and marks
students = [
    ("Ravi", 78),
    ("Sita", 92),
    ("Amit", 65)
]

# Sort students by marks in descending order
sorted_students = sorted(
    students,
    key=lambda s: s[1],
    reverse=True
)

print("Students sorted by marks:")
for student in sorted_students:
    print(student)


# List of strings
names = ["Ravi", "Sita", "Amit", "Priya", "Raj"]

# Sort strings by their length
sorted_names = sorted(names, key=lambda name: len(name))

print("\nNames sorted by length:")
for name in sorted_names:
    print(name)


# Output:
# Students sorted by marks:
# ('Sita', 92)
# ('Ravi', 78)
# ('Amit', 65)
#
# Names sorted by length:
# Raj
# Sita
# Ravi
# Amit
# Priya

# lab4_task4.py

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use map() with lambda to find cubes
cubes = list(map(lambda x: x ** 3, numbers))

# Use filter() with lambda to find numbers divisible by 3
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))

print("Original numbers:", numbers)
print("Cubes:", cubes)
print("Numbers divisible by 3:", divisible_by_3)


# Output:
# Original numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Cubes: [1, 8, 27, 64, 125, 216, 343, 512, 729]
# Numbers divisible by 3: [3, 6, 9]



# lab4_task5.py

# Dictionary containing item names and prices
items = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2500
}

# Sort dictionary items by price
sorted_items = sorted(
    items.items(),
    key=lambda item: item[1]
)

print("Items from cheapest to most expensive:")

for item, price in sorted_items:
    print(item, ":", price)


# Output:
# Items from cheapest to most expensive:
# Mouse : 800
# Keyboard : 1500
# Headphones : 2500
# Monitor : 12000
# Laptop : 55000


