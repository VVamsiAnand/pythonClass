#list_1
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
print(len(list))

'''sample output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
10 '''


#LIST_2
list=[12, 3.14, 'spring', True , ['example']]
for item in list:
    print("Value:", item, "Type:", type(item))

'''sample output:
Value: 12 Type: <class 'int'>
Value: 3.14 Type: <class 'float'>
Value: spring Type: <class 'str'>
Value: True Type: <class 'bool'>
Value: ['example'] Type: <class 'list'>
'''

#lists_3
list=[]
list.append(12)
list.append(23)
list.append(34)
list.append(45)
list.append(56)
print(list)

'''sample output:
[12, 23, 34, 45, 56]'''

#lists_4
fruits=['mango', 'banana', 'orange', 'apple', 'grapes', 'gouva', 'cherry', 'kiwi' ]
print(fruits[0])
print(fruits[-1])
print(fruits[2])

'''sample output:
mango
kiwi
orange'''

#list_5
numbers=[1,2,12,4,5,45,44,77]
for i,v in enumerate(numbers):
    print(i,v)

'''sample output:
0 1
1 2
2 12
3 4
4 5
5 45
6 44
7 77 '''

#list_6
numbers=[1,12,3,34,5,56,7,78,9,90]
print(numbers[:3])
print(numbers[-3:])
print(numbers[::2])

'''sample output:
[1, 12, 3]
[78, 9, 90]
[1, 3, 5, 7, 9] '''

#list_7
list=[1,2,3,4,5]
print(list[::-1])

'''sample output:
[5, 4, 3, 2, 1] '''


#list_8
elements=[1,2,3,4,5,6,7,8,9,10,11,12]
print(elements[4:8])

'''sample output:
[5, 6, 7, 8] '''

#list_9
colors=['red', 'yellow', 'green', 'blue', 'black', 'orange', 'violet']
print(colors[-1:])
print(colors[-2:-1])
print(colors[-3:])

'''sample output:
['violet']
['orange']
['black', 'orange', 'violet'] '''

#list_10
fruits=['orange', 'custord apple', 'green apple']
print(fruits[::-1])

 '''sample output:
['green apple', 'custord apple', 'orange'] '''

 #list_11
 num=[11,22,33,44,55,66,77]
num.append(99)
print(num)
num.insert(3,88)
print('after inserting:', num)
num.extend([12,23])
print('after extend:', num)
num.remove(22)
print('after removing 22:', num)
num.pop()
print('after pop:', num)
num.sort()
print('sorting order:', num)
num.reverse()
print('reverse order:', num)
print('count of 55 is',num.count(55))
print('index of 33:', num.index(33))

'''sample output:
[11, 22, 33, 44, 55, 66, 77, 99]
after inserting: [11, 22, 33, 88, 44, 55, 66, 77, 99]
after extend: [11, 22, 33, 88, 44, 55, 66, 77, 99, 12, 23]
after removing 22: [11, 33, 88, 44, 55, 66, 77, 99, 12, 23]
after pop: [11, 33, 88, 44, 55, 66, 77, 99, 12]
sorting order: [11, 12, 33, 44, 55, 66, 77, 88, 99]
reverse order: [99, 88, 77, 66, 55, 44, 33, 12, 11]
count of 55 is 1
index of 33: 6  '''

#lists_12
numbers=[67,57,34,57,67,77]
result=[]
for num in numbers:
    if num not in result:
        result.append(num)
print(result)

'''sample output:
[67, 57, 34, 77] '''

#lists_13
numbers=[22,53,71,92,19,45]
maximum=numbers[0]
minimum=numbers[0]
total=0
for num in numbers:
    if num>maximum:
        maximum
    if num<minimum:
        minimum=num
    total+=num
print("maximum=", maximum)
print("minimum=", minimum)
print("sum=", total)

'''sample output:
maximum= 92
minimum= 19
sum= 302  '''

#lists_14
list1=[25,26,27,28]
list2=[39,40,41,42]
merged=list1 + list2
merged.sort(reverse=True)
print("merged sort:", merged)

'''sample output:

erged sort: [42, 41, 40, 39, 28, 27, 26, 25]  '''

#lists_15
squares=[number * number for number in range(1,21)]
print(squares)

'''sample output:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
  '''

#lists_16
even=[number for number in range(1,51) if number%2==0]
print("even numbers between 1 to 50 are ", even)

'''sample output:
even numbers between 1 to 50 are  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50] '''

#lists_17
words=['success','failure','disappointment','sacrife','big','brave']
result = [word for word in words if len(word) > 4]
print(result)

'''sample output:
['success', 'failure', 'disappointment', 'sacrife', 'brave']  '''

#lists_18
matrix = [[1 + row * 3 + col for col in range(3)] for row in range(3)]
print("Matrix:")
for row in matrix:
    print(row)

'''sample output:
Matrix:
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]  '''

#lists_19
numbers = [5, -2, 8, -7, 3, -1,0]
result = [number if number >= 0 else 0 for number in numbers]
print("Original list:", numbers)
print("New list:", result)

'''sample output:
Original list: [5, -2, 8, -7, 3, -1, 0]
New list: [5, 0, 8, 0, 3, 0, 0]  '''

    
    





