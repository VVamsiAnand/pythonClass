# lab3_task1.py

def factorial(n):
    # Negative numbers are not allowed
    if n < 0:
        return "Factorial is not defined for negative numbers"

    # Base case
    if n == 0:
        return 1

    # Recursive case
    return n * factorial(n - 1)


def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


# Recursive version
print("Recursive factorial of 5:", factorial(5))
print("Recursive factorial of 0:", factorial(0))
print("Recursive factorial of -2:", factorial(-2))

# Iterative version
print("Iterative factorial of 5:", factorial_iterative(5))

# Output:
# Recursive factorial of 5: 120
# Recursive factorial of 0: 1
# Recursive factorial of -2: Factorial is not defined for negative numbers
# Iterative factorial of 5: 120
#
# Difference:
# Recursive version calls itself repeatedly until it reaches the base case.
# Iterative version uses a loop to calculate the factorial.


# lab3_task2.py

count = 0


def fibonacci(n):
    global count

    # Count every call to fibonacci()
    count += 1

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# Print first 15 Fibonacci terms
print("First 15 Fibonacci terms:")

for i in range(15):
    print(fibonacci(i), end=" ")

print()

# Count how many times fibonacci(5) is called
count_fib5 = 0


def fibonacci_count(n):
    global count_fib5

    if n == 5:
        count_fib5 += 1

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_count(n - 1) + fibonacci_count(n - 2)


fibonacci_count(10)

print("fibonacci(5) is recomputed:", count_fib5, "times while calculating fibonacci(10)")


# Output:
# First 15 Fibonacci terms:
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# fibonacci(5) is recomputed: 8 times while calculating fibonacci(10)
#
# Observation:
# The recursive Fibonacci function repeatedly calculates the same values.
# This is why memoization can be used to improve its performance.


# lab3_task3.py

def sum_of_digits(n):
    # Base case
    if n == 0:
        return 0

    # Recursive case
    return (n % 10) + sum_of_digits(n // 10)


def reverse_number(n, result=0):
    # Base case
    if n == 0:
        return result

    # Recursive case
    return reverse_number(n // 10, result * 10 + n % 10)


number = 12345

print("Number:", number)
print("Sum of digits:", sum_of_digits(number))
print("Reversed number:", reverse_number(number))


# Output:
# Number: 12345
# Sum of digits: 15
# Reversed number: 54321

# lab3_task4.py

def power(base, exp):
    # Base case
    if exp == 0:
        return 1

    # Handle negative exponent
    if exp < 0:
        return 1 / power(base, -exp)

    # Recursive case
    return base * power(base, exp - 1)


print("2^5 =", power(2, 5))
print("5^0 =", power(5, 0))
print("2^-3 =", power(2, -3))
print("3^4 =", power(3, 4))


# Output:
# 2^5 = 32
# 5^0 = 1
# 2^-3 = 0.125
# 3^4 = 81

# lab3_task5.py

def gcd(a, b):
    # Base case
    if b == 0:
        return abs(a)

    # Recursive case
    return gcd(b, a % b)


def lcm(a, b):
    if a == 0 or b == 0:
        return 0

    return abs(a * b) // gcd(a, b)


a = 12
b = 18

gcd_result = gcd(a, b)
lcm_result = lcm(a, b)

print("First number:", a)
print("Second number:", b)
print("GCD:", gcd_result)
print("LCM:", lcm_result)


# Output:
# First number: 12
# Second number: 18
# GCD: 6
# LCM: 36
#
# Euclidean Algorithm:
# gcd(12, 18)
# = gcd(18, 12)
# = gcd(12, 6)
# = gcd(6, 0)
# = 6


# lab3_task6.py

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, destination, auxiliary)

    # Move the largest disk to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)


# Tower of Hanoi for 3 disks
print("Tower of Hanoi for 3 disks:")

tower_of_hanoi(3, "A", "B", "C")

moves_3 = 2 ** 3 - 1
print("Total moves:", moves_3)


# Tower of Hanoi for 4 disks
print("\nTower of Hanoi for 4 disks:")

tower_of_hanoi(4, "A", "B", "C")

moves_4 = 2 ** 4 - 1
print("Total moves:", moves_4)


# Output:
# Tower of Hanoi for 3 disks:
# Move disk 1 from A to C
# Move disk 2 from A to B
# Move disk 1 from C to B
# Move disk 3 from A to C
# Move disk 1 from B to A
# Move disk 2 from B to C
# Move disk 1 from A to C
# Total moves: 7
#
# Tower of Hanoi for 4 disks:
# Move disk 1 from A to B
# Move disk 2 from A to C
# Move disk 1 from B to C
# Move disk 3 from A to B
# Move disk 1 from C to A
# Move disk 2 from C to B
# Move disk 1 from A to B
# Move disk 4 from A to C
# Move disk 1 from B to C
# Move disk 2 from B to A
# Move disk 1 from C to A
# Move disk 3 from B to C
# Move disk 1 from A to B
# Move disk 2 from A to C
# Move disk 1 from B to C
# Total moves: 15
#
# Verification:
# For n = 3: 2^3 - 1 = 7 moves
# For n = 4: 2^4 - 1 = 15 moves
