#exercise_8
n=int(input('enter n:'))
i=1
while i <= n:
    print(i, end=' ')
    i=i+1

'''sample output:
enter n:7
1 2 3 4 5 6 7 enter a number:'''

#exercise_9
n=int(input('enter a number:'))
temp=n
sum=0
count=0
while temp > 0:
    digit= temp%10
    sum=sum+digit
    count=count+1
    temp=temp//10
average=sum/count
print('sum= ', sum)
print('average= ', average)

'''sample output:
enter a number:3421
sum=  10
average=  2.5'''

#exercise_10
n=int(input('enter a number:'))
rev=0
while n > 0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reverse of  given number is ", rev)

'''sample output:
enter a number:1234
reverse of  given number is  4321'''

#exercise-11
n=int(input('enter a number:'))
original=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if original==rev:
    print('palindrome.')
else:
    print('not a palindrome.')

'''sample output:
enter a number:31313
palindrome.'''

#exercise_12
n=int(input('enter a number of terms:'))
a=0
b=1
i=1
while i<=n:
    print(a, end=' ')
    a,b=b, a+b
    i=i+1

'''sample output:
enter a number of terms:7
0 1 1 2 3 5 8 '''
    

