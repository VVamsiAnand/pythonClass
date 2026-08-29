#tuple_1
countries=('India', 'Russia','France', 'Germany', 'Japan')
print('countries:', countries)
print('type:',type(countries))
print('lenghth:', len(countries))

'''sample output:
countries: ('India', 'Russia', 'France', 'Germany', 'Japan')
type: <class 'tuple'>
lenghth: 5  '''

#tuple_2
element=('single',)
print('tuple:',element)
print('type:',type(element))

'''sample output:
tuple: ('single',)
type: <class 'tuple'>  '''

#tuple_3
numbers=[12,13,14,15,16]
tuple=tuple(numbers)
print('list: ',numbers)
print('tuple: ',tuple)
new_list=list(tuple)
print('converted list: ',new_list)

'''sample output:
list:  [12, 13, 14, 15, 16]
tuple:  (12, 13, 14, 15, 16)
converted list:  [12, 13, 14, 15, 16]  '''

#tuple_4
tuple=(1,2,3,4,5,6,7,8,9,10)
print(tuple[0])
print(tuple[5])
print(tuple[-1])

'''sample output:
1
6
10 '''

#tuple_5
numbers=(1,21,31,41,51,61,7,17,27,37,47,57)
print('first half:',numbers[:6])
print('secoend half:',numbers[6:])

'''sample output:
first half: (1, 21, 31, 41, 51, 61)
secoend half: (7, 17, 27, 37, 47, 57) '''

#tuple_6
colors=('green','orange','pink','red','white','yellow')
if 'green' in colors:
    print('this color exists in the given tuple')
else:
    print('this color is not exists in the given tuple')
    
'''sample output:
this color exists in the given tuple  '''

#tuple_7
numbers=(45,67,25,87,9,9,90,60,34,78,9)
print('minimum:',  min(numbers))
print('maximum:',max(numbers))
print('count of 9:',numbers.count(9))

'''sample output:
minimum: 9
maximum: 90
count of 9: 3  '''

#tuple_8
integers=(90,80,70,60,50,40)
veg=('tamoto','cucumber','brinjal','drumstick','bitter guard')
add=integers+veg
repeat=integers*3
print('concatinating two tuples:',add)
print('repeating tuple 3 times:', repeat)

'''sample output:
concatinating two tuples: (90, 80, 70, 60, 50, 40, 'tamoto', 'cucumber', 'brinjal', 'drumstick', 'bitter guard')
repeating tuple 3 times: (90, 80, 70, 60, 50, 40, 90, 80, 70, 60, 50, 40, 90, 80, 70, 60, 50, 40)  '''

#tuple_9
marks=(91,94,96,92,97)
m1,m2,m3,m4,m5=marks
average=(m1+m2+m3+m4+m5)/5
print('marks:', m1,m2,m3,m4,m5)
print('average:',average)

'''sample output:
marks: 91 94 96 92 97
average: 94.0  '''

#tuple_10
numbers=(11,22,33)
try:
    numbers[0]=77
except TypeError as error:
    print('error:',error)

'''saple error:
error: 'tuple' object does not support item assignment  '''

#tuple_11
#tuples containg list
data=(10,20,[30,40],50,60)
#modify the nested list
data[2].append(70)
#the tuple is immutable,but the list inside it is mutable
print('updated tuple:', data)

'''sample output:
updated tuple: (10, 20, [30, 40, 70], 50, 60) '''

#tuple_12
numbers=(28,89,24,82,79)
sorted_numbers=sorted(numbers)
print('atcual tuple:', numbers)
print('sorted tuple:', sorted_numbers)

'''sample output:
atcual tuple: (28, 89, 24, 82, 79)
sorted tuple: [24, 28, 79, 82, 89]  '''



