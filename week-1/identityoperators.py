

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2 :", list1 == list2)
print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 is not list2 :", list1 is not list2)

print("\nMemory Addresses:")
print("id(list1) =", id(list1))
print("id(list2) =", id(list2))
print("id(list3) =", id(list3))

# Sample Output:
# list1 == list2 : True
# list1 is list2 : False
# list1 is list3 : True
# list1 is not list2 : True
#
# Memory Addresses:
# id(list1) = 140123456789120
# id(list2) = 140123456789376
# id(list3) = 140123456789120