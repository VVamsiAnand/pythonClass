#dictionaries_1
students={1:'Vamsi Anand',
              2:'Vasantha',
              3:'Lokesh',
              4:'Sai meghana',
              5:'Phanith',
              6:'Varsha'
              }
print('students:',students)

'''sample output:
students: {1: 'Vamsi Anand', 2: 'Vasantha', 3: 'Lokesh', 4: 'Sai meghana', 5: 'Phanith', 6: 'Varsha'}
  '''
#dictionaries_2
students={1:'Ram', 2:'Sita', 3:'Lakshmi'}
students[4]='Shiv'
students[5]='Maha'
students[6]='Brahma'
print('final dict:',students)

'''sample output:
final dict: {1: 'Ram', 2: 'Sita', 3: 'Lakshmi', 4: 'Shiv', 5: 'Maha', 6: 'Brahma'}  '''

#dictionaries_3
dict={1:'key', 2:'lock', 3:'solution'}
print('before update:',dict)
dict[2]='problem'
print('after update:',dict)

'''sample output:
before update: {1: 'key', 2: 'lock', 3: 'solution'}
after update: {1: 'key', 2: 'problem', 3: 'solution'}  '''

#dictionaries_4
keys=['name','place','color']
values=['mirchi','guntur','red']
zip()
data=dict(zip(keys,values))
print('dictionary:',data)

'''sample output:
dictionary: {'name': 'mirchi', 'place': 'guntur', 'color': 'red'} '''

#dictionaries_5
employees={
    1:{'name':'priya','department':'CSE','salary':100000},
    2:{'name':'shankar','departmrnt':'mechanical','salary':100000},
    3:{'name':'maheswar','department':'EEE','salary':100000}
    }
print('employees:',employees)

'''sample output:
employees: {1: {'name': 'priya', 'department': 'CSE', 'salary': 100000}, 2: {'name': 'shankar', 'departmrnt': 'mechanical', 'salary': 100000}, 3: {'name': 'maheswar', 'department': 'EEE', 'salary': 100000}} '''
    
#dictionaries_6

