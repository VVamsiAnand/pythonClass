# B6.1: Membership Operators

fruits = ["apple", "banana", "mango", "grape", "kiwi"]

item = input("Enter a fruit: ")

print(item, "is in the list:", item in fruits)
print(item, "is not in the list:", item not in fruits)

# Sample Output 1:
# Enter a fruit: mango
# mango is in the list: True
# mango is not in the list: False

# Sample Output 2:
# Enter a fruit: orange
# orange is in the list: False
# orange is not in the list: True