# Program 6: Iterate through a dictionary

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}
print("Keys:")
for key in student.keys():
    print(key)
print("\nValues:")
for value in student.values():
    print(value)
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

# Output:
# Keys:
# name
# age
# course
#
# Values:
# Rahul
# 20
# Python
#
# Key-Value Pairs:
# name : Rahul
# age : 20
# course : Python

# Program 7: Remove keys from a dictionary

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}
removed_value = student.pop("age")
print("Removed value:", removed_value)
value = student.get("marks", "Key not found")
print("Marks:", value)

print("Dictionary:", student)

# Output:
# Removed value: 20
# Marks: Key not found
# Dictionary: {'name': 'Rahul', 'course': 'Python'}


# Program 8: Check whether a key exists

student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

key = "age"

if key in student:
    print("Key exists")
    print("Value:", student[key])
else:
    print("Key does not exist")

# Output:
# Key exists
# Value: 20


# Program 9: Merge two dictionaries

dict1 = {
    "name": "Rahul",
    "age": 20
}

dict2 = {
    "course": "Python",
    "marks": 90
}
merged1 = dict1.copy()
merged1.update(dict2)

print("Using update():", merged1)
merged2 = dict1 | dict2

print("Using | operator:", merged2)

# Output:
# Using update(): {'name': 'Rahul', 'age': 20, 'course': 'Python', 'marks': 90}
# Using | operator: {'name': 'Rahul', 'age': 20, 'course': 'Python', 'marks': 90}


# Program 10: Find highest and lowest priced items

prices = {
    "Laptop": 75000,
    "Mobile": 25000,
    "Headphones": 5000,
    "Keyboard": 3000,
    "Monitor": 15000
}

highest_item = max(prices, key=prices.get)
lowest_item = min(prices, key=prices.get)

print("Highest priced item:", highest_item)
print("Price:", prices[highest_item])

print("Lowest priced item:", lowest_item)
print("Price:", prices[lowest_item])

# Output:
# Highest priced item: Laptop
# Price: 75000
# Lowest priced item: Keyboard
# Price: 3000


# Program 11: Count character frequency

text = "hello"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character frequency:", frequency)

# Output:
# Character frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# Program 12: Create a dictionary of numbers and their cubes

cubes = {number: number ** 3 for number in range(1, 11)}

print("Numbers and their cubes:")
print(cubes)

# Output:
# Numbers and their cubes:
# {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}
