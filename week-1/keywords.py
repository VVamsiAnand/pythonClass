 # Program to demonstrate Python keywords

import keyword

# 1. Print total number of keywords and the keyword list
print("Total Keywords:", len(keyword.kwlist))
print("Keywords:")
print(keyword.kwlist)

# 2. Check whether the input is a keyword
word = input("\nEnter a word: ")

if keyword.iskeyword(word):
    print(word, "is a Python keyword.")
else:
    print(word, "is NOT a Python keyword.")

# 3. Reserved keyword errors (Keep these lines commented)
for = 5
# Error: SyntaxError: invalid syntax

True = 10
#output
# Error: SyntaxError: cannot assign to True
#Total Keywords: 35
#Keywords:
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
'except', 'finally', 'for', 'from', 'global', 'if', 'import',
'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']

#Enter a word: for
#for is a Python keyword.
