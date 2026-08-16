#exercise_18
n=int(input('enter number of rows:'))
for i in range(1, n+1):
    for j in range(i):
        print('*', end=' ')
    print()

'''sample output:
enter number of rows:5
* 
* * 
* * * 
* * * * 
* * * * * 
'''

#exercise_19
n=int(input('enter number of rows:'))
for i in range(n,0,-1):
    for j in range(i):
        print('*', end=' ')
    print()

'''sample output:
enter number of rows:5
* * * * * 
* * * * 
* * * 
* * 
*
'''

#exercise_20
n=int(input('enter number of rows:'))
for i in range(1, n+1):
    spaces=n-i
    stars=' '.join(['*'] * i)
    print(' ' * spaces+stars)

'''sample output:
enter number of rows:5
    *
   * *
  * * *
 * * * *
* * * * *
'''

#exercise_21
n=int(input('enter number of rows:'))
for i in range(n,0,-1):
    spaces=n-i
    stars=' '.join(['*']*i)
    print(' ' * spaces+stars)

'''sample output:enter number of rows:5
* * * * *
 * * * *
  * * *
   * *
    *
    '''

#exercise_22
n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

'''sample output:Enter N: 4
   *
  ***
 *****
*******
*******
 *****
  ***
   *
   '''

#exercise_23
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

'''sample output:
Enter number of rows: 5
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''

#exercise_24
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

'''sample output:
Enter number of rows: 5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

#exercise_25
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()

'''sample output:
Enter number of rows: 5
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1
'''

#exercise_26
n = int(input("Enter number of rows: "))

for i in range(n):
    ch = chr(65 + i)

    for j in range(i + 1):
        print(ch, end=" ")

    print()

'''sample output:Enter number of rows: 5
A 
B B 
C C C 
D D D D 
E E E E E
'''

#exercise_27
n = int(input("Enter size: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

'''sample output:
Enter size: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * *
'''

#exercise_28
n = int(input("Enter N: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    
    if i == 1:
        print("*")
    else:
        print("*" + " " * (2 * i - 3) + "*")

'''sample output:Enter N: 5
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''

#exercise_29
n = int(input("Enter number of rows: "))

num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()

'''sample output:Enter number of rows: 5
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
'''

#exercise_30
n = int(input("Enter N: "))

for i in range(1, n + 1):
    print("* " * i + " " * max(0, 4 * (n - i) - 2) + "* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i + " " * max(0, 4 * (n - i) - 2) + "* " * i)

'''sample output:
Enter N: 4
*           * 
* *       * * 
* * *   * * * 
* * * * * * * * 
* * *   * * * 
* *       * * 
*           *
'''

      

