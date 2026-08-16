#exercise_13
num=int(input('enter a num:'))
for i in range(1,11):
    print(num, '*', i,'=', num*i)

'''sample output:
enter a num:17
17 * 1 = 17
17 * 2 = 34
17 * 3 = 51
17 * 4 = 68
17 * 5 = 85
17 * 6 = 102
17 * 7 = 119
17 * 8 = 136
17 * 9 = 153
17 * 10 = 170 '''

#exercise_14
n=int(input('enter a number:'))
fact=1
for i in range(1, n+1):
    fact=fact*i
print('factorial= ', fact)

'''sample output:
enter a number:7
factorial=  5040'''

#exercise_15
s=input('enter string:')
vowels=0
consonants=0
digits=0
spaces=0
for ch in s:
    if ch.lower() in 'aeiou':
        vowels=vowels+1
    elif ch.isalpha():
        consonants=consonants+1
    elif ch.isdigit():
        digits=digits+1
    elif ch==' ':
        spaces=spaces+1
print('vowels=', vowels)
print('consonants=',consonants)
print('digits=', digits)
print('spaces=', spaces)

'''sample output:
enter string:unity is strength
vowels= 4
consonants= 11
digits= 0
spaces= 2'''

#exercise_16
n=int(input('enter a number:'))
count=0
for i in range(1, n+1):
    if n%i==0:
        count=count+1
if count==2:
    print('prime')
else:
    print('not prime')

'''sample output:
enter a number:23
prime'''

#exercise_17
start=int(input('enter starting number:'))
end=int(input('enter ending number:'))
for n in range(start, end+1):
    count=0
    for i in range(1, n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print(n,end=' ')

'''sample output:
enter starting number:1
enter ending number:100
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
'''

