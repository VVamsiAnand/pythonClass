# Program 1: Create a Set with Duplicate Elements

my_set = {10, 20, 30, 20, 40, 50, 10, 60}

print(my_set)

# Output:
# {40, 10, 50, 20, 60, 30}


# Program 2: Create Sets from a List and a String

numbers = [1, 2, 3, 2, 4, 1, 5]
text = "programming"

set_from_list = set(numbers)
set_from_string = set(text)

print("Set from list:", set_from_list)
print("Set from string:", set_from_string)

# Output:
# Set from list: {1, 2, 3, 4, 5}
# Set from string: {'p', 'r', 'o', 'g', 'a', 'm', 'i', 'n'}


# Program 3: Add Single and Multiple Elements to a Set

my_set = {1, 2, 3}

my_set.add(4)
print("After add():", my_set)

my_set.update([5, 6, 7])
print("After update():", my_set)

# Output:
# After add(): {1, 2, 3, 4}
# After update(): {1, 2, 3, 4, 5, 6, 7}


# Program 4: Perform Operations on Two Sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Output:
# Union: {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection: {4, 5}
# Difference: {1, 2, 3}
# Symmetric Difference: {1, 2, 3, 6, 7, 8}


# Program 5: Check Subset and Superset of Sets

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print("set1 is subset of set2:", set1.issubset(set2))
print("set2 is superset of set1:", set2.issuperset(set1))

# Output:
# set1 is subset of set2: True
# set2 is superset of set1: True


# Program 6: Remove Elements Using remove() and discard()

my_set = {10, 20, 30, 40}

my_set.remove(20)
print("After remove():", my_set)

my_set.discard(30)
print("After discard():", my_set)

my_set.discard(50)
print("After discarding a non-existing element:", my_set)

# Output:
# After remove(): {10, 30, 40}
# After discard(): {10, 40}
# After discarding a non-existing element: {10, 40}


# Program 7: Check Whether Two Sets Are Disjoint

set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

print("set1 and set2 are disjoint:", set1.isdisjoint(set2))
print("set1 and set3 are disjoint:", set1.isdisjoint(set3))

# Output:
# set1 and set2 are disjoint: True
# set1 and set3 are disjoint: False


# Program 8: Find Unique Elements and Convert Them to a Sorted List

numbers = [5, 2, 8, 2, 3, 5, 1, 8, 4, 3]

unique_numbers = set(numbers)
sorted_numbers = sorted(unique_numbers)

print("Unique elements:", unique_numbers)
print("Sorted list:", sorted_numbers)

# Output:
# Unique elements: {1, 2, 3, 4, 5, 8}
# Sorted list: [1, 2, 3, 4, 5, 8]


# Program 9: Create a Set of Squares of Odd Numbers from 1 to 20

squares = {number ** 2 for number in range(1, 21) if number % 2 != 0}

print(squares)

# Output:
# {1, 9, 25, 49, 81, 121, 169, 225, 289, 361}
