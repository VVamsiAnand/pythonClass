# 1. Input Name and Age

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you will turn {age + 1} next year.")

# 2. Arithmetic Operations

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Quotient =", a / b)

# 3. Output Formatting

name = "Vamsi"
marks = 95

# Comma-separated print()
print("\nName:", name, "Marks:", marks)

# str.format()
print("Name: {} Marks: {}".format(name, marks))

# f-string
print(f"Name: {name} Marks: {marks}")

# 4. Multiple Values in One Line

numbers = list(map(int, input("\nEnter numbers separated by space: ").split()))
print("Sum =", sum(numbers))

# Errors:
# 1. ValueError: If non-numeric input is entered for int().
# 2. ZeroDivisionError: If second number is 0 while finding quotient.
# 3. No error for valid.
#output
#Enter your name: Vamsi
#Enter your age: 18
#Hello Vamsi, you will turn 19 next year.#

#Enter first number: 20
#Enter second number: 10
#Sum = 30
#Difference = 10
Product = 200
Quotient = 2.0
