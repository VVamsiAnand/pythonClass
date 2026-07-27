# 1. if-else with Correct Indentation

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
else:
    print("Negative or Zero")

# Indentation Error Example (Keep Commented)
 if num > 0:
 print("Positive")
 else:
     print("Negative")

# Error:
# IndentationError: expected an indented block after 'if' statement


# 2. Nested for loop with inner if-else

print("\nEven or Odd Numbers:")

for i in range(1, 11):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")


# 3. code rewritten with correct Python indentation

number = 15

if number > 10:
    print("\nGreater")
else:
    print("\nSmaller")

# Errors:
# IndentationError: expected an indented block after 'if' statement
# (Occurs only if indentation is incorrect.)
# No errors in the corrected program.
# Vamsi: Enter a number: 5
#Positive
#outdut
#Even or Odd Numbers:
#1 Odd
#2 Even
#3 Odd
#4 Even
#5 Odd
#6 Even
#7 Odd
#8 Even
##9 Odd
#10 Even

#Greater
