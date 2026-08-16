#exercise_1
num=int(input('enter a number:'))
if num > 0:
    print(num, 'is positive.')
elif num < 0:
    print(num, 'is negative.')
else:
    print(num, 'is zero.')

'''sample output:
enter a number:34
34 is positive.'''


#exercise_2
year=int(input('enter year:'))
if year%400 == 0:
    print(year, 'is a leap year')
elif year%4 == 0:
    print(year, 'is a leap year')
elif year%100 == 0:
    print(year, 'is not a leap year')
else:
    print(year, 'is not a leap year')

'''sample output:
enter year:2008
2008 is a leap year'''

#exercise_3
a=int(input('enter first side:'))
b=int(input('enter secoend side:'))
c=int(input('enter third side:'))
if a == b == c:
    print('equilateral triangle')
elif a==b or b==a or a==c:
    print('isosceles triangle')
elif a+b>c and b+c>a and c+a>b:
    print('scalene triangle')
else:
    print('not a valid triangle')

'''sample output:
enter first side:5
enter secoend side:6
enter third side:5
isosceles triangle'''

#exercise_4
a=int(input('enter first number:'))
b=int(input('enter secoend number'))
c=int(input('enter third number'))
if a>b:
    if a>c:
        largest=a
    else:
        largest=c
else:
    if b>c:
        largest=b
    else:
        largest=c
print('largest= ',largest)
'''sample output:
enter first number:12
enter secoend number23
enter third number34
largest=  34'''

#exercise_5
marks=int(input('enter student marks:'))
if marks >= 90:
    print('Grade: A')
elif marks >=  75:
    print('Grade: B')
elif marks >= 60:
    print('Grade: C')
elif marks >= 40:
    print('Grade: D')
else:
    print('Grade: F')

'''sample output:
enter student marks:95
Grade: A'''

#exercise_6
ch=input('enter character:')
if ch.isalpha():
    if ch.lower() in 'aeiou':
        print('vowel')
    else:
        print('consonent')
elif ch.isdigit():
    print('digit')
else:
    print('special symbol')

'''sample output:
enter character:@
special symbol'''

#exercise_7
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

if month < 1 or month > 12:
    print("Invalid date")
else:
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_days = 29
        else:
            max_days = 28
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        max_days = 31

    if day >= 1 and day <= max_days:
        print("Valid date")
    else:
        print("Invalid date")

'''sample output:
Enter year: 2030
Enter month: 5
Enter day: 7
Valid date'''



        

