# Combined program for Command Line Arguments

import sys

# 3. Print script name and total arguments
print("Script Name:", sys.argv[0])
print("Total Arguments:", len(sys.argv) - 1)

# Check number of arguments
if len(sys.argv) != 4:
    print("\nUsage: python command_line.py <name> <num1> <num2>")
else:
    # 1. Greet the user
    name = sys.argv[1]
    print("Hello,", name + "!")

    # 2. Sum of two numbers
    num1 = int(sys.argv[2])
    num2 = int(sys.argv[3])

    print("Sum =", num1 + num2)

# Errors:
# 1. If wrong number of arguments are passed:
#    Usage: python command_line.py <name> <num1> <num2>
#
# 2. If num1 or num2 is not an integer:
#    ValueError: invalid literal for int() with base 10
#
# 3. No error for valid input
#output
#Script Name: command_line.py
#Total Arguments: 3
#Hello, Alice!
#Sum = 30
